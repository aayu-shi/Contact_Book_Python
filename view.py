from tkinter import *
import sqlite3
from tkinter import messagebox
from add_contact import addContact
from update import Update
from display import Display

con = sqlite3.connect('database.db')
cur = con.cursor()


class my_contacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("My Contacts")
        self.geometry("650x650+600+200")
        self.resizable(False, False)

        # frames
        self.top = Frame(self, height=100, bg='#a5b5c4')
        self.top.pack(fill=X)

        # self.bottom = Frame(master, height=500, bg='#e9e3ff')
        self.bottom = Frame(self, height=650, bg='#e6e39c')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='icons/group.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='#a5b5c4')
        self.top_image_label.place(x=200, y=40)

        # heading
        self.heading = Label(self.top, text='My Contacts', font='times 18 bold', bg='#a5b5c4', fg='black')
        self.heading.place(x=250, y=40)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
        self.listbox = Listbox(self.bottom, width=50, height=27)  # width=characters,height=lines hence height>width
        self.listbox.grid(row=0, column=0, padx=(40, 0))

        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.grid(row=0, column=1, sticky=N + S)

        persons = cur.execute("select * from 'contacts'").fetchall()
        count = 0
        for person in persons:
            self.listbox.insert(count, str(person[0])+". "+ person[1]+" "+ person[2])
            count+=1

        # buttons
        b1 = Button(self.bottom, text="Add", width=15, font='Sans 12 bold', command=self.add_people)
        b1.grid(row=0, column=2, padx=30, pady=20, sticky=N)

        b2 = Button(self.bottom, text="Update", width=15, font='Sans 12 bold', command=self.update_contact)
        b2.grid(row=0, column=2, padx=30, pady=60, sticky=N)

        b3 = Button(self.bottom, text="Display", width=15, font='Sans 12 bold', command=self.display_contact)
        b3.grid(row=0, column=2, padx=30, pady=100, sticky=N)

        b4 = Button(self.bottom, text="Delete", width=15, font='Sans 12 bold', command=self.delete_contact)
        b4.grid(row=0, column=2, padx=30, pady=140, sticky=N)

    def delete_contact(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]
        query = "delete from contacts where person_id='{}'".format(person_id)
        answer= messagebox.askquestion("Warning", "Are you sure you want to delete this contact")
        if answer == 'yes':
            try:

                cur.execute(query)
                con.commit()  # commit data to add to database
                messagebox.showinfo("Success", "Contact deleted")
                self.destroy()

            except EXCEPTION as e:
                messagebox.showerror("Info", str(e))
        else:
            messagebox.showerror("Error", "fill all fields", icon='warning')

    def add_people(self):
        people = addContact()
        self.destroy()

    def update_contact(self):
        selected_item=self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]
        updt= Update(person_id)


    def display_contact(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]
        info = Display(person_id)




