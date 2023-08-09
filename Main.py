# ----- Package importing area -----
from tkinter import *
from PIL import Image, ImageTk
from customtkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkinter import filedialog
import smtplib

# ----- Main class importing area -----
class Main:
# ----- Constructor -----
    def __init__(self,window):
        
    # ----- Variable for Colors -----
        self.primary = "#FF233C"
        self.secondary = "#FF2B49"
        self.background = "#FFF0F4"
        self.text = "#33000E"
        self.secondary_text = "#479CFF"
        
    # ----- Window config -----
        self.win = window
        self.win.title("Blood Donor Application")
        self.win.geometry("1366x768+0+0")
        self.win.config(bg=self.background)
        self.win.resizable(0,0)
        self.win.iconbitmap("assets/icon.ico")
    
    # ----- Image importing area -----
        home_open = Image.open("assets/#1_background.png") #Home_Image
        home_resize = home_open.resize((1166,601),Image.ANTIALIAS)
        self.home_img = ImageTk.PhotoImage(home_resize)
        
        Start_btn_open = Image.open("assets/Start_btn.jpg") #Start_Button
        self.start_btn = ImageTk.PhotoImage(Start_btn_open)
        
        contact_open = Image.open("assets/#2_contact_background.png") #contact_Image
        contact_resize = contact_open.resize((1166,601),Image.ANTIALIAS)
        self.contact_img = ImageTk.PhotoImage(contact_resize)
        
        Donor_login_open = Image.open("assets/#3_donor_login_background.png") #Donor_login_Image
        Donor_login_resize = Donor_login_open.resize((1166,601),Image.ANTIALIAS)
        self.Donor_login_img = ImageTk.PhotoImage(Donor_login_resize)
        
        Donor_Signup_open = Image.open("assets/#4_signup_background.png") #Donor_signup_Image
        Donor_Signup_resize = Donor_Signup_open.resize((1166,601),Image.ANTIALIAS)
        self.Donor_Signup_img = ImageTk.PhotoImage(Donor_Signup_resize)
        
        Forgot_pass_open = Image.open("assets/#5_forgot_password_background.png") #Forgot_Password_Image
        Donor_Forgot_pass_resize = Forgot_pass_open.resize((1166,601),Image.ANTIALIAS)
        self.Forgot_pass_img = ImageTk.PhotoImage(Donor_Forgot_pass_resize)
        
        donor_reg_open = Image.open("assets/#7_donor_reg_background.png") #Donor_registration_Image
        donor_reg_resize = donor_reg_open.resize((1166,601),Image.ANTIALIAS)
        self.Donor_reg_img = ImageTk.PhotoImage(donor_reg_resize)
        
        donor_req_open = Image.open("assets/#8_donor_request_background.png") #Donor_request_Image
        donor_req_resize = donor_req_open.resize((868,601),Image.ANTIALIAS)
        self.Donor_req_img = ImageTk.PhotoImage(donor_req_resize)
        
        Submit_btn_open = Image.open("assets/Submit_btn.png") #Start_Button
        self.submit_btn = ImageTk.PhotoImage(Submit_btn_open)
        
        side_img_open = Image.open("assets/side.png") #Side_background
        self.side_img = ImageTk.PhotoImage(side_img_open)
        
        donor_panel_img_open = Image.open("assets/#6_donor_panel_icon.png") #Donor_background_icon
        self.donor_panel_img = ImageTk.PhotoImage(donor_panel_img_open)
        
        Login_btn_open = Image.open("assets/Login_btn.png") #Login_Button
        self.Login_btn = ImageTk.PhotoImage(Login_btn_open)
        
        Change_pass_btn_open = Image.open("assets/Change_pass_btn.png") #Change_password_Button
        self.Change_pass_btn = ImageTk.PhotoImage(Change_pass_btn_open)
        
        Signup_btn_open = Image.open("assets/signup_btn.png") #Signup_Button
        self.Signup_btn = ImageTk.PhotoImage(Signup_btn_open)
        
        upload_btn_open = Image.open("assets/upload_btn.png") #upload_Button
        self.upload_btn = ImageTk.PhotoImage(upload_btn_open)
        
        Home_btn_open = Image.open("assets/Home_btn.png") #Home_icon
        self.Home_btn = ImageTk.PhotoImage(Home_btn_open)
        
        back_btn_open = Image.open("assets/back_btn.png") #Back_icon
        self.Back_btn = ImageTk.PhotoImage(back_btn_open)
        
        Logout_btn_open = Image.open("assets/Logout.png") #Logout_icon
        self.Logout_btn = ImageTk.PhotoImage(Logout_btn_open)
        
        upload_img_open = Image.open("assets/upload_image.png") #upload_image
        self.upload_img = ImageTk.PhotoImage(upload_img_open)
        
        register_btn_open = Image.open("assets/register_btn.png") #register_btn
        self.register_btn = ImageTk.PhotoImage(register_btn_open)
        
        request_btn_open = Image.open("assets/request_btn.png") #request_btn
        self.request_btn = ImageTk.PhotoImage(request_btn_open)
        
        image_open = Image.open("assets/Box_8.png") #Entry_box_in_donor_request_page
        self.Image_box = ImageTk.PhotoImage(image_open)
    #Entry_box_in_contact_page   
        image2_resize = image_open.resize((345,45),Image.ANTIALIAS)
        self.Image2_box = ImageTk.PhotoImage(image2_resize)
        
        image2_2_resize = image_open.resize((345,100),Image.ANTIALIAS)
        self.Image2_2_box = ImageTk.PhotoImage(image2_2_resize)
    #Entry_box_in_Login_page
        image3_resize = image_open.resize((375,40),Image.ANTIALIAS)
        self.Image3_box = ImageTk.PhotoImage(image3_resize)
    #Entry_box_in_Signup_page
        image4_resize = image_open.resize((394,40),Image.ANTIALIAS)
        self.Image4_box = ImageTk.PhotoImage(image4_resize)
    #Entry_box_in_Forgot_password_page
        image5_resize = image_open.resize((350,40),Image.ANTIALIAS)
        self.Image5_box = ImageTk.PhotoImage(image5_resize)
    #Entry_box_in_donor_register_page
        image7_resize = image_open.resize((377,35),Image.ANTIALIAS)
        self.Image7_box = ImageTk.PhotoImage(image7_resize)
        
        image7_2_resize = image_open.resize((377,100),Image.ANTIALIAS)
        self.Image7_2_box = ImageTk.PhotoImage(image7_2_resize)
        
        self.Home_page(1)
    
# ----- 1) Home Page -----
    def Home_page(self, where):
        
        if(where=="contact" or where == "home"):
            self.main_frame_home.destroy()
        if(where=="forget" or where == "login" or where == "signup"):
            self.Main_frame_for.destroy()
        
    # ----- Header Frame -----
        Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
        Header_fr.place(x=0,y=0)
        
        Button_fr = Frame(Header_fr, width=400, height=80, bg=self.primary)
        Button_fr.place(x=866)
    
    # ----- Main Frame -----
        self.main_frame_home = Frame(self.win, width=1166, height=601, bg=self.background)
        self.main_frame_home.place(x=100, y=122)
        
    # ----- Labels -----
        Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Blood Donor Application", fg=self.background, bg=self.primary)
        Header_lab.place(x=100, height=80)
        
        back_lab = Label(self.main_frame_home, image=self.home_img, bd=0, bg=self.background)
        back_lab.place(x=0)
        
    # ----- Buttons -----
        home_btn = Button(Button_fr, text="Home", fg=self.background, font=("poppins",14,"bold"), bg=self.primary, border=0, activeforeground=self.text, cursor="hand2", command=lambda:self.Home_page("home"))
        home_btn.place(x=0, height=80, width=200)
        
        contact_btn = Button(Button_fr, text="Contact", fg=self.background, font=("poppins",14,"bold"), bg=self.primary, border=0, activeforeground=self.text, cursor="hand2", command=self.Contact_page)
        contact_btn.place(x=200, height=80, width=200)
        
        start_button = Button(self.win, image=self.start_btn, bd=0, bg="White", activebackground="white", command= lambda: self.Donor_login("home"))
        start_button.place(x=891, y=554)
    
# ----- 2) Contact Page -----
    def Contact_page(self):
        
        self.main_frame_home.destroy()
    # ----- Header Frame -----
        Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
        Header_fr.place(x=0,y=0)
        
        Button_fr = Frame(Header_fr, width=400, height=80, bg=self.primary)
        Button_fr.place(x=866)
        
    # ----- Main Frame -----
        self.main_frame_home = Frame(self.win, width=1166, height=601, bg=self.background)
        self.main_frame_home.place(x=100, y=122)
        
    # ----- Lables -----
        Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Blood Donor Application", fg=self.background, bg=self.primary)
        Header_lab.place(x=100, height=80)
        
        contact_lab = Label(self.main_frame_home, image=self.contact_img, bd=0, bg=self.background)
        contact_lab.place(x=0)
        
        name_lab = Label(self.main_frame_home, text="Full name", font=("poppins",12), fg=self.text, bg="White")
        name_lab.place(x=50, y=145)
        
        Email_lab = Label(self.main_frame_home, text="Email Id", font=("poppins",12), fg=self.text, bg="White")
        Email_lab.place(x=50, y=250)
        
        message_lab = Label(self.main_frame_home, text="Message", font=("poppins",12), fg=self.text, bg="White")
        message_lab.place(x=50, y=355)
        
        box1 = Label(self.main_frame_home, bg="white", image=self.Image2_box)
        box1.place(x=50,y=185)
        box2 = Label(self.main_frame_home, bg="white", image=self.Image2_box)
        box2.place(x=50,y=290)
        box3 = Label(self.main_frame_home, bg="white", image=self.Image2_2_box)
        box3.place(x=50,y=395)
        
    # ----- Entry Boxes -----
        self.username = StringVar()
        self.email = StringVar()
        
        self.name_ent = Entry(self.main_frame_home, fg=self.primary, font=("poppins",16),bd=0, textvariable=self.username)
        self.name_ent.place(x=60, y=194, width=335,height=35)
        
        self.email_ent = Entry(self.main_frame_home, fg=self.primary, font=("poppins",16),bd=0, textvariable=self.email)
        self.email_ent.place(x=60, y=299,width=335,height=35)
        
        self.message_ent = Text(self.main_frame_home, fg=self.primary, font=("poppins",16), bd=0)
        self.message_ent.place(x=60,y=404, width=335, height=85)
    
    # ----- Buttons -----
        home_btn = Button(Button_fr, text="Home", fg=self.background, font=("poppins",14,"bold"), bg=self.primary, border=0, activeforeground=self.text, cursor="hand2", command=lambda:self.Home_page("contact"))
        home_btn.place(x=0, height=80, width=200)
        
        contact_btn = Button(Button_fr, text="Contact", fg=self.background, font=("poppins",14,"bold"), bg=self.primary, border=0, activeforeground=self.text, cursor="hand2", command=self.Contact_page)
        contact_btn.place(x=200, height=80, width=200)
        
        submit_button = Button(self.main_frame_home, image=self.submit_btn, bd=0, bg="white", activebackground="white", command=self.Contact_message)
        submit_button.place(x=50, y=525)
        
# ----- 3) Login Page -----
    def Donor_login(self,ch):
        
        if (ch == 0):
            self.Side_frame.destroy()
        if(ch == 1):
            self.Main_frame_for.destroy()
        else:
            self.main_frame_home.destroy()
            if(ch=="signup"):
                self.Main_frame_for.destroy()
        
    # ----- Header Frame -----
        Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
        Header_fr.place(x=0,y=0)
        
    # ----- Main Frame -----
        self.Main_frame_for = Frame(self.win, width=1166, height=601, bg=self.background)
        self.Main_frame_for.place(x=100, y=122)
           
    # ----- Labels -----
        Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Blood Donor Application", fg=self.background, bg=self.primary)
        Header_lab.place(x=100, height=80)
        
        Donor_login_lab = Label(self.Main_frame_for, image=self.Donor_login_img, bd=0, bg=self.background)
        Donor_login_lab.place(x=0)
        
        Username_lab = Label(self.Main_frame_for, text="Username", font=("poppins",12), fg=self.text, bg="White")
        Username_lab.place(x=692, y=150)
        
        Password_lab = Label(self.Main_frame_for, text="Password", font=("poppins",12), fg=self.text, bg="White")
        Password_lab.place(x=692, y=250)
        
        signup_lab = Label(self.Main_frame_for, text="Don't have a account?", font=("poppins",10), fg="grey", bg="White")
        signup_lab.place(x=765,y=440,height=50)
        
        box1 = Label(self.Main_frame_for, bg="white", image=self.Image3_box)
        box1.place(x=692,y=190)
        box2 = Label(self.Main_frame_for, bg="white", image=self.Image3_box)
        box2.place(x=692,y=290)
        
    # ----- Entry Boxes -----
        self.username = StringVar()
        self.password = StringVar()
        
        self.Username_ent = Entry(self.Main_frame_for, fg=self.primary, font=("poppins",16),bd=0, textvariable=self.username)
        self.Username_ent.place(x=702, y=199, width=365,height=30)
        
        self.Password_ent = Entry(self.Main_frame_for, fg=self.primary, font=("poppins",16),bd=0, show="*", textvariable=self.password)
        self.Password_ent.place(x=702, y=299, width=365,height=30)
        
    # ----- Buttons -----
        home_btn = Button(Header_fr, image=self.Home_btn, bg=self.primary, border=0, activebackground=self.primary, cursor="hand2", command=lambda:self.Home_page("login"))
        home_btn.place(x=1226, height=80)
        
        forgot_btn = Button(self.Main_frame_for, text="Forgot Password?", font=("poppins",10), fg=self.secondary_text, bg="White", activeforeground=self.secondary, bd=0, activebackground="white", command=self.Forgot_password)
        forgot_btn.place(x=692, y=350)
        
        login_btn = Button(self.Main_frame_for, image=self.Login_btn, bg="white", border=0, activebackground="white", cursor="hand2", command=self.Check_login)
        login_btn.place(x=692, y=390)
        
        Signup_btn = Button(self.Main_frame_for, text="Sign Up", font=("poppins",12,"bold"), fg=self.secondary_text, bg="White", bd=0, activebackground="white", command=self.Donor_signup)
        Signup_btn.place(x=900,y=440 ,height=50)
    
# ----- 4) Signup Page -----
    def Donor_signup(self):
    
        self.Main_frame_for.destroy()
    # ----- Header Frame -----
        Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
        Header_fr.place(x=0,y=0)
        
    # ----- Main Frame -----
        self.Main_frame_for = Frame(self.win, width=1166, height=601, bg=self.background)
        self.Main_frame_for.place(x=100, y=122)
        
    # ----- Labels -----
        Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Blood Donor Application", fg=self.background, bg=self.primary)
        Header_lab.place(x=100, height=80)
        
        Donor_signup_lab = Label(self.Main_frame_for, image=self.Donor_Signup_img, bd=0, bg=self.background)
        Donor_signup_lab.place(x=0)
        
        Username_lab = Label(self.Main_frame_for, text="Username", font=("poppins",12), fg=self.text, bg="White")
        Username_lab.place(x=50, y=140)
        
        Password_lab = Label(self.Main_frame_for, text="Password", font=("poppins",12), fg=self.text, bg="White")
        Password_lab.place(x=50, y=240)
        
        Conform_Password_lab = Label(self.Main_frame_for, text="Conform Password", font=("poppins",12), fg=self.text, bg="White")
        Conform_Password_lab.place(x=50, y=340)
        
        Login_lab = Label(self.Main_frame_for, text="Already have a account?", font=("poppins",10), fg="grey", bg="White")
        Login_lab.place(x=130,y=515,height=50)
        
        box1 = Label(self.Main_frame_for, bg="white", image=self.Image4_box)
        box1.place(x=50,y=180)
        box2 = Label(self.Main_frame_for, bg="white", image=self.Image4_box)
        box2.place(x=50,y=280)
        box3 = Label(self.Main_frame_for, bg="white", image=self.Image4_box)
        box3.place(x=50,y=380)
        
    # ----- Entry Boxes -----
        self.username = StringVar()
        self.password = StringVar()
        self.conform_passsword = StringVar()
        
        self.Username_ent = Entry(self.Main_frame_for, fg=self.primary, font=("poppins",16),bd=0, textvariable=self.username)
        self.Username_ent.place(x=60, y=189, width=384,height=30)
        
        self.Password_ent = Entry(self.Main_frame_for, fg=self.primary, font=("poppins",16),bd=0, show="*", textvariable=self.password)
        self.Password_ent.place(x=60, y=289, width=384,height=30)
        
        self.Confrom_Password_ent = Entry(self.Main_frame_for, fg=self.primary, font=("poppins",16),bd=0, show="*", textvariable=self.conform_passsword)
        self.Confrom_Password_ent.place(x=60, y=389, width=384,height=30) 
        
    # ----- Buttons -----
        Signup_btn = Button(self.Main_frame_for, image=self.Signup_btn, bg="white", border=0, activebackground="white", cursor="hand2", command=self.db_Signup)
        Signup_btn.place(x=50, y=460)
        
        login_btn = Button(self.Main_frame_for, text="Log In", font=("poppins",12,"bold"), fg=self.secondary_text, bg="White", bd=0, activebackground="white", command=lambda:self.Donor_login("signup"))
        login_btn.place(x=282,y=515,height=50)
        
        home_btn = Button(Header_fr, image=self.Home_btn, bg=self.primary, border=0, activebackground=self.primary, cursor="hand2", command=lambda:self.Home_page("signup"))
        home_btn.place(x=1226, height=80)
        
# ----- 5) Forgot Password Page -----
    def Forgot_password(self):
        
        self.Main_frame_for.destroy()
    # ----- Header Frame -----
        Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
        Header_fr.place(x=0,y=0)
        
    # ----- Main Frame -----
        self.Main_frame_for = Frame(self.win, width=1166, height=601, bg=self.background)
        self.Main_frame_for.place(x=100, y=122) 
        
    # ----- Labels -----
        Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Blood Donor Application", fg=self.background, bg=self.primary)
        Header_lab.place(x=100, height=80)
        
        Donor_Forgot_pass_lab = Label(self.Main_frame_for, image=self.Forgot_pass_img, bd=0, bg=self.background)
        Donor_Forgot_pass_lab.place(x=0)
        
        Username_lab = Label(self.Main_frame_for, text="Username", font=("poppins",12), fg=self.text, bg="White")
        Username_lab.place(x=50, y=160)
        
        Password_lab = Label(self.Main_frame_for, text="Password", font=("poppins",12), fg=self.text, bg="White")
        Password_lab.place(x=50, y=260)
        
        Conform_Password_lab = Label(self.Main_frame_for, text="Conform Password", font=("poppins",12), fg=self.text, bg="White")
        Conform_Password_lab.place(x=50, y=360)
        
        box1 = Label(self.Main_frame_for, bg="white", image=self.Image5_box)
        box1.place(x=50,y=200)
        box2 = Label(self.Main_frame_for, bg="white", image=self.Image5_box)
        box2.place(x=50,y=300)
        box3 = Label(self.Main_frame_for, bg="white", image=self.Image5_box)
        box3.place(x=50,y=400)
        
    # ----- Entry Boxes -----
        self.username = StringVar()
        self.password = StringVar()
        self.conform_password = StringVar()
        
        self.for_Username_ent = Entry(self.Main_frame_for, fg=self.primary, font=("poppins",16),bd=0, textvariable=self.username)
        self.for_Username_ent.place(x=60, y=209, width=340,height=30)
        
        self.for_Password_ent = Entry(self.Main_frame_for, fg=self.primary, font=("poppins",16),bd=0, show="*", textvariable=self.password)
        self.for_Password_ent.place(x=60, y=309, width=340,height=30)
        
        self.for_Confrom_Password_ent = Entry(self.Main_frame_for, fg=self.primary, font=("poppins",16),bd=0, show="*", textvariable=self.conform_password)
        self.for_Confrom_Password_ent.place(x=60, y=409, width=340,height=30) 
        
    # ----- Buttons -----
        home_btn = Button(Header_fr, image=self.Home_btn, bg=self.primary, border=0, activebackground=self.primary, cursor="hand2", command=lambda:self.Home_page("forget"))
        home_btn.place(x=1226, height=80)
        
        change_pass_btn = Button(self.Main_frame_for, image=self.Change_pass_btn, bg="white", border=0, activebackground="white", cursor="hand2", command=self.db_forgot_passwrd)
        change_pass_btn.place(x=50, y=470)
        
# ----- 6) Donor Panel Page -----
    def Donor_panel(self,ch,where):
        
        if(ch == 0):
            self.Main_frame.destroy()
        if(ch == "donor_request" or ch =="donor_details"):
            self.Side_frame_req.destroy()
            self.center_frame.destroy()
        
        if(len(self.result)>0):
            if(where=="login"):
                messagebox.showinfo("Success Message","Login Sucessfull!!!")
            if(where=="signup"):
                messagebox.showinfo("Success Message","Sucessfully created your account")
            if(ch==1):
                self.Main_frame_for.destroy()
                self.main_frame_home.destroy()
        # ----- Header Frame -----
            Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
            Header_fr.place(x=0,y=0)
            
        # ----- side Frame -----
            self.Side_frame = Frame(self.win, width=377, height=688, bg=self.background)
            self.Side_frame.place(x=0, y=80) 
            
        # ----- Labels -----
            Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Donor Panel", fg=self.background, bg=self.primary)
            Header_lab.place(x=100, height=80)
            
            Donor_side_lab = Label(self.Side_frame, image=self.side_img, bd=0, bg=self.background)
            Donor_side_lab.place(x=0)
            
            self.Donor_panel_lab = Label(self.win, image=self.donor_panel_img, bd=0, bg=self.background)
            self.Donor_panel_lab.place(x=533,y=90)
            
        # ----- Buttons -----
            logout_btn = Button(Header_fr, image=self.Logout_btn, bg=self.primary, border=0, activebackground=self.primary, cursor="hand2", command=lambda: self.Donor_login(0))
            logout_btn.place(x=1226, height=80)
            
            donor_reg_btn = Button(self.Side_frame, text="Donor Register", font=("poppins",22,"bold"), fg=self.text, bg="White", bd=0, activebackground="white", command=lambda:self.Donor_register(0))
            donor_reg_btn.place(x=0, y=140, width=377, height=100)
            
            donor_req_btn = Button(self.Side_frame, text="Donor Request", font=("poppins",22,"bold"), fg=self.text, bg="White", bd=0, activebackground="white", command=lambda:self.Donor_request("donor_panel"))
            donor_req_btn.place(x=0, y=290, width=377, height=100)
            
            donor_details_btn = Button(self.Side_frame, text="Donor Details", font=("poppins",22,"bold"), fg=self.text, bg="White", bd=0, activebackground="white", command=lambda:self.Details("donor_panel"))
            donor_details_btn.place(x=0, y=440, width=377, height=100)
        else:
            messagebox.showwarning("Invalid Entry", "Your Username or Password may Wrong\n\nPlease Enter valid Username and Password")
        
# ----- 7) Donor Register Page -----
    def Donor_register(self,ch):
        
        if(ch == 0):
            self.Side_frame.destroy()
            self.Donor_panel_lab.destroy()
        
    # ----- Header Frame -----
        Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
        Header_fr.place(x=0,y=0)   
        
    # ----- Main Frame -----
        self.Main_frame = Frame(self.win, width=1166, height=601, bg=self.background)
        self.Main_frame.place(x=100, y=122)
    
    # ----- Labels -----
        Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Donor Registration Page", fg=self.background, bg=self.primary)
        Header_lab.place(x=100, height=80)
        
        Donor_registration_lab = Label(self.Main_frame, image=self.Donor_reg_img, bd=0, bg=self.background)
        Donor_registration_lab.place(x=0)
        
        self.upload_frame = CTkFrame(self.Main_frame, width=276, height=184, fg_color="white", corner_radius=10)
        self.upload_frame.place(x=151, y=50)
        
        upload_img_lab = Label(self.upload_frame, image=self.upload_img, bd=0, bg="white")
        upload_img_lab.place(x=0)
        
        reg_name_lab = Label(self.Main_frame, text="Name", font=("poppins",12), fg=self.text, bg="White")
        reg_name_lab.place(x=50, y=315)
        
        reg_Gender_lab = Label(self.Main_frame, text="Gender", font=("poppins",12), fg=self.text, bg="White")
        reg_Gender_lab.place(x=50, y=400)     
        
        reg_Blood_group_lab = Label(self.Main_frame, text="Blood Group", font=("poppins",12), fg=self.text, bg="White")
        reg_Blood_group_lab.place(x=50, y=480)
        
        reg_email_lab = Label(self.Main_frame, text="Email Id", bg="white", fg=self.text, font=("poppins",12))
        reg_email_lab.place(x=672,y=30)
        
        reg_age_lab = Label(self.Main_frame, text="Age", bg="white", fg=self.text, font=("poppins",12))
        reg_age_lab.place(x=672,y=110)

        reg_contact_lab = Label(self.Main_frame, text="Phone Number", bg="white", fg=self.text, font=("poppins",12))
        reg_contact_lab.place(x=672,y=195)
        
        reg_city_lab = Label(self.Main_frame, text="District ", bg="white", fg=self.text, font=("poppins",12))
        reg_city_lab.place(x=672,y=275)
        
        reg_address_lab = Label(self.Main_frame, text="Address ", bg="white", fg=self.text, font=("poppins",12))
        reg_address_lab.place(x=672,y=360)
        
        box1 = Label(self.Main_frame, bg="white", image=self.Image7_box)
        box1.place(x=50,y=357)
        box2 = Label(self.Main_frame, bg="white", image=self.Image7_box)
        box2.place(x=672,y=67)
        box3 = Label(self.Main_frame, bg="white", image=self.Image7_box)
        box3.place(x=672,y=149)
        box4 = Label(self.Main_frame, bg="white", image=self.Image7_box)
        box4.place(x=672,y=231)
        box5 = Label(self.Main_frame, bg="white", image=self.Image7_box)
        box5.place(x=672,y=313)
        box6 = Label(self.Main_frame, bg="white", image=self.Image7_2_box)
        box6.place(x=672,y=390)
        
    # ----- Entry Boxes -----
        self.reg_name = StringVar()
        self.reg_gender = StringVar()
        self.reg_bld_group = StringVar()
        self.reg_email = StringVar()
        self.reg_age = StringVar()
        self.reg_contact = StringVar()
        self.reg_city = StringVar()
        
        self.reg_name_ent = Entry(self.Main_frame,textvariable=self.reg_name,bg="white",fg=self.primary,font=("poppins",16),bd=0)
        self.reg_name_ent.place(x=60, y=366,width=367, height=25)
        
        self.reg_gender_ent = ttk.Combobox(self.Main_frame, textvariable=self.reg_gender, state="readonly",font=("poppins", 16), foreground=self.primary, justify="center")
        self.reg_gender_ent['values']=['--- Select ---','Male','Female','Others']
        self.reg_gender_ent.current(0)
        self.reg_gender_ent.place(x=50, width=377, height=35, y=434)
        
        self.reg_bld_group_ent = ttk.Combobox(self.Main_frame, textvariable=self.reg_bld_group, state="readonly",font=("poppins", 16), foreground=self.primary, justify="center")
        self.reg_bld_group_ent['values']=['--- Select ---',"A+",'A-','B+',"B-","O+","O-","AB+","AB-"]
        self.reg_bld_group_ent.current(0)
        self.reg_bld_group_ent.place(x=50, width=377, height=35, y=516)      
        
        self.reg_email_ent = Entry(self.Main_frame,textvariable=self.reg_email,bg="white",fg=self.primary,font=("poppins",16),bd=0)
        self.reg_email_ent.place(x=682, y=76,width=367, height=25)
        
        self.reg_age_ent = Entry(self.Main_frame,textvariable=self.reg_age,bg="white",fg=self.primary,font=("poppins",16),bd=0)
        self.reg_age_ent.place(x=682, y=158,width=367, height=25)
        
        self.reg_contact_ent = Entry(self.Main_frame,textvariable=self.reg_contact,bg="white",fg=self.primary,font=("poppins",16),bd=0)
        self.reg_contact_ent.place(x=682, y=240,width=367, height=25)
        
        self.reg_city_ent = Entry(self.Main_frame,textvariable=self.reg_city,bg="white",fg=self.primary,font=("poppins",16),bd=0)
        self.reg_city_ent.place(x=682, y=322,width=367, height=25)
        
        self.reg_address_ent = Text(self.Main_frame,bg="white",fg=self.primary,font=("poppins",16),bd=0)
        self.reg_address_ent.place(x=682, y=400,width=367, height=90)
        
        self.reg_path_ent = Entry(self.Main_frame,bg="white",fg=self.primary,font=("poppins",16),bd=0)
        self.reg_path_ent.place(x=100,y=5000)
        
        self.reg_path_donor_ent = Entry(self.Main_frame,bg="white",fg="#ff3030",font=("consolas",16),bd=0)
        self.reg_path_donor_ent.place(x=250,y=4000)
        
    # ----- Buttons -----
        back_btn = Button(Header_fr, image=self.Back_btn, bg=self.primary, border=0, activebackground=self.primary, cursor="hand2", command=lambda:self.Donor_panel(0,"register"))
        back_btn.place(x=1206, height=80)
        
        upload_btn = Button(self.Main_frame, image=self.upload_btn, bg="white", border=0, activebackground="white", cursor="hand2", command= lambda:self.upload(0))
        upload_btn.place(x=151, y=254)
        
        register_btn = Button(self.Main_frame, image=self.register_btn, bg="white", border=0, activebackground="white", cursor="hand2", command=self.reg_database)
        register_btn.place(x=672, y=515)
        
# ----- 8) Donor Request Page -----
    def Donor_request(self,ch):
        
        if(ch == "donor_panel"):
            self.Donor_panel_lab.destroy()
            self.Side_frame.destroy()
            
        self.connector_reg = sqlite3.connect("Donor_register.db")
        self.cursor_reg = self.connector_reg.cursor()
        self.cursor_reg.execute("SELECT * FROM register_details")
        self.donor_count = len(self.cursor_reg.fetchall())
            
    # ----- Header Frame -----
        Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
        Header_fr.place(x=0,y=0)
        
    # ----- side Frame -----
        self.Side_frame_req = Frame(self.win, width=377, height=688, bg=self.background)
        self.Side_frame_req.place(x=0, y=80)
    
    # ----- Center Frame -----
        self.center_frame = Frame(self.win, width=868, height=601, bg=self.background)
        self.center_frame.place(x=398, y=122)
        
    # ----- Labels -----
        Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Donor Request Page", fg=self.background, bg=self.primary)
        Header_lab.place(x=100, height=80)
        
        Donor_req_side_lab = Label(self.Side_frame_req, image=self.side_img, bd=0, bg=self.background)
        Donor_req_side_lab.place(x=0)
        
        Donor_request_lab = Label(self.center_frame, image=self.Donor_req_img, bd=0, bg=self.background)
        Donor_request_lab.place(x=0)
        
        tot_lab = Label(self.Side_frame_req, text="Total Donors", font=("poppins",28,"bold"),fg=self.background,bg="#FF3051")
        tot_lab.place(x=64,y=270)
        
        self.tot_count_lab = Label(self.Side_frame_req, text="0"+str(self.donor_count), font=("poppins",28,"bold"),fg=self.background,bg="#FF3051")
        self.tot_count_lab.place(y=320, width=377)
        
        patient_lab = Label(self.center_frame,text="Patient Name",bg="white",fg=self.text,font=('poppins',14))
        patient_lab.place(x=60,y=25)
        
        con_no_lab = Label(self.center_frame,text="Phone Number",bg="white",fg=self.text,font=('poppins',14))
        con_no_lab.place(x=60,y=125)
        
        blood_grp_lab = Label(self.center_frame,text="Blood Group",bg="white",fg=self.text,font=('poppins',14))
        blood_grp_lab.place(x=60,y=225)
        
        unit_lab = Label(self.center_frame,text="Units",bg="white",fg=self.text,font=('poppins',14))
        unit_lab.place(x=60,y=325)
        
        hos_add_lab = Label(self.center_frame,text="Hospital Details",bg="white",fg=self.text,font=('poppins',14))
        hos_add_lab.place(x=60, y=425)
        
        box1 = Label(self.center_frame, bg="white", image=self.Image_box)
        box1.place(x=60,y=60)
        box2 = Label(self.center_frame, bg="white", image=self.Image_box)
        box2.place(x=60,y=160)  
        box4 = Label(self.center_frame, bg="white", image=self.Image_box)
        box4.place(x=60,y=360)
        box5 = Label(self.center_frame, bg="white", image=self.Image_box)
        box5.place(x=60,y=460)
    
    # ----- Entry boxes -----
        self.patient_name = StringVar()
        self.attenter_no = StringVar()
        self.blood_grp = StringVar()
        self.units = StringVar()
        self.address = StringVar()

        self.patient_ent = Entry(self.center_frame,textvariable=self.patient_name,bg="white", fg=self.primary,font=('poppins',16), bd=0)
        self.patient_ent.place(x=70,y=69, width=340, height=40)
        
        self.attenter_ent = Entry(self.center_frame,textvariable=self.attenter_no,bg="white", fg=self.primary,font=('poppins',16), bd=0)
        self.attenter_ent.place(x=70,y=169, width=340, height=40)
        
        self.blood_grp_ent = ttk.Combobox(self.center_frame, textvariable=self.blood_grp, state="readonly",font=("poppins", 16), foreground=self.primary, justify="center")
        self.blood_grp_ent['values']=["A+",'A-','B+',"B-","O+","O-","AB+","AB-"]
        self.blood_grp_ent.current(0)
        self.blood_grp_ent.place(x=60,y=260, width=350, height=50)
        
        self.units_ent = Entry(self.center_frame,textvariable=self.units,bg="white", fg=self.primary,font=('poppins',16), bd=0)
        self.units_ent.place(x=70,y=369, width=340, height=40)
        
        self.hos_add_ent = Entry(self.center_frame,bg="white",fg=self.primary,font=('poppins',16),textvariable=self.address, bd=0)
        self.hos_add_ent.place(x=70,y=469, width=340, height=40)
        
    # ----- Buttons -----
        back_btn = Button(Header_fr, image=self.Back_btn, bg=self.primary, border=0, activebackground=self.primary, cursor="hand2", command=lambda:self.Donor_panel("donor_request","request"))
        back_btn.place(x=1206, height=80)
        
        request_btn = Button(self.center_frame, image=self.request_btn, bg="white", border=0, activebackground="white", cursor="hand2", command=self.Request)
        request_btn.place(x=60, y=525)
        
# ----- 9) To check the login details -----
    def Check_login(self):
   
        if(self.Username_ent.get() == "" and self.Password_ent.get() == ""):
            messagebox.showerror("INVALID DETAILS", "PLEASE ENTER YOUR USERNAME AND PASSWORD")
        elif(self.Username_ent.get() == "" or self.Password_ent.get() == ""):
            if(self.Username_ent.get()==""):
                messagebox.showerror("INVALID DETAILS", "PLEASE ENTER YOUR USERNAME")
            else:
                messagebox.showerror("INVALID DETAILS", "PLEASE ENTER YOUR PASSWORD")
        else:
            self.connector = sqlite3.connect("Login.db", timeout=10)
            self.cursor = self.connector.cursor()
        
            self.connector.execute(
                "CREATE TABLE IF NOT EXISTS Login_details(Username TEXT PRIMARY KEY,Password TEXT,Con_password TEXT)"
            )
            un = self.Username_ent.get()
            pw = self.Password_ent.get()
            self.cursor.execute("SELECT * FROM Login_details WHERE Username=? AND Password=?",(un,pw))
            self.result = self.cursor.fetchall()
            self.connector.commit()
            self.cursor.close()
            self.Donor_panel(1,"login")
            
# ----- 10) To add the new donor accounts(signup) -----
    def db_Signup(self):
        
        self.username= self.Username_ent.get()
        self.password= self.Password_ent.get()
        self.con_password= self.Confrom_Password_ent.get()
        
        if ((self.username and self.password and self.con_password)!=""):
            if (self.password == self.con_password):
                try:
                    self.connector = sqlite3.connect("Login.db", timeout=10)
                    self.cursor = self.connector.cursor()
                    
                    self.connector.execute(
                        "INSERT INTO Login_details(Username,Password,Con_password) VALUES (?,?,?)",
                        (self.username,self.password,self.con_password)
                    )
                    self.cursor.execute("SELECT * FROM Login_details WHERE Username=? AND Password=?",(self.username,self.password))
                    self.result = self.cursor.fetchall()
                    self.Donor_panel(1,"signup")
                    self.connector.commit()
                    self.cursor.close()
                except:
                    self.Username_ent.delete(0,"end")
                    self.Password_ent.delete(0,"end")
                    self.Confrom_Password_ent.delete(0,"end")
                    messagebox.showerror("Wrong Entry","Username may already exists")
                    self.connector.commit()
                    self.cursor.close()
            else:
                messagebox.showerror("Password error","Password and conform Password Should be same")
        else:
            messagebox.showerror("Login Error","Please Fill All the Fields")

# ----- 11) To change the password(forgot password) -----
    def db_forgot_passwrd(self):
        
        self.for_username= self.for_Username_ent.get()
        self.for_password= self.for_Password_ent.get()
        self.for_con_password= self.for_Confrom_Password_ent.get()
        
        if ((self.for_username and self.for_password and self.for_con_password)!=""):
            if (self.for_password == self.for_con_password):
                try:
                    self.connector = sqlite3.connect("Login.db", timeout = 10)
                    self.cursor = self.connector.cursor()
                    self.cursor.execute("SELECT * FROM Login_details WHERE Username=?",(self.for_username,))
                    result_fetch = self.cursor.fetchall()
                    if(len(result_fetch)==0):
                        self.for_Username_ent.delete(0,"end")
                        self.for_Password_ent.delete(0,"end")
                        self.for_Confrom_Password_ent.delete(0,"end")
                        messagebox.showerror("Wrong Entry","Username Doesn't Exits")
                    else:
                        self.connector.execute(
                            "UPDATE Login_details SET Password=?, Con_password=? WHERE Username=?",
                            (self.for_password,self.for_con_password,self.for_username,)
                        )
                        messagebox.showinfo("Password update","Your password sucessfully updated")
                        self.Donor_login(1)
                        self.connector.commit()
                        self.cursor.close()
                except:
                    messagebox.showerror("Wrong Entry","Username Doesn't Exits")
            else:
                messagebox.showerror("Password error","Password and conform Password Should be same")
        else:
            messagebox.showerror("Login Error","Please Fill All the Fields")
            
# ----- 12) To upload a image -----
    def upload(self,src):

        if (self.reg_path_ent.get()==''):
            if (src==0):
                self.path = filedialog.askopenfilename(title="Select an Image", filetype=(("JPG Files","*.jpg"),("PNG Files","*.png"),("All Files", "*.*")))
                self.donor_img_open = Image.open(self.path)
                self.img = self.donor_img_open.resize((276,184),Image.ANTIALIAS)
                self.img = ImageTk.PhotoImage(self.img)
                
                self.img_fr = Frame(self.upload_frame,bg="white",bd=2)
                self.img_fr.place(width=276,height=184)
                self.donor_img_lab = Label(self.img_fr, image=self.img)
                self.donor_img_lab.image = self.img
                self.donor_img_lab.pack()
                self.reg_path_ent.insert(0,self.path)
                self.reg_path_donor_ent.insert(0,self.path)
        else:
            self.reg_path_ent.delete(0)
            if (src==0):
                self.reg_path_donor_ent.delete(0)
                self.upload(0)
                
# ----- 13) Donor regisration database -----
    def reg_database(self):
        
        self.reg_name = self.reg_name_ent.get()
        self.reg_gender = self.reg_gender_ent.get()
        self.reg_bld_group = self.reg_bld_group_ent.get()
        self.reg_email = self.reg_email_ent.get()
        self.reg_age = self.reg_age_ent.get()
        self.reg_contact = self.reg_contact_ent.get()
        self.reg_city = self.reg_city_ent.get()
        self.reg_address = self.reg_address_ent.get("1.0","end")
        
        print(f"1) Name = {self.reg_name}\n2) Gender = {self.reg_gender}\n3) Blood Group = {self.reg_bld_group}\n4) Email = {self.reg_email}\n5) Age = {self.reg_age}\n6) Phone number = {self.reg_contact}\n7) City = {self.reg_city}\n8) Address = {self.reg_address}")
        
        self.connector_reg = sqlite3.connect("Donor_register.db")
        self.cursor_reg = self.connector_reg.cursor()
        try:
            if ((self.reg_name or self.reg_gender or self.reg_bld_group or self.reg_email or self.reg_age or self.reg_contact or self.reg_city or self.reg_address) ==''):
                messagebox.showwarning("Invalid Entry","Please Enter the All fields")
            else:
                if (len(self.reg_contact)!=10):
                    messagebox.showerror("Invalid Entry","Enter the valid Phone number")
                elif (self.reg_gender=='--- Select ---'):
                    messagebox.showerror("Invaild Entry","Please Select your 'Gender'")
                elif(self.reg_bld_group=='--- Select ---'):
                    messagebox.showerror("Invaild Entry","Please Select your 'Blood Group'")
                else:
                    self.connector_reg.execute(
                        "CREATE TABLE IF NOT EXISTS register_details(Name TEXT,Gender TEXT,Blood TEXT,Email TEXT PRIMARY KEY,Age INTEGER,Number INTEGER,City TEXT,Address TEXT,Img BLOB)"
                    )
        
                    self.donor_img = self.img_to_binary(self.path)
        
                    self.connector_reg.execute(
                        "INSERT INTO register_details(Name,Gender,Blood,Email,Age,Number,City,Address,Img) VALUES (?,?,?,?,?,?,?,?,?)",
                        (self.reg_name,self.reg_gender,self.reg_bld_group,self.reg_email,self.reg_age,self.reg_contact,self.reg_city,self.reg_address,self.donor_img)
                    )
                    self.connector_reg.commit()
                    opt = self.reg_gender_ent["values"]
                    self.reg_name_ent.delete(0,"end")
                    self.reg_email_ent.delete(0,"end")
                    self.reg_age_ent.delete(0,"end")
                    self.reg_contact_ent.delete(0,"end")
                    self.reg_city_ent.delete(0,"end")
                    self.reg_address_ent.delete(1.0,END)
                    self.reg_gender_ent.set(opt[0])
                    self.reg_bld_group_ent.set(opt[0])
                    self.reg_path_ent.delete(0,"end")
                    self.img_fr.destroy()
                    
                    messagebox.showinfo("Reg-Registeration",f"Hello {self.reg_name},\n\nWelcome to the Donor Socity")
        except:
            messagebox.showwarning("Alert","Check the information you are entered\n\nAll informaton for required")

# ----- 14) Function to convert image into binary file -----
    def img_to_binary(self,image):
        
        with open(image,'rb') as file:
            bin_image = file.read()
        return bin_image
    
# ----- 15) Funtion to send a request to the registed donors -----
    def Request(self):
        
        name = self.patient_ent.get()
        contact = self.attenter_ent.get()
        blood = self.blood_grp_ent.get()
        unit = self.units_ent.get()
        details =self.hos_add_ent.get()
        
        if(name=="" or contact=="" or unit=="" or details==""):
            messagebox.showwarning("Details Incomplete", "Please enter all the details")
        else:
            try:
                self.connector_reg = sqlite3.connect("Donor_register.db")
                self.cursor_reg = self.connector_reg.cursor()
                self.cursor_reg.execute("SELECT Email from register_details WHERE Blood=?", (self.blood_grp_ent.get(),))
                email_row = self.cursor_reg.fetchall()
                email =[]
                for j in email_row:
                    email.append("".join(list(j)))
                for email_id in email:
                    if("@" in email_id):
                        self.cursor_reg.execute("SELECT Name FROM register_details WHERE Email=?", (email_id,))
                        name_row = self.cursor_reg.fetchall()
                        for k in name_row:
                            username = "".join(list(k))
                        session = smtplib.SMTP('smtp.gmail.com', 587)
                        session.starttls()
                        session.ehlo()
                        session.login("blood.donor.application@gmail.com","jdoedhfdjoqgvjdu")
                        message = f"Hello {username},\n\n----- Details -----\nName: {name}\nPhone number: {contact}\nBlood Group: {blood}\nUnits: {unit}\nHospital Details: {details}"
                        session.sendmail("blood.donor.application@gmail.com",email_id, message)
                        session.quit()
                messagebox.showinfo("Request Sucessfull", "Thanks for using our service\nYour request has send.")
            except:
                messagebox.showerror("Internet error", "Please Check your Internet connection")
# ----- 16) Funtion to see the donnor details -----
    def Details(self, ch):
        
        if(ch == "donor_panel"):
            self.Donor_panel_lab.destroy()
            self.Side_frame.destroy()
            
        self.connector_reg = sqlite3.connect("Donor_register.db")
        self.cursor_reg = self.connector_reg.cursor()
        self.cursor_reg.execute("SELECT * FROM register_details")
        self.donor_count = len(self.cursor_reg.fetchall())
            
    # ----- Header Frame -----
        Header_fr = Frame(self.win, width=1366, height=80, bg=self.primary)
        Header_fr.place(x=0,y=0)
        
    # ----- side Frame -----
        self.Side_frame_req = Frame(self.win, width=377, height=688, bg=self.background)
        self.Side_frame_req.place(x=0, y=80)
    
    # ----- Center Frame -----
        self.center_frame = Frame(self.win, width=868, height=601, bg="white")
        self.center_frame.place(x=398, y=122)
        
    # ----- Labels -----
        Header_lab = Label(Header_fr, font=("poppins",28,'bold'), text="Donor Details Page", fg=self.background, bg=self.primary)
        Header_lab.place(x=100, height=80)
        
        Donor_req_side_lab = Label(self.Side_frame_req, image=self.side_img, bd=0, bg=self.background)
        Donor_req_side_lab.place(x=0)
        
        tot_lab = Label(self.Side_frame_req, text="Total Donors", font=("poppins",28,"bold"),fg=self.background,bg="#FF3051")
        tot_lab.place(x=64,y=270)
        
        self.tot_count_lab = Label(self.Side_frame_req, text="0"+str(self.donor_count), font=("poppins",28,"bold"),fg=self.background,bg="#FF3051")
        self.tot_count_lab.place(y=320, width=377)
        
        search_lab = Label(self.center_frame, text="Search By", font=("poppins",16),fg=self.secondary,bg="white")
        search_lab.place(x=30,y=0, height=80)

    #----- search box -----
        self.search = StringVar()
        self.search_ent = ttk.Combobox(self.center_frame, textvariable=self.search, state="readonly",font=("consolas", 16,'bold'), foreground=self.text)
        self.search_ent['values']=["City"]
        self.search_ent.current(0)
        self.search_ent.place(x=150, y=23, width=170)
        
        self.connector_reg = sqlite3.connect("Donor_register.db")
        self.cursor_reg = self.connector_reg.cursor()
        self.cursor_reg.execute("SELECT DISTINCT(City) from register_details")
        row = self.cursor_reg.fetchall()
        City =[]
        for i in row:
            City.append(list(i))
        self.search_city = StringVar()
        self.search_city_ent = ttk.Combobox(self.center_frame, textvariable=self.search_city, state="readonly",font=("consolas", 16,'bold'), foreground=self.text)
        self.search_city_ent['values']=City
        self.search_city_ent.current(0)
        self.search_city_ent.place(x=350, y=23, width=170)
    
    #----- Search Button -----
        search_btn = Button(self.center_frame,text="Search",fg="white",bg=self.primary, font=('poppins',16),bd=0, command=self.Search)
        search_btn.place(x=550,y=23,width=120, height=30)
        
        showall_btn = Button(self.center_frame,text="Show all",fg="white",bg=self.primary, font=('poppins',16),bd=0, command=self.fech_data)
        showall_btn.place(x=700,y=23,width=120, height=30)
        
    #============Treeview frame ======================
        table_fr = Frame(self.center_frame, bg="white")
        table_fr.place(x=0,y=80,height=521, width=868)
        
        scroll_x = Scrollbar(table_fr, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_fr, orient=VERTICAL)
        self.donor_table = ttk.Treeview(table_fr, columns=("Name","Gender","Blood Group","Contact","City"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.donor_table.xview)
        scroll_y.config(command=self.donor_table.yview)
        self.donor_table.heading("Name",text="Name")
        self.donor_table.heading("Gender",text="Gender")
        self.donor_table.heading("Blood Group",text="Blood Group")
        self.donor_table.heading("Contact",text="Contact")
        self.donor_table.heading("City",text="City")
        self.donor_table['show']='headings'
        self.donor_table.column("Name",width=150)
        self.donor_table.column("Gender",width=100)
        self.donor_table.column("Blood Group",width=100)
        self.donor_table.column("Contact",width=100)
        self.donor_table.column("City",width=100)
        self.donor_table.pack(fill=BOTH, expand=1)
        self.connector_reg = sqlite3.connect("Donor_register.db")
        self.cursor_reg = self.connector_reg.cursor()
        self.fech_data()
        
    # ----- Buttons -----
        back_btn = Button(Header_fr, image=self.Back_btn, bg=self.primary, border=0, activebackground=self.primary, cursor="hand2", command=lambda:self.Donor_panel("donor_details","details"))
        back_btn.place(x=1206, height=80)

# ----- 17) Funtion to fetch donor record from database -----
    def fech_data(self):
        
        try:     
            self.connector_reg = sqlite3.connect("Donor_register.db")
            self.cursor_reg = self.connector_reg.cursor()
            self.cursor_reg.execute("SELECT Name, Gender, Blood, Number, City from register_details")
            self.row = self.cursor_reg.fetchall()
             
            if len(self.row)!=0:
                    self.donor_table.delete(*self.donor_table.get_children())
                    for rows in self.row:
                        self.donor_table.insert('',END,values=rows)
                        self.connector_reg.commit()
        except:
            self.connector_reg = sqlite3.connect("Donor_register.db")
            self.cursor_reg = self.connector_reg.cursor()
            
            self.connector_reg.execute(
                        "CREATE TABLE IF NOT EXISTS register_details(Name TEXT,Gender TEXT,Blood TEXT,Email TEXT PRIMARY KEY,Age INTEGER,Number INTEGER,City TEXT,Address TEXT,Img BLOB)"
                    )
            self.Details("details")
            
    # ----- 18) function to search a donor by City -----
    def Search(self):
        
        self.connector_reg = sqlite3.connect("Donor_register.db")
        self.cursor_reg = self.connector_reg.cursor()
        self.cursor_reg.execute("SELECT Name, Gender, Blood, Number, City from register_details WHERE City=?", (self.search_city_ent.get(),))
        self.row = self.cursor_reg.fetchall()
                
        if len(self.row)!=0:
                self.donor_table.delete(*self.donor_table.get_children())
                for rows in self.row:
                    self.donor_table.insert('',END,values=rows)
                    self.connector_reg.commit()
                    
    # ----- 19) function to send a message from the contact page -----
    def Contact_message(self):
        
        name = self.name_ent.get()
        email_id = self.email_ent.get()
        message = self.message_ent.get("1.0","end")        
        print(f"Name: {name}\nEmail Id: {email_id}\nMessage: {message}")
        thank_message = f"Hello {name},\n\nYour message was received."
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.ehlo()
        session.login("blood.donor.application@gmail.com","jdoedhfdjoqgvjdu")
        session.sendmail("blood.donor.application@gmail.com", "blood.donor.application@gmail.com", message)
        session.sendmail("blood.donor.application@gmail.com", email_id, thank_message)
        session.quit()
    
# ----- Object declaration area -----
window = Tk()      
obj = Main(window)
window.mainloop()