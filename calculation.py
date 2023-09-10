from tkinter import*
import tkinter.messagebox
import time
import random

operator = ""
#### creating window and its geometry ######

root = Tk()
root.geometry("1200x1000")
root.title("Customer Bill Calculator")

root.configure(bg='dark red')


#### creating Frame ######

top = Frame(root, width = 1600, height = 50, relief = SUNKEN)
top.pack(side = TOP)

left = Frame(root, width = 800, height = 700, relief = SUNKEN)
left.pack(side = RIGHT)

right = Frame(root, width = 300, height = 700, relief = SUNKEN)
right.pack(side = LEFT)







##### creating label of title and time ###

label_info = Label(top, font = ('arial',50,'bold'), text ="Customer Bill Calculator", fg = "steel blue", bd = 10, anchor = 'w')
label_info.grid(row = 0, column = 0)

local_time = time.asctime(time.localtime(time.time()))

label_info = Label(top, font = ('arial',20,'bold'), text = local_time, fg = "steel blue", bd = 10, anchor = 'w')
label_info.grid(row = 1, column = 0)


######## creating calculator #######

txt_inp = StringVar()

def btn_click(number):
	global operator
	operator = operator+ str(number)
	txt_inp.set(operator)

def fun_clear():
	global operator
	operator = ""
	txt_inp.set(operator)

def calculate():
	global operator
	try:
		sumup = str(eval(operator))
	except Exception as e:
		tkinter.messagebox.showinfo('Error','Incorrect Input')
		sumup = 0
		fun_clear()
	txt_inp.set(sumup)
	operator = ""




txt = Entry(right, font = ('arial',20,'bold'), textvariable = txt_inp, bd = 30, insertwidth = 4, bg = "powderblue", justify = 'right')
txt.grid(columnspan = 4)


#=========first row button=========

btn7 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="7", bg="powder blue", command=lambda: btn_click(7))
btn7.grid(row= 2, column= 0)

btn8 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="8", bg="powder blue", command=lambda: btn_click(8))
btn8.grid(row= 2, column= 1)

btn9 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="9", bg="powder blue", command=lambda: btn_click(9))
btn9.grid(row= 2, column= 2)

plus = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="+", bg="powder blue", command=lambda: btn_click("+"))
plus.grid(row= 2, column= 3)


#=========second row button=========

btn4 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="4", bg="powder blue", command=lambda: btn_click(4))
btn4.grid(row= 3, column= 0)

btn5 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="5", bg="powder blue", command=lambda: btn_click(5))
btn5.grid(row= 3, column= 1)

btn6 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="6", bg="powder blue", command=lambda: btn_click(6))
btn6.grid(row= 3, column= 2)

minus = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="-", bg="powder blue", command=lambda: btn_click("-"))
minus.grid(row= 3, column= 3)


#=========third row button=========


btn1 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="1", bg="powder blue", command=lambda: btn_click(1))
btn1.grid(row= 4, column= 0)

btn2 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="2", bg="powder blue", command=lambda: btn_click(2))
btn2.grid(row= 4, column= 1)

btn3 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="3", bg="powder blue", command=lambda: btn_click(3))
btn3.grid(row= 4, column= 2)

multiply = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="*", bg="powder blue", command=lambda: btn_click("*"))
multiply.grid(row= 4, column= 3)


#=========fourth row button=========

btn0 = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="0", bg="powder blue", command=lambda: btn_click(0))
btn0.grid(row= 5, column= 0)

btn_clear = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="C", bg="powder blue",command=fun_clear)
btn_clear.grid(row= 5, column= 1)

btn_equal = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="=", bg="powder blue",command= calculate)
btn_equal.grid(row= 5, column= 2)

division = Button(right, padx= 16, pady=16, bd= 8, fg= "black", font= ('arial',20,'bold'), text="/", bg="powder blue", command=lambda: btn_click("/"))
division.grid(row= 5, column= 3) 


###########now on left frame  enter menu ####################################################################








def qexit():
	root.destroy()


	 




subtotal = Label(left, font=('arial',16,'bold'),text = ":Customer  all charges:", bd = 16, anchor = 'w' )
subtotal.grid(row=1,column=2,sticky = E)


services = Label(left, font=('arial',16,'bold'),text = "PER DAY ROOM RENT = 5000", bd = 16, anchor = 'w' )
services.grid(row=2,column=2,sticky = E)


tax = Label(left, font=('arial',16,'bold'),text = "LUNCH = 1000/DAY", bd = 16, anchor = 'w' )
tax.grid(row=3,column=2,sticky = E)


cost = Label(left, font=('arial',16,'bold'),text = "DINNER = 1500/DAY", bd = 16, anchor = 'w' )
cost.grid(row=4,column=2,sticky = E)

total = Label(left, font=('arial',16,'bold'),text = "OTHER CHARGES [TOILET+TAX+OTHER ACESSORIES]", bd = 16, anchor = 'w' )
total.grid(row=5,column=2,sticky = E)
 


### right Frame Button ###########



btn_exit = Button(left, padx= 5, pady= 50, bd= 40, fg= "black", font=('arial',16,'bold'), width=10, text= "Exit", bg= "powder blue",command = qexit)
btn_exit.grid(row=7, column= 3)





root.mainloop()


