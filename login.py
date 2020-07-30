from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk #pip install pillow
import pymysql #pip install pymysql

class Login_Window:
    def register_window(self):
        self.root.destroy()
        import register

    def login_sucess(self):
        self.root.destroy()
        import Student_Management_System

    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("2350x1000+0+0")



        self.bg = ImageTk.PhotoImage(file="images/Freyja.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="images/image.jpg")
        left = Label(self.root, image=self.left).place(x=215, y=225, width=435, height=600)

        login_frame = Frame(self.root, bg="#7395AE")
        login_frame.place(x=650, y=225, width=1000, height=600)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="#7395AE", fg="blue").place(x = 320, y=30)

        email = Label(login_frame, text="Email", font=("times new roman", 20, "bold"), bg="#7395AE", fg="#1F2833").place(x=150,y=150)
        self.txt_email = ttk.Entry(login_frame, font=("times new roman", 15))
        self.txt_email.place(x=415, y=155, width=300)

        password = Label(login_frame, text="Password", font=("times new roman", 20, "bold"), bg="#7395AE", fg="#1F2833").place(x=150, y=250)
        self.txt_password = ttk.Entry(login_frame, show="*", font=("times new roman", 15))
        self.txt_password.place(x=415, y=255, width=300)

        btn_reg = Button(login_frame,cursor="hand2", text="Register New Account?", font=("times new roman", 14),command=self.register_window,bg= "#7395AE", activebackground='#7395AE', bd=0, fg="#B00857").place(x=150,y=325)

        #btn_login = Button(login_frame, text="Login", font=("times new roman", 20), command=self.login).place(x=375, y=400, width=180, height=50)
        btn_login = ttk.Button(login_frame, text="Login",command=self.login, width=20)
        btn_login.grid(row=0, column=0, padx=385,pady=400)

        # scroll_x = Scrollbar(self.root, orient=HORIZONTAL)
        # scroll_y = Scrollbar(self.root, orient=VERTICAL)
        # xscrollcommand = scroll_x.set
        # yscrollcommand = scroll_y.set
        # scroll_x.pack(side=BOTTOM, fill=X)
        # scroll_y.pack(side=RIGHT, fill=Y)

    def clear(self):
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)




    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            self.clear()
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="ravi_app")
                cur = con.cursor()
                cur.execute("select * from student where email=%s and password=%s", (self.txt_email.get(),self.txt_password.get()))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Email & Password", parent=self.root)
                    self.clear()
                else:
                    self.login_sucess()
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)





root = Tk()
obj = Login_Window(root)
root.mainloop()