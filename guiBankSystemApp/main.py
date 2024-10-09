import tkinter
import customtkinter
from PIL import Image
import csv
from Owner import Owner
import datetime
import pandas as pd
from configparser import ConfigParser
import re


parser = ConfigParser()
parser.read("settings.ini")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'



class Account:
    def __init__(self, id, balance, owner):
        self.id = id
        self.balance = balance
        self.owner = owner
        
        
    def showIncoming(self):
        with open("transakce.csv", "r", encoding="utf-8") as transakce_file:
            transakce_reader = csv.reader(transakce_file)
            for line in transakce_reader:
                if (line[5] == self.id):
                    print(line)
                    
    def showOutgoing(self):
        with open("transakce.csv", "r", encoding="utf-8") as transakce_file:
            transakce_reader = csv.reader(transakce_file)
            for line in transakce_reader:
                if (line[4] == self.id):
                    print(line)
                    
    
    def showAllTransactions(self):
        print("registred2"+str(registered))
        for label in transactionsFrame.winfo_children():
            label.destroy()
        with open("transakce.csv", "r", encoding="utf-8") as transakce_file:
            transakce_reader = csv.reader(transakce_file)
            transactionCount = 0
            for line in reversed(list(transakce_reader)):
                if (line[4] == self.id or line[5] == self.id):
                    print("registred"+str(registered))
                    
                    transactionLabelFrame = customtkinter.CTkFrame(transactionsFrame,
                                               height=95,
                                               width=app.winfo_screenwidth(),
                                               border_width=1,
                                               border_color="gray")
                    #transactionLabelFrame.place(relx=0, rely=0+transactionCount, anchor=tkinter.NW)
                    transactionLabelFrame.pack()

                    transactionLabelType = customtkinter.CTkLabel(transactionLabelFrame,
                                                                  text=line[2],
                                                                  font=("Rubik", 30, "bold"))
                    transactionLabelType.place(relx=0.01, rely=0.01, anchor=tkinter.NW)
                    
                    transactionDate = customtkinter.CTkLabel(transactionLabelFrame,
                                                        text=line[0],
                                                        font=("Rubik", 20, "bold"))
                    transactionDate.place(relx=0.01, rely=0.35, anchor=tkinter.NW)
                    
                    transactionTime = customtkinter.CTkLabel(transactionLabelFrame,
                                                             text=line[1],
                                                             font=("Rubik", 15, "bold"))
                    transactionTime.place(relx=0.01, rely=0.6, anchor=tkinter.NW)

                    transactionAmount = customtkinter.CTkLabel(transactionLabelFrame,
                                                               text=line[3],
                                                               font=("Rubik", 30, "bold"),
                                                               text_color="green")
                    transactionAmount.place(relx=0.95, rely=0.01, anchor=tkinter.NE)
                    
                    if (line[4] == self.id):
                        transactionAmount.configure(text="-"+str(line[3]),
                                                    text_color="red")
                        
                    if (line[2] == "transakce"):
                        if (line[4] != self.id):
                            transactionLabelType.configure(text=getRecieverFName(line[4]))
                        elif (line[5] != self.id):
                            transactionLabelType.configure(text=getRecieverFName(line[5]))
                              
                    
                    transactionCount = transactionCount + 0.17
                    print(line)
            
                    
            
                    
            
                    
                    
                    
        
    def getOwnerEmail(self, owner):
        return owner.getEmail()
        
        
    def deposit(self, amount, transfer):
        if (depositEntry.get().isdigit() or transfer == True):
            self.balance = self.balance + int(amount)
            errorMessageD.configure(text="Vklad proběhl úspěšně!",
                                    text_color="green")  
            depositEntry.delete(0,tkinter.END)
            print("fachat oo")


            if (transfer != True):
                  with open("transakce.csv", "a", newline="", encoding="utf-8") as transakce_file:
                    transaction_writer = csv.writer(transakce_file)
                    dateAndTime = datetime.datetime.now()
                    line = [dateAndTime.strftime("%x"), dateAndTime.strftime("%X"), "vklad", amount, "--", self.id]
                    transaction_writer.writerow(line)
                    transfer = False

            #přepsání zůstatků



            with open("accounts.csv", "r", encoding="utf-8") as accountsRead_file:
                content = accountsRead_file.readlines()
                for i in range(0, len(content)):
                    if (content[i].startswith(str(self.id))):
                        df = pd.read_csv("accounts.csv")
                        df.loc[i-1, "amount"] = self.balance
                        df.to_csv("accounts.csv", index=False)
                        break
        else:
            errorMessageD.configure(text="Prosím, zadejte částku ve tvaru ČÍSLA",
                                    text_color="red")  
            depositEntry.delete(0,tkinter.END)
                    
                    
                
        
        
    def withdraw(self, amount, transfer):
        if (withdrawEntry.get().isdigit() or transfer):
            amount = int(amount)
            if (self.balance >= amount):
                errorMessageW.forget()
                self.balance = self.balance - amount
                #přepsání zůstatků 

                if (transfer != True):
                  with open("transakce.csv", "a", newline="", encoding="utf-8") as transakce_file:
                    transaction_writer = csv.writer(transakce_file)
                    dateAndTime = datetime.datetime.now()
                    line = [dateAndTime.strftime("%x"), dateAndTime.strftime("%X"), "výběr", amount, self.id, "--"]
                    transaction_writer.writerow(line)
                    transfer = False
                    errorMessageW.configure(text="Výběr proběhl úspěšně!",
                                        text_color="green")  
                    withdrawEntry.delete(0,tkinter.END)

                with open("accounts.csv", "r", encoding="utf-8") as accountsRead_file:
                    content = accountsRead_file.readlines()
                    for i in range(0, len(content)):
                        if (content[i].startswith(str(self.id))):
                            df = pd.read_csv("accounts.csv")
                            df.loc[i-1, "amount"] = self.balance
                            df.to_csv("accounts.csv", index=False)
                            break
                        
                return True
            else:
                print("Nemánte dostatek na účtu")
                mainAccount.printBalance()
                errorMessageW.configure(text="Nemánte dostatek na účtu",
                                    text_color="red")
                return False
        else:
            errorMessageW.configure(text="Prosím, zadejte částku ve tvaru ČÍSLA",
                                    text_color="red")  
            withdrawEntry.delete(0,tkinter.END)
    
    def printBalance(self):
        print("zůstatek na účtě: "+str(self.balance))
        
    def transferMoney(self, amount, reciever, transfer):
        global recieverAccount
        global recieverOwner
        amount = int(amount)
        transfer = True
        if(transferIdEntry.get() == mainAccount.id):
            errorMessageT.configure(text="Nemůžete zadat ID vašeho účtu!",
                                text_color="red")
        else:            
            if (self.withdraw(amount, transfer)):
                reciever.deposit(amount, transfer)
                errorMessageT.configure(text="Transakce proběhla v pořádku",
                                        text_color="green")
                print("success")
                transferIdEntry.delete(0,tkinter.END)
                transferAmountEntry.delete(0,tkinter.END)


                #na zápis transakce do databáze
                with open("transakce.csv", "a", newline="", encoding="utf-8") as transakce_file:
                    transaction_writer = csv.writer(transakce_file)
                    dateAndTime = datetime.datetime.now()
                    line = [dateAndTime.strftime("%x"), dateAndTime.strftime("%X"), "transakce", amount, self.id, reciever.id]
                    transaction_writer.writerow(line)
            else:
                errorMessageT.configure(text="Nemáte dostatek peněz na účtě.")






customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")




def login():
    global mainAccount
    global recieverAccount
    global recieverOwner
    global owner
    global loginCheck
    global transfer
    global registered
    registered = False
    print("login test")
    #print(inputEmail.get())
    #print(passEntry.get())
    with open("userData.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[3] == inputEmailLogin.get() and line[4] == passEntryLogin.get():
                inputEmailLogin.configure(border_color = "gray")
                passEntryLogin.configure(border_color = "gray")
                print("login was succesful")
                owner = Owner(line[0], line[1], line[2], line[3], line[4])
                passMessage.forget()
                owner.printOwnerInfo()
                with open("accounts.csv", "r", encoding="utf-8") as accounts_file:
                    accounts_reader = csv.reader(accounts_file)
                    for accountLine in accounts_reader:
                        if accountLine[2] == inputEmailLogin.get():
                            mainAccount = Account(accountLine[0], int(accountLine[1]), owner)
                            print(mainAccount.printBalance())
                            print(mainAccount.owner)
                            print(mainAccount.id) 
                            print(str(type(mainAccount.balance))) 
                            break
                inputEmailLogin.delete(0,tkinter.END)
                passEntryLogin.delete(0,tkinter.END)
                loginFrame.forget()                
                logoFrame.forget()
                loginButton.forget()
                loginBackButton.forget()
                bankTransactionFrame.forget()
                bankFrame.pack(fill="both",expand=True)
                userBalanceLabel.configure(text=str(mainAccount.balance)+",-")
                userNameLabel.configure(text=owner.firstName + " " + owner.lastName)
                fullNameLabel.configure(text=owner.firstName + " " + owner.lastName)
                idLabel.configure(text=mainAccount.id)
                emailLabel.configure(text=owner.email)
                mainAccount.showAllTransactions()
                break
            else:
                inputEmail.configure(border_color = "red")
                passEntry.configure(border_color = "red")
                passMessage.pack(pady=6)
                
 
 
 
 
def showBankFrame():
     bankTransactionFrame.forget()
     bankInformationFrame.forget()
     bankSettingsFrame.forget()
     bankFrame.pack(fill="both",expand=True)
     userBalanceLabel.configure(text=str(mainAccount.balance)+",-")
     mainAccount.showAllTransactions()
     
     

def showTransactionFrame():
    errorMessageD.forget()
    errorMessageW.forget()
    errorMessageT.forget()
    withdrawBackButton.forget()
    withdrawFrame.forget()
    bankFrame.forget()
    depositFrame.forget()
    transferFrame.forget()
    bankTransactionFrame.pack(fill="both",expand=True)
    withdrawEntry.delete(0,tkinter.END)
    depositEntry.delete(0,tkinter.END)
    transferAmountEntry.delete(0,tkinter.END)
    transferIdEntry.delete(0,tkinter.END)
    
    
    
def showInformationFrame():
    bankFrame.forget()
    bankInformationFrame.pack(fill="both",expand=True)
    


    
def showSettingsFrame():
    bankFrame.forget()
    bankSettingsFrame.pack(fill="both", expand=True)
 
 
               
 
def register():
    print("donre")
    global mainAccount
    global recieverAccount
    global recieverOwner
    global owner
    global loginCheck
    global transfer
    global good
    inputsToCheck = [inputFName, inputLName, inputAddress, inputEmail, passEntry, passEntry2]
    for i in range(0, len(inputsToCheck)):
        if (inputsToCheck[i].get() == ""):
            inputsToCheck[i].configure(border_color = "red")
            registerMissingMessage.configure(text="Prosím, vyplňte všechna pole.")
        else:
            inputsToCheck[i].configure(border_color = "gray")
            good = good + 1

    
    if (good == len(inputsToCheck)):
        if(re.fullmatch(regex, inputEmail.get())):
            inputEmail.configure(border_color = "gray")
        else:
            inputEmail.configure(border_color = "red")
            registerMissingMessage.configure(text="Prosím, zadejte správný formát emailové adresy")
            good = good - 1
    
    print(good)
    if (good == len(inputsToCheck)):
        with open("accounts.csv", "r", encoding="utf-8") as accounts_file:
            accounts_reader = csv.reader(accounts_file)
            for line in accounts_reader:
                if (line[2] == inputEmail.get()):
                    good = good - 1
                    inputEmail.configure(border_color = "red")
                    registerMissingMessage.configure(text="Vámi zadaný email již někdo používá")
                    break
                else:
                    inputEmail.configure(border_color = "gray")
    
    if (good == len(inputsToCheck)):
        if (passEntry.get() != passEntry2.get()):           
            passEntry.configure(border_color = "red")
            passEntry2.configure(border_color = "red")
            good = good - 1
            registerMissingMessage.configure(text="Vámi zadaná hesla se neshodují")
        else:
            passEntry.configure(border_color = "gray")
            passEntry2.configure(border_color = "gray")
                        
                    
    if (good == len(inputsToCheck)):              
        with open("userData.csv", "a", newline="", encoding="utf-8") as user_File:
            user_Writer = csv.writer(user_File)
            line = [inputFName.get(), inputLName.get(), inputAddress.get(), inputEmail.get(), passEntry.get()]
            user_Writer.writerow(line)
        
        owner = Owner(inputFName.get(), inputLName.get(), inputAddress.get(), inputEmail.get(), passEntry.get())
        owner.printOwnerInfo()
        with open("accounts.csv", "a", encoding="utf-8", newline="") as accounts_file:
            accounts_writer = csv.writer(accounts_file)
            mainAccount = Account(str(1000 + len(results)+1), 0, owner)
            print("account id "+str(mainAccount.id))
            line = [str(1000 + len(results)+1), 0, inputEmail.get()]
            accounts_writer.writerow(line)
        registerFrame.forget()
        bankFrame.pack(fill="both",expand=True)
        userBalanceLabel.configure(text=str(mainAccount.balance)+",-")
        userNameLabel.configure(text=owner.firstName + " " + owner.lastName)
        fullNameLabel.configure(text=owner.firstName + " " + owner.lastName)
        idLabel.configure(text=mainAccount.id)
        emailLabel.configure(text=owner.email)
        mainAccount.showAllTransactions()
        logoFrame.forget()
    
    good = 0
                


def globalSet():
    global mainAccount
    global recieverAccount
    global recieverOwner
    global owner
    global loginCheck
    global transfer
    global registered
    
    
def loginOptionFun():
    startFrame.forget()
    loginFrame.pack(pady=8)
    loginButton.pack(pady=5)
    loginBackButton.pack(pady=6)
    
    
    
def registerOptionFun():
    startFrame.forget()
    registerFrame.pack(pady=8)
    
    
    
def withdrawScreen():
    bankTransactionFrame.forget()
    errorMessageW.configure(text="")
    withdrawFrame.pack(fill="both", expand=True)
    
    
def depostiScreen():
    bankTransactionFrame.forget()
    errorMessageD.configure(text="")
    depositFrame.pack(fill="both", expand=True)
    
    
def transferScreen():
    bankTransactionFrame.forget()
    errorMessageT.configure(text="")
    transferFrame.pack(fill="both", expand=True)
    
    
    
def findReciever(amount, recieverId, transfer):
    transfer = True
    global recieverFound
    recieverFound = False 
    global recieverAccount
    global recieverOwner           
    with open("accounts.csv", "r", encoding="utf-8") as accounts_file:
        accounts_reader = csv.reader(accounts_file)
        for accountLine in accounts_reader:
            if accountLine[0] == recieverId:
                #na nalezení ownera
                with open("userData.csv", "r", encoding="utf-8") as user_File:
                    user_Reader = csv.reader(user_File)
                    for userLine in user_Reader:
                        if userLine[3] == accountLine[2]:
                            recieverOwner = Owner(userLine[0], userLine[1], userLine[2], userLine[3], userLine[4])
                recieverAccount = Account(accountLine[0], int(accountLine[1]), recieverOwner)
                recieverFound = True
                
                
    if (not recieverFound):
        errorMessageT.configure(text="Účet s tímto ID neexistuje.",
                                text_color="red")
    
    if (not transferAmountEntry.get().isdigit() or not transferIdEntry.get().isdigit()):
        errorMessageT.configure(text="Prosím, zadejte všechny údaje ve tvaru čísla.",
                                text_color="red")
              
    if (transferIdEntry.get() == ""):
        transferIdEntry.configure(border_color="red")
        errorMessageT.configure(text="Prosim, vyplnte vsechna pole",
                                text_color="red")
    else:
        transferIdEntry.configure(border_color="gray")  
    
    if (transferAmountEntry.get() == ""):
        transferAmountEntry.configure(border_color="red")
        errorMessageT.configure(text="Prosím, vyplňte všechna pole",
                                text_color="red")
    else:
        transferAmountEntry.configure(border_color="gray")
        mainAccount.transferMoney(amount, recieverAccount, transfer)
    
    
                
                
                
                
                
def getRecieverFName(recieverId):
    with open("accounts.csv", "r", encoding="utf-8") as accounts_file:
        accounts_reader = csv.reader(accounts_file)
        for accountLine in accounts_reader:
            if accountLine[0] == recieverId:
                #na nalezení ownera
                with open("userData.csv", "r", encoding="utf-8") as user_File:
                    user_Reader = csv.reader(user_File)
                    for userLine in user_Reader:
                        if userLine[3] == accountLine[2]:
                            return userLine[0] + " " + userLine[1]
                
                
                
                
                
                
                
    
def themeSet():
    idk = themeSwitch.get()
    if idk == "on":
        customtkinter.set_appearance_mode("dark")   
    else:
        customtkinter.set_appearance_mode("light")
    parser.set("settings", "dark_mode", idk)
    with open("settings.ini", "w") as configfile:
        parser.write(configfile)
    print(idk)
    
    
    
def logout():
    bankFrame.forget()
    logoFrame.pack(padx=20, pady=50)
    logoLabel.pack()
    startFrame.pack(pady=8)
    inputEmail.configure(border_color = "gray")
    passEntry.configure(border_color = "gray")
    
def showFirstFrame():
    inputEmailLogin.delete(0,tkinter.END)
    passEntryLogin.delete(0,tkinter.END)
    loginFrame.forget()
    passMessage.forget()
    inputsToCheck = [inputFName, inputLName, inputAddress, inputEmail, passEntry, passEntry2]
    for i in range(0, len(inputsToCheck)):
        inputsToCheck[i].delete(0,tkinter.END)
        inputsToCheck[i].configure(border_color = "gray")
    registerMissingMessage.configure(text="")
    registerFrame.forget()
    loginButton.forget()
    loginBackButton.forget()
    startFrame.pack(pady=8)
    
   
    
##################################
#          main program          # 
##################################     
    
    

mainAccount = Account(0,0,0)
recieverAccount = Account(0,0,0)
recieverOwner = Owner(0,0,0,0,0)
owner = Owner(0,0,0,0,0)
loginCheck = True
transfer = False
results = pd.read_csv("accounts.csv")
print(len(results)) 
good = 0
registered = True

globalSet()    


mode_state = parser.get("settings", "dark_mode")
if mode_state == "on":
    customtkinter.set_appearance_mode("dark")   
else:
    customtkinter.set_appearance_mode("light")

app = customtkinter.CTk()
app.geometry("400x700")
app.title("Banking App")
 

width = 400
height = 700
x = (app.winfo_screenwidth()//2)-(width//2)
y = (app.winfo_screenheight()//2)-(height//2)
app.geometry("{}x{}+{}+{}".format(width, height, x, y))





appHeight = app.winfo_height()
appWidth = app.winfo_width()




logoFrame = customtkinter.CTkFrame(master=app,
                                   width=150,
                                   height=150)
logoFrame.pack(padx=20, pady=15)

logo = customtkinter.CTkImage(light_image=Image.open("image.png"), 
                              dark_image=Image.open("image.png"),
                              size=(150,150))

logoLabel = customtkinter.CTkLabel(logoFrame, image = logo, text="", bg_color="#242424")
logoLabel.pack()





startFrame = customtkinter.CTkFrame(app,
                                    height=150,
                                    width=300)
startFrame.pack(pady=8)

infoText = customtkinter.CTkLabel(startFrame,
                                  text="Dobrý den",
                                  font=("Arial", 25))
infoText.place(relx= 0.5, rely=0.2, anchor=tkinter.CENTER)

loginOption = customtkinter.CTkButton(startFrame,
                                      text="Přihlásit se",
                                      command=lambda: loginOptionFun())
loginOption.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

registerOption = customtkinter.CTkButton(startFrame,
                                         text="Registrovat se",
                                         command=lambda:registerOptionFun())
registerOption.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)






loginFrame = customtkinter.CTkFrame(app,
                                    height=150,
                                    width=300)
#loginFrame.pack(pady=15)
loginFrame.forget()

inputEmailLogin = customtkinter.CTkEntry(loginFrame,
                                   placeholder_text="Zadejte svůj email...",
                                   height=50,
                                   width=250,
                                   border_color="gray")
inputEmailLogin.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

passEntryLogin = customtkinter.CTkEntry(loginFrame,
                                   placeholder_text="Zadejte své heslo...",
                                   height=50,
                                   width=250,
                                   show="*",
                                   border_color="gray")
passEntryLogin.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

loginButton = customtkinter.CTkButton(app, text="Přihlásit se", command=lambda: login())
#loginButton.pack(pady=5)
loginButton.forget()

loginBackButton = customtkinter.CTkButton(app, 
                                          text="Zpět",
                                          command=lambda:showFirstFrame())
loginBackButton.forget()





registerFrame = customtkinter.CTkFrame(app,
                                  height=500,
                                  width=300)
registerFrame.forget()

inputFName = customtkinter.CTkEntry(registerFrame,
                                   placeholder_text="Zadejte své křestní jméno...",
                                   height=50,
                                   width=250,
                                   border_color="gray")
inputFName.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

inputLName = customtkinter.CTkEntry(registerFrame,
                                   placeholder_text="Zadejte své příjmení...",
                                   height=50,
                                   width=250,
                                   border_color="gray")
inputLName.place(relx=0.5, rely=0.21, anchor=tkinter.CENTER)

inputAddress = customtkinter.CTkEntry(registerFrame,
                                   placeholder_text="Zadejte svou adresu...",
                                   height=50,
                                   width=250,
                                   border_color="gray")
inputAddress.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)

inputEmail = customtkinter.CTkEntry(registerFrame,
                                   placeholder_text="Zadejte svůj email...",
                                   height=50,
                                   width=250,
                                   border_color="gray")
inputEmail.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

passEntry = customtkinter.CTkEntry(registerFrame,
                                   placeholder_text="Zadejte své heslo...",
                                   height=50,
                                   width=250,
                                   border_color="gray",
                                   show="*")
passEntry.place(relx=0.5, rely=0.60, anchor=tkinter.CENTER)

passEntry2 = customtkinter.CTkEntry(registerFrame,
                                   placeholder_text="Zadejte heslo znovu...",
                                   height=50,
                                   width=250,
                                   border_color="gray",
                                   show="*")
passEntry2.place(relx=0.5, rely=0.73, anchor=tkinter.CENTER)

registerButton = customtkinter.CTkButton(registerFrame, 
                                      text="Zaregistrovat se", 
                                      command=lambda: register())
registerButton.place(relx=0.5, rely=0.82, anchor=tkinter.CENTER)

registerBackButton = customtkinter.CTkButton(registerFrame,
                                             text="Zpět",
                                             command=lambda:showFirstFrame())
registerBackButton.place(relx=0.5,rely=0.89, anchor=tkinter.CENTER)






passMessage = customtkinter.CTkLabel(app, text="Zadali jste spatne uzivatelske jmeno nebo heslo", text_color="red")
passMessage.forget()


registerMissingMessage = customtkinter.CTkLabel(registerFrame, 
                                                text="", 
                                                text_color="red")
registerMissingMessage.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)




#FRAME FOR DEFAULT WINDOW

bankFrame = customtkinter.CTkFrame(app)
bankFrame.forget()


logOutImage = customtkinter.CTkImage(Image.open("logout.png"), size=(40,40))


mainFrame = customtkinter.CTkFrame(bankFrame,
                                   height=100)
mainFrame.pack(side="top", fill="both",expand=True)




userBalanceLabel = customtkinter.CTkLabel(mainFrame,
                                       font=("Rubik", 40, "bold"),
                                       text_color="green")
userBalanceLabel.place(x=20, y=10)

userNameLabel = customtkinter.CTkLabel(mainFrame)
userNameLabel.place(x=20, y=60)

logOutButton = customtkinter.CTkButton(mainFrame,
                                       text="",
                                       image=logOutImage,
                                       bg_color="#333333",
                                       fg_color="#333333",
                                       hover_color="#434343",
                                       command=lambda:logout(),
                                       width=40)
logOutButton.place(relx=0.99, rely=0.1, anchor=tkinter.NE)


optionsFrame = customtkinter.CTkFrame(bankFrame,
                                      height=50,
                                      bg_color="#1F6AA5",
                                      fg_color="#1F6AA5")
optionsFrame.pack(side="top", fill="both",expand=True)


transactionsFrame = customtkinter.CTkScrollableFrame(bankFrame,
                                           height=500)
transactionsFrame.pack(side="top", fill="both",expand=True)





transactionButton = customtkinter.CTkButton (optionsFrame,
                                             text="Finanční operace",
                                             command=lambda:showTransactionFrame())
transactionButton.pack(side="left", fill="both", expand=True)


infoButton = customtkinter.CTkButton (optionsFrame,
                                             text="Informace",
                                             command=lambda:showInformationFrame())
infoButton.pack(side="left", fill="both", expand=True)


settingsButton = customtkinter.CTkButton (optionsFrame,
                                             text="Nastavení",
                                             command=lambda:showSettingsFrame())
settingsButton.pack(side="left", fill="both", expand=True)





backImage = customtkinter.CTkImage(Image.open("backArrow.png"), size=(40,40))




#BANK TRANSACTION FRAME

bankTransactionFrame = customtkinter.CTkFrame(app)
bankTransactionFrame.forget()

barFrame = customtkinter.CTkFrame(bankTransactionFrame,
                                  height=50,
                                  bg_color="#1F6AA5",
                                  fg_color="#1F6AA5")
barFrame.pack(side="top", fill="both", expand=True)

toChooseFrameTransaction = customtkinter.CTkFrame(bankTransactionFrame,
                                       height=600)
toChooseFrameTransaction.pack(side="top", fill="both", expand=True)


transactionBackButton = customtkinter.CTkButton(barFrame,
                                                image=backImage,
                                                text="",
                                                corner_radius=60,
                                                height=50,
                                                width=20,
                                                command=lambda:showBankFrame())
transactionBackButton.place(relx=0.1, rely=0.5,anchor=tkinter.CENTER)




transactionWithdrawButton = customtkinter.CTkButton(toChooseFrameTransaction,
                                                    height=50,
                                                    width=250,
                                                    text="Vybrat",
                                                    command=lambda:withdrawScreen())
transactionWithdrawButton.place(relx=0.5, rely= 0.2, anchor=tkinter.CENTER)

transactionDepositButton = customtkinter.CTkButton(toChooseFrameTransaction,
                                                    height=50,
                                                    width=250,
                                                    text="Vložit",
                                                    command=lambda:depostiScreen())
transactionDepositButton.place(relx=0.5, rely= 0.5, anchor=tkinter.CENTER)

transactionTransferButton = customtkinter.CTkButton(toChooseFrameTransaction,
                                                    height=50,
                                                    width=250,
                                                    text="Platba",
                                                    command=lambda:transferScreen())
transactionTransferButton.place(relx=0.5, rely= 0.8, anchor=tkinter.CENTER)





#WITHDRAW window

withdrawFrame = customtkinter.CTkFrame(app)
withdrawFrame.forget()


barFrame = customtkinter.CTkFrame(withdrawFrame,
                                  height=50,
                                  bg_color="#1F6AA5",
                                  fg_color="#1F6AA5")
barFrame.pack(side="top", fill="both", expand=True)

withdrawBackButton = customtkinter.CTkButton(barFrame,
                                                image=backImage,
                                                text="",
                                                corner_radius=60,
                                                height=50,
                                                width=20,
                                                command=lambda:showTransactionFrame())
withdrawBackButton.place(relx=0.1, rely=0.5,anchor=tkinter.CENTER)


withdrawOptionsFrame = customtkinter.CTkFrame(withdrawFrame,
                                       height=600)
withdrawOptionsFrame.pack(side="top", fill="both", expand=True)





infoWithdrawText = customtkinter.CTkLabel(withdrawOptionsFrame,
                                          text="Prosím, zadejte částku kterou si přejete vybrat:")
infoWithdrawText.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

withdrawEntry = customtkinter.CTkEntry(withdrawOptionsFrame,
                                       height=50,
                                       width=250)
withdrawEntry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


errorMessageW = customtkinter.CTkLabel(withdrawOptionsFrame,
                                      text="")
errorMessageW.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


withdrawButton = customtkinter.CTkButton(withdrawOptionsFrame,
                                                    height=50,
                                                    width=250,
                                                    text="Vybrat",
                                                    command=lambda:mainAccount.withdraw(withdrawEntry.get(), transfer))
withdrawButton.place(relx=0.5, rely= 0.5, anchor=tkinter.CENTER)





#DEPOSIT window

depositFrame = customtkinter.CTkFrame(app)
depositFrame.forget()

barFrame = customtkinter.CTkFrame(depositFrame,
                                  height=50,
                                  bg_color="#1F6AA5",
                                  fg_color="#1F6AA5")
barFrame.pack(side="top", fill="both", expand=True)

depositBackButton = customtkinter.CTkButton(barFrame,
                                                image=backImage,
                                                text="",
                                                corner_radius=60,
                                                height=50,
                                                width=20,
                                                command=lambda:showTransactionFrame())
depositBackButton.place(relx=0.1, rely=0.5,anchor=tkinter.CENTER)




depositOptionsFrame = customtkinter.CTkFrame(depositFrame,
                                       height=600)
depositOptionsFrame.pack(side="top", fill="both", expand=True)

errorMessageD = customtkinter.CTkLabel(depositOptionsFrame,
                                      text="")
errorMessageD.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)



infoDepositText = customtkinter.CTkLabel(depositOptionsFrame,
                                          text="Prosím, zadejte částku kterou si přejete vložit:")
infoDepositText.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

depositEntry = customtkinter.CTkEntry(depositOptionsFrame,
                                       height=50,
                                       width=250)
depositEntry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


depositButton = customtkinter.CTkButton(depositOptionsFrame,
                                                    height=50,
                                                    width=250,
                                                    text="Vložit",
                                                    command=lambda:mainAccount.deposit(depositEntry.get(), transfer))
depositButton.place(relx=0.5, rely= 0.5, anchor=tkinter.CENTER)




#TRANSFER window

transferFrame = customtkinter.CTkFrame(app)
transferFrame.forget()

barFrame = customtkinter.CTkFrame(transferFrame,
                                  height=50,
                                  bg_color="#1F6AA5",
                                  fg_color="#1F6AA5")
barFrame.pack(side="top", fill="both", expand=True)

transferBackButton = customtkinter.CTkButton(barFrame,
                                                image=backImage,
                                                text="",
                                                corner_radius=60,
                                                height=50,
                                                width=20,
                                                command=lambda:showTransactionFrame())
transferBackButton.place(relx=0.1, rely=0.5,anchor=tkinter.CENTER)




transferOptionsFrame = customtkinter.CTkFrame(transferFrame,
                                       height=600)
transferOptionsFrame.pack(side="top", fill="both", expand=True)





infoTransferText = customtkinter.CTkLabel(transferOptionsFrame,
                                          text="Prosím, zadejte id účtu na který chcete poslat peníze:")
infoTransferText.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

transferIdEntry = customtkinter.CTkEntry(transferOptionsFrame,
                                       height=50,
                                       width=250,
                                       border_color="gray")
transferIdEntry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


infoTransferText2 = customtkinter.CTkLabel(transferOptionsFrame,
                                          text="Prosím, zadejte částku kterou chcete poslat:")
infoTransferText2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

transferAmountEntry = customtkinter.CTkEntry(transferOptionsFrame,
                                       height=50,
                                       width=250,
                                       border_color="gray")
transferAmountEntry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


transferButton = customtkinter.CTkButton(transferOptionsFrame,
                                                    height=50,
                                                    width=250,
                                                    text="Provést platbu",
                                                    command=lambda:findReciever(transferAmountEntry.get(), transferIdEntry.get(), True))
transferButton.place(relx=0.5, rely= 0.6, anchor=tkinter.CENTER)


errorMessageT = customtkinter.CTkLabel(transferOptionsFrame,
                                      text="")
errorMessageT.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


#BANK IMFORMATION FRAME


bankInformationFrame = customtkinter.CTkFrame(app)
bankInformationFrame.forget()

barFrame = customtkinter.CTkFrame(bankInformationFrame,
                                  height=50,
                                  bg_color="#1F6AA5",
                                  fg_color="#1F6AA5")
barFrame.pack(side="top", fill="both", expand=True)

informationBackButton = customtkinter.CTkButton(barFrame,
                                                image=backImage,
                                                text="",
                                                corner_radius=60,
                                                height=50,
                                                width=20,
                                                command=lambda:showBankFrame())
informationBackButton.place(relx=0.1, rely=0.5,anchor=tkinter.CENTER)

toChooseFrameInformation = customtkinter.CTkFrame(bankInformationFrame,
                                       height=600)
toChooseFrameInformation.pack(side="top", fill="both", expand=True)




fullNameTitleLabel = customtkinter.CTkLabel(toChooseFrameInformation,
                                            font=("Rubik", 20),
                                            text_color="gray",
                                            text="Jméno")
fullNameTitleLabel.place(relx=0.1, rely=0.05, anchor=tkinter.CENTER)

fullNameLabel = customtkinter.CTkLabel(toChooseFrameInformation,
                                            font=("Rubik", 30, "bold"),
                                            text_color="#1F6AA5")
fullNameLabel.place(rely=0.1, anchor=tkinter.CENTER)
fullNameLabel.place(relx=0.025, anchor=tkinter.W)



idTitleLabel = customtkinter.CTkLabel(toChooseFrameInformation,
                                      font=("Rubik", 20),
                                      text_color="gray",
                                      text="Id")
idTitleLabel.place(relx=0.05, rely=0.2, anchor=tkinter.CENTER)

idLabel = customtkinter.CTkLabel(toChooseFrameInformation,
                                 font=("Rubik", 30, "bold"),
                                 text_color="#1F6AA5")
idLabel.place(rely=0.25, anchor=tkinter.CENTER)
idLabel.place(relx=0.025, anchor=tkinter.W)



emailTitleLabel = customtkinter.CTkLabel(toChooseFrameInformation,
                                      font=("Rubik", 20),
                                      text_color="gray",
                                      text="email")
emailTitleLabel.place(relx=0.08, rely=0.35, anchor=tkinter.CENTER)

emailLabel = customtkinter.CTkLabel(toChooseFrameInformation,
                                 font=("Rubik", 25, "bold"),
                                 text_color="#1F6AA5")
emailLabel.place(rely=0.4, anchor=tkinter.CENTER)
emailLabel.place(relx=0.025, anchor=tkinter.W)




#BANK SETTINGS FRAME

bankSettingsFrame = customtkinter.CTkFrame(app)
bankSettingsFrame.forget()

barFrame = customtkinter.CTkFrame(bankSettingsFrame,
                                  height=50,
                                  bg_color="#1F6AA5",
                                  fg_color="#1F6AA5")
barFrame.pack(side="top", fill="both", expand=True)


settingsBackButton = customtkinter.CTkButton(barFrame,
                                                image=backImage,
                                                text="",
                                                corner_radius=60,
                                                height=50,
                                                width=20,
                                                command=lambda:showBankFrame())
settingsBackButton.place(relx=0.1, rely=0.5,anchor=tkinter.CENTER)

toChooseFrameSettings = customtkinter.CTkFrame(bankSettingsFrame,
                                       height=600)
toChooseFrameSettings.pack(side="top", fill="both", expand=True)


switchVar = customtkinter.StringVar(value=parser.get("settings", "dark_mode"))

themeSwitch = customtkinter.CTkSwitch(toChooseFrameSettings,
                                      text="Povolit tmavý režim",
                                      command=themeSet,
                                      variable=switchVar,
                                      onvalue="on",
                                      offvalue="off")
themeSwitch.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)

app.mainloop()
