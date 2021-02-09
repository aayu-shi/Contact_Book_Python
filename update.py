from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


class Update(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)
        self.title("Update Contact")
        self.geometry("650x450+600+200")
        self.resizable(False, False)
        query = "select * from contacts where person_id='{}'".format(person_id)
        result = cur.execute(query).fetchall()[0]
        print(result)
        self.person_id=person_id
        person_name = result[1]  # tuples
        person_surname = result[2]
        person_email = result[3]
        person_phone = result[4]
        person_address = result[5]

        # frames
        self.top = Frame(self, height=100, bg='#a5b5c4')
        self.top.pack(fill=X)

        # self.bottom = Frame(master, height=500, bg='#e9e3ff')
        self.bottom = Frame(self, height=350, bg='#e6e39c')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/update.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='#a5b5c4')
        self.top_image_label.place(x=190, y=26)

        # heading
        self.heading = Label(self.top, text='Update Contact', font='times 18 bold', bg='#a5b5c4', fg='black')
        self.heading.place(x=250, y=40)

        # name
        self.label_name = Label(self.bottom, text='Name', font='arial 15 bold', fg='black', width=8)
        self.label_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=180, y=40, height=30)

        # surname
        self.label_surname = Label(self.bottom, text='Last Name', font='arial 15 bold', fg='black', width=8)
        self.label_surname.place(x=40, y=80)
        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.place(x=180, y=80, height=30)

        # email

        self.label_email = Label(self.bottom, text='Email', font='arial 15 bold', fg='black', width=8)
        self.label_email.place(x=40, y=120)
        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=180, y=120, height=30)

        # phone
        self.label_phone = Label(self.bottom, text='Phone No.', font='arial 15 bold', fg='black', width=8)
        self.label_phone.place(x=40, y=160)
        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, person_phone)
        self.entry_phone.place(x=180, y=160, height=30)

        # address
        self.label_address = Label(self.bottom, text='Address', font='arial 15 bold', fg='black', width=8)
        self.label_address.place(x=40, y=200)
        self.entry_address = Text(self.bottom, width=23, height=4)
        self.entry_address.insert(0.1, person_address)
        self.entry_address.place(x=180, y=200)

        # save button
        button = Button(self.bottom, text="Save Changes", width=15, font='Sans 12 bold', command=self.update_person)
        button.place(x=270, y=300)

    def update_person(self):
        person_id = self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')

        query = "update contacts set person_name='{}', person_surname='{}', person_email='{}', person_phone='{}', " \
                "person_address='{}' where person_id={}".format(name, surname, email, phone, address, person_id)

        try:
            cur.execute(query)
            con.commit() # commit data to add to database
            messagebox.showinfo("Success", "Contact Updated")

        except EXCEPTION as e:
            messagebox.showerror("Error", str(e))
