from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Login_Window:
    def clear(self):
        self.Roll_No_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.txt_address.delete("1.0", END)

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="" or self.txt_address.get('1.0', END)=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="ravi_app")
            cur = con.cursor()
            cur.execute("insert into studentdata values(%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.Roll_No_var.get(),
                            self.name_var.get(),
                            self.email_var.get(),
                            self.gender_var.get(),
                            self.contact_var.get(),
                            self.dob_var.get(),
                            self.txt_address.get('1.0', END)
                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="ravi_app")
        cur = con.cursor()
        cur.execute("update studentdata set name=%s, email=%s, gender=%s, contact=%s,dob=%s, address=%s where roll_no=%s",
                    (
                        self.name_var.get(),
                        self.email_var.get(),
                        self.gender_var.get(),
                        self.contact_var.get(),
                        self.dob_var.get(),
                        self.txt_address.get('1.0', END),
                        self.Roll_No_var.get(),
                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="ravi_app")
        cur = con.cursor()
        cur.execute("delete from studentdata where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="ravi_app")
        cur = con.cursor()
        cur.execute("select * from studentdata")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="ravi_app")
        cur = con.cursor()

        cur.execute("select * from studentdata where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        else:
            messagebox.showerror("Error", "No Data Found")

        con.close()


    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])



    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("2350x1000+0+0")

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", bd=10, relief=GROOVE,
                      font=("times new roman", 30, "bold"), bg="sky blue", fg="blue")
        title.pack(side=TOP, fill=X)

        frame1 = Frame(self.root, bd=4, relief=RIDGE, bg="sky blue")
        frame1.place(x=20, y=100, width=500, height=850)

        title = Label(frame1, text="Manage Student", bd=10, relief=RIDGE, font=("times new roman", 30, "bold"),
                      bg="sky blue", fg="blue")
        title.grid(row=0, columnspan=2, pady=20, padx=50)

        lbl_roll = Label(frame1, text="Roll no.", font=("times new roman", 17, "bold"), bg="sky blue", fg="Black")
        lbl_roll.grid(row=1, column=0, pady=15, padx=5, sticky="w")
        txt_roll = Entry(frame1, text="Roll no.", textvariable=self.Roll_No_var, font=("times new roman", 17, "bold"),
                         width=23, bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=15, padx=5, sticky="w")

        lbl_name = Label(frame1, text="Name", font=("times new roman", 17, "bold"), bg="sky blue", fg="Black")
        lbl_name.grid(row=2, column=0, pady=15, padx=5, sticky="w")
        txt_name = Entry(frame1, text="Name", textvariable=self.name_var, font=("times new roman", 17, "bold"),
                         width=23, bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=15, padx=5, sticky="w")

        lbl_email = Label(frame1, text="Email", font=("times new roman", 17, "bold"), bg="sky blue", fg="Black")
        lbl_email.grid(row=3, column=0, pady=15, padx=5, sticky="w")
        txt_email = Entry(frame1, text="Email", textvariable=self.email_var, font=("times new roman", 17, "bold"),
                          width=23, bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=15, padx=5, sticky="w")

        lbl_gender = Label(frame1, text="Gender", font=("times new roman", 17, "bold"), bg="sky blue", fg="Black")
        lbl_gender.grid(row=4, column=0, pady=15, padx=5, sticky="w")
        combo_gender = ttk.Combobox(frame1, textvariable=self.gender_var, font=("times new roman", 17, "bold"), width=22, state="readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=15, padx=5, sticky="w")

        lbl_contact = Label(frame1, text="Contact", font=("times new roman", 17, "bold"), bg="sky blue", fg="Black")
        lbl_contact.grid(row=5, column=0, pady=15, padx=5, sticky="w")
        txt_contact = Entry(frame1, text="Contact", textvariable=self.contact_var, font=("times new roman", 17, "bold"),
                            width=23, bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=15, padx=5, sticky="w")

        lbl_dob = Label(frame1, text="D.O.B", font=("times new roman", 17, "bold"), bg="sky blue", fg="Black")
        lbl_dob.grid(row=6, column=0, pady=15, padx=5, sticky="w")
        txt_dob = Entry(frame1, text="D.O.B", textvariable=self.dob_var, font=("times new roman", 17, "bold"), width=23,
                        bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=15, padx=5, sticky="w")

        lbl_address = Label(frame1, text="Address", font=("times new roman", 17, "bold"), bg="sky blue", fg="Black")
        lbl_address.grid(row=7, column=0, pady=15, padx=5, sticky="w")
        self.txt_address = Text(frame1, width=23, height=4, font=("times new roman", 17, "bold"))
        self.txt_address.grid(row=7, column=1, pady=15, padx=5, sticky="w")

        btn_frame = Frame(frame1, bd=4, relief=RIDGE, bg="sky blue")
        btn_frame.place(x=10, y=720, width=450)

        addbtn = ttk.Button(btn_frame, text="Add", width=10, command=self.add_students)
        addbtn.grid(row=0, column=0, padx=10, pady=10)

        updatebtn = ttk.Button(btn_frame, text="Update", width=10, command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=10, pady=10)

        deletebtn = ttk.Button(btn_frame, text="Delete", width=10, command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=10, pady=10)

        clearbtn = ttk.Button(btn_frame, text="Clear", width=10, command=self.clear)
        clearbtn.grid(row=0, column=3, padx=10, pady=10)

        frame2 = Frame(self.root, bd=4, relief=RIDGE, bg="#D3D3D3")
        frame2.place(x=550, y=100, width=1320, height=850)

        lbl_search = Label(frame2, text="Search By", font=("times new roman", 20, "bold"), bg="#D3D3D3", fg="Black")
        lbl_search.grid(row=0, column=0, pady=15, padx=20, sticky="w")

        combo_search = ttk.Combobox(frame2, textvariable=self.search_by, font=("times new roman", 17, "bold"), width=10, state="readonly")
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=15, padx=20, sticky="w")

        txt_search = ttk.Entry(frame2, textvariable=self.search_txt, width=23, font=("times new roman", 17, "bold"))
        txt_search.grid(row=0, column=2, pady=15, padx=20, sticky="w")

        searchbtn = ttk.Button(frame2, text="Search", width=10, command=self.search_data)
        searchbtn.grid(row=0, column=3, padx=20, pady=10)

        searchallbtn = ttk.Button(frame2, text="Search All", width=10, command=self.fetch_data)
        searchallbtn.grid(row=0, column=4, padx=20, pady=10)

        frame3 = Frame(frame2, bd=4, relief=RIDGE, bg="#D3D3D3")
        frame3.place(x=35, y=70, width=1250, height=750)

        scroll_x = Scrollbar(frame3, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame3, orient=VERTICAL)
        self.Student_table = ttk.Treeview(frame3,
                                          columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=174)
        self.Student_table.column("name", width=174)
        self.Student_table.column("email", width=174)
        self.Student_table.column("gender", width=174)
        self.Student_table.column("contact", width=174)
        self.Student_table.column("dob", width=174)
        self.Student_table.column("address", width=174)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


root = Tk()
obj = Login_Window(root)
root.mainloop()
