import tkinter
import tkinter
import sys

class CoreGUI(object):
    def __init__(self, parent):
        text_box = tkinter.Text(parent, state=tkinter.DISABLED)
        text_box.pack()

        output_button = tkinter.Button(parent, text="Output", command=self.main)
        output_button.pack()

    def main(self):
        print ("Std Output")
        raise ValueError("Std Error")

root = tkinter.Tk()
CoreGUI(root)
root.mainloop()
