from tkinter import *
from tkinter import messagebox
root = Tk()
#region config
root.title("Mastermind Game")
root.geometry("400x300")
root.resizable(width=0 , height=0)
#endregion

int(input ("enter a name :"))



def click_btn():
    messagebox.showinfo("information , information")

def click_btn_guess():
    messagebox.showinfo("Check Number , information")

#region label
lbl_choose = Label(root,text="choose your label (4 - 9):")
lbl_choose.grid(row=1 , column=0 , padx=5 , pady=5 , sticky=W)    

lbl_guess = Label(root , text= "guess number : ")
lbl_guess.grid(row= 2 , column=0 , padx=5 , pady=5 , sticky=W)
#endregion

#region Entry
var_label = StringVar()
entry_label = Entry(root,textvariable=var_label )
entry_label.grid(row=1 , column=1 , padx=5 , pady=5)

var_guess = StringVar()
entry_guess = Entry(root , textvariable = var_guess )
entry_guess.grid(row= 2 , column= 1 , padx=5 , pady=5 )
#endregion

#region button
btn_label1 = Button(root,command = click_btn,text = "go",fg = "white" , bg = "black" ,activeforeground = "black" , activebackground = "white"  )   
btn_label1.grid(row=1 , column=3 , columnspan = 2 , padx=5 , pady=5 , sticky=E)
btn_guess1 = Button(root , command=click_btn_guess,text = "check",fg = "white" , bg = "black" ,activeforeground = "black" , activebackground = "white" )
btn_guess1.grid(row= 2 , column= 3 , padx=5 , pady=5 , sticky=E)

#endregion

#region scrollbar



guess_numbers_listbox = Listbox(root,yscrollcommand=scrol_listbox.set )
guess_numbers_listbox.grid(row=4 , column=0 ,rowspan=3 ,columnspan= 8 ,sticky=E+W+S+N , padx=5 , pady=5 )


scrol_listbox = Scrollbar(root )
scrol_listbox.grid(row= 4 , column= 3 , rowspan=8 , sticky=N+S+E , pady= 5)

scrol_listbox.config(command = guess_numbers_listbox.yview)





#endregion
root.mainloop()