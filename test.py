from tkinter import * 
from tkinter.ttk import *
  
master = Tk() 
master.geometry("175x175") 
  
v = StringVar(master, "1") 
  
values = {"RadioButton 1" : "1", 
          "RadioButton 2" : "2", 
          "RadioButton 3" : "3", 
          "RadioButton 4" : "4", 
          "RadioButton 5" : "5"} 
  
for (text, value) in values.items(): 
    Radiobutton(master, text = text, variable = v, 
        value = value).pack(side = TOP, ipady = 5) 
  
mainloop() 