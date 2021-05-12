from tkinter import Tk, Label, Button, messagebox
from tkinter import *
from PIL import Image, ImageTk
import time

import matplotlib.pyplot as plt
import numpy as np


##### Login Page #####

class Login_Page:

    def __init__(self, login=Tk()):  # This is my first change so i already initialize a Tk window inside the class
      
        self.login = login
        login.protocol("WM_DELETE_WINDOW",self.event_X)
        login.title("Login - Fullwood Packo")
        login.geometry("280x230+450+170")
        login.resizable(False,False) 
        
        
        # Login S.M McKee Company Logo Banner Image
        self.left=ImageTk.PhotoImage(file="image1.png")
        smmckeelogo=Label(self.login,image=self.left).place(x=0,y=-85,relwidth=1,relheight=1)
        
        # Creating login and password labels

        self.username = Label(login, text="Username:")
        self.username.place(relx=0.03, rely=0.298, height=20, width=70)

        self.password = Label(login, text="Password:")
        self.password.place(relx=0.03, rely=0.468, height=20, width=70)

        # Creating entry boxes

        self.username_box = Entry(login)
        self.username_box.place(relx=0.29, rely=0.298, height=20, relwidth=0.30)

        self.password_box = Entry(login)
        self.password_box.place(relx=0.29, rely=0.468, height=20, relwidth=0.30)
        self.password_box.configure(show="*")
        
        
        # Creating login and exit buttons

        self.login_button = Button(login, text="Login")
        self.login_button.place(relx=0.15, rely=0.638, height=30, width=60)
        self.login_button.configure(command=self.login_user)

        self.login_completed = IntVar()

        self.exit_button = Button(login, text="Exit") 
        self.exit_button.place(relx=0.37, rely=0.638, height=30, width=60)
        self.exit_button.configure(command=self.exit_login)


        # Creating checkbox to reveal password

        self.var = IntVar()
        self.show_password = Checkbutton(login)
        self.show_password.place(relx=0.15, rely=0.8, relheight=0.100, relwidth=0.43)
        self.show_password.configure(justify='left')
        self.show_password.configure(text='''Show password''')
        self.show_password.configure(variable=self.var, command=self.cb)
    
    def event_X(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            exit()

    def cb(self, ):
        if self.var.get() == True:
            self.password_box.configure(show="")
        else:
            self.password_box.configure(show="*")


    # Giving function to login process

    def login_user(self):
        name = self.username_box.get()
        password = self.password_box.get()
        login_completed = self.login_completed.get()

        if name == "" and password == "":
            messagebox.showinfo("Success, designed and developed by Hamish McKee 2021", "Login successful!")
            self.login.destroy()  # Removes the toplevel window
            self.login_completed == 1

        else:
            messagebox.showwarning("Login Failed - Acess Denied", "Please check your credentials or enter if needed!") # If name is anything but 'admin' and password is anything but 'fusion' messagebox (or empty)

        # return


    def exit_login(self):
        msg = messagebox.askyesno("Exit login page", "Do you really want to exit?")
        if (msg):
            exit()


    def mainloop_window(self):  # This is the class function that helps me to mainloop the window
        self.login.mainloop()

login_page = Login_Page()  # I dont need to pass the root now since its initialized inside the class
login_page.mainloop_window()  # Just mainlooping the login window


    ##### Main Window #####


class Main_Win:
    def __init__(self, main_win=Tk()):  # This is my first change so i already initialize a Tk window inside the class
        self.main_win = main_win
        main_win.title("Cow Teat Visualiser v1.0")
        main_win.geometry("900x500+250+130")
        main_win.resizable(False,False)
        
        
        # Main window backround image
        self.left=ImageTk.PhotoImage(file="image2.png")
        main_bk=Label(self.main_win,image=self.left).place(x=-175,y=115,relwidth=1,relheight=1)
        
        # Cow icon image
        #self.left=ImageTk.PhotoImage(file="cow_icon.png")
        #cowicon=Label(self.main_win,image=self.left).place(x=220,y=0,relwidth=1,relheight=1)
        
        # Creating teat labels (RF, RR, LF, LR)

        # Right Front
        self.rightfront = Label(main_win, text="Right Front", bg="yellow")
        self.rightfront.place(x=80, y=40)
        
        # Right Rear
        self.rightrear = Label(main_win, text="Right Rear",fg="white", bg="red")
        self.rightrear.place(x=80, y=140)
        
        # Left Front
        self.leftfront = Label(main_win, text="Left Front", bg="light green")
        self.leftfront.place(x=310, y=40)
        
        # Left Rear
        self.leftfront = Label(main_win, text="Left Rear", bg="light blue")
        self.leftfront.place(x=310, y=140)
        
        
        # Creating teat co-ordinate section title
        self.teat_title = Label(main_win, text="Teat Co-ordinates", font="Helvetica 18 underline")
        self.teat_title.place(x=160, y=3.5)
        
        
        # Creating x and y labels for RF, RR, LF and LR    
        
        self.x_rightfront = Label(main_win, text="X:")
        self.x_rightfront.place(x=10, y=60)
        
        self.y_rightfront = Label(main_win, text="Y:")
        self.y_rightfront.place(x=10, y=100)
        
        self.x_rightrear = Label(main_win, text="X:")
        self.x_rightrear.place(x=10, y=160)
        
        self.y_rightrear = Label(main_win, text="Y:")
        self.y_rightrear.place(x=10, y=200)
        
        self.x_leftfront = Label(main_win, text="X:")
        self.x_leftfront.place(x=240, y=60)
        
        self.y_leftfront = Label(main_win, text="Y:")
        self.y_leftfront.place(x=240, y=100)
        
        self.x_leftrear = Label(main_win, text="X:")
        self.x_leftrear.place(x=240, y=160)
        
        self.y_leftrear = Label(main_win, text="Y:")
        self.y_leftrear.place(x=240, y=200)
        
        
        # Creating teat x and y entry boxes
        
        # Teat Right Front (RF) entry boxes
        self.teat1_x_box = Entry(main_win)
        self.teat1_x_box.place(x=30, y=60)

        self.teat1_y_box = Entry(main_win)
        self.teat1_y_box.place(x=30, y=100)

        # Teat Right Rear (RR) entry boxes
        self.teat2_x_box = Entry(main_win)
        self.teat2_x_box.place(x=30, y=160)

        self.teat2_y_box = Entry(main_win)
        self.teat2_y_box.place(x=30, y=200)
        
        # Teat Left Front (LF) entry boxes
        self.teat3_x_box = Entry(main_win)
        self.teat3_x_box.place(x=260, y=60)

        self.teat3_y_box = Entry(main_win)
        self.teat3_y_box.place(x=260, y=100)
        
        # Teat Left Rear (LR) entry boxes
        self.teat4_x_box = Entry(main_win)
        self.teat4_x_box.place(x=260, y=160)

        self.teat4_y_box = Entry(main_win)
        self.teat4_y_box.place(x=260, y=200)
        
        # Creating teat plot button
        
        self.teat_plot_button = Button(main_win, text="Plot Teats On Scatter Graph") 
        self.teat_plot_button.place(relx=0.29, rely=0.48, height=35, width=190)
        #self.teat_plot_button.configure(command=self.teat_plot)
        
        # Giving function to the teat plot button
        
        
        
        
    def mainloop_window(self):  # This is the class function that helps me to mainloop the window
        self.main_win.mainloop()


main_win = Main_Win()  # I dont need to pass the root now since its initialized inside the class
main_win.mainloop_window()  # Just mainlooping the authentication window