from tkinter import*
import tkinter.messagebox as tmsg
import os




screen = Tk()


screen.geometry("500x500")
screen.title("registration form")
heading = Label(text = " REGISTER YOUR DETAILS ", bg = "brown", fg = "black", width = "500", height="3")
heading.pack()




#-----------------alignments--------------

f1 = Frame(screen,width = 700,height=700,relief=SUNKEN)
f1.pack(side=TOP)


#-----------------------------info--------------------


firstname = StringVar()
lastname = StringVar()
age = IntVar()
address = StringVar()



lblfirstname = Label(f1,font=( 'aria' ,16, 'bold' ),text="First name",fg="blue",bd=10,anchor='w')
lblfirstname.grid(row=12,column=0)
txtfirstname = Entry(f1, font=('ariel' ,16,'bold'), textvariable=firstname, bd=6,insertwidth=2,bg="white" ,justify='right')
txtfirstname.grid(row=12,column=1)


lbllastname = Label(f1,font=( 'aria' ,16, 'bold' ),text="Last name",fg="blue",bd=10,anchor='w')
lbllastname.grid(row=13,column=0)
txtlastname = Entry(f1, font=('ariel' ,16,'bold'), textvariable=lastname, bd=6,insertwidth=2,bg="white" ,justify='right')
txtlastname.grid(row=13,column=1)




lblage = Label(f1,font=( 'aria' ,16, 'bold' ),text="Age",fg="blue",bd=10,anchor='w')
lblage.grid(row=14,column=0)
txtage = Entry(f1, font=('ariel' ,16,'bold'), textvariable=age, bd=6,insertwidth=2,bg="white" ,justify='right')
txtage.grid(row=14,column=1)


lbladdress = Label(f1,font=( 'aria' ,16, 'bold' ),text="Address",fg="blue",bd=10,anchor='w')
lbladdress.grid(row=15,column=0)
txtaddress = Entry(f1, font=('ariel' ,16,'bold'), textvariable=address, bd=6,insertwidth=2,bg="white" ,justify='right')
txtaddress.grid(row=15,column=1)




#-------------------------------------------------------------------
def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    age_info = str(age_info)
    print (firstname_info, lastname_info, age_info)


    file = open("user.txt", "w")
    file.write(firstname_info)
    file.write(lastname_info)
    file.write(age_info)
    file.close()
    print("user ", firstname_info, " has been registered successfully")



    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    age_entry.delete(0, END)






register = Button(screen,text = "Register", width= "30", height = "2", command = save_info, bg = "grey")
register.place(x = 150, y = 300)

#---------------------------------------------------------------








screen.mainloop()
