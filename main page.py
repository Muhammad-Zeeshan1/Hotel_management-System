from tkinter import*
import random
import time
import os

root = Tk()
root.geometry("900x370")
root.title("Hotel Mangement System")

root.configure(bg='dark red')

Tops = Frame(root,bg="black",width = 1000,height=500,relief=SUNKEN)
Tops.pack(side=TOP)

f12 = Frame(root,width = 500,height=700,relief=SUNKEN)
f12.pack(side=BOTTOM)

f1 = Frame(root,width = 500,height=700,relief=SUNKEN)
f1.pack(side=BOTTOM)




#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'Arial black' ,30, 'bold' ),text="Hotel Mangement System",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="black",anchor=W)
lblinfo.grid(row=1,column=0)

#--------------------------------------------

   

def Ref():
    filename = 'registrationform2.py'
    os.system(filename) #open file [same as right click open]


def qexit():
    root.destroy()

def reset():
    home.set("")
    fullname.set("")
    fathername.set("")
    customer.set("")


def record():
    filename = 'recordpage.py'
    os.system(filename) #Open file [Same as Right-click Open]


def calculator():
    filename = 'calculation.py'
    os.system(filename) #Open file [Same as Right-Click open]








#----------------------------------------------


#---------------info entries-----------------
    
home = StringVar()
fullname = StringVar()
fathername = StringVar()
customer = StringVar()









lblfullname = Label(f1, font=( 'aria' ,16, 'bold' ),text="full name",fg="blue",bd=10,anchor='w')
lblfullname.grid(row=12,column=0)
txtfullname = Entry(f1,font=('ariel' ,16,'bold'), textvariable=fullname, bd=6,insertwidth=2,bg="white" ,justify='right')
txtfullname.grid(row=12,column=1)


lblfathername = Label(f1, font=( 'aria' ,16, 'bold' ),text="father name",fg="blue",bd=10,anchor='w')
lblfathername.grid(row=13,column=0)
txtfathername = Entry(f1,font=('ariel' ,16,'bold'), textvariable=fathername , bd=6,insertwidth=2,bg="white" ,justify='right')
txtfathername.grid(row=13,column=1)


lblcustomer = Label(f1, font=( 'aria' ,16, 'bold' ),text="customer no.",fg="blue",bd=10,anchor='w')
lblcustomer.grid(row=14,column=0)
txtcustomer = Entry(f1,font=('ariel' ,16,'bold'), textvariable=customer , bd=6,insertwidth=2,bg="white" ,justify='right')
txtcustomer.grid(row=14,column=1)


lblhome = Label(f1, font=( 'aria' ,16, 'bold' ),text="home address",fg="blue",bd=10,anchor='w')
lblhome.grid(row=15,column=0)
txthome = Entry(f1,font=('ariel' ,16,'bold'), textvariable=home , bd=6,insertwidth=2,bg="white" ,justify='right')
txthome.grid(row=15,column=1)

#-----------------------------------------buttons-----------------------------------------------------------------------------------------------------------------------------

btn=Button(f12,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Registeration", bg="purple",command=Ref)
btn.grid(row=17, column=0)

btn=Button(f12,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="reset", bg="blue",command=reset)
btn.grid(row=17, column=1)

btn=Button(f12,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Exit", bg="purple",command=qexit)
btn.grid(row=17, column=2)

btn=Button(f12,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="INFO", bg="purple",command=record)
btn.grid(row=17, column=4)


btn=Button(f12,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="Bill Calculator", bg="blue",command=calculator)
btn.grid(row=17, column=3)


root.mainloop()
