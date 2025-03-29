<?php
namespace App\Module\Front\Presenters;

use App\Module\Model\User\UsersRepository;
use Nette;
use Nette\Application\UI\Form;
use App\Module\Model\Security\MyAuthenticator;

final class SignPresenter extends Nette\Application\UI\Presenter
{
    public function __construct(
        protected Nette\Database\Explorer $database,
        protected Nette\Security\Passwords $passwords,    //práce s heslama
        protected UsersRepository $usersRepository,
        protected MyAuthenticator $authenticator
    ) {

    }
    protected function createComponentSignUpForm(): Form
    {
        $form = new Form;
        $form->addText('username', "Uživatelské jméno:")
            ->setRequired('Prosím vyplňte své uživatelské jméno.')
            ->setHtmlAttribute("class", "form-control");
        
        $form->addEmail('email', 'Emailová adresa:')
            ->setRequired('Prosím, vyplňte svou emailovou adresu.')
            ->setHtmlAttribute("class", "form-control");

        $form->addPassword('password','Heslo:')
            ->setRequired('Prosím, zvolte si své heslo.')
            ->setHtmlAttribute("class", "form-control");
        
        $form->addPassword('passwordCheck', "Heslo znovu: ")
            ->setRequired('Prosím, vyplňte své heslo znovu.')
            ->setHtmlAttribute("class", "form-control");

        $form->addSubmit('send', 'Zaregistrovat se')
             ->setHtmlAttribute("class", "btn btn-outline-primary");

        $form->onSuccess[] = [$this, 'signUpFormSucceeded'];
        return $form;
    }

    public function signUpFormSucceeded(Form $form): void
    {
        $data = $form->getValues();
        $data["role"] = "user";
        bdump($data);
        $data->password = $this->passwords->hash($data->password);
        if ($this->usersRepository->getRowByUsername($data->username) || $this->usersRepository->getRowByEmail($data->email)){
            $form->addError('Tento účet již existuje');
        }
        elseif (!$this->passwords->verify($data->passwordCheck, $data->password)) { //funkce verify zkontroluje hash a zadaný heslo, samotná funkce hash totiž udělá jinej hash i ze stejných slov
            bdump($data);
            $form->addError('Vámi zadaná hesla musí být stejná');
        } else {
            $passwordCheck = $data->passwordCheck;
            unset($data->passwordCheck);
            bdump($data);
            $this->usersRepository->saveRow((array) $data, $id=null);
            $this->getUser()->login(
                $this->authenticator->authenticate($data->username, $passwordCheck));
            bdump($this->getUser());
            bdump($this->getUser()->getIdentity());
            $this->redirect('Homepage:');
        }
        
    }

	protected function createComponentSignInForm(): Form
	{
		$form = new Form;
		$form->addText('username', 'Uživatelské jméno:')
			->setRequired('Prosím vyplňte své uživatelské jméno.')
            ->setHtmlAttribute("class", "form-control");

		$form->addPassword('password', 'Heslo:')
			->setRequired('Prosím vyplňte své heslo.')
            ->setHtmlAttribute("class", "form-control");

		$form->addSubmit('send', 'Přihlásit se')
             ->setHtmlAttribute("class", "btn btn-outline-primary");

        $form->onSuccess[] = [$this, 'signInFormSucceeded'];
		return $form;
	}


    public function signInFormSucceeded(Form $form): void
    {
       $data = $form->getValues();
       $username = isset($data->username) ? strval($data->username) : '';  // Pokud není setováno, použije prázdný řetězec
       $password = isset($data->password) ? strval($data->password) : '';

        try {
            $this->getUser()->login($this->authenticator->authenticate($username, $password));
            bdump($this->getUser());
            bdump($this->getUser()->getIdentity());
            $this->redirect('Homepage:');
    
        } catch (Nette\Security\AuthenticationException $e) {
            $form->addError('Nesprávné přihlašovací jméno nebo heslo.');
        }
    }

    public function actionOut(): void
    {
        $this->getUser()->logout();
        $this->flashMessage('Odhlášení bylo úspěšné.');
        $this->redirect('Homepage:');
    }


}
