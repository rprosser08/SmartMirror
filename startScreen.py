from tkinter import *
import tkinter, MirrorMainFrame

class StartWindow:
    def __init__(self, master):
        self.master = master

        root.bind("<Return>", StartWindow.getUserData)

        StartWindow.createFrames()
        StartWindow.createLabels()
        StartWindow.createEntrys()

    def createFrames():
        global zipFrame

        # Creates the zip code frame
        zipFrame = Frame(root)
        # zipFrame.grid(row=1, column=1)
        zipFrame.place(relx=0.3, rely=0.5)

    def createLabels():
        # Zip label
        zipLabel = Label(zipFrame, text="Please Enter Your Zip Code: ", bg="black", fg="white", font=("TkDefaultFont", 20))
        zipLabel.pack(side=LEFT)

    def createEntrys():
        global zipString

        zipString = tkinter.StringVar()
        # Zip code user entry box
        zipEntry = Entry(zipFrame, textvariable=zipString, bg="black", fg="white")
        zipEntry.focus()
        zipEntry.pack()

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