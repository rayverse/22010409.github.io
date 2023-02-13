from tkinter import *  
import os
  
root = Tk()  
root.title('Hi ;P')
root.geometry("100x100")  

def choice(option):
    pop.destroy()
    if option=="yes":
        my_label.config(text= "You clicked yes <3")
        os.startfile("D:\Renju\guitar\RentAdForHim\Apricity.txt")

    else:
        my_label.config(text="You clicked no :o")
        



def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("New message!")
    pop.geometry("250x150")
    pop.config(bg="blue")

    global letter
    letter = PhotoImage(file="pixil-frame-0.png")

    pop_label = Label(pop, text="Open?", fg="black", font=("helvetica", 12))
    pop_label.pack(pady=10)

    my_frame = Frame(pop, bg="blue")
    my_frame.pack(pady=5)

    letter_pic = Label(my_frame, image=letter, borderwidth=0)
    letter_pic.grid(row=0, column= 0, padx=10)

    yes = Button(my_frame, text="Yes", command=lambda:choice("yes"))
    yes.grid(row=0, column=2)

    no = Button(my_frame, text="No", command=lambda:choice("no"))
    no.grid(row=0, column=4)

my_button = Button(root, text="Click me", command= clicker)
my_button.pack(pady=0)
 
my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()