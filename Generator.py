from random import choice
import string
from time import sleep
from tkinter import *
import _thread

# Setting default background color
bg = "#FFF"
bg_action = "#555"

# Boot/Conf screen
root = Tk()
root.title("Generator")
root.geometry("400x300+200+200")
root.resizable(False, False)
root.iconbitmap("Icon.ico")
root.config(bg=bg)

# Reset variable
var1     = IntVar()
var2     = IntVar()
var3     = IntVar()
scaleVar = IntVar()


labelTitle = Label (root, text="Password Generator!", 
                          font="Terminal 22", 
                          pady=10,
                          width=50,
                          bg=bg_action, 
                          fg=bg)

chk1 = Checkbutton (root, text="Uppercase",
                          variable=var1, 
                          onvalue=1,
                          offvalue=0,
                          font="Calibri 12",
                          bg=bg,
                          justify="left",
                          anchor="w",
                          width=15,
                          border=1,
                          padx=4)

chk2 = Checkbutton (root, text="Number",
                          variable=var2, 
                          onvalue=1,
                          offvalue=0,
                          font="Calibri 12",
                          bg=bg,
                          justify="left",
                          anchor="w",
                          width=15,
                          border=1,
                          padx=4)



chk3 = Checkbutton (root, text="Special Character",
                          variable=var3, 
                          onvalue=1,
                          offvalue=0,
                          font="Calibri 12",
                          bg=bg,
                          justify="left",
                          anchor="w",
                          width=15,
                          border=1,
                          padx=4)


scale = Scale(root, variable = scaleVar, 
                    orient='horizontal', 
                    from_= 4, 
                    to = 32, 
                    length=300,
                    sliderlength=15,
                    width=15,
                    font="Terminal 11",
                    activebackground=bg_action,
                    sliderrelief="flat",
                    troughcolor='#aaa',
                    relief="flat",
                    highlightbackground = bg,
                    bg=bg)
scaleVar.set(16)

labelPassword = Label(root,  text="", 
                          font="Arial 20", 
                          pady=5, 
                          bg=bg)

labelCopy = Label(root, text="", 
                        font="Arial 8", 
                        pady=4, 
                        fg='red', 
                        bg=bg)

# buttonGerar = Button(root,  text="GERAR SENHA",  
#                             font="Terminal 20", 
#                             command=passwordGenerator,
#                             width=50, 
#                             height=8, 
#                             bg='#555', 
#                             relief="raised", 
#                             border=0, 
#                             fg=bg)


labelTitle.pack()
chk1.pack()
chk2.pack()
chk3.pack()
scale.pack()
labelPassword.pack()
labelCopy.pack()
# buttonGerar.pack()

root.mainloop()