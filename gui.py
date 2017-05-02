import tkinter
from tkinter import ttk
from tkinter import *
import psycopg2


import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'lokahi_dropbox.lokahi_dropbox.settings'
from django.contrib.auth.hashers import check_password



class Lokahi(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        """Exits program."""
        #dj_logout()
        quit()

    def show_table(self, table):
        table['height'] = 10
        table['show'] = 'tree headings'

    def hide_table(self, table):
        table['show'] = []
        table['height'] = 0

    def setup_report_table(self, table, row):
        table.insert("", 1, "reportid", text="Report ID:", values=(row[0]))
        table.insert("", 2, "title", text="Report Title:", values=(row[1]))
        table.insert("", 3, "compName", text="Company Name:", values=(row[2]))
        table.insert("", 4, "CEO", text="CEO:", values=(row[3]))
        table.insert("", 5, "phonenum", text="Phone Number:", values=(row[4]))
        table.insert("", 6, "email", text="Email:", values=(row[5]))
        table.insert("", 7, "location", text="Location:", values=(row[6]))
        table.insert("", 8, "country", text="Country:", values=(row[7]))
        table.insert("", 9, "sector", text="Sector:", values=(row[8]))
        table.insert("", 10, "projects", text="Projects:", values=(row[9]))
        table.insert("", 11, "files", text="Files:", values=(row[11]))
        table.insert("", 12, "timestamp", text="Time Created:", values=(row[12]))


    def view_reports(self):
        try:
            conn = psycopg2.connect("dbname='lokahi_dropbox' user='admin' host='localhost' password='password'")
        except:
            print("Database failure")
        cur = conn.cursor()
        row = []
        try:
            cur.execute("""SELECT * from reports_report WHERE owner_id = %(un)s """, {'un': self.root.user_id})
            row = cur.fetchall()
        except:
            print("Failed to view reports")
        if row.__len__() > 0:
            self.view_reports_table.delete(*self.view_reports_table.get_children())
            self.show_table(self.view_reports_table)
            self.view_reports_table['columns'] = ('Report Title')
            for item in row:
                e = tkinter.Button(self, text=item[1])
                self.view_reports_table.insert('', 'end', e, text=e['text'])
            self.view_reports_table.bind("<Button-1>", self.onclick)
        else:
            self.answer_label['text'] = "You have no reports submitted"

    def onclick(self, event):
        item = self.view_reports_table.identify('item', event.x, event.y)
        report = self.view_reports_table.item(item, "text")
        try:
            conn = psycopg2.connect("dbname='lokahi_dropbox' user='admin' host='localhost' password='password'")
        except:
            print("Database failure")
        cur = conn.cursor()
        row = []
        try:
            cur.execute("""SELECT * from reports_report WHERE title = %(un)s """, {'un': report})
            row = cur.fetchall()
        except:
            print("Failed to view reports")
        self.hide_table(self.view_reports_table)
        self.show_table(self.show_report)
        self.setup_report_table(self.show_report, row[0])




    def login(self):

        username = self.username.get()
        password = self.password.get()

        encoded = ""
        try:
            conn = psycopg2.connect("dbname='lokahi_dropbox' user='admin' host='localhost' password='password'")
        except:
            print("Database failure")
        cur = conn.cursor()

        try:
            cur.execute("""SELECT * from auth_user WHERE username = %(un)s""", {'un': username})
            rows = cur.fetchall()
            encoded = rows[0][1]
            person_id = rows[0][0]
            self.root.user_id = person_id
        except:
            print("Could not execute SELECT Query for table 'auth_user'")

        if check_password(password, encoded):
            self.view_reports_button['state'] = 'enabled'

        else:
            self.answer_label['text'] = "The username and password did not match."




    def init_gui(self):
        """Builds GUI."""
        self.root.title('Lokahi')
        self.root.option_add('*tearOff', 'FALSE')
        self.root.user_id = ""

        self.grid(column=0, row=0, sticky='nsew')

        self.menubar = tkinter.Menu(self.root)

        self.menu_file = tkinter.Menu(self.menubar)
        self.menu_file.add_command(label='Exit', command=self.on_quit)

        self.menu_edit = tkinter.Menu(self.menubar)

        self.menubar.add_cascade(menu=self.menu_file, label='File')
        self.menubar.add_cascade(menu=self.menu_edit, label='Edit')

        self.root.config(menu=self.menubar)



        self.username = ttk.Entry(self, width=15)
        self.username.grid(column=1, row=2)

        self.password = ttk.Entry(self, width=15, show="*")
        self.password.grid(column=1, row=3)

        self.login_button = ttk.Button(self, text='Login',
                                      command=self.login)
        self.login_button.grid(column=0, row=4, columnspan=4)

        self.answer_frame = ttk.LabelFrame(self, text='',
                                           height=100)
        self.answer_frame.grid(column=0, row=5, columnspan=4, sticky='nesw')

        self.answer_label = ttk.Label(self.answer_frame, text='')
        self.answer_label.grid(column=0, row=5)


        self.view_reports_button = ttk.Button(self, text='View Reports', command=self.view_reports, state=DISABLED)
        self.view_reports_button.grid(column = 0, row=5, columnspan=4)
        self.view_reports_table = ttk.Treeview(self, selectmode='browse',show=[], height=0, columns=('placeholder'))
        self.view_reports_table.grid(column=0, row=6, columnspan=4)
        self.show_report = ttk.Treeview(self, selectmode='browse', show=[], height=0, columns=('placeholder'))
        self.show_report.grid(column=0, row=7, columnspan=4)


        # Labels that remain constant throughout execution.
        ttk.Label(self, text='Login').grid(column=0, row=0,
                                                  columnspan=4)
        ttk.Label(self, text='Username').grid(column=0, row=2,
                                                sticky='w')
        ttk.Label(self, text='Password').grid(column=0, row=3,
                                                sticky='w')

        ttk.Separator(self, orient='horizontal').grid(column=0,
                                                      row=1, columnspan=4, sticky='ew')
        for child in self.winfo_children():
            child.grid_configure(padx=50, pady=10)


if __name__ == '__main__':
    root = tkinter.Tk()
    Lokahi(root)
    root.mainloop()

