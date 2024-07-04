import tkinter as tk 
import customtkinter as cutk 
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from CTkMenuBar import *
from tkinter import filedialog 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas 
from datetime import datetime
import time 

app = cutk.CTk()

color1 = "#315041" #green
color2 = "#3CD37A" #green fath
color3 = "#FE7101" #ORANGE
color4 = "#547D69" #SELVER
color5 = "#000000" #black math
color6 = "#9efd38" #vert citron

font1 = ('Arial',20,'bold')
font2 = ('Arial',12,'bold')

app.title("Quality Manage")
app.geometry("1900x1050")
app.config(bg=color1)
app.resizable(True,True)

####LOGIN####
def login():
    # Replace with your admin validation logic
    if user_entry.get() == "admin" and password_entry.get() == "admin":
        login_frame.pack_forget()
        time.sleep(0.5)
        premier_page.pack(fill='both',expand=True)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

####sign up####
def signup():
    pass

####REPORT####
def show_report():
    premier_page.pack_forget()
    time.sleep(0.5)
    deuxieme_page.pack(fill='both',expand=True)

def log_out():
    if messagebox.askyesno("Log out","Are you sure you want to logout ?"):
        login_frame.pack(fill='both',expand=True)
        time.sleep(0.5)
        premier_page.pack_forget()
        user_entry.delete(0,END)
        password_entry.delete(0,END)
def search_date():
    if premier_page.winfo_viewable() or deuxieme_page.winfo_viewable() or search_page_intervalle.winfo_viewable() or search_page_n_serie.winfo_viewable():
        deuxieme_page.pack_forget()
        premier_page.pack_forget()
        search_page_intervalle.pack_forget()
        search_page_n_serie.pack_forget()
        time.sleep(0.5)
        search_page_date.pack(fill='both',expand=True) 
def search_intervalle(): 
    if premier_page.winfo_viewable() or deuxieme_page.winfo_viewable() or search_page_date.winfo_viewable() or search_page_n_serie.winfo_viewable(): 
        deuxieme_page.pack_forget()
        premier_page.pack_forget()
        search_page_date.pack_forget()
        search_page_n_serie.pack_forget()
        time.sleep(0.5)
        search_page_intervalle.pack(fill='both',expand=True)
def search_n_serie():
    if premier_page.winfo_viewable() or deuxieme_page.winfo_viewable() or search_page_date.winfo_viewable() or search_page_intervalle.winfo_viewable():
        deuxieme_page.pack_forget()
        premier_page.pack_forget()
        search_page_date.pack_forget()
        search_page_intervalle.pack_forget()
        time.sleep(0.5)
        search_page_n_serie.pack(fill='both',expand=True)
def search_model():
    if premier_page.winfo_viewable() or deuxieme_page.winfo_viewable() or search_page_date.winfo_viewable() or search_page_n_serie.winfo_viewable():
        deuxieme_page.pack_forget()
        premier_page.pack_forget()
        search_page_date.pack_forget()
        search_page_n_serie.pack_forget()
        time.sleep(0.5)
        search_page_model.pack(fill='both',expand=True)
####CURRENT TIME####
def update_time():
    current_time = datetime.now().strftime("%d/%m/%Y")
    current_year = datetime.now().strftime("%Y")
    date_entry.configure(state='normal')  
    date_entry.delete(0, tk.END)       
    date_entry.insert(0, current_time) 
    date_entry.configure(state='readonly')
    annee_entry.configure(state='normal')
    annee_entry.delete(0,tk.END)
    annee_entry.insert(0,current_year)
    annee_entry.configure(state='readonly')
    premier_page.after(1000, update_time) 

################LOGIN FRAME################
login_frame =cutk.CTkFrame(app,bg_color=color1,fg_color=color1)
login_frame.pack(fill='both',expand=True)
########LOGIN LABEL########
login_label = cutk.CTkLabel(login_frame,text='LOGIN' , font=font1,text_color="white",bg_color=color1)
login_label.place(x=500,y=50)
########USER LABEL########
user_label = cutk.CTkLabel(login_frame,text='Username',
                            font=font1,text_color='white',
                            bg_color=color1)
user_label.place(x=450,y=150)
########USER ENTRY########
user_entry = cutk.CTkEntry(login_frame,font=font1,
                            text_color='black',fg_color='white',
                            bg_color=color1)
user_entry.place(x=600,y=150)
########PASSWORD LABEL########
password_label = cutk.CTkLabel(login_frame,text='Password',
                            font=font1,text_color='white',bg_color=color1)
password_label.place(x=450,y=200)
########PASSWORD ENTRY########
password_entry = cutk.CTkEntry(login_frame,font=font1,
                            text_color='black',
                            fg_color='white',
                            bg_color=color1,show="*")
password_entry.place(x=600 , y=200)
########LOGIN BUTTON########
login_button = cutk.CTkButton(login_frame,text='Login',
                            font=font1,
                            text_color="white",
                            fg_color=color2,
                            bg_color=color1,
                            cursor="hand1",
                            command=login)
login_button.place(x=600,y=260)
########SIGN UP BUTTON########
signup_button = cutk.CTkButton(login_frame,text="Sign Up",
                            font=font1,
                            text_color="white",
                            fg_color=color3,
                            bg_color=color1,
                            cursor='hand2',
                            command=signup)
signup_button.place(x=770,y=260)
###############################
def back():
    if deuxieme_page.winfo_viewable():
        deuxieme_page.pack_forget()
        time.sleep(0.5)
        premier_page.pack(fill='both',expand=True)
    elif search_page_date.winfo_viewable() or search_page_intervalle.winfo_viewable() or search_page_n_serie.winfo_viewable() or search_page_model.winfo_viewable():
        search_page_intervalle.pack_forget()
        search_page_date.pack_forget()
        search_page_n_serie.pack_forget()
        search_page_model.pack_forget()
        time.sleep(0.5)
        deuxieme_page.pack(fill='both',expand=True)
def forward():
    if premier_page.winfo_viewable():
        premier_page.pack_forget()
        time.sleep(0.5)
        deuxieme_page.pack(fill='both',expand=True)
def search_date():
    if premier_page.winfo_viewable() or deuxieme_page.winfo_viewable() or search_page_intervalle.winfo_viewable() or search_page_n_serie.winfo_viewable():
        deuxieme_page.pack_forget()
        premier_page.pack_forget()
        search_page_intervalle.pack_forget()
        search_page_n_serie.pack_forget()
        time.sleep(0.5)
        search_page_date.pack(fill='both',expand=True) 
def search_intervalle(): 
    if premier_page.winfo_viewable() or deuxieme_page.winfo_viewable() or search_page_date.winfo_viewable() or search_page_n_serie.winfo_viewable(): 
        deuxieme_page.pack_forget()
        premier_page.pack_forget()
        search_page_date.pack_forget()
        search_page_n_serie.pack_forget()
        time.sleep(0.5)
        search_page_intervalle.pack(fill='both',expand=True)
def search_n_serie():
    if premier_page.winfo_viewable() or deuxieme_page.winfo_viewable() or search_page_date.winfo_viewable() or search_page_intervalle.winfo_viewable():
        deuxieme_page.pack_forget()
        premier_page.pack_forget()
        search_page_date.pack_forget()
        search_page_intervalle.pack_forget()
        time.sleep(0.5)
        search_page_n_serie.pack(fill='both',expand=True)
def search_model():
    if premier_page.winfo_viewable() or deuxieme_page.winfo_viewable() or search_page_date.winfo_viewable() or search_page_n_serie.winfo_viewable() or search_page_intervalle.winfo_viewable():
        deuxieme_page.pack_forget()
        premier_page.pack_forget()
        search_page_date.pack_forget()
        search_page_n_serie.pack_forget()
        time.sleep(0.5)
        search_page_model.pack(fill='both',expand=True)
################PREMIER PAGE FRAME################
premier_page = cutk.CTkFrame(app, bg_color=color1,fg_color=color1)
########BARE MENU########
menu = CTkMenuBar(app)
back = menu.add_cascade("↩",command=back)
forward = menu.add_cascade("↪",command=forward)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Profile")
button_3 = menu.add_cascade("Settings")
button_4 = menu.add_cascade("About")
search = menu.add_cascade("🔎")
####DROPDOWN####
# dropdownR = CustomDropdownMenu(widget=search)
# dropdownR.add_option(command=back)
#button_1#
dropdown1 = CustomDropdownMenu(widget=button_1)
sub_menu = dropdown1.add_submenu("Export As")
# sub_menu.add_option(option=".TXT",command= lambda : export("txt"))
# sub_menu.add_option(option=".PDF",command= lambda : export("pdf"))
#button_2#
dropdown2 = CustomDropdownMenu(widget=button_2)
dropdown2.add_option(option="log out",command=log_out)
#button_3#
# dropdown3 = CustomDropdownMenu(widget=button_3)
# dropdown3.add_option(option="dark mode",command=switch)
# dropdown3.add_option(option="light mode",command=switch)
dropdownsearch = CustomDropdownMenu(widget=search)
dropdownsearch.add_option(option="search par date",command=search_date)
dropdownsearch.add_option(option="search par intervalle",command=search_intervalle)
dropdownsearch.add_option(option="search par N°serie",command=search_n_serie)
dropdownsearch.add_option(option="search par Model",command=search_model)
#button_4#
# dropdown4 = CustomDropdownMenu(widget=button_4)
# dropdown4.add_option(option="About us",command=about_us)
########DATE LABEL########
date_label = cutk.CTkLabel(premier_page,font=font1,
                            text="date : ",
                            text_color="white",
                            bg_color=color1)
date_label.place(x=20,y=40)
########DATE ENTRY########
date_entry = cutk.CTkEntry(premier_page,font=font1,
                            text_color="black",
                            state='readonly',
                            bg_color=color1)
date_entry.place(x=220,y=40)
########NAME LABEL########
fabricant_label = cutk.CTkLabel(premier_page,font=font1,
                            text='Fabricant : ',
                            text_color="white",
                            bg_color=color1)
fabricant_label.place(x=20,y=100)
########NAME ENTRY########
fabricant_entry = cutk.CTkEntry(premier_page,font=font1,
                            text_color='black',
                            bg_color=color1)
fabricant_entry.insert(0,"ALAMIA Electro")
fabricant_entry.configure(state="readonly")
fabricant_entry.place(x=220,y=100)
########YEAR LABEL########
annee_label = cutk.CTkLabel(premier_page,font=font1,
                            text='Année de fabrication : ',
                            text_color="white",
                            bg_color=color1)
annee_label.place(x=20,y=160)
########YEAR ENTRY########
annee_entry = cutk.CTkEntry(premier_page,font=font1,
                            text_color="black",
                            state='readonly',
                            bg_color=color1)
annee_entry.place(x=220,y=160)
########TYPE DE COMPTEUR LABEL########
type_compteur_label = cutk.CTkLabel(premier_page,font=font1,
                            text='Type de compteur  : ',
                            text_color="white",
                            bg_color=color1)
type_compteur_label.place(x=20,y=220)
########TYPE DE COMPTEUR ENTRY########
type_compteur_entry = cutk.CTkEntry(premier_page,font=font1,
                            text_color='black',
                            bg_color=color1)
type_compteur_entry.place(x=220,y=220)
########MODELE LABEL########
modele_label = cutk.CTkLabel(premier_page,font=font1,
                            text='Modele : ',
                            text_color="white",
                            bg_color=color1)
modele_label.place(x=20,y=280)
########MODELE ENTRY########
modele_entry = cutk.CTkEntry(premier_page,font=font1,
                            text_color='black',
                            bg_color=color1)
modele_entry.place(x=220,y=280)
########DIAMETRE LABEL########
diametre_label = cutk.CTkLabel(premier_page,font=font1,
                            text='Diametre nominal : ',
                            text_color="white",
                            bg_color=color1)
diametre_label.place(x=20,y=340)
########DIAMETRE ENTRY########
diametre_entry = cutk.CTkEntry(premier_page,font=font1,
                            text_color='black',
                            bg_color=color1)
diametre_entry.place(x=220,y=340)
########CLASSE LABEL########
classe_label = cutk.CTkLabel(premier_page,font=font1,
                            text='classe : ',
                            text_color="white",
                            bg_color=color1)
classe_label.place(x=20,y=400)
########CLASSE ENTRY########
class_entry = cutk.CTkEntry(premier_page,font=font1,
                            text_color='black',
                            bg_color=color1)
class_entry.place(x=220,y=400)
########PRESSION LABEL########
pression_label = cutk.CTkLabel(premier_page,font=font1,
                            text='Pression Max : ',
                            text_color="white",
                            bg_color=color1)
pression_label.place(x=20,y=460)
########PRESSION ENTRY########
pression_entry = cutk.CTkEntry(premier_page,font=font1,
                            text_color='black',
                            bg_color=color1)
pression_entry.place(x=220,y=460)
########DEBIT PERMANENT LABEL##########
debit_permanent_label = cutk.CTkLabel(premier_page,font=font1,
                                      text="Debit permanent(Q3):",
                                      text_color="white",
                                      bg_color=color1,
                                      )
debit_permanent_label.place(x=380,y=40)
########DEBIT PERMANENT ENTRY##########
debit_permanent_entry = cutk.CTkEntry(premier_page,font=font1,
                                      text_color="black",
                                      bg_color=color1)
debit_permanent_entry.place(x=680,y=40)
########RAPPORT 1 LABEL##########
rapport1_label = cutk.CTkLabel(premier_page,font=font1,
                               text="Rapport des denits(R=Q3/Q1):"
                               ,text_color="white",
                               bg_color=color1)
rapport1_label.place(x=380,y=100)
########RAPPORT 1 ENTRY##########
rapport1_entry = cutk.CTkEntry(premier_page,
                               font=font1,
                                text_color='black',
                                bg_color=color1
                               )
rapport1_entry.place(x=680,y=100)
########RAPPORT 2 LABEL #########
rapport2_label = cutk.CTkLabel(premier_page,
                               font=font1,text="Rapport des debits(Q2/Q1):",
                               text_color="white",
                               bg_color=color1)
rapport2_label.place(x=380, y=160)
########RAPPORT 2 ENTRY #########
rapport2_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",bg_color=color1)
rapport2_entry.place(x=680,y=160)
########RAPPORT 3 LABEL #########
rapport3_label = cutk.CTkLabel(premier_page,font=font1,
                               text="Rapport(Q4/Q3):",
                               text_color="white",
                               bg_color=color1)
rapport3_label.place(x=380,y=220)
########RAPPORT 3 ENTRY #########
rapport3_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
rapport3_entry.place(x=680,y=220)
########METHODE LABEL #########
methode_label = cutk.CTkLabel(premier_page,font=font1,
                              text="Methode d'essai : ",
                              text_color="white",
                              bg_color=color1)
methode_label.place(x=840,y=40)
########METHODE ENTRY #########
methode_entry = cutk.CTkEntry(premier_page,font=font1,
                              text_color="black",
                              bg_color=color1)
methode_entry.place(x=1070,y=40)
########procedure LABEL #########
methode_label = cutk.CTkLabel(premier_page,font=font1,
                              text="Procedure interne : ",
                              text_color="white",
                              bg_color=color1)
methode_label.place(x=840,y=100)
########procedure ENTRY #########
methode_entry = cutk.CTkEntry(premier_page,font=font1,
                              text_color="black",
                              bg_color=color1)
methode_entry.place(x=1070,y=100)
########BANC LABEL #########
banc_label = cutk.CTkLabel(premier_page,font=font1,
                           text="Banc d'essai :",
                           text_color="white",
                           bg_color=color1)
banc_label.place(x=840,y=160)
########BANC ENTRY #########
banc_entry = cutk.CTkEntry(premier_page,font=font1,
                           text_color="black",
                           bg_color=color1)
banc_entry.place(x=1070,y=160)
########TEMPA LABEL #########
temp_A_label = cutk.CTkLabel(premier_page,font=font1,
                             text="Temperature ambiante :",
                             text_color="white",
                             bg_color=color1)
temp_A_label.place(x=840,y=220)
########TEMPA ENTRY#########
temp_A_entry = cutk.CTkEntry(premier_page,font=font1,
                             text_color="black",
                             bg_color=color1)
temp_A_entry.place(x=1070,y=220)
########HUMIDITE LABEL#########
humidite_label = cutk.CTkLabel(premier_page,font=font1,
                               text="Humidite relative :",
                               text_color="white",
                               bg_color=color1)
humidite_label.place(x=840,y=280)
########HUMIDITE ENTRY#########
humidite_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
humidite_entry.place(x=1070,y=280)
########temp d'eau LABEL#########
temperature_eau_label = cutk.CTkLabel(premier_page,font=font1,
                               text="Temperature d'eau :",
                               text_color="white",
                               bg_color=color1)
temperature_eau_label.place(x=840,y=340)
########temp d'eau ENTRY#########
temperature_eau_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
temperature_eau_entry.place(x=1070,y=340)
########temp d'eau 2 ENTRY#########
temperature_eau_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
temperature_eau_entry.place(x=1280,y=340)
########pression d'eau LABEL#########
pression_eau_label = cutk.CTkLabel(premier_page,font=font1,
                               text="Pression d'eau :",
                               text_color="white",
                               bg_color=color1)
pression_eau_label.place(x=840,y=400)
########pression d'eau ENTRY#########
pression_eau_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
pression_eau_entry.place(x=1070,y=400)
########pression d'eau 2 ENTRY#########
pression_eau_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
pression_eau_entry.place(x=1280,y=400)
########Echelon LABEL#########
Echelon_label = cutk.CTkLabel(premier_page,font=font1,
                               text="Echelon :",
                               text_color="white",
                               bg_color=color1)
Echelon_label.place(x=840,y=460)
########Echelon ENTRY#########
Echelon_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Echelon_entry.place(x=1070,y=460)
#***********########### tb du masse et volume ################************#
#*********************le Q******************#
#######les Q############
Masse_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Masse_entry.insert(0,"Q1=     L/h")
Masse_entry.place(x=650,y=540)
#######les Q############
Masse_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Masse_entry.insert(0,"Q3=     L/h")
Masse_entry.place(x=860,y=540)
#######les Q############
Masse_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Masse_entry.insert(0,"Q2=     L/h")
Masse_entry.place(x=1070,y=540)
#######les Q############
Masse_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Masse_entry.insert(0,"Q4=     L/h")
Masse_entry.place(x=1280,y=540)
#**********#
#######Masse kg############
Masse_label = cutk.CTkLabel(premier_page,font=font1,
                               text="Masse (Kg) ",
                               text_color="white",
                               bg_color=color1)
Masse_label.place(x=440,y=580)
#######Masse kg############
Masse_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Masse_entry.place(x=650,y=580)
#######Masse kg############
Masse_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Masse_entry.place(x=860,y=580)
#######Masse kg############
Masse_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Masse_entry.place(x=1070,y=580)
#######Masse kg############
Masse_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
Masse_entry.place(x=1280,y=580)
#*****************volume lit************************#
#######Volume (litres)############
volume_label = cutk.CTkLabel(premier_page,font=font1,
                               text="Volume (litre) ",
                               text_color="white",
                               bg_color=color1)
volume_label.place(x=440,y=620)
#######Volume (litres)############
volume_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
volume_entry.place(x=650,y=620)
#######Volume (litres)############
volume_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
volume_entry.place(x=860,y=620)
#######Volume (litres)############
volume_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
volume_entry.place(x=1070,y=620)
#######Volume (litres)############
volume_entry = cutk.CTkEntry(premier_page,font=font1,
                               text_color="black",
                               bg_color=color1)
volume_entry.place(x=1280,y=620)
################DEUXIEME PAGE FRAME################
deuxieme_page = cutk.CTkFrame(app, bg_color=color1,fg_color=color1)
########N°SERIE ENTRY########
n_serie_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text="N°série : ",
                            text_color="white",
                            bg_color=color1,
                            width=260)
n_serie_label.place(x=20,y=40)
########N°SERIE ENTRY########
n_serie_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1)
n_serie_entry.place(x=330,y=40)
########DEBIT LABEL########
debit_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text="débit actuel : ",
                            text_color="white",
                            bg_color=color1,
                            width=260)
debit_label.place(x=20,y=100)
########DEBIT ENTRY########
debit_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1)
debit_entry.place(x=330,y=100)
########YEAR LABEL########
pression2_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Pression : ',
                            text_color="white",
                            bg_color=color1,
                            width=260)
pression2_label.place(x=20,y=160)
########YEAR ENTRY########
pression2_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1)
pression2_entry.place(x=330,y=160)
########YEAR LABEL########
temperature_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Température : ',
                            text_color="white",
                            bg_color=color1,
                            width=260
                            )
temperature_label.place(x=20,y=160)
########YEAR ENTRY########
p_temper=StringVar()
temperature_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1,
                            textvariable=p_temper)
temperature_entry.place(x=330,y=160)
########poids LABEL########
poids_initial_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Poids initial : ',
                            text_color="white",
                            bg_color=color1,
                            width=260
                            )
poids_initial_label.place(x=20,y=220)
########poids ENTRY########
p_initial=StringVar()
poids_initial_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1,
                            textvariable=p_initial)
poids_initial_entry.place(x=330,y=220)
########poids final LABEL########
poids_initial_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Poids final : ',
                            text_color="white",
                            bg_color=color1,
                            width=260
                            )
poids_initial_label.place(x=20,y=280)
########poids final ENTRY########
p_final=StringVar()
poids_initial_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1,
                            textvariable=p_final)
poids_initial_entry.place(x=330,y=280)
########calcule de volume reel########
def calcule_volume_reel(*args):
    try:
        temper=float(p_temper.get())
        Pinitial=float(p_initial.get())
        Pfinal=float(p_final.get())
        reel=(Pinitial-Pfinal)/temper
        volume_reel_entry.configure(state='normal')
        volume_reel_entry.delete(0, tk.END)
        volume_reel_entry.insert(0, f"{reel:.2f}")
        volume_reel_entry.configure(state='readonly')
    except ValueError:
        volume_reel_entry.configure(state='normal')
        volume_reel_entry.delete(0, tk.END)
        volume_reel_entry.insert(0, "volume saisie")
        volume_reel_entry.configure(state='readonly')
#Add trace to update error automatically
p_temper.trace_add("write",calcule_volume_reel)
p_initial.trace_add("write", calcule_volume_reel)
p_final.trace_add("write", calcule_volume_reel)
########TYPE DE COMPTEUR LABEL########
index_initial_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Index initial  : ',
                            text_color="white",
                            bg_color=color1,
                            width=260)
index_initial_label.place(x=20,y=340)
########TYPE DE COMPTEUR ENTRY########
index_initial=StringVar()
index_initial_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1,
                            textvariable=index_initial)
index_initial_entry.place(x=330,y=340)
########MODELE LABEL########
index_final_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Index Final : ',
                            text_color="white",
                            bg_color=color1,
                            width=260)
index_final_label.place(x=20,y=400)
########MODELE ENTRY########
index_final= StringVar()
index_final_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1,
                            textvariable=index_final)
index_final_entry.place(x=330,y=400)
####VOLUME INDIQUE####
def calcule_volume(*args):
    try:
        initial=float(index_initial.get())
        final=float(index_final.get())
        indique=(initial-final)
        volume_indique_entry.configure(state='normal')
        volume_indique_entry.delete(0, tk.END)
        volume_indique_entry.insert(0, f"{indique:.2f}")
    except ValueError:
        volume_indique_entry.configure(state='normal')
        volume_indique_entry.delete(0, tk.END)
        volume_indique_entry.insert(0, "volume saisie")
#Add trace to update error automatically
index_initial.trace_add("write", calcule_volume)
index_final.trace_add("write", calcule_volume)
########DIAMETRE LABEL########
volume_indique_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Volume Indiqué : ',
                            text_color="white",
                            bg_color=color1,
                            width=260)
volume_indique_label.place(x=20,y=460)
########DIAMETRE ENTRY########
volume_indique = StringVar()
volume_indique_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1,
                            textvariable=volume_indique,)
volume_indique_entry.place(x=330,y=460)
########CLASSE LABEL########
volume_reel_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Volume Réel : ',
                            text_color="white",
                            bg_color=color1,
                            width=260)
volume_reel_label.place(x=20,y=520)
########CLASSE ENTRY########
volume_reel = StringVar()
volume_reel_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1,
                            textvariable=volume_reel,)
volume_reel_entry.place(x=330,y=520)
########PRESSION LABEL########
erreur_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='Erreur : ',
                            text_color="white",
                            bg_color=color1,
                            width=260)
erreur_label.place(x=20,y=580)
########PRESSION ENTRY########
erreur = StringVar()
erreur_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1,
                            textvariable=erreur,)
erreur_entry.place(x=330,y=580)
########PRESSION LABEL########
EMT_label = cutk.CTkLabel(deuxieme_page,font=font1,
                            text='EMT : ',
                            text_color="white",
                            bg_color=color1,
                            width=260)
EMT_label.place(x=20,y=640)
########PRESSION ENTRY########
EMT_entry = cutk.CTkEntry(deuxieme_page,font=font1,
                            text_color="black",
                            bg_color=color1)
EMT_entry.insert(0,"±   %")
EMT_entry.place(x=330,y=640)
#################################################
####erreur####
def calculer_erreur(*args):
    try:
        indique = float(volume_indique.get())
        reel = float(volume_reel.get())
        erreur = ((indique - reel) / reel) * 100
        erreur_entry.configure(state='normal')
        erreur_entry.delete(0, tk.END)
        erreur_entry.insert(0, f"{erreur:.2f}%")
        erreur_entry.configure(state='readonly')
    except ValueError:
        erreur_entry.configure(state='normal')
        erreur_entry.delete(0, tk.END)
        erreur_entry.insert(0, "Erreur de saisie")
        erreur_entry.configure(state='readonly')

# Add trace to update error automatically
volume_indique.trace_add("write", calculer_erreur)
volume_reel.trace_add("write", calculer_erreur)
########ADD BUTTON########
add_button = cutk.CTkButton(deuxieme_page,font=font1,
                            text_color="white",
                            text='Ajouter',
                            #fg_color=color2,
                            #hover_color='silver',
                            #bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            border_width=2,
                            #border_color=color2,
                            width=260,
                            )
add_button.place(x=20,y=700)
########UPDATE BUTTON########
update_button = cutk.CTkButton(deuxieme_page,font=font1,
                            text_color=color2,
                            text='Enregistrer',
                            fg_color=color1,
                            hover_color='white',
                            #bg_color=color1,
                            border_color='white',
                            border_width=2,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260,
                            )
update_button.place(x=330,y=700)
########DELETE BUTTON########
delete_button = cutk.CTkButton(deuxieme_page,font=font1,
                            text_color=color5,
                            text="Modifier l'ajoutent",
                            fg_color=color6,
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260,
                            )
delete_button.place(x=630,y=700)
########MOdifier########
delete_button = cutk.CTkButton(deuxieme_page,font=font1,
                            text_color="white",
                            text="Suprimer l'ajoutent",
                            fg_color=color3,
                            bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            width=260,
                            )
delete_button.place(x=950,y=700)
########REPORT BUTTON########
report_button = cutk.CTkButton(deuxieme_page,font=font1,
                            text_color=color2,
                            text="Afficher Raport >>>",
                            fg_color=color1,
                            border_color='white',
                            border_width=2,
                            hover_color='white',
                            cursor="hand2",
                            corner_radius=0,
                            width=260,
                            )
report_button.place(x=1255,y=700)
########ADD BUTTON########
add_button = cutk.CTkButton(premier_page,font=font1,
                            text_color=color5,
                            text='Enregistrer',
                            #fg_color=color2,
                            #hover_color='silver',
                            #bg_color=color1,
                            cursor ='hand2',
                            corner_radius=0,
                            border_width=2,
                            #border_color=color2,
                            width=260,
                            )
add_button.place(x=20,y=700)

################TREE###############
style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview',font=font2,foreground='white',
                background=color1,fieldbackground=color4,)
style.map('Treeview',background=[('selected',color4)])

tree = ttk.Treeview(deuxieme_page,height=38)
tree['columns'] = ('N°serie','debit actuel','pression','temperature','poids initial','poids final','Index initial','Index final','Volume indiqué','Volume réel','erreur','EMT')
tree.place(x=750,y=50)
tree.column('#0',width=0,stretch=tk.NO) #hide the default ffirst colomn
tree.column('N°serie',anchor=tk.CENTER,width=95)
tree.column('debit actuel',anchor=tk.CENTER,width=95)
tree.column('pression',anchor=tk.CENTER,width=95)
tree.column('temperature',anchor=tk.CENTER,width=95)
tree.column('poids initial',anchor=tk.CENTER,width=95)
tree.column('poids final',anchor=tk.CENTER,width=95)
tree.column('Index initial',anchor=tk.CENTER,width=95)
tree.column('Index final',anchor=tk.CENTER,width=95) #hide the default ffirst colomn
tree.column('Volume indiqué',anchor=tk.CENTER,width=95)
tree.column('Volume réel',anchor=tk.CENTER,width=95)
tree.column('erreur',anchor=tk.CENTER,width=95)
tree.column('EMT',anchor=tk.CENTER,width=95)
########REPORT HEADING########
tree.heading('N°serie',text='N°serie')
tree.heading('debit actuel',text='debit actuel')
tree.heading('pression',text='pression')
tree.heading('temperature',text='temperature')
tree.heading('poids initial',text='poids initial')
tree.heading('poids final',text='poids final')
tree.heading('Index initial',text='Index initial')
tree.heading('Index final',text='Index final')
tree.heading('Volume indiqué',text='Volume indiqué')
tree.heading('Volume réel',text='Volume réel')
tree.heading('erreur',text='erreur')
tree.heading('EMT',text='EMT')
###################################SEARCH FRAME ####################################
###################################SEARCH PAR DATE FRAME ####################################
search_page_date = cutk.CTkFrame(app, bg_color=color1,fg_color=color1)
cherche_date = cutk.CTkLabel(search_page_date,font=font1,
                             text="entrer la date🔎 : ",
                             text_color="white",
                             bg_color=color1)
cherche_date.place(x=20,y=40)
cherche_entry = cutk.CTkEntry(search_page_date,font=font1,
                              text_color="black",
                              bg_color=color1)
cherche_entry.place(x=220,y=40)
###################################SEARCH PAR  (INTERVALLE) FRAME ####################################
search_page_intervalle = cutk.CTkFrame(app, bg_color=color1,fg_color=color1)
cherche_label_interv_1 = cutk.CTkLabel(search_page_intervalle,font=font1,
                             text="entrer la date de debut : ",
                             text_color="white",
                             bg_color=color1)
cherche_label_interv_1.place(x=20,y=40)
cherche_entry_interv_1 = cutk.CTkEntry(search_page_intervalle,font=font1,
                              text_color="black",
                              bg_color=color1)
cherche_entry_interv_1.place(x=280,y=40)
cherche_label_interv_2 = cutk.CTkLabel(search_page_intervalle,font=font1,
                             text="entrer la date de fin : ",
                             text_color="white",
                             bg_color=color1)
cherche_label_interv_2.place(x=500,y=40)
cherche_entry_interv_1 = cutk.CTkEntry(search_page_intervalle,font=font1,
                              text_color="black",
                              bg_color=color1)
cherche_entry_interv_1.place(x=750,y=40)
###################################SEARCH PAR N°SERIE FRAME ####################################
search_page_n_serie = cutk.CTkFrame(app, bg_color=color1,fg_color=color1)
cherche_label_n_serie = cutk.CTkLabel(search_page_n_serie,font=font1,
                             text="N°SERIE🔎 : ",
                             text_color="white",
                             bg_color=color1)
cherche_label_n_serie.place(x=20,y=40)
cherche_entry_n_serie = cutk.CTkEntry(search_page_n_serie,font=font1,
                              text_color="black",
                              bg_color=color1)
cherche_entry_n_serie.place(x=220,y=40)
tree = ttk.Treeview(search_page_n_serie,height=35)
tree['columns'] = ('N°serie','debit actuel','pression','temperature','poids initial','poids final','Index initial','Index final','Volume indiqué','Volume réel','erreur','EMT','date/heure')
tree.place(x=750,y=50)
tree.column('#0',width=0,stretch=tk.NO) #hide the default ffirst colomn
tree.column('N°serie',anchor=tk.CENTER,width=80)
tree.column('debit actuel',anchor=tk.CENTER,width=80)
tree.column('pression',anchor=tk.CENTER,width=80)
tree.column('temperature',anchor=tk.CENTER,width=80)
tree.column('poids initial',anchor=tk.CENTER,width=80)
tree.column('poids final',anchor=tk.CENTER,width=80)
tree.column('Index initial',anchor=tk.CENTER,width=80)
tree.column('Index final',anchor=tk.CENTER,width=80) #hide the default ffirst colomn
tree.column('Volume indiqué',anchor=tk.CENTER,width=80)
tree.column('Volume réel',anchor=tk.CENTER,width=80)
tree.column('erreur',anchor=tk.CENTER,width=80)
tree.column('EMT',anchor=tk.CENTER,width=80)
tree.column('date/heure',anchor=tk.CENTER,width=90)
########REPORT HEADING########
tree.heading('N°serie',text='N°serie')
tree.heading('debit actuel',text='debit actuel')
tree.heading('pression',text='pression')
tree.heading('temperature',text='temperature')
tree.heading('poids initial',text='poids initial')
tree.heading('poids final',text='poids final')
tree.heading('Index initial',text='Index initial')
tree.heading('Index final',text='Index final')
tree.heading('Volume indiqué',text='Volume indiqué')
tree.heading('Volume réel',text='Volume réel')
tree.heading('erreur',text='erreur')
tree.heading('EMT',text='EMT')
tree.heading('date/heure',text='date/heure')
##############################modele###############################
search_page_model = cutk.CTkFrame(app, bg_color=color1,fg_color=color1)
cherche_label_model = cutk.CTkLabel(search_page_model,font=font1,
                             text="Modele : ",
                             text_color="white",
                             bg_color=color1)
cherche_label_model.place(x=20,y=40)
cherche_entry_model = cutk.CTkEntry(search_page_model,font=font1,
                              text_color="black",
                              bg_color=color1)
cherche_entry_model.place(x=220,y=40)
########search BUTTON########
seaech_button = cutk.CTkButton(search_page_n_serie,font=font1,
                            text_color=color2,
                            text="SEARCH",
                            fg_color=color1,
                            border_color='white',
                            border_width=2,
                            hover_color='white',
                            cursor="hand2",
                            corner_radius=0,
                            width=260,
                            )
seaech_button.place(x=255,y=100)
########search BUTTON########
seaech_button = cutk.CTkButton(search_page_date,font=font1,
                            text_color=color2,
                            text="SEARCH",
                            fg_color=color1,
                            border_color='white',
                            border_width=2,
                            hover_color='white',
                            cursor="hand2",
                            corner_radius=0,
                            width=260,
                            )
seaech_button.place(x=255,y=100)
########search BUTTON########
seaech_button = cutk.CTkButton(search_page_intervalle,font=font1,
                            text_color=color2,
                            text="SEARCH",
                            fg_color=color1,
                            border_color='white',
                            border_width=2,
                            hover_color='white',
                            cursor="hand2",
                            corner_radius=0,
                            width=260,
                            )
seaech_button.place(x=255,y=100)
########search BUTTON########
seaech_button = cutk.CTkButton(search_page_model,font=font1,
                            text_color=color2,
                            text="SEARCH",
                            fg_color=color1,
                            border_color='white',
                            border_width=2,
                            hover_color='white',
                            cursor="hand2",
                            corner_radius=0,
                            width=260,
                            )
seaech_button.place(x=255,y=100)


update_time()
app.mainloop()
