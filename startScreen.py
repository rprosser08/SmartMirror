from tkinter import *
from tkinter import ttk
import tkinter, MirrorMainFrame

class StartWindow:
    def __init__(self, master):
        self.master = master

        StartWindow.instantiateGrid()
        StartWindow.createFrames()
        StartWindow.createLabels()
        StartWindow.createEntrys()
        StartWindow.createSubmitButton(self)

    def instantiateGrid():
        # Configures the columns for the grid for the window
        for x in range(3):
            root.columnconfigure(x, weight=1)
        
        # Configures the rows for the grid for the window
        for y in range(3):
            root.rowconfigure(y, weight=1)

    def createFrames():
        global zipFrame

        # Creates the zip code frame
        zipFrame = Frame(root)
        zipFrame.grid(row=1, column=1)

    def createLabels():
        # Zip label
        zipLabel = Label(zipFrame, text="Please Enter Your Zip Code: ", bg="black", fg="white", font=("TkDefaultFont", 20))
        zipLabel.pack(side=LEFT)

    def createEntrys():
        global zipString

        zipString = tkinter.StringVar()

        # Zip code user entry box
        zipEntry = Entry(zipFrame, textvariable=zipString, bg="black", fg="white")
        zipEntry.pack()

    def createSubmitButton(self):
        # Create the submit button
        # submitButton = Button(root, text="Submit", bg="black", fg="white", command=self.getUserData)
        submitButton = ttk.Button(root, text="Submit", command=self.getUserData)
        submitButton.grid(row=1, column=2)

    def getUserData(self):
        #Close the start up window
        root.destroy()

        #Call the mirror main frame main function to start that tkinter window
        MirrorMainFrame.main(zipString.get())

if __name__ == "__main__":
    root = Tk()

    root.title("Smart Mirror")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    StartWindow(root)

    root.mainloop()