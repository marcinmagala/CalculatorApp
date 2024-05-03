#przepisać tworzenie przycisków na klasy i tworzenie obiektów z listy rzeczy do stworzenia
#memory może narazie dodawać tylko pojedyncze liczby = najpierw powinno policzyć wyrażenie a dopiero potem je zapisać
#działania na liczbach
#dzielenie przez zero


#import library
from tkinter import * 
from tkinter import font
import re
from math import *


countClicked = 0
memory = 0

#initialization Application
def initApp():

   
    
    #creating main window tkinter
    mainWindow = Tk()

    #design font
    designFont = font.Font(size=25, weight='bold')


    #create result place 
    resultLabel = Entry(mainWindow, width=20, font=designFont)
    resultLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

    # make calculations
    def makeResult():
        #multiply and devide
        preResult = resultLabel.get()
        tempResult = re.findall(r"((\d*\.?\d*)(\*|\/){1}(\d*\.?\d*)){1,}",preResult)
        # print(preResult)
        # print(tempResult)
        # print(tempResult[0][1])
        # print(tempResult[0][2])
        # print(tempResult[0][3])
        if(tempResult[0][2] == "*"):
            result = round(float(tempResult[0][1])*float(tempResult[0][3]))
        if(tempResult[0][2] == "/"):
            if(tempResult[0][3] == "0"):
                resultLabel.delete(0,END)
                resultLabel.insert(0, "Math ERROR!")
                return
            else:
                result = round(float(tempResult[0][1])/float(tempResult[0][3]))
        resultLabel.delete(0,END)
        resultLabel.insert(0, str(float(result)))
        print(result)
        
        


    #set parameters for main window app
    def settingMainWindowParameters():
        #creating app title and app window size
        mainWindow.title("Calculator")
        mainWindow.geometry('384x620')

        #block resize app window by user
        mainWindow.resizable(width=False, height=False)

    settingMainWindowParameters()

    

    def creatingLogicAndWidgets():

        #create logic

        #insert number by buttons 
        
        def buttonClick(number):
            global countClicked
            #Exeption double special sign
            if(len(resultLabel.get())>0):
    
                if (resultLabel.get()[-1] == "+" and number == "+"):  
                    return
                if (resultLabel.get()[-1] == "+" and number == "/"):  
                    return
                if (resultLabel.get()[-1] == "+" and number == "*"):  
                    return
                if (resultLabel.get()[-1] == "+" and number == "."):  
                    return
                if (resultLabel.get()[-1] == "-" and number == "+"):  
                    return
                if (resultLabel.get()[-1] == "-" and number == "*"):  
                    return
                if (resultLabel.get()[-1] == "-" and number == "/"):  
                    return
                if (resultLabel.get()[-1] == "-" and number == "."):  
                    return
                if (resultLabel.get()[-1] == "*" and number == "*"):  
                    return
                if (resultLabel.get()[-1] == "*" and number == "/"):  
                    return
                if (resultLabel.get()[-1] == "*" and number == "."):  
                    return
                if (resultLabel.get()[-1] == "/" and number == "*"):  
                    return
                if (resultLabel.get()[-1] == "/" and number == "/"):  
                    return
                if (resultLabel.get()[-1] == "/" and number == "."):  
                    return
                if (resultLabel.get()[-1] == "." and number == "+"):  
                    return
                if (resultLabel.get()[-1] == "." and number == "-"):  
                    return
                if (resultLabel.get()[-1] == "." and number == "/"):  
                    return
                if (resultLabel.get()[-1] == "." and number == "*"):  
                    return
                if (resultLabel.get()[-1] == "." and number == "."):  
                    return
                if (resultLabel.get()[-1] == "-" and number == "-"):
                    print("nie wiem po co print ale bez niego nie działa")
                    
                    
            
            #maximum digit in line to 18
        
            countClicked += 1
            print(countClicked)
            
            if countClicked < 19:
                
            
                currentLabel = resultLabel.get()
                resultLabel.delete(0,END)
                resultLabel.insert(0, str(currentLabel) + str(number))

                # --
                tempLabel = resultLabel.get().replace("--","+")
                resultLabel.delete(0,END)
                resultLabel.insert(len(resultLabel.get()), tempLabel)

                # ++
                tempLabel = resultLabel.get().replace("++","+")
                resultLabel.delete(0,END)
                resultLabel.insert(len(resultLabel.get()), tempLabel)
                
            
            

        def buttonClear():
            global countClicked
            countClicked = 0
            resultLabel.delete(0,END)
            

        def buttonMemoryPlus():
            global memory
            if (len(resultLabel.get())>0):
                memory = memory + int(resultLabel.get())
                print(memory)
            

        def buttonMemoryMinus():
            global memory
            if (len(resultLabel.get())>0):
                memory = memory - int(resultLabel.get())
                print(memory)
        
        def buttonMemoryClear():
            global memory
            memory = 0
            print(memory)
        
        def buttonMemorySave():
            global memory
            if (len(resultLabel.get())>0):

                memory = int(resultLabel.get())
                print(memory)
        
        def buttonMemoryRead():
            
            resultLabel.insert(len(resultLabel.get()), memory)
            print(memory)
        
        def buttonChangeFirstSign():
            if (len(resultLabel.get()) > 0 and resultLabel.get()[0] == "+"):
                    temp = resultLabel.get().replace("+","")
                    resultLabel.delete(0,END)
                    resultLabel.insert(0, "-" + str(temp))
                    return
            
            if (len(resultLabel.get()) > 0 and resultLabel.get()[0] == "-"):
                    temp = resultLabel.get().replace("-","")
                    resultLabel.delete(0,END)
                    resultLabel.insert(0, "+" + str(temp))
            try:
                int(resultLabel.get()[0])
            except:
                return
            else:
                print('llll')
                temp = resultLabel.get()
                resultLabel.delete(0,END)
                resultLabel.insert(0, "-" + str(temp))
            

        def buttonDeleteLastSign():
            resultLabel.delete(len(resultLabel.get())-1,END)
            global countClicked
            countClicked -=1
            

        def buttonEqual():
            #show result
            makeResult()
            # resultLabel.delete(0,END)
            # resultLabel.insert(0, str(makeResult()))

            global countClicked
            countClicked = len(resultLabel.get())
            



        def creatingWidgets():

            # #design font
            # global designFont = font.Font(size=25, weight='bold')


            # #create result place 
            # resultLabel = Entry(mainWindow, width=20, font=designFont)
            # resultLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=15)


            #create buttons
            btnClear = Button(mainWindow, text="C", pady=10, width=4, font= designFont,  command=buttonClear, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMemoryPlus = Button(mainWindow, text="M+", pady=10, width=4, font= designFont, command=buttonMemoryPlus, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMemoryMinus = Button(mainWindow, text="M-", pady=10, width=4, font= designFont, command=buttonMemoryMinus, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMemoryClear = Button(mainWindow, text="MC", pady=10, width=4, font= designFont, command=buttonMemoryClear, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMemoryRead = Button(mainWindow, text="MR", pady=10, width=4, font= designFont, command=buttonMemoryRead, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMemorySave = Button(mainWindow, text="MS", pady=10, width=4, font= designFont, command=buttonMemorySave, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnChangeFirstSign = Button(mainWindow, text="+/-", pady=10, width=4, font= designFont, command=buttonChangeFirstSign, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnDeleteLastSign = Button(mainWindow, text="DEL", pady=10, width= 4, font= designFont, command=buttonDeleteLastSign, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btn1 = Button(mainWindow, text="1", pady=10, width=4, font= designFont,  command=lambda: buttonClick(1), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn2 = Button(mainWindow, text="2", pady=10, width=4, font= designFont,  command=lambda: buttonClick(2), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn3 = Button(mainWindow, text="3", pady=10, width=4, font= designFont,  command=lambda: buttonClick(3), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn4 = Button(mainWindow, text="4", pady=10, width=4, font= designFont,  command=lambda: buttonClick(4), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn5 = Button(mainWindow, text="5", pady=10, width=4, font= designFont,  command=lambda: buttonClick(5), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn6 = Button(mainWindow, text="6", pady=10, width=4, font= designFont,  command=lambda: buttonClick(6), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn7 = Button(mainWindow, text="7", pady=10, width=4, font= designFont,  command=lambda: buttonClick(7), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn8 = Button(mainWindow, text="8", pady=10, width=4, font= designFont,  command=lambda: buttonClick(8), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn9 = Button(mainWindow, text="9", pady=10, width=4, font= designFont,  command=lambda: buttonClick(9), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn0 = Button(mainWindow, text="0", pady=10, width=4, font= designFont,  command=lambda: buttonClick(0), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btnDivide = Button(mainWindow, text="/", pady=10, width=4, font= designFont,  command=lambda: buttonClick("/"), borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMultiply = Button(mainWindow, text="*", pady=10, width=4, font= designFont,  command=lambda: buttonClick("*"), borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMinus = Button(mainWindow, text="-", pady=10, width=4, font= designFont,  command=lambda: buttonClick("-"), borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnPlus = Button(mainWindow, text="+", pady=10, width=4, font= designFont,  command=lambda: buttonClick("+"), borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnEqual = Button(mainWindow, text="=", pady=10, width=4, font= designFont,  command=buttonEqual, borderwidth=1, relief="solid", bg="#4082ed", activebackground="#8ff584")
            btnComma = Button(mainWindow, text=".", pady=10, width=4, font= designFont,  command=lambda: buttonClick("."), borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")


            #gridding buttons
            btnMemoryRead.grid(row=1, column=0, pady=4, padx=4)
            btnMemoryPlus.grid(row=1, column=1, pady=4, padx=4)
            btnMemoryMinus.grid(row=1, column=2, pady=4, padx=4)
            btnMemorySave.grid(row=1, column=3, pady=4, padx=4)
            btnChangeFirstSign.grid(row=6, column=0, pady=4, padx=4)
            btnMemoryClear.grid(row=2, column=0, pady=4, padx=4)
            btnClear.grid(row=2, column=1, pady=4, padx=4)
            btnDeleteLastSign.grid(row=2, column=2, pady=4, padx=4)
            btn7.grid(row=3, column=0, pady=4, padx=4)
            btn8.grid(row=3, column=1, pady=4, padx=4)
            btn9.grid(row=3, column=2, pady=4, padx=4)
            btnDivide.grid(row=2, column=3, pady=4, padx=4)
            btn4.grid(row=4, column=0, pady=4, padx=4)
            btn5.grid(row=4, column=1, pady=4, padx=4)
            btn6.grid(row=4, column=2, pady=4, padx=4)
            btnMultiply.grid(row=3, column=3, pady=4, padx=4)
            btn1.grid(row=5, column=0, pady=4, padx=4)
            btn2.grid(row=5, column=1, pady=4, padx=4)
            btn3.grid(row=5, column=2, pady=4, padx=4)
            btnMinus.grid(row=4, column=3, pady=4, padx=4)
            btn0.grid(row=6, column=1, pady=4, padx=4)
            btnComma.grid(row=6, column=2, pady=4, padx=4)
            btnEqual.grid(row=6, column=3, pady=4, padx=4)
            btnPlus.grid(row=5, column=3, pady=4, padx=4)
        
        creatingWidgets()
        
        

    creatingLogicAndWidgets()
        
    #looping app 
    mainWindow.mainloop()

initApp()