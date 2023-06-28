from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Hotel:

    def __init__(self,root):
        self.root = root
        self.root.title("Check In System")
        self.root.geometry("5963x5749+540+110")
        self.root.config(background="#bf00ff")

        MainFrame =Frame(self.root)
        MainFrame.grid()

        
        #====================================================================================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def receipt():
            amt=0
            if RoomType=='Single':
                TotalDays=int()
                amt=TotalDays*2000

            elif RoomType=='Double':
                TotalDays=int()
                amt=TotalDays*5000
                
            elif RoomType=='Deluxe':
                TotalDays=int()
                amt=TotalDays*8000
                
            elif RoomType=='Suite':
                TotalDays=int()
                amt=TotalDays*10000
                
            elif RoomType=='Super Deluxe':
                TotalDays=int()
                amt=TotalDays*15000
                
            elif RoomType=='Prince Suite':
                TotalDays=int()
                amt=TotalDays*25000
            amt=str(amt)
            k = tkinter.messagebox.askyesno("Total amount", "The amount uptil now is:"+amt)
            if k > 0:
                iExit()
                return
            

        def saveChanges():
            f.write(3*"\n")
            save = tkinter.messagebox.askyesno("Check In form", "Confirm if you are ready to Save Details")
            if save > 0:
                root.destroy()
                return
        
        def Reset():
            CustomerRef.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            Aadharnumber.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")
            receipt.set("")
        

        def TotalCostandDate():

            InDate = CheckInDate.get()
            OutDate = CheckOutDate.get()
            InDate = datetime.strptime(InDate, "%d/%m/%Y")
            OutDate = datetime.strptime(OutDate, "%d/%m/%Y")
            TotalDays.set(abs((OutDate - InDate).days))

        
        CustomerRef =str()
        Firstname =str()
        Surname =str()
        Address=str()
        PostCode=str()
        Mobile=str()
        Email=str()
        Nationality=str()
        DOB=str()
        Gender=str()
        TotalDays=CheckOutDate=CheckInDate=head=str()
        RoomType=RoomNo=RoomExtNo=TotalCost=SubTotal=PaidTax=TotalDays=Receipt=str()
        #============================================================Widget====================================================================
        lblinfo = Label(font=( 'aria' ,30, 'bold' ),text="Check In Form",bd=1,relief="solid",fg="blue",bg="#33ccff",anchor=N)
        lblinfo.grid(row=9,column=9)
        lblinfo = Label(font=( 'aria' ,20 ),text=head,fg="steel blue")
        lblinfo.grid(row=9,column=8)

        self.lblCustomer_Ref =Label(font=('arial',12,'bold'),text="Customer Ref No.:",padx=2,bg="#8000ff")
        self.lblCustomer_Ref.grid(row=10,column=7, sticky=W)
        self.txtCustomer_Ref =Entry(font=('arial',12,'bold'),textvariable =CustomerRef,width=20)
        self.txtCustomer_Ref.grid(row=10,column=8)
        f.write("Customer ID:"+CustomerRef+",")

        self.lblFirstName =Label(font=('arial',12,'bold'),text="First Name:",padx=2,bg="#8000ff")
        self.lblFirstName.grid(row=11,column=7, sticky=W)
        self.txtFirstname =Entry(font=('arial',12,'bold'),textvariable =Firstname,width=20)
        self.txtFirstname.grid(row=11,column=8, pady=3, padx=20)
        f.write("First Name:"+Firstname+",")

        self.lblSurname =Label(font=('arial',12,'bold'),text="Surname:",padx=2,bg="#8000ff")
        self.lblSurname.grid(row=12,column=7, sticky=W)
        self.txtSurname =Entry( font=('arial',12,'bold'),textvariable =Surname,width=20)
        self.txtSurname.grid(row=12,column=8, pady=3, padx=20)
        f.write("Surname:"+Surname+",")

        self.lblAddress =Label(font=('arial',12,'bold'),text="Address:",padx=2,bg="#8000ff")
        self.lblAddress.grid(row=13,column=7, sticky=W)
        self.txtAddress =Entry(font=('arial',12,'bold'),textvariable =Address,width=20)
        self.txtAddress.grid(row=13,column=8, pady=3, padx=20)
        f.write("Address:"+Address+",")

        self.lblPostCode =Label(font=('arial',12,'bold'),text="PostCode:",padx=2,bg="#8000ff")
        self.lblPostCode.grid(row=14,column=7, sticky=W)
        self.txtPostCode =Entry(font=('arial',12,'bold'),textvariable =PostCode,width=20)
        self.txtPostCode.grid(row=14,column=8, pady=3, padx=20)
        f.write("Customer ID:"+CustomerRef+",")

        self.lblMobile =Label(font=('arial',12,'bold'),text="Mobile:",padx=2,bg="#8000ff")
        self.lblMobile.grid(row=15,column=7, sticky=W)
        self.txtMobile =Entry(font=('arial',12,'bold'),textvariable =Mobile,width=20)
        self.txtMobile.grid(row=15,column=8, pady=3, padx=20)
        f.write("PostCode:"+PostCode+",")

        self.lblEmail =Label(font=('arial',12,'bold'),text="Email:",padx=2,bg="#8000ff")
        self.lblEmail.grid(row=16,column=7, sticky=W)
        self.txtEmail =Entry(font=('arial',12,'bold'),textvariable =Email,width=20)
        self.txtEmail.grid(row=16,column=8, pady=3, padx=20)
        f.write("Email:"+Email+",")

        self.lblNationality=Label(font=('arial',12,'bold'),text="Nationality:",padx=2,bg="#8000ff")
        self.lblNationality.grid(row=17,column=7, sticky=W)
        self.cboNationality =ttk.Combobox(textvariable =Nationality, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboNationality['value'] = ('','British','Nigerian','Kenyan','Indian','Iranian','Moroccan','Canadian','French','Norwegian','American')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=17,column=8, pady=3, padx=20)
        f.write("Nationality:"+Nationality+",")

        self.lblDOB =Label(font=('arial',12,'bold'),text="DOB:",padx=2,bg="#8000ff")
        self.lblDOB.grid(row=18,column=7, sticky=W)
        self.txtDOB =Entry(font=('arial',12,'bold'),textvariable =DOB,width=20)
        self.txtDOB.grid(row=18,column=8, pady=3, padx=20)
        f.write("DOB:"+DOB+",")

        self.lblCheck_In_Date =Label(font=('arial',12,'bold'),text="Check In Date:",padx=2,bg="#8000ff")
        self.lblCheck_In_Date.grid(row=19,column=7, sticky=W)
        self.txtCheck_In_Date =Entry(font=('arial',12,'bold'),textvariable =CheckInDate,width=20)
        self.txtCheck_In_Date.grid(row=19,column=8, pady=3, padx=20)
        f.write("Check In Date:"+CheckInDate+",")

        self.lblCheck_Out_Date =Label(font=('arial',12,'bold'),text="Check Out Date:",padx=2,bg="#8000ff")
        self.lblCheck_Out_Date.grid(row=20,column=7, sticky=W)
        self.txtCheck_Out_Date =Entry(font=('arial',12,'bold'),textvariable =CheckOutDate,width=20)
        self.txtCheck_Out_Date.grid(row=20,column=8, pady=3, padx=20)
        f.write("Check Out Date:"+CheckOutDate+",")
        
        self.lblRoomType=Label(font=('arial',12,'bold'),text="Room Type:",padx=2,bg="#8000ff")
        self.lblRoomType.grid(row=21,column=7, sticky=W)
        self.cboRoomType =ttk.Combobox(textvariable =RoomType, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomType['value'] = ('','Single','Double','Deluxe','Suite','Super Deluxe','Prince Suite')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=21,column=8, pady=3, padx=20)
        f.write("Room Type:"+RoomType+",")

        self.lblRoomNo=Label(font=('arial',12,'bold'),text="Room No.:",padx=2,bg="#8000ff")
        self.lblRoomNo.grid(row=22,column=7, sticky=W)
        self.cboRoomNo =ttk.Combobox(textvariable =RoomNo, state='readonly',font=('arial',12,'bold'),width=18)
        self.cboRoomNo['value'] = ('','101','102','103','104','105','106','107','108','109')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=22,column=8, pady=3, padx=20)
        f.write("Room No.:"+RoomNo+",")

        self.lblDays =Label(font=('arial',12,'bold'),text="No. of Days:",bd=7,bg="powder blue",fg="black")
        self.lblDays.grid(row=23,column=7, sticky=W)
        self.lblDays =Entry(font=('arial',12,'bold'),text=TotalDays,width=20)
        self.lblDays.grid(row=23,column=8, pady=3, padx=20)
        f.write("No. of days:"+TotalDays+",")
        
        
        #========================================================================================================================================
       
        self.btnExit=Button(fg="black",font=('arial',16,'bold'),width=21,height=2,bg="#ff00bf",text="Save Details",command=saveChanges).grid(row=28, column=8, padx=4)
        self.btnSave=Button(fg="black",font=('arial',16,'bold'),width=21,height=2,bg="#ff00bf",text="Exit",command=iExit).grid(row=28, column=7, padx=4)
        self.btnRec=Button(fg="black",font=('arial',16,'bold'),width=21,height=2,bg="#ff00bf",text="Entry Receipt",command=receipt).grid(row=28, column=9, padx=4)

        
if __name__=='__main__':
    f=open("Info_All_Guests.txt",'w')
    root = Tk()
    application = Hotel (root)
    root.mainloop()
    f.close()
    

    
