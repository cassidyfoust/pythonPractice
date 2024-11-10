import tkinter as tk

# ------------------ GUI class and methods ----------------

class BasicGui:

    def __init__(self):
        self.mainWin = tk.Tk()
        quitButton = tk.Button(self.mainWin, text="Quit",
                               font="Arial 16", command=self.quit)
        quitButton.grid(row=1, column=1)
        helloButton = tk.Button(self.mainWin, text="Hello",
                               font="Arial 16", command=self.quit)
        helloButton.grid(row=1, column=2)
        goodbyeButton = tk.Button(self.mainWin, text="Goodbye",
                               font="Arial 16", command=self.quit)
        goodbyeButton.grid(row=1, column=3)
        welcomeLabel = tk.Label(self.mainWin, text="Welcome", font="Arial 16")

        """Add a label to this GUI, to the right of the buttons,
        and in the same row as the Hello button. Use the Label function to create the label,
        and give it the text "Welcome". Assign this label object to an object variable,
        by marking the variable name with self.. Use the grid method (a method of the label 
        widget object) to place the label in the window. """

    def run(self):
        self.mainWin.mainloop()

    def quit(self):
        """This is a callback method attached to the quit button.
        It destroys the main window, which ends the program"""
        self.mainWin.destroy()

# ------------------ Main program ----------------------

myGui = BasicGui()
myGui.run()