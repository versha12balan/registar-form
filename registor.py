from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Register():
    def __init__(self,win):
        self.win=win
        self.win.title("Registor")
        self.win.geometry("1600x900+0+0")


        # variables----------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar
        self.var_securityQ=StringVar()
        self.var_secuirtyA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # background image--------------------------
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\New folder\glenn-carstens-peters-npxXWgQ33ZQ-unsplash.jpg")
        bg_lb1=Label(self.win,image=self.bg)
        bg_lb1.place(x=0,y=0,relwidth=1,relheight=1)

        #left image---------------------------------
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\Desktop\New folder\image.jpg")
        left_lb1=Label(self.win,image=self.bg1)
        left_lb1.place(x=50,y=100,width=470,height=600)

        #main frame--------------------------------------
        frame=Frame(self.win,bg="white")
        frame.place(x=520,y=100,height=600,width=800)
        
        # register name
        label=Label(frame,text=" REGISTER HERE",font=("Times New Roman",30,"bold"),bg="white")
        label.place(x=20,y=20)

        #first name and entry---------
        #=========row1================
        fname=Label(frame,text="First Name",font=("Times New Roman",17,"bold"),bg="white")
        fname.place(x=35,y=110)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Times New Roman",17,"bold"))
        self.fname_entry.place(x=35,y=140,width=250)


        l_name=Label(frame,text="Last Name",font=("Times New Roman",17,"bold"),bg="white",fg="black")
        l_name.place(x=355,y=110)

    
        self.entry_l=ttk.Entry(frame,textvariable= self.var_lname,font=("Times New Roman",15,"bold"))
        self.entry_l.place(x=355,y=140,width=300)

        #=========row2==================

        contact=Label(frame,text="Contact No.",font=("Times New Roman",17,"bold"),bg="white",fg="black")
        contact.place(x=35,y=180)

        self.entry_c=ttk.Entry(frame,textvariable= self.var_contact,font=("Times New Roman",15,"bold"))
        self.entry_c.place(x=35,y=210,width=250)


        e_label=Label(frame,text="Email",font=("Times New Roman",17,"bold"),bg="white",fg="black")
        e_label.place(x=355,y=180)

        self.entry_e=ttk.Entry(frame,textvariable= self.var_email,font=("Times New Roman",15,"bold"))
        self.entry_e.place(x=355,y=210,width=300)

        #============row3=======================
        security_q=Label(frame,text="Select Security Question",font=("Times New Roman",17,"bold"),bg="white",fg="black")
        security_q.place(x=35,y=250)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("Times New Roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Fvourite Pet","Your First Pet Name")
        self.combo_security_Q.place(x=35,y=280)
        self.combo_security_Q.current(0)

        # self.entry_1=Entry(frame,font=("Times New Roman",15,"bold"),textvariable=self.var_securityQ)
        # self.entry_1.place(x=35,y=280,width=250)


        security_a=Label(frame,text="Security Answer",font=("Times New Roman",17,"bold"),bg="white",fg="black")
        security_a.place(x=355,y=250)

        self.entry_a=ttk.Entry(frame,textvariable=self.var_secuirtyA,font=("Times New Roman",15,"bold"))
        self.entry_a.place(x=355,y=280,width=300)

        # =============row4=====================

        password_1=Label(frame,text="Password",font=("Times New Roman",17,"bold"),bg="white",fg="black")
        password_1.place(x=35,y=320)

        self.entry_p=ttk.Entry(frame,textvariable=self.var_pass,font=("Times New Roman",15,"bold"))
        self.entry_p.place(x=35,y=350,width=250)


        c_pass=Label(frame,text="Confirm Password",font=("Times New Roman",17,"bold"),bg="white",fg="black")
        c_pass.place(x=355,y=320)

        self.entry_cp=ttk.Entry(frame,textvariable=self.var_confpass,font=("Times New Roman",15,"bold"))
        self.entry_cp.place(x=355,y=350,width=300)


        # =================checkbutton================
        self.var_check=IntVar()
        checkbutton=Checkbutton(frame,variable= self.var_check,text="I Agree The Terms And Conditions",font=("Times New Roman",15,"bold"),onvalue=1,offvalue=0)
        checkbutton.place(x=35,y=390)

        #=================buttons=====================
        # img=Image.open(r"C:\Users\HP\Desktop\New folder\images (14).jpeg")
        # img=img.resize((250,50),Image.LANCZOS)
        # self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,text="REGISTOR ON",font=("Times New Roman",17,"bold"),bg="black",fg="white")
        b1.place(x=30,y=450,width=250)
        
        
        img=Image.open(r"C:\Users\HP\Desktop\New folder\download (5).jpeg")
        img=img.resize((250,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2")
        b1.place(x=420,y=450,width=250)


    #===================function declaration=================
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" :
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm passwor must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree terms and conditions")
        else:
            messagebox.showinfo("successfull","WELCOME")

    





if __name__ == "__main__":
    win=Tk()   
    app=Register(win)  
    win.mainloop()  

