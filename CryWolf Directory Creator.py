import tkinter
import backend
from tkinter import *

class Application(Frame):
    def packit(self):
        # logo and input
        self.logo.pack(side=TOP)
        self.labelJurisdictionName.pack(side=TOP)
        self.inputJurisdictionName.pack(side=TOP)
        # check boxes for folders
        self.checkframe.pack(side=TOP, pady=20)
        self.checkBoxOne.pack(side=TOP, anchor=W)
        self.checkBoxTwo.pack(side=TOP, anchor=W)
        self.checkBoxThree.pack(side=TOP, anchor=W)
        self.checkBoxFour.pack(side=TOP, anchor=W)
        self.checkBoxFive.pack(side=TOP, anchor=W)
        self.checkBoxSix.pack(side=TOP, anchor=W)
        self.checkBoxSeven.pack(side=TOP, anchor=W)
        self.checkBoxEight.pack(side=TOP, anchor=W)
        self.checkBoxNine.pack(side=TOP, anchor=W)
        self.checkBoxEight.pack(side=TOP, anchor=W)
        self.checkBoxTen.pack(side=TOP, anchor=W)
        # button and return text
        self.createButton.pack(side=TOP)
        self.labelResultsTitle.pack(side=TOP)
        self.labelResults.pack(side=TOP)

        self.signature.pack(side=BOTTOM, anchor=W)

        # main loop to run the form
        self.window.mainloop()

    def createFiles(self):
        self.counter = 0
        self.title = []
        if self.check1.get() == True:
            self.counter += 1
            self.title.append('Payments')
        else:
            pass
        if self.check2.get() == True:
            self.counter += 1
            self.title.append('Appeals')
        else:
            pass
        if self.check3.get() == True:
            self.counter += 1
            self.title.append('Bank Reconciliations')
        else:
            pass
        if self.check4.get() == True:
            self.counter += 1
            self.title.append('End Of Month Reports')
        else:
            pass
        if self.check5.get() == True:
            self.counter += 1
            self.title.append('Refunds')
        else:
            pass
        if self.check6.get() == True:
            self.counter += 1
            self.title.append('Collections')
        else:
            pass
        if self.check7.get() == True:
            self.counter += 1
            self.title.append('Spreadsheets')
        else:
            pass
        if self.check8.get() == True:
            self.counter += 1
            self.title.append('Returned Checks')
        else:
            pass
        if self.check9.get() == True:
            self.counter += 1
            self.title.append('Registration Forms')
        else:
            pass
        if self.check10.get() == True:
            self.counter += 1
            self.title.append('Misc')
        else:
            pass
        print(self.counter)


        jurisdiction = backend.pullJD(self)
        self.result.set("Working...")
        update = backend.makeCWDirectory(self, jurisdiction, self.counter, self.title)
        if update == True:
            self.result.set("Directory Created Succesfully!")
        else:
            pass



    def makeWindow(self):
        self.window = tkinter.Tk()
        self.window.title('CryWolf Directory Creator')
        self.window.geometry("375x525")
        self.window.iconbitmap('icon.ico')

        self.img = tkinter.PhotoImage(file="logo_CryWolf.png")
        # setting a default string for "load"
        self.result = StringVar()
        self.result.set("Waiting...")

        # saving myself from typing self a million more times
        window = self.window
        img = self.img

        #basic labels and buttons
        self.labelJurisdictionName = tkinter.Label(window, text="New Jurisdiction Name:")
        self.inputJurisdictionName = tkinter.Entry(window)
        self.createButton = tkinter.Button(window, text="Create Directories", command=self.createFiles)
        self.createButton.bind("<Return>", self.createFiles)
        self.logo = tkinter.Label(window, anchor='n', image=self.img)
        self.labelResultsTitle = tkinter.Label(window, text="Status:")
        self.labelResults = tkinter.Label(window, textvariable=self.result)

        #check box variables

        self.check1 = BooleanVar()
        self.check2 = BooleanVar()
        self.check3 = BooleanVar()
        self.check4 = BooleanVar()
        self.check5 = BooleanVar()
        self.check6 = BooleanVar()
        self.check7 = BooleanVar()
        self.check8 = BooleanVar()
        self.check9 = BooleanVar()
        self.check10 = BooleanVar()




        # the check boxes for different folders
        self.checkframe = LabelFrame(self.window, text='Folders:')
        self.checkBoxOne = tkinter.Checkbutton(self.checkframe, text=" Payments", variable=self.check1)
        self.checkBoxTwo = tkinter.Checkbutton(self.checkframe, text=" Appeals", variable=self.check2)
        self.checkBoxThree = tkinter.Checkbutton(self.checkframe, text=" Bank Reconciliations", variable=self.check3)
        self.checkBoxFour = tkinter.Checkbutton(self.checkframe, text=" End of Month Reports", variable=self.check4)
        self.checkBoxFive = tkinter.Checkbutton(self.checkframe, text=" Refunds", variable=self.check5)
        self.checkBoxSix = tkinter.Checkbutton(self.checkframe, text=" Collections", variable=self.check6)
        self.checkBoxSeven = tkinter.Checkbutton(self.checkframe, text=" Spreadsheets", variable=self.check7)
        self.checkBoxEight = tkinter.Checkbutton(self.checkframe, text=" Returned Checks", variable=self.check8)
        self.checkBoxNine = tkinter.Checkbutton(self.checkframe, text=" Registration Forms", variable=self.check9)
        self.checkBoxTen = tkinter.Checkbutton(self.checkframe, text=" Misc", variable=self.check10)

        self.signature = tkinter.Label(window, text="Francisco Costoya 2019", fg='cornsilk3')




        self.packit()

    def __init__(self):
        self.makeWindow()
Application()
