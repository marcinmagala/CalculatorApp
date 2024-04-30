#przepisać tworzenie przycisków na klasy i tworzenie obiektów z listy rzeczy do stworzenia

#import library
from tkinter import * 
from tkinter import font

#initialization Application
def initApp():
    
    #creating main window tkinter
    mainWindow = Tk()

    #set parameters for main window app
    def settingMainWindowParameters():
        #creating app title and app window size
        mainWindow.title("Calculator")
        mainWindow.geometry('384x531')

        #block resize app window by user
        mainWindow.resizable(width=False, height=False)

    settingMainWindowParameters()

    def creatingLogicAndWidgets():

        #create logic
        def buttonClear():
            return

        def buttonMemoryPlus():
            return

        def buttonMemoryMinus():
            return

        def buttonDeleteLastSign():
            return

        def buttonDivide():
            return

        def buttonMultiply():
            return

        def buttonPlus():
            return

        def buttonMinus():
            return

        def buttonEqual():
            return

        def buttonComma():
            return

        def buttonClick():
            return



        def creatingWidgets():

            #design font
            designFont = font.Font(size=25, weight='bold')


            #create result place 
            resultLabel = Entry(mainWindow, width=20, font=designFont)
            resultLabel.grid(row=0, column=0, columnspan=4, padx=10, pady=15)


            #create buttons
            btnClear = Button(mainWindow, text="C", pady=10, width=4, font= designFont,  command=buttonClear, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMemoryPlus = Button(mainWindow, text="M+", pady=10, width=4, font= designFont, command=buttonMemoryPlus, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMemoryMinus = Button(mainWindow, text="M-", pady=10, width=4, font= designFont, command=buttonMemoryMinus, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584" )
            btnDeleteLastSign = Button(mainWindow, text="DEL", pady=10, width= 4, font= designFont, command=buttonDeleteLastSign, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btn1 = Button(mainWindow, text="1", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn2 = Button(mainWindow, text="2", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn3 = Button(mainWindow, text="3", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn4 = Button(mainWindow, text="4", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn5 = Button(mainWindow, text="5", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn6 = Button(mainWindow, text="6", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn7 = Button(mainWindow, text="7", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn8 = Button(mainWindow, text="8", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn9 = Button(mainWindow, text="9", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btn0 = Button(mainWindow, text="0", pady=10, width=4, font= designFont,  command=lambda: buttonClick(), borderwidth=1, relief="solid", bg="white", activebackground="#8ff584")
            btnDivide = Button(mainWindow, text="/", pady=10, width=4, font= designFont,  command=buttonDivide, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMultiply = Button(mainWindow, text="*", pady=10, width=4, font= designFont,  command=buttonMultiply, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnMinus = Button(mainWindow, text="-", pady=10, width=4, font= designFont,  command=buttonMinus, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnPlus = Button(mainWindow, text="+", pady=10, width=4, font= designFont,  command=buttonPlus, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")
            btnEqual = Button(mainWindow, text="=", pady=10, width=4, font= designFont,  command=buttonEqual, borderwidth=1, relief="solid", bg="#4082ed", activebackground="#8ff584")
            btnComma = Button(mainWindow, text=",", pady=10, width=4, font= designFont,  command=buttonComma, borderwidth=1, relief="solid", bg="#e8e8e8", activebackground="#8ff584")


            #gridding buttons
            btnClear.grid(row=1, column=0, pady=6, padx=4)
            btnMemoryPlus.grid(row=1, column=1, pady=6, padx=4)
            btnMemoryMinus.grid(row=1, column=2, pady=6, padx=4)
            btnDeleteLastSign.grid(row=1, column=3, pady=6, padx=4)
            btn7.grid(row=2, column=0, pady=4, padx=4)
            btn8.grid(row=2, column=1, pady=4, padx=4)
            btn9.grid(row=2, column=2, pady=4, padx=4)
            btnDivide.grid(row=2, column=3, pady=4, padx=4)
            btn4.grid(row=3, column=0, pady=4, padx=4)
            btn5.grid(row=3, column=1, pady=4, padx=4)
            btn6.grid(row=3, column=2, pady=4, padx=4)
            btnMultiply.grid(row=3, column=3, pady=4, padx=4)
            btn1.grid(row=4, column=0, pady=4, padx=4)
            btn2.grid(row=4, column=1, pady=4, padx=4)
            btn3.grid(row=4, column=2, pady=4, padx=4)
            btnMinus.grid(row=4, column=3, pady=4, padx=4)
            btn0.grid(row=5, column=0, pady=4, padx=4)
            btnComma.grid(row=5, column=1, pady=4, padx=4)
            btnEqual.grid(row=5, column=2, pady=4, padx=4)
            btnPlus.grid(row=5, column=3, pady=4, padx=4)
        
        creatingWidgets()

    creatingLogicAndWidgets()
        
    #looping app 
    mainWindow.mainloop()

initApp()