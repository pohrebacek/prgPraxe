import sys

def getTotalParts(splitBy, textLength):
    parts = int(textLength / splitBy)
    if textLength % splitBy != 0:
        return str(parts+1)
    return str(parts)


while True:
    try:
        splitBy = int(input("Zadejte, po kolika znacích chcete text rozdělit: "))
        if splitBy <= 0:
            print("číslo musí být větší než 0")
        else:
            break
    except ValueError:
        print("zadejte číslo")

print("Zadejte text (ukončete pomocí Enter a Ctrl+D): ")
textToSplit = sys.stdin.read()  #běžnej input() se ukončí po znaku enteru
print("------------------------------------------------------------------------------")

finalText = ""
currentPart = 1
#print(len(textToSplit))
for i in range(len(textToSplit)):
    #print(textToSplit[i])
    #print(i)
    finalText += textToSplit[i]

    #print("dléka final text: "+str(len(finalText)))
    if len(finalText) == splitBy or i == len(textToSplit)-1:
        print(finalText)
        print("[" + str(currentPart) + "/" + getTotalParts(splitBy, len(textToSplit)) + "]")
        print("------------------------------------------------------------------------------")
        currentPart += 1
        with open("splittedFiles/" + str(currentPart-1)+".txt", "a", encoding="utf-8") as file:  # to w je že to bude číst, "a" je že to napíše na další řádek
            file.write(finalText)
        finalText = ""