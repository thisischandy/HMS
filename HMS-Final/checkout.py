from tkinter import *

root = Tk()
root.geometry('5000x5000')
root.title("Check Out Portal")

label_0 = Label(root, text="\tGrand Jade Hotel",width=20,font=("bold", 20))
label_0.place(x=400,y=53)


label_1 = Label(root, text="Customer Ref. No",width=20,font=("bold", 10))
label_1.place(x=400,y=130)

entry_1 = Entry(root)
entry_1.place(x=650,y=130)

label_2 = Label(root, text="Room Number:",width=20,font=("bold", 10))
label_2.place(x=400,y=180)

entry_2 = Entry(root)
entry_2.place(x=650,y=180)

label_3 = Label(root, text="Memberships Sign ups",width=20,font=("bold", 10))
label_3.place(x=400,y=230)
var = IntVar()
Radiobutton(root, text="Hotel Club",padx = 5, variable=var, value=1).place(x=615,y=230)
Radiobutton(root, text="Reading Club",padx = 20, variable=var, value=2).place(x=700,y=230)

label_4 = Label(root, text="Payment method",width=20,font=("bold", 10))
label_4.place(x=400,y=280)

list1 = [' Card','Cash'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your option') 
droplist.place(x=650,y=280)


Button(root, text='Submit (Generate Receipt)',width=30,bg='brown',fg='white').place(x=525,y=400)

root.mainloop()
