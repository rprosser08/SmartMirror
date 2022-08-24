from tkinter import *
import tkinter

class StartWindow:
    def __init__(self, master):
        self.master = master

        StartWindow.instantiateGrid()
        StartWindow.createFrames()
        StartWindow.createLabels()
        StartWindow.createEntrys()
        StartWindow.createSubmitButton()

    def instantiateGrid():
        # Configures the columns for the grid for the window
        for x in range(3):
            root.columnconfigure(x, weight=1)
        
        # Configures the rows for the grid for the window
        for y in range(15):
            root.rowconfigure(y, weight=1)

    def createFrames():
        global cityFrame, stateFrame, countryFrame

        # Creates the city frame
        cityFrame = Frame(root)
        cityFrame.grid(row=6, column=1)

        # Creates the state frame
        stateFrame = Frame(root)
        stateFrame.grid(row=7, column=1)

        # Creates the country frame
        countryFrame = Frame(root)
        countryFrame.grid(row=8, column=1)
        
    def createLabels():
        # City label
        cityLabel = Label(cityFrame, text="City:\t\t", bg="black", fg="white", font=("TkDefaultFont", 20))
        cityLabel.pack(side=LEFT)

        # State label
        stateLabel = Label(stateFrame, text="State Abbreviation:\t", bg="black", fg="white", font=("TkDefaultFont", 20))
        stateLabel.pack(side=LEFT)

        # Country label
        countryLabel = Label(countryFrame, text="Country Abbreviation:\t", bg="black", fg="white", font=("TkDefaultFont", 20))
        countryLabel.pack(side=LEFT)

    def createEntrys():
        global cityString, stateString, countryString

        # varibles to store the user input strings
        cityString = tkinter.StringVar()
        stateString = tkinter.StringVar()
        countryString = tkinter.StringVar()

        # City user text entry box
        cityEntry = Entry(cityFrame, textvariable=cityString, bg="black", fg="white")
        cityEntry.pack()
        cityEntry.focus()

        # State user entry box
        stateEntry = Entry(stateFrame, textvariable=stateString, bg="black", fg="white")
        stateEntry.pack()

        # Country user entry box
        countryEntry = Entry(countryFrame, textvariable=countryString, bg="black", fg="white")
        countryEntry.pack()

    def createSubmitButton():
        # Create the submit button
        submitButton = Button(root, text="Submit", bg="black", fg="white", command=StartWindow.getUserData)
        submitButton.grid(row=9, column=1)

    def getUserData():
        print(cityString.get())
        print(stateString.get())
        print(countryString.get())


if __name__ == "__main__":
    root = Tk()

    root.title("Smart Mirror")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    StartWindow(root)

    root.mainloop()