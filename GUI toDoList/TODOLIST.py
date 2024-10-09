from tkinter import *
from PIL import Image, ImageTk
import codecs


count = 0
tasks = {}
state = 0


def addItem():
    print("pico "+str(entry.winfo_height()))
    global count
    global tasks
    text = entry.get()
    entry.delete(0, END)
    
    if (text != ""):
        
    
        x = IntVar()
    
        check_button = Checkbutton(window,
                      text=text,
                      font=("arial", 20),
                      variable=x,
                      onvalue=1,
                      offvalue=0)
        check_button.grid(row=count+2, column=0)


        delete_button = Button(window,
                               text="SMAZAT POLOŽKU",
                               image=crossImageFinal)
        delete_button.grid(row=count+2, column=1)



        delete_button.config(command=lambda chb=check_button, de=delete_button, tasks=tasks, text=text: deleteFun(chb, de, tasks, text))
        #check_button.config(command=lambda x=x, chb=check_button, de=delete_button: move(x, chb, de))
        check_button.config(command=lambda x=x, dic = tasks, txt = text, state = state: changeState(state, x, dic, txt))
        

        count = count + 1
        tasks.update({text:state})
        with codecs.open("taskFile.txt","a") as file:
            file.write(text+"-"+str(state)+"\n")
        print(list(tasks.keys()))
        print(list(tasks.values()))
        tasksList = list(tasks)
        print("tasklist: "+str(tasksList))
        
        




def deleteFun(check_button, delete_button, tasks, text):
    check_button.destroy()
    delete_button.destroy()
    tasks.pop(text)
    print(list(tasks.keys()))
    print(list(tasks.values()))
    
    with open("taskFile.txt", "r") as file:
            content = file.readlines()
            for i in range (0, len(content)):
                if content[i].startswith(text):
                    content[i] = ""
    with open("taskFile.txt", "w") as file:
        file.writelines(content)
  
  
  
    
    
def changeState(state, x, dic, txt):
    if (x.get() == 1):
        state = 1
        dic.update({txt:state})
        print(list(dic.keys()))
        print(list(dic.values()))

        
        with open("taskFile.txt", "r") as file:
            content = file.readlines()
            for i in range (0, len(content)):
                if content[i].startswith(txt):
                    content[i] = txt + "-" + "1\n"
        with open("taskFile.txt", "w") as file:
            file.writelines(content)
                            
                                
    else:
        state = 0
        dic.update({txt:state})
        print(list(dic.keys()))
        print(list(dic.values()))
        
        with open("taskFile.txt", "r") as file:
            content = file.readlines()
            for i in range (0, len(content)):
                if content[i].startswith(txt):
                    content[i] = txt + "-" + "0\n"
        with open("taskFile.txt", "w") as file:
            file.writelines(content)
  
  


        

def taskWrite():
    global count
    tasksList = list(tasks)
    print(tasksList)
    i = 0
    for line in file: 
        for i in range(0,len(line)):
            if line[i] == "-":
                kslice = slice(0,i)
                key = line[kslice]
                vslice = slice(i+1, len(line)-1)
                value = line[vslice]
                tasks.update({key:value})
                print("key loaded: "+key)
                print("value loaded: "+value)
                
                
            
                
                #část na vytvoření labelů podle položek v souboru
                print("Typ: "+str(type(value)))
                loadedState = int(value)
                x = IntVar()
                x.set(loadedState)
                check_button = Checkbutton(window,
                                text=key,
                                font=("arial", 20),
                                variable=x,
                                onvalue=1,
                                offvalue=0)
                check_button.grid(row=count+2, column=0)
                delete_button = Button(window,
                                       text="SMAZAT POLOŽKU",
                                       image=crossImageFinal)
                delete_button = Button(window,
                                        text="SMAZAT POLOŽKU",
                                        image=crossImageFinal)
                delete_button.grid(row=count+2, column=1)
                delete_button.config(command=lambda chb=check_button, de=delete_button, tasks=tasks, text=key: deleteFun(chb, de, tasks, text))
                #check_button.config(command=lambda x=x, chb=check_button, de=delete_button: move(x, chb, de))
                check_button.config(command=lambda x=x, dic = tasks, txt = key, state = state: changeState(state, x, dic, txt))
                count += 1
                
                
                
                
    tasksList = list(tasks)
    print("tasklist: "+str(tasksList))
    
    
       
    

    
    
    
    
    
       






window = Tk()
window.geometry("600x800")
window.title("To do list")




crossImage = Image.open("Cross.png")
crossImageResize = crossImage.resize((25,25))
crossImageFinal = ImageTk.PhotoImage(crossImageResize)  #převede to do formátu se kterým umí Tkinter pracovat ig


try:
    with codecs.open("taskFile.txt", "x") as file:
        taskWrite()
except FileExistsError:
    with codecs.open("taskFile.txt", "r") as file:
        taskWrite()
except TypeError:
    with codecs.open("taskFile.txt", "r") as file:
        taskWrite()
except:
    print("idk")


entry = Entry(window,
              font= ("arial", 30))
entry.grid(row=0, column=0)
#entry.place(relx=0.5, rely=0.05, anchor=CENTER)

add_button = Button(window,
                    text="PŘIDAT",
                    command=addItem)
add_button.grid(row=1, column=0)
#add_button.place(relx=0.5, rely=0.05, anchor=CENTER)



window.mainloop()
