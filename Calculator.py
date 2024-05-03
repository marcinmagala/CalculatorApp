
#import library
from tkinter import * 
from tkinter import font
import re
from math import *


countClicked = 0
countSpecialClicked = 0
memory = 0
result = ""

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
        global result

        #multiply and devide
        preResult = resultLabel.get()
        tempResult = re.findall(r"((\d*\.?\d*)(\*|\/|\+|\-){1}(\d*\.?\d*))",preResult)
        #multipy two minus
        if (len(tempResult)>1):
            if(tempResult[1][0] == "*"):
                resultLabel.delete(0,END)
                resultLabel.insert(0, float(tempResult[0][0])*float(tempResult[2][0]))
                return
        
        #devide two minus
        if (len(tempResult)>1):
            if(tempResult[1][0] == "/"):
                resultLabel.delete(0,END)
                resultLabel.insert(0, float(tempResult[0][0])/float(tempResult[2][0]))
                return

        if (len(tempResult)>2):
            del tempResult[1]
        

        # ?mixed +*?
        if len(tempResult)>1:
            if(tempResult[0][2] == "+"):
                if(tempResult[1][2] == "*"):
                    resultLabel.delete(0,END)
                    result = float(tempResult[0][3]) * float(tempResult[1][3])
                    result = result + float(tempResult[0][1]) 
        # ?mixed +/?
        if len(tempResult)>1:
            if(tempResult[0][2] == "+"):
                if(tempResult[1][2] == "/"):
                    if(tempResult[1][3] == "0"):
                        resultLabel.delete(0,END)
                        resultLabel.insert(0, "Math ERROR!")
                        return
                    else:
                        resultLabel.delete(0,END)
                        result = float(tempResult[0][3]) / float(tempResult[1][3])
                        result = result + float(tempResult[0][1]) 
        # ?mixed -*?
        if len(tempResult)>1:
            if(tempResult[0][2] == "-"):
                if(tempResult[1][2] == "*"):
                    resultLabel.delete(0,END)
                    result = float(tempResult[0][3]) * float(tempResult[1][3])
                    if (tempResult[0][1] == ''):
                        resultLabel.delete(0,END)
                        resultLabel.insert(0, -result)
                        return
                    else:
                        result = float(tempResult[0][1]) - result
        # ?mixed -/?
        if len(tempResult)>1:
            if(tempResult[0][2] == "-"):
                if(tempResult[1][2] == "/"):
                    if(tempResult[1][3] == "0"):
                        resultLabel.delete(0,END)
                        resultLabel.insert(0, "Math ERROR!")
                        return
                    else:
                        resultLabel.delete(0,END)
                        result = float(tempResult[0][3]) / float(tempResult[1][3])
                        if (tempResult[0][1] == ''):
                            resultLabel.delete(0,END)
                            resultLabel.insert(0, -result)
                            return
                        else:
                            result = float(tempResult[0][1]) - result
        # ?mixed *+?
        if len(tempResult)>1:
            if(tempResult[0][2] == "*"):
                if(tempResult[1][2] == "+"):
                    resultLabel.delete(0,END)
                    result = float(tempResult[0][1]) * float(tempResult[0][3])
                    result = result + float(tempResult[1][3]) 
        # ?mixed *-?
        if len(tempResult)>1:
            if(tempResult[0][2] == "*"):
                if(tempResult[1][2] == "-"):
                    resultLabel.delete(0,END)
                    if (tempResult[0][3] == ''):
                            resultLabel.delete(0,END)
                            resultLabel.insert(0, float(tempResult[0][1]) * float(tempResult[1][0]) )
                            return
                    else:
                        result = float(tempResult[0][1]) * float(tempResult[0][3])
                        result = result - float(tempResult[1][3]) 
        # ?mixed /+?
        if len(tempResult)>1:
            if(tempResult[0][2] == "/"):
                if(tempResult[1][2] == "+"):
                    if(tempResult[0][3] == "0"):
                        resultLabel.delete(0,END)
                        resultLabel.insert(0, "Math ERROR!")
                        return
                    else:
                        resultLabel.delete(0,END)
                        result = float(tempResult[0][1]) / float(tempResult[0][3])
                        result = result + float(tempResult[1][3])
        # ?mixed /-?
        if len(tempResult)>1:
            if(tempResult[0][2] == "/"):
                if(tempResult[1][2] == "-"):
                    if(tempResult[0][3] == "0"):
                        resultLabel.delete(0,END)
                        resultLabel.insert(0, "Math ERROR!")
                        return
                    else:
                        resultLabel.delete(0,END)
                        if (tempResult[0][3] == ''):
                            resultLabel.delete(0,END)
                            resultLabel.insert(0, float(tempResult[0][1]) / float(tempResult[1][0]) )
                            return
                        else:
                            result = float(tempResult[0][1]) / float(tempResult[0][3])
                            result = result - float(tempResult[1][3])
                                     



        # *
        if(tempResult[0][2] == "*") and len(tempResult)<2:
            result = float(tempResult[0][1])*float(tempResult[0][3])
        # **
        if len(tempResult)>1:
            if(tempResult[1][2] == "*"):
                if result == "":
                    result = 1
                result = result * float(tempResult[1][3])
                
        # /
        if(tempResult[0][2] == "/") and len(tempResult)<2:
            if(tempResult[0][3] == "0"):
                resultLabel.delete(0,END)
                resultLabel.insert(0, "Math ERROR!")
                return
            else:
                result = float(tempResult[0][1])/float(tempResult[0][3])
        # //
        if len(tempResult)>1:
            if(tempResult[1][2] == "/"):
                if(tempResult[1][3] == "0"):
                    resultLabel.delete(0,END)
                    resultLabel.insert(0, "Math ERROR!")
                    return
                else:
                    if result == "":
                        result = 0
                    result = result / float(tempResult[1][3])          
        
        # +
        if(tempResult[0][2] == "+") and len(tempResult)<2:
            if result == "":
                result = 0
            if (tempResult[0][1] == ''):
                    resultLabel.delete(0,END)
                    resultLabel.insert(0, "Syntax ERROR!")
                    return
            else:
                result = float(tempResult[0][1])+float(tempResult[0][3])
        # ++
        if len(tempResult)>1:
            if(tempResult[1][2] == "+"):
                if result == "":
                    result = 0
                result = float(tempResult[0][1]) + float(tempResult[0][3])
                result = result + float(tempResult[1][3])
        # -
        if(tempResult[0][2] == "-") and len(tempResult)<3:
            if result == "":
                result = 0
            if (tempResult[0][1] == ''):
                result = float(tempResult[0][0])-float(tempResult[1][0])
            else:
                result = float(tempResult[0][1])-float(tempResult[0][3])
        # --
        if len(tempResult)>2:
            if(tempResult[1][2] == "-"):
                if (tempResult[0][1] == ''):
                    resultLabel.delete(0,END)
                    resultLabel.insert(0, "Syntax ERROR!")
                    return
                else:
                    if result == "":
                        result = 0
                    result = float(tempResult[0][1]) - float(tempResult[0][3])
                    result = result - float(tempResult[1][3])        


# WYNIK 
        resultLabel.delete(0,END)
        resultLabel.insert(0, str(float(result)))

        # set countClicked
        global countClicked
        countClicked = len(resultLabel.get())    
        
        


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
            global countSpecialClicked

            #max three operations
            if (number == "+" or number == "-" or number == "*" or number == "/"):
                countSpecialClicked += 1

            

            if resultLabel.get() == "Math ERROR!":
                resultLabel.delete(0,END)
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
                    print("")
                    
                    
            
            #maximum digit in line to 18
            countClicked += 1
            
            if countClicked < 19 :
                if (countSpecialClicked > 2): 
                    if (number == "+" or number == "-" or number == "/" or number == "*"):
                        number = ""

                
            
                currentLabel = resultLabel.get()
                resultLabel.delete(0,END)
                resultLabel.insert(0, str(currentLabel) + str(number))

                # --
                tempLabel = resultLabel.get().replace("--","+")
                resultLabel.delete(0,END)
                resultLabel.insert(len(resultLabel.get()), tempLabel)
                countClicked = len(resultLabel.get())

            
                

                #+-
                tempLabel = resultLabel.get().replace("+-","-")
                resultLabel.delete(0,END)
                resultLabel.insert(len(resultLabel.get()), tempLabel)
                countClicked = len(resultLabel.get())

                
                

                # ++
                tempLabel = resultLabel.get().replace("++","+")
                resultLabel.delete(0,END)
                resultLabel.insert(len(resultLabel.get()), tempLabel)
                countClicked = len(resultLabel.get())

                

                
                
                
            
            

        def buttonClear():
            global countClicked
            countClicked = 0
            resultLabel.delete(0,END)

            global result
            result = ""

            global countSpecialClicked
            countSpecialClicked = 0
            

        def buttonMemoryPlus():
            global memory
            if (len(resultLabel.get())>0):
                memory = memory + float(resultLabel.get())
            

        def buttonMemoryMinus():
            global memory
            if (len(resultLabel.get())>0):
                memory = memory - float(resultLabel.get())
        
        def buttonMemoryClear():
            global memory
            memory = 0
        
        def buttonMemorySave():
            global memory
            if (len(resultLabel.get())>0):

                memory = float(resultLabel.get())
        
        def buttonMemoryRead():
            global memory
            memory = "+" + str(memory)
            resultLabel.insert(len(resultLabel.get()), memory)
        
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

            global countClicked
            countClicked = len(resultLabel.get())

            global countSpecialClicked
            countSpecialClicked = 0

        
            



        def creatingWidgets():

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