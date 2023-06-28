from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Hotel:

    def __init__(self,root):
        self.root = root
        self.root.title("Extra Charges Billing system")
        self.root.geometry("3000x25000+0+0")
        self.root.config(background="powder blue")

        MainFrame =Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame, bd=14, width=1350,height=550, padx=20, relief=RIDGE,bg="cadet blue")
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=10, width=450,height=550, padx=2, relief=RIDGE,bg="powder blue")
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=10, width=820,height=550, padx=20, relief=RIDGE,bg="cadet blue")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(MainFrame, bd=10, width=1350,height=150, padx=20, relief=RIDGE,bg="powder blue")
        BottomFrame.pack(side=BOTTOM)
        
        #====================================================================================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Receipt():
            self.txtReceipt.insert(END, CustomerRef.get()+ "\t" + Firstname.get()+ "\t" + Surname.get()+ "\t" +  Address.get()+"\t"
                                   +  PostCode.get()+"\t"+  Mobile.get()+"\t"+  Nationality.get()+"\t"+  CheckInDate.get()+"\t"
                                   +  CheckOutDate.get()+"\t"+  PaidTax.get()+"\t"+  SubTotal.get()+"\t"+  TotalCost.get()+"\t")

        def TotalCostandDate():
            pass

        def Reset():
            CustomerRef.set("")
            Firstname.set("")
            Surname.set("")

        
        
            hair.set("")
            body.set("")
            events.set("")
            std.set("")
            pool.set()
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")
            Receipt.set("")
            self.txtReceipt.delete("1.0",END)

        CustomerRef =StringVar()
        Firstname =StringVar()
        Surname =StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Mobile=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        DOB=StringVar()
        IDType=StringVar()
        Gender=StringVar()
        CheckInDate=StringVar()
        CheckOutDate=StringVar()
        hair =StringVar()
        body=StringVar()
        RoomNo=StringVar()
        std=StringVar()
        pool=StringVar()
        events=StringVar()
        RoomExtNo=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()
        TotalDays=StringVar()
        Receipt=StringVar()
        #============================================================Widget====================================================================
    
        self.lblCustomer_Ref =Label(LeftFrame, font=('arial',12,'bold'),text="Customer Ref No.:",padx=2,bg="powder blue")
        self.lblCustomer_Ref.grid(row=0,column=0, sticky=W)
        self.txtCustomer_Ref =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =CustomerRef,width=20)
        self.txtCustomer_Ref.grid(row=0,column=1, pady=3, padx=20)

        self.lblFirstName =Label(LeftFrame, font=('arial',12,'bold'),text="First Name:",padx=2,bg="powder blue")
        self.lblFirstName.grid(row=1,column=0, sticky=W)
        self.txtFirstname =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Firstname,width=20)
        self.txtFirstname.grid(row=1,column=1, pady=3, padx=20)

        self.lblSurname =Label(LeftFrame, font=('arial',12,'bold'),text="Surname:",padx=2,bg="powder blue")
        self.lblSurname.grid(row=2,column=0, sticky=W)
        self.txtSurname =Entry(LeftFrame, font=('arial',12,'bold'),textvariable =Surname,width=20)
        self.txtSurname.grid(row=2,column=1, pady=3, padx=20)

        self.lblMeal=Label(LeftFrame, font=('arial',12,'bold'),text="Hair:",padx=2,bg="powder blue")
        self.lblMeal.grid(row=12,column=0, sticky=W)
        self.cboMeal =ttk.Combobox(LeftFrame, textvariable =hair, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboMeal['value'] = ('','Hair cut','Oil massage','Hair treatment','Hair setting')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=12,column=1, pady=3, padx=20)

        self.lblRoomType=Label(LeftFrame, font=('arial',12,'bold'),text="Body:",padx=2,bg="powder blue")
        self.lblRoomType.grid(row=13,column=0, sticky=W)
        self.cboRoomType =ttk.Combobox(LeftFrame, textvariable =body, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomType['value'] = ('','Massage','Accupunction points stimulations','Blood circulation')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=13,column=1, pady=3, padx=20)

        self.lblRoomNo=Label(LeftFrame, font=('arial',12,'bold'),text="Events:",padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=14,column=0, sticky=W)
        self.cboRoomNo =ttk.Combobox(LeftFrame, textvariable =RoomNo, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomNo['value'] = ('','No Event chosen','Pongal','Diwali','Independence day','Ramzan','Christmas',"Women's day",'Birthday','Rent out hall','Others')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=14,column=1, pady=3, padx=20)

        self.lblRoomNo=Label(LeftFrame, font=('arial',12,'bold'),text="STD (Total time used):",padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=15,column=0, sticky=W)
        self.cboRoomNo =ttk.Combobox(LeftFrame, textvariable =RoomNo, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomNo['value'] = ('','Unused','10 minutes','30 minutes','1 hour','2 hours','3 hours','Over 3 hours')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15,column=1, pady=3, padx=20)

        self.lblRoomNo=Label(LeftFrame, font=('arial',12,'bold'),text="Pool Usage(Days used):",padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=16,column=0, sticky=W)
        self.cboRoomNo =ttk.Combobox(LeftFrame, textvariable =RoomNo, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomNo['value'] = ('','No Usage','1','2','3','4','5','6','7','More than 7 days','All days')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=16,column=1, pady=3, padx=20)

        self.lblRoomNo=Label(LeftFrame, font=('arial',12,'bold'),text="Room Number",padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=17,column=0, sticky=W)
        self.cboRoomNo =ttk.Combobox(LeftFrame, textvariable =RoomNo, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomNo['value'] = ('','101','102','103','104','105','106','107','108','109')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=17,column=1, pady=3, padx=20)
        

        
        
        #============================================================Receipt1====================================================================
        self.lblLabel = Label(RightFrame, font=('arial',10,'bold'),pady=10,bg="cadet blue")
        text="CustomerRef\tFirstname\tSurname\tAddress\tPostCode\tMobile\tNationality\tCheckInDate\tCheckOutDate"
        self.lblLabel.grid(row = 0, column = 0, columnspan = 17)

        self.txtReceipt =Text(RightFrame,height=15,width=108,bd=10, font=('arial',11,'bold'))
        self.txtReceipt.grid(row=1,column=0,columnspan=2, pady=5, padx=2)        

        #============================================================Receipt2====================================================================


        self.lblPaidTax =Label(RightFrame, font=('arial',14,'bold'),text="Paid Tax:",bd=7,bg="cadet blue",fg="black")
        self.lblPaidTax.grid(row=3,column=0, sticky=W)
        self.txtPaidTax =Entry(RightFrame, font=('arial',14,'bold'),textvariable =PaidTax,bd=7,bg="white",width=67,justify=LEFT)
        self.txtPaidTax.grid(row=3,column=1)

        self.lblSubTotal =Label(RightFrame, font=('arial',14,'bold'),text="Sub Total:",bd=7,bg="cadet blue",fg="black")
        self.lblSubTotal.grid(row=4,column=0, sticky=W)
        self.txtSubTotal =Entry(RightFrame, font=('arial',14,'bold'),textvariable =SubTotal,bd=7,bg="white",width=67,justify=LEFT)
        self.txtSubTotal.grid(row=4,column=1)

        self.lblTotalCost =Label(RightFrame, font=('arial',14,'bold'),text="Total Cost:",bd=7,bg="cadet blue",fg="black")
        self.lblTotalCost.grid(row=5,column=0, sticky=W)
        self.txtTotalCost =Entry(RightFrame, font=('arial',14,'bold'),textvariable =TotalDays,bd=7,bg="white",width=67,justify=LEFT)
        self.txtTotalCost.grid(row=5,column=1)

        #========================================================================================================================================
        self.btnTotal=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=21,height=2,bg="powder blue",text="Add to hms",command=TotalCostandDate).grid(row=0, column=4, padx=4)
        self.btnReceipt=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=21,height=2,bg="powder blue",text="Receipt",command=Receipt).grid(row=0, column=5, padx=4)
        self.btnReset=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=21,height=2,bg="powder blue",text="Reset",command=Reset).grid(row=0, column=6, padx=4)
        self.btnExit=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=21,height=2,bg="powder blue",text="Exit",command=iExit).grid(row=0, column=7, padx=4)

if __name__=='__main__':
    root = Tk()
    application = Hotel (root)
    root.mainloop()
