<?php

require 'vendor/autoload.php';
use \Mailjet\Resources;
use Google\Cloud\SecretManager\V1\SecretManagerServiceClient;


function getDecryptionKey() {
    putenv('GOOGLE_APPLICATION_CREDENTIALS=' . __DIR__ . '/service-account.json');
    $projectId = '';
    $secretId = '';
    $versionId = 'latest';

    $client = new SecretManagerServiceClient();
    $secretName = $client->secretVersionName($projectId, $secretId, $versionId);

    try {
        $response = $client->accessSecretVersion($secretName);
        $secretPayload = $response->getPayload()->getData();
        return $secretPayload;
    } catch (Exception $e) {
        echo "Chyba při načítání klíče: " . $e->getMessage();
        return null;
    }
}

function decryptEmail($encryptedEmail, $key) {
    list($encryptedData, $iv) = explode('::', base64_decode($encryptedEmail), 2);
    return openssl_decrypt($encryptedData, "aes-256-cbc", $key, 0, $iv);
}










$apikey = '';  
$apisecret = '';  
$mj = new \Mailjet\Client($apikey, $apisecret, true,['version' => 'v3.1']);
if($_SERVER['REQUEST_METHOD'] == 'POST') {
    $key = getDecryptionKey(); // Získání klíče
    if ($key) {
        $encryptedEmail = "ZAŠIFROVANEJ EMAIL";     
        $body = [
            'Messages' => [
                [
                    'From' => [
                        'Email' => "NO_REPLY_EMAIL",   
                        'Name' => ""
                    ],
                    'To' => [
                        [
                            'Email' => decryptEmail($encryptedEmail, $key),
                            'Name' => ""
                        ]
                    ],
                    'Subject' => $_POST["subject"],
                    'TextPart' => $_POST["msg"],
                    'HTMLPart' => $_POST["msg"],
                    "Headers" => [
                        "Reply-To" => $_POST["email"]
                            ]
                ]
            ]
        ];
        $response = $mj->post(Resources::$Email, ['body' => $body]);
        if ($response->success()) {
            $data = $response->getData();
            echo "Email was sent successfully.\n";
            var_dump($data);
        } else {
            echo "Failed to send email. Error: " . $response->getReasonPhrase() . "\n";
            var_dump($response->getData());
        }
    } else {
        echo "Nepodařilo se získat šifrovací klíč.\n";
    }
    
}
?>
