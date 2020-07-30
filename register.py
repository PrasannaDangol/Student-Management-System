from tkinter import *
from tkinter import messagebox
from PIL import ImageTk #pip install pillow
import pymysql #pip install pymysql

class Register:

    def login_window(self):
        self.root.destroy()
        import login

    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("2350x1000+0+0")

        self.bg=ImageTk.PhotoImage(file="images/Freyja.jpg")
        bg = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.left = ImageTk.PhotoImage(file="images/image.jpg")
        left = Label(self.root, image=self.left).place(x=215, y=100, width=435, height=800)

        frame1= Frame(self.root, bg="skyblue")
        frame1.place(x=650, y=100, width=1000, height=800)

        title=Label(frame1, text="REGISTER HERE", font=("times new roman", 30, "bold"), bg="sky blue",fg="blue").place(x = 320, y=30)

        fname = Label(frame1, text="First Name", font=("times new roman", 20, "bold"), bg="sky blue", fg="grey").place(x=150, y=150)
        self.txt_fname = Entry(frame1,font=("times new roman",15),bg="light grey")
        self.txt_fname.place(x=415,y=155,width=300)

        lname = Label(frame1, text="Last Name", font=("times new roman", 20, "bold"), bg="sky blue",fg="grey").place(x=150, y=225)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_lname.place(x=415, y=230, width=300)

        username = Label(frame1, text="User Name", font=("times new roman", 20, "bold"), bg="sky blue", fg="grey").place(x=150, y=300)
        self.txt_username = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_username.place(x=415, y=305, width=300)

        email = Label(frame1, text="Email", font=("times new roman", 20, "bold"), bg="sky blue", fg="grey").place(x=150, y=375)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_email.place(x=415, y=380, width=300)

        contact = Label(frame1, text="Contacct No.", font=("times new roman", 20, "bold"), bg="sky blue", fg="grey").place(x=150, y=450)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="light grey")
        self.txt_contact.place(x=415, y=455, width=300)

        password = Label(frame1, text="Password", font=("times new roman", 20, "bold"), bg="sky blue",fg="grey").place(x=150, y=525)
        self.txt_password = Entry(frame1, show="*", font=("times new roman", 15), bg="light grey")
        self.txt_password.place(x=415, y=530, width=300)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 20, "bold"), bg="sky blue", fg="grey").place(x=150, y=600)
        self.txt_cpassword = Entry(frame1, show="*", font=("times new roman", 15), bg="light grey")
        self.txt_cpassword.place(x=415, y=605, width=300)

        self.var_chk = IntVar()
        chk = Checkbutton(frame1,text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="sky blue", font=("times new roman",12)).place(x=150,y=675)

        self.btn_img= ImageTk.PhotoImage(file="images/image1.png")
        btn_register = Button(frame1, image=self.btn_img, bg="sky blue", activebackground='sky blue', bd=0, cursor="hand2", command=self.register_data).place(x=350,y=720)
        btn_login = Button(self.root, text="Sign In", font=("times new roman", 20), bg="sky blue", bd=0, cursor="hand2",command=self.login_window).place(x=350, y=750, width=150)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_username.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.txt_fname.delete(0, END)




    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_username.get() == "" or self.txt_email.get() == "" or self.txt_contact.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree our terms and conditions", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="ravi_app")
                cur = con.cursor()
                cur.execute("select * from student where username=%s", self.txt_username.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "User already exists", parent=self.root)
                else:
                    cur.execute("insert into student (f_name,l_name,username,contact,email,password) values(%s,%s,%s,%s,%s,%s)",
                                (
                                 self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_username.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.txt_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successful", parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)




root = Tk()
obj = Register(root)
root.mainloop()