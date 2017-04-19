import tkinter
from tkinter import ttk
import requests
from django.contrib.auth import logout as dj_logout
import psycopg2
from Crypto.Hash import SHA256
import sys
#from lokahi_dropbox.frontend.models import BaseUser
#import django.contrib.auth.views as logger
#from django.contrib.auth.models import User



class Lokahi(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.init_gui()

    def on_quit(self):
        """Exits program."""
        #dj_logout()
        quit()

    def login(self):

        username = self.username.get()
        password = self.password.get()
        h = SHA256.new()
        h.update(password.encode())
        print(h.hexdigest())
        URL = "http://localhost:8000/"

        client = requests.session()

        # Retrieve the CSRF token first
        client.get(URL)  # sets cookie
        csrftoken = client.cookies['csrftoken']
        r = client.post(URL, data={'username': username, 'password': password , 'csrfmiddlewaretoken': csrftoken, "next": "home/"})
        #print(r.content.decode())
        try:
            conn = psycopg2.connect("dbname='lokahi_dropbox' user='admin' host='localhost' password='password'")
            cur = conn.cursor()
            cur.execute("""SELECT * from auth_user WHERE username = %(un)s""", {'un': username})
            rows = cur.fetchall()
            print("\nShow me the databases:\n")
            print(rows)
            for row in rows:
                print("   ", row[0])

        except:
            print("ARGH")

        #buser = BaseUser.objects.get(user=User())
        #logger.login
        self.answer_label['text'] = username + " " + password


    def init_gui(self):
        """Builds GUI."""
        self.root.title('Lokahi')
        self.root.option_add('*tearOff', 'FALSE')

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

        self.answer_frame = ttk.LabelFrame(self, text='Answer',
                                           height=100)
        self.answer_frame.grid(column=0, row=5, columnspan=4, sticky='nesw')

        self.answer_label = ttk.Label(self.answer_frame, text='')
        self.answer_label.grid(column=0, row=5)

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

