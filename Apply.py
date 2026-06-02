import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import random, os, sys, re
from tkinter import PhotoImage
from tkinter.filedialog import askopenfilename, asksaveasfilename # Plus spécifiques
from tkinter.messagebox import showinfo, showerror # Plus spécifiques
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
import os
import sqlite3
from datetime import datetime
import smtplib
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# Copyright (C) 2013 Riverbank Computing Limited.
# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause



        
        


# --- Dictionnaire de couleurs pour une gestion facile ---
COLORS = {
    "nero": "#252726",
    "purple": "#800080",
    "white": "#FFFFFF",
    "green_dark": "#006400",  # Un vert plus foncé pour les cadres
    "orange_dark": "#FF8C00" } # Un orange plus foncé pour les bannières et boutons


#Ma base de données 

DB_NAME = "etudiants.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS inscription (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        numero_carte TEXT UNIQUE,
        email TEXT,
        departement TEXT,
        date TEXT
    )
    """)
    conn.commit()
    return conn, cur

          
              
                
                  
                    
                        

# Fonction pour afficher une frame et cacher les autres
def afficher_page(page):
    page.tkraise()
    
    # "%H : %M : %S    %d/%m/%Y"

#update time page accueil           

def update_time():
   
    
    current_time = time.strftime("%kh : %Mmn  : %Ss : %A    \n                     %d/ %m/ %Y")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)                      
                                            

    
        
            
                    
 

# Fenêtre principale
app = tk.Tk()
app.geometry("600x400")
app.title("Portail Étudiant")

# Configuration du système de "pages"
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)

#verificattion de connexion 
import urllib.request

def check_internet():
    try:
        urllib.request.urlopen("http://www.google.com", timeout=5)
        return True 
    except:
        return False 
        
       




#1er fenêtre 
# ---------- Page d'accueil ----------
page_accueil = tk.Frame(app, bg="gray100")
page_accueil.grid(row=0, column=0, sticky="nsew", rowspan=20)
#lbl_bienvenue = tk.Label(page_accueil, text="Bienvenue sur le portail étudiant", font=("Arial", 16))
#lbl_bienvenue.pack(pady=30)






#le frame du top sur la page_accueil
frame = tk.Frame(page_accueil, bg="#0e6645", relief="groove", bd=0)
frame.pack(side="top", fill = tk.X)



canvas = tk.Canvas(page_accueil, width=95, height=20, bg="#0e6647", highlightthickness=0)
canvas.place(x=580, y=20)

# Exemple : texte incliné de 0°
canvas.create_text(45, 10, text="★★★★★", angle=0, fill="gray100", font=("ExtraCondensed", 5), tags="rotated")






# label time

clock_label = tk.Label(page_accueil, fg="gray35", bg="gray100", font= "ExtraCondensed 9")
clock_label.place(x=170, y= 1095)

update_time()




# Titre
tk.Label(page_accueil, text="\n\n \n           \n\n", font=("Helvetica", 5, "bold"), bg="gray100", fg="#CE8000",highlightbackground="gray85", highlightthickness=10, width =50, height= 9, bd=6, relief="raised").place(x=20, y= 147)




# Titre
tk.Label(page_accueil, text="FRATERNITE TRAVAIL PROGRES\n MINISTRE\n DE L'ENSEIGNEMENT \nSUPÉRIEUR\n DE LA RECHERCHE ET DE\n L'INNOVATION TECHNOLOGIQUE", font=("Helvetica", 5, "bold"), bg="gray100", fg="#0e6647", highlightbackground="gray85", height=8, highlightthickness=4,  bd=0, relief="raised").place(x=342, y= 240)



navE = PhotoImage(file='Screenshot_20260216-001720_1 (1).png')



tk.Button(page_accueil, image=navE, bg="gray98", width= 85, height=90, bd=-2, activebackground="gray100", highlightthickness=-2).place(x=447, y=174)


navC = PhotoImage(file='file_00000000ef3871fda4626a6638d9cded_1 (3).png')



tk.Button(page_accueil, image=navC, bg="gray98", width= 190, height=190, bd=-2, activebackground="gray100", highlightthickness=-2).place(x=150, y=195)










# Text sur le frame si-haut)

accueilText = tk.Label(frame, text="UENUZ", font=("Arial", 14), bg="#0e6647", fg="white", height=2, padx=55)
accueilText.pack(side="right")

canvas22 = tk.Canvas(page_accueil, borderwidth=1, bg="gray100", width=160, highlightthickness=0, height=-2)
canvas22.place(x=432, y=90)

canvas22 = tk.Canvas(page_accueil, borderwidth=1, bg="gray100", width=160, highlightthickness=0, height=2)
canvas22.place(x=432, y=93)

canvas22 = tk.Canvas(page_accueil, borderwidth=1, bg="gray100", width=160, highlightthickness=0, height=2)
canvas22.place(x=545, y=40)

canvas22 = tk.Canvas(page_accueil, borderwidth=1, bg="gray100", width=160, highlightthickness=0, height=-2)
canvas22.place(x=545, y=37)







# Def du chargement connexion en cours 
def show_loading(callback):
    # Petite fenêtre popup
    load = tk.Toplevel(app)
    load.title("Chargement…")
    load.geometry("750x1500")
    load.resizable(False, False)
    load.configure(bg="gray58")
    
    
    #canvas2 = tk.Canvas(load, borderwidth=1, bg="white", width=600, highlightthickness=15, height=100)
    #canvas2.place(x=25, y=105)
    
    
    

    lbl = tk.Label(load, text="Connexion en cours...", font=("Arial", 9), bg="gray58", fg="gray85")
    lbl.place(x=40, y=1040)

    # Simule une progression
    pb = ttk.Progressbar(load, mode='indeterminate', length=500)
    pb.place(x=40, y=1100)
    pb.start(10)

    # Après 1.2 seconde → fermer le popup et appeler la suite
    def finish():
        pb.stop()
        load.destroy()
        callback()

    load.after(3200, finish)










# photo uas

navucon = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (3).png')



tk.Button(page_accueil, image=navucon, bg="gray100", width= 250, height=258, bd=-2, activebackground="gray100", highlightthickness=-2).place(x=245, y=435)








#les trois bars horizontal
# eeefee
canvas22 = tk.Canvas(page_accueil, borderwidth=1, bg="gray85", width=30, highlightbackground="white", highlightthickness=6, relief= "groove", bd= 0, height=312)
canvas22.place(x=93, y=203)

canvas22 = tk.Canvas(page_accueil, borderwidth=1, bg="gray80", width=30, highlightbackground="gray85", highlightthickness=4, relief= "groove", bd= 1, height=287)
canvas22.place(x=134, y=345)

canvas22 = tk.Canvas(page_accueil, borderwidth=1, bg="gray80", width=28, highlightbackground="gray85", highlightthickness=4, relief= "groove", bd= 1, height=282)
canvas22.place(x=55, y=345)







#les canvas 

#cadran canvas en bas du champ
canvas1 = tk.Canvas(page_accueil, borderwidth=1, bg="#0e6647", highlightthickness=20,highlightbackground="gray90", relief='groove', bd = 2, width=115, height=458)
canvas1.place(x=535, y=570)


#cadran canvas en bas du champ
canvas = tk.Canvas(page_accueil, borderwidth=1, bg="#0e6647", highlightthickness=20, relief='groove', bd= 2, width=115, height=450)
canvas.place(x=35, y=578)


#cadran canvas en bas du champ
canvas2 = tk.Canvas(page_accueil, borderwidth=1, bg=COLORS ["orange_dark"], width=20, highlightthickness=20, height=100)
canvas2.place(x=35, y=880)

#cadran canvas en bas du champ
canvas2 = tk.Canvas(page_accueil, borderwidth=1, bg=COLORS["orange_dark"], width=19, highlightthickness=20, height=100)
canvas2.place(x=630, y=880)



liste = tk.Listbox(page_accueil, width=9, font = "ExtraCondensed 5", bd=4, relief= "groove", height =5, bg="#0e6647", fg= "#ffffff",highlightbackground="gray85", highlightthickness=6)
liste.insert(1, "   |||||||||||||")
liste.insert(2, "|||||||||||||")
liste.insert(3, "|||||||||||||")
liste.insert(4, "|||||||||||||")
liste.insert(5, "   |||||||||||||")
liste.place(x= 56, y= 452)







#can.pack()

#text de l'honneur de la patrie 
txt= tk.Label(page_accueil, text="L' HONNEUR DE LA PATRIE\n\n\n     Des rives du Niger au confins du Ténéré frère et soeur nous sommes\n  Enfants d'une même patrie le Niger\nNourris de la sève des même idéaux\nPour un Niger de Paix libre fort et uni\nPour un Niger prospère le pays de nos rêves\n\npour l'honneur de la patrie\nincarnons la vaillance et la perseverance\net toutes les vertus de nos digne aïeux\nguerriers intrépides déterminés et fiers\ndéfendons la patrie aux prix de notre sang\nfaisons du Niger symbole de dignité \nemblème et flambeau de l'Afrique qui avance\n\npour ces notre idéaux début et en avant\nen avant pour le travail en avant pour le combat\n\nnous demeurons debout\nportant haut le drapeau de notre cher pays\ndans le ciel de l'Afrique et dans tout l'univers\npour construire en ensemble\nun monde de justice de paix et de progrès\net pour faire du Niger la fierté de l'Afrique.   ", highlightthickness=4, relief="groove", bd= 2, bg="#0e6647", fg="#eeefee", font =("Arial", 3))
txt.place(x=159, y=690)

'''

liste= tk.Listbox(page_accueil, bg="#ACC0CE", fg="yellow", font="ExtraCondensed 10", bd=10, highlightthickness=12, width=8, height=5, relief="solid")
liste.insert(1,"    FLSH")
liste.insert(2, "    FSS")
liste.insert(3, "    FSE")
liste.insert(4, "    FST")
liste.insert(5, "    IUT")
liste.place(x=500, y=740)



'''

#image alarm 


navuconh = PhotoImage(file='alarm-outline.72.png')



tk.Button(page_accueil, image=navuconh, bg="gray100", width= 70, height=70, bd=-2, activebackground="gray100", highlightthickness=-2).place(x=80, y= 1095)



#image = Image.open('alarm-outline.72.png')

#photo = ImageTk.PhotoImage(image)
#tk.Label(page_accueil, image=photo,  bg="gray80").place(x=80, y= 1095)





# --- Cadre du bas (Bottom Frame) ---
bottom_frame = tk.Frame(page_accueil, bg="#0e6647", relief="solid", bd=3)
bottom_frame.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg="#0e6647", fg="white",
         height=4).pack() # Texte de copyright au lieu de labels vides
 

'''

#Text de bienvenue 
accueilText = tk.Label(page_accueil, text="Veuillez taper notre adress ip  ...........  \n afin de vous contacter à UAS", font=("Helvetica", 8), bg="#CCCCCC", fg="gray50",  highlightthickness=8, height=2,  pady=2)
accueilText.place(x=100, y= 210)


#text de login _____-------_____
bannerText = tk.Label(page_accueil, text="Login....", font=" ExtraCondensed 8", fg="gray40", bg="white" ,bd=0, relief="groove", foreground="black")
bannerText.place(x=35, y= 460)

canvas = tk.Canvas(page_accueil, width=100, height=130, bg="white", highlightthickness=0)
canvas.place(x=120, y=340)

# Exemple : texte " ⬅" incliné de 90°
canvas.create_text(50, 50, text="⬅", angle=90, fill="orange", font=("ExtraCondensed", 18), tags="rotated")

'''


'''

#Le champ entry sur la page_accueil
numéro1= tk.Entry(page_accueil, placeholder = "   Adress IP : .......... ", bg="white", fg="gray4", bd=8, font="ExtraCondensed 20" , width=14 , highlightthickness=20, relief="solid").place(x=35, y=520)

'''


'''


navBcon = PhotoImage(file='Minduka_Present_Blue_pack.png')

#navIcon = PhotoImage(file='font.png')

#tk.Button(page_accueil, image=navIcon, bg=COLORS ["orange_dark"], width= 18, height=24, highlightthickness=-1).place(x=80, y=90)

#tk.Button(page_accueil, image=navIcon, bg=COLORS ["orange_dark"], width= 22, height=24, highlightthickness=-1).place(x=50, y=90)

#tk.Button(page_accueil, image=navIcon, bg=COLORS ["orange_dark"], width= 18, height=24, highlightthickness=-1).place(x=200, y=200)



tk.Button(page_accueil, image=navBcon, bg=COLORS ["orange_dark"], width= 190, height=114, bd=0, activebackground=COLORS["orange_dark"], highlightthickness=-0).place(x=550, y=380)


'''
















#fenetre de la création d'un compte 
page_compte = tk.Frame(app, bg="gray86")
page_compte.grid(row=0, column=0, sticky="nsew", rowspan=20)



#text en haut "Vous n'avez pas de compte du frame page_accueil
bannerText = tk.Label(page_accueil, text="Vous n'avez pas de compte ?", font=" ExtraCondensed 8", fg="#CE8000", bg="white", bd=0, relief="groove")
bannerText.place(x=30, y= 1340)



N = tk.Button(page_accueil, text=" Créer un compte", font=" ExtraCondensed 9",bd=0, relief="groove", fg=COLORS ["green_dark"], activebackground="white", bg="white", highlightthickness=-1, command=lambda: afficher_page(page_compte))
N.place(x=418, y= 1324)

btnEtatF= False 

def switchF():
    def open_panel():
        global btnEtatF
        if btnEtatF:
            navLateralF.place(x=800, y=0)
            btnEtatF = False
        else:
            navLateralF.place(x=5, y=20)
            btnEtatF = True

    # Vérifier la connexion Internet AVANT de charger
    #if not check_internet():
        #messagebox.showerror("Connexion  échouée...........................", "\n\n\n IMPOSSIBLE QUE NOUS PUISSIONS\n VOUS CONNECTER À INTERNET. \n\n\n\n\n\n\n\n\n\n\n VOICI QUELQUES CONSEILS :\n   •Desactivez le mode Avion.\n   • Activiez les données mobiles ou le\n      réseau WI-FI.\n   •Vérifiez le signal dans votre zone.\n\n\n\n\n\n\n ERR_INTERNET_DISCONNECTED\n\n")
    #return # On arrête la fonction

    # Sinon → afficher l’effet de chargement puis ouvrir
    show_loading(open_panel)


'''

#Petite fenêtre de la sélection des Facultés 
btn_E = False 
btnEtatF= False 
def switchF():
    global btnEtatF
    if btnEtatF:
        navLateralF.place(x=800, y=0)
        btnEtatF = False
    else:
        navLateralF.place(x=30, y=20)
        btnEtatF = True
        
  
'''
    
        
          
            
                
# button connectez vous 
    
btn_F = tk.Button(
    page_accueil,
    text="Connectez-vous", activebackground=COLORS["green_dark"], padx=150, pady=30, bd=5, relief="sunken",
    command=switchF, 
    bg="#CE8000", highlightbackground="gray80", highlightthickness=9, fg="#ffffff", font=("Arial", 6)
)
btn_F.place(x=130, y=1200)        
            
                
                        
   
  
#frame sur page_accueil 

navLateralF = tk.Frame(page_accueil, bg="gray94", width=705, height=1390)
navLateralF.place(x=-800, y=200)








'''



navCcon = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (3).png')




tk.Button(navLateralF, image=navCcon, bg="gray100", width= 760, height=360, bd=0, activebackground="gray100", highlightthickness=-2).place(x=-10, y=1085)

'''


#cadran canvas 
canvas = tk.Canvas(navLateralF, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=690, height=2)
canvas.place(x=15, y=203)

#cadran canvas en dessous de placeholder 
canvas = tk.Canvas(navLateralF, borderwidth=1, bg="#356E27", highlightthickness=0, relief='groove', width=620, height=15)
canvas.place(x=39, y=950)



#cadran canvas côté gauche 
canvas = tk.Canvas(navLateralF, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=21, height=205)
canvas.place(x=0, y=0)

#cadran canvas côté droit 
canvas = tk.Canvas(navLateralF, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=21, height=205)
canvas.place(x=685, y=0)


#photo uas sur navLateralF 




navnaLcon = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (1).png')



tk.Button(navLateralF, image=navnaLcon, bg="gray100", width= 658, height=110, bd=0, activebackground="gray100", highlightthickness=-2).place(x=22, y=0)


#cadran canvas tirer -------------
canvas = tk.Canvas(navLateralF, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=273, height=5)
canvas.place(x=21, y=53)


#cadran canvas tirer ---------------
canvas = tk.Canvas(navLateralF, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=280, height=5)
canvas.place(x=403, y=53)




F_T= tk.Label(navLateralF, bg="gray95", text= " Veuillez renseigner le compte Créer ?", font= "ExtraCondensed 10", fg="orange")
F_T.place(x=30, y= 130)

'''
canvas = tk.Canvas(navLateralF, borderwidth=1, bg="#", highlightthickness=0, width=300, height=270, relief="raised", bd=6)
canvas.place(x=35, y=220)
'''











#Screenshot_20260216-001720_1 (5).png

#Screenshot_20241125-143152_1.jpg
# photo du logo du Niger

image = Image.open('Screenshot_20260417-162631 (1).png')

photo = ImageTk.PhotoImage(image)
tk.Label(navLateralF, bg= "gray100", highlightbackground="gray100",   highlightthickness=2, height = 480, width = 700, image=photo).place(x= 0, y= 300)



# Titre
#tk.Label(navLateralF, text="\nMINISTRE\n DE L'ENSEIGNEMENT SUPÉRIEUR DE LA RECHERCHE ET DE L'INNOVATION TECHNOLOGIQUE\nUNIVERSITÉ ANDRÉ SALIFOU\n SERVICE DE SCOLARITÉ\n\n", font=("Helvetica", 5, "bold"), bg="gray95", fg="orange",highlightbackground="gray98", highlightthickness=5,  bd=5, relief="raised").place(x=62, y= 408)




# photo image Google 

image = Image.open('Screenshot_20260216-130122_1 (1).png')

photo1 = ImageTk.PhotoImage(image)
tk.Label(navLateralF, bg= "gray100", bd = 0, highlightthickness= -2, height = 90, width = 500, image=photo1).place(x=110, y= 1300)









#text
entrerS = tk.Label(navLateralF, text= "Login....", font= "ExtraCondensed 11", bg= "gray100", fg=COLORS ["orange_dark"])
entrerS.place(x=44, y= 630)



# limite des canvas en dessous des facilités 







#placeholder

P_F1 = tk.Entry(navLateralF, placeholder = "ID-User   ", bg="white", fg="gray0" ,highlightbackground="green", highlightthickness=3, font="ExtraCondensed 20" , bd=2, width=14).place(x=45, y=700)




#placeholder

P_F1 = tk.Entry(navLateralF, placeholder = " Mot de passe", bg="white", fg="gray0" ,highlightbackground="green", highlightthickness=3, font="ExtraCondensed 20" , bd=2, width=14).place(x=45, y=830)



#text j'ai déjà un compte 
bannerText = tk.Button(navLateralF, text="Mot de pass Oublié ?", font=" ExtraCondensed 8", fg="#CE8000", bg="gray95", bd=0, highlightthickness =-2)
bannerText.place(x=335, y= 980)




# btn Annuler
Btn_rF= tk.Button(navLateralF, text="ANNULER" ,bg="#CE8000", fg="white", pady=10, activebackground="white", bd=9,highlightthickness=8, highlightbackground="gray80",font ="ExtraCondensed 9", command=switchF)
Btn_rF.place(x=40, y=1120)




#command=lambda: afficher_page(page_inscription)

#btn envoyer sur la navLateralF 

















#frame d'aide 

page_aide = tk.Frame(app, bg="gray68")
page_aide.grid(row=0, column=0, sticky="nsew", rowspan=20)






#Btn_Aid= tk.Button(navLateralF, text="Aide", bg="gray95", fg="#CE8000", activebackground="white", bd=0,highlightthickness=-4, command=lambda: afficher_page(page_aide), font ="ExtraCondensed 10")
#Btn_Aid.place(x=460,  y=530)



#Btn retour 






























btnEtat_F= False 

def switch_F():
        
        
        global btnEtat_F
        if btnEtat_F:
            navLateral_F.place(x=800, y=0)
            btnEtat_F = False
        else:
            navLateral_F.place(x=20, y=20)
            btnEtat_F = True





#frame sur page_accueil 

navLateral_F = tk.Frame(page_accueil, bg="gray94", width=670, height=1395)
navLateral_F.place(x=-800, y=200)



# Btn Valider les Facultés 

btn_E = tk.Button(
    navLateralF,
    text="Valider",  activebackground="white", padx=50, pady=10, relief= "sunken",
    bg="#CE8000", highlightthickness=8, highlightbackground="gray80", command=switch_F, bd=9, fg="white", font=("Arial", 9))
btn_E.place(x=430, y=1120)









navCcon_F= PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (3).png')



tk.Button(navLateral_F, image=navCcon_F, bg="gray100", width= 800, height=330, bd=0, activebackground="gray100", highlightthickness=-2).place(x=-60, y=1097)





#cadran canvas 
canvas = tk.Canvas(navLateral_F, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=640, height=2)
canvas.place(x=15, y=203)

#cadran canvas en dessous de placeholder 
canvas = tk.Canvas(navLateral_F, borderwidth=1, bg="#356E27", highlightthickness=0, relief='groove', width=580, height=15)
canvas.place(x=40, y=924)



#cadran canvas côté gauche 
canvas = tk.Canvas(navLateral_F, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=21, height=205)
canvas.place(x=0, y=0)

#cadran canvas côté droit 
canvas = tk.Canvas(navLateral_F, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=21, height=205)
canvas.place(x=655, y=0)


#photo uas sur navLateralF 




navnaLcon_F = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (1).png')



tk.Button(navLateral_F, image=navnaLcon_F, bg="gray100", width= 630, height=110, bd=0, activebackground="gray100", highlightthickness=-2).place(x=22, y=0)


#cadran canvas tirer -------------
canvas = tk.Canvas(navLateral_F, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=260, height=5)
canvas.place(x=21, y=53)


#cadran canvas tirer ---------------
canvas = tk.Canvas(navLateral_F, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, relief='groove', width=260, height=5)
canvas.place(x=393, y=53)




F_T= tk.Label(navLateral_F, bg="gray95", text= " Quelle est votre Faculté ?", font= "ExtraCondensed 13", fg="orange")
F_T.place(x=55, y= 130)

'''
canvas = tk.Canvas(navLateralF, borderwidth=1, bg="#", highlightthickness=0, width=300, height=270, relief="raised", bd=6)
canvas.place(x=35, y=220)
'''

# text 
p = tk.Label(navLateral_F, text= "1.", font= "ExtraCondensed 12", bg= "gray94", fg= "gray0")
p.place(x=40, y=230)



#cadran canvas en haute 
canvas1 = tk.Canvas(navLateral_F, borderwidth=1, bg="gray90", highlightthickness=0, relief='groove', width=530, height=1)
canvas1.place(x=65, y=300)


T_F= tk.Label(navLateral_F, text= "FLSH", font= "ExtraCondensed 12", bg= "gray94", fg= "gray45")
T_F.place(x=90, y= 230)



T_F= tk.Label(navLateral_F, text= "FSE", font= "ExtraCondensed 12", bg= "gray94", fg= "gray45")
T_F.place(x=90, y= 317)



# text 
p = tk.Label(navLateral_F, text= "2.", font= "ExtraCondensed 12", bg= "gray94", fg= "gray0")
p.place(x=40, y=317)


#cadran canvas en haute 
canvas1 = tk.Canvas(navLateral_F, borderwidth=1, bg="gray90", highlightthickness=0, relief='groove', width=530, height=1)
canvas1.place(x=65, y=387)





T_F1 = tk.Label(navLateral_F, text= "FST", font= "ExtraCondensed 12", bg= "gray94", fg= "gray45")
T_F1.place(x=90, y= 407)

#text
p1 = tk.Label(navLateral_F, text= "3.", font= "ExtraCondensed 12", bg= "gray94", fg= "gray0")
p1.place(x=40, y= 407)

#cadran canvas en haute 
canvas1 = tk.Canvas(navLateral_F, borderwidth=1, bg="gray90", highlightthickness=0, relief='groove', width=530, height=1)
canvas1.place(x=65, y=480)






T_F2= tk.Label(navLateral_F, text= "FSS", font= "ExtraCondensed 12", bg= "gray94", fg= "gray45")
T_F2.place(x=90, y= 500)


#text
p2 = tk.Label(navLateral_F, text= "4.", font= "ExtraCondensed 12", bg= "gray94", fg= "gray0")
p2.place(x=40, y= 500)


#cadran canvas en haute 
canvas1 = tk.Canvas(navLateral_F, borderwidth=1, bg="gray90", highlightthickness=0, relief='groove', width=530, height=1)
canvas1.place(x=65, y=580)





T_F3= tk.Label(navLateral_F, text= "IUT", font= "ExtraCondensed 12", bg= "gray94", fg= "gray45")
T_F3.place(x=90, y= 600)


#text
p3 = tk.Label(navLateral_F, text= "5.", font= "ExtraCondensed 12", bg= "gray94", fg= "gray0")
p3.place(x=40, y= 600)

#cadran canvas en haute 
canvas1 = tk.Canvas(navLateral_F, borderwidth=1, bg="gray90", highlightthickness=0, relief='groove', width=530, height=1)
canvas1.place(x=65, y=680)




#pour la Faculté "école de pétrole de minime"


T_F3= tk.Label(navLateral_F, text= "ÉCOLE DU PÉTROLE DE MINES", font= "ExtraCondensed 10", bg= "gray94", fg= "gray45")
T_F3.place(x=90, y= 699)


#text
p3 = tk.Label(navLateral_F, text= "6.", font= "ExtraCondensed 12", bg= "gray94", fg= "gray0")
p3.place(x=40, y= 694)

#cadran canvas en haute 
canvas1 = tk.Canvas(navLateral_F, borderwidth=1, bg="gray90", highlightthickness=0, relief='groove', width=530, height=1)
canvas1.place(x=65, y=766)









#text
entrerS = tk.Label(navLateral_F, text= "Taper 1 ou 2.. puis valider", font= "ExtraCondensed 7", bg= "gray94", fg= "gray40")
entrerS.place(x=50, y= 770)



# limite des canvas en dessous des facilités 












#placeholder

P_F = tk.Entry(navLateral_F, placeholder = "             ", bg="white", fg="gray0" ,highlightbackground="green", highlightthickness=3, font="ExtraCondensed 17" , bd=2, width=16).place(x=40, y=810)






# btn Annuler
Btn_rF= tk.Button(navLateral_F, text="ANNULER" ,bg="#CE8000", fg="white", pady=10, activebackground="white", bd=9,highlightthickness=8, highlightbackground="gray80",font ="ExtraCondensed 9", command=switch_F)
Btn_rF.place(x=10, y=970)






#btn envoyer sur la navLateralF 
btn_E = tk.Button(
    navLateral_F,
    text="Valider",  activebackground="white", padx=50, pady=10, relief= "sunken",
    bg="#CE8000", highlightthickness=8, highlightbackground="gray80", command=lambda: afficher_page(page_inscription), bd=9, fg="white", font=("Arial", 9))
btn_E.place(x=400, y=970)
















#frame d'aide 

#page_aide = tk.Frame(app, bg="gray68")
#page_aide.grid(row=0, column=0, sticky="nsew", rowspan=20)






Btn_Aid= tk.Button(navLateral_F, text="Aide", bg="gray95", fg="#CE8000", activebackground="white", bd=0,highlightthickness=-4, command=lambda: afficher_page(page_aide), font ="ExtraCondensed 10")
Btn_Aid.place(x=460,  y=1100)





























'''
#text au dessus du frame compte 
bannerText = tk.Label(page_compte, text="Créer un compte ?", font=" ExtraCondensed 9", fg="white", bg=COLORS ["green_dark"] ,bd=0, relief="groove")
bannerText.place(x=230, y= 40)
'''







#cadran canvas : celui-ci recouvre presque la "page_comte"
canvasC = tk.Canvas(page_compte, borderwidth=1, bg="gray95", highlightbackground="white", highlightthickness=3, bd= 10, relief="raised", width=647, height=1310)
canvasC.place(x=20, y=40)




T_G= tk.Label(page_compte, text= "Créer un compte", font= "ExtraCondensed 13", bg= "gray95", fg= "gray50")
T_G.place(x=180, y= 90)





#placeholder sur la page_compte  
prenom = tk.Entry(page_compte, highlightthickness = 3, bg="gray100", fg="gray70", font="ExtraCondensed 18", highlightbackground="green", bd=8, width=16, relief= "solid")
prenom.place(x=40, y=200)


#placeholder sur la page_compte  
nom = tk.Entry(page_compte, highlightthickness = 3, bg="gray100", fg="gray70", font="ExtraCondensed 18", bd=8, highlightbackground="green", width=16, relief= "solid")
nom.place(x=40, y=350)



#placeholder sur la page_compte  
email1 = tk.Entry(page_compte, placeholder="Entrer votre email", highlightthickness = 3, highlightbackground="green", bg="gray100", fg="gray70", font="ExtraCondensed 18", bd=8, width=16, relief= "solid")
email1.place(x=40, y=500)


#placeholder sur la page_compte  
Telephone = tk.Entry(page_compte, placeholder=" N° de Telephone", highlightthickness = 3, bg="gray100", fg="orange", highlightbackground="green", font="ExtraCondensed 18", bd=8, width=16, relief= "solid")
Telephone.place(x=40, y=650)

#text j'ai déjà un compte 
#bannerText = tk.Button(page_compte, text="Mot de pass Oublié ?", font=" ExtraCondensed 6", fg="green", bg="gray95", bd=0, highlightthickness =-2)
#bannerText.place(x=395, y= 1080)


#Checkbox sur la page_compte
check_compte = tk.Checkbutton(page_compte, text="j'ai lu et j'accepte les Termes et \n conditions de confidentialité", bg="gray95", fg="gray10", font="ExtraCondensed 10", bd = 0, highlightthickness = -3, relief = "raised", activebackground="green", borderwidth = 0, height= 3)
check_compte.place(x=45, y=1080)


#text
entrerS = tk.Label(page_compte, text= "Termes", font= "ExtraCondensed 10", bg= "gray95", fg= "green")
entrerS.place(x=455, y= 1098)






#btn envoyer sur page_compte

btn_compte = tk.Button(
    page_compte,
    text="Suivant", activebackground=COLORS["green_dark"], padx=80, pady=30, bd=1, relief="solid", 
    bg="white", fg="green", font=("Arial", 6)
)
btn_compte.place(x=420, y=1250)











#placeholder sur la page_compte  
MotPass = tk.Entry(page_compte, highlightthickness = 3, bg="gray100", fg="gray70", font="ExtraCondensed 18", highlightbackground="green", bd=8, width=16, relief= "solid")
MotPass.place(x=40, y=800)

#placeholder sur la page_compte  
MotPassC = tk.Entry(page_compte, highlightthickness = 3, bg="gray100", fg="gray70", font="ExtraCondensed 18", highlightbackground="green", bd=8, width=16, relief= "solid")
MotPassC.place(x=40, y=950)



def toggle_visibility():
    if MotPassC.cget('show') == '':
        MotPassC.config(show='*')
        toggle_btn4.config(fg= 'green', text='voir')
    else:
        MotPassC.config(show='')
        toggle_btn4.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if MotPassC.get() == "Confirmer":
        MotPassC.delete(0, tk.END)
        MotPassC.config( fg="gray", show="*")  # Afficher les caractères masqués après clic



MotPassC.insert(0,  "Confirmer")  

#Bind des événements
MotPassC.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)


# button qui commande la fonction "toggle_visibility"
toggle_btn4 = tk.Button(page_compte, text="(• _ • )", command=toggle_visibility, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn4.place(x=508, y=970)






def toggle_visibility():
    if MotPass.cget('show') == '':
        MotPass.config(show='*')
        toggle_btn3.config(fg= 'green', text='voir')
    else:
        MotPass.config(show='')
        toggle_btn3.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if MotPass.get() == "Mot de passe":
        messagebox.showinfo("Alerte", "Assurez-vous de taper 7 caractères ")
        MotPass.delete(0, tk.END)
        MotPass.config( fg="gray", show="*")  # Afficher les caractères masqués après clic



MotPass.insert(0,  "Mot de passe")  

#Bind des événements
MotPass.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)




# button qui commande la fonction "toggle_visibility"
toggle_btn3 = tk.Button(page_compte, text="(• _ • )", command=toggle_visibility, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn3.place(x=508, y=823)






#fonction qui permet de voir le contenu de notre placeholder en caractères visibles (lettres, nombres, symboles.......) et invisible ( caractères d'un mot de passe "*****"")


def toggle_visibility():
    if prenom.cget('show') == '':
        prenom.config(show='')
   
    else:
        prenom.config(show='')
        

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if prenom.get() == "Entrer votre Prénom":
        prenom.delete(0, tk.END)
        prenom.config( fg="orange", show="")  # Afficher les caractères masqués après clic






prenom.insert(0,  "Entrer votre Prénom")  

#Bind des événements
prenom.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)
















#fonction qui permet de voir le contenu de notre placeholder en caractères visibles (lettres, nombres, symboles.......) et invisible ( caractères d'un mot de passe "*****"")


def toggle_visibility():
    if nom.cget('show') == '':
        prenom.config(show='')
   
    else:
        nom.config(show='')
        

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if nom.get() == "Entrer votre nom":
        nom.delete(0, tk.END)
        nom.config( fg="orange", show="")  # Afficher les caractères masqués après clic






nom.insert(0,  "Entrer votre nom")  

#Bind des événements
nom.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)






























N1 = tk.Button(page_compte, text="Annuler", font=" ExtraCondensed 9",bd=0, relief="groove", fg="#CE8000", bg="gray86", activebackground="gray90", highlightthickness=-1, command=lambda: afficher_page(page_accueil))
N1.place(x=10, y= 1420)


















# Button sur la  page_accueil qui enverra vers la nav faculté -------------------__________-------------------













































    
    

#------------ la 2eme fenêtre Geo -------------#

 #---------- Page d'inscription ----------
page_inscription = tk.Frame(app, bg="white")
page_inscription.grid(row=0, column=0, sticky="nsew")

   

#lbl_inscription = tk.Label(page_inscription, text="Formulaire d'inscription", font=("Arial", 16))
#lbl_inscription.pack(pady=20)

#frame au top sur la 2eme fenêtre 
topFrame2 = tk.Frame(page_inscription, bg=COLORS ["green_dark"], relief="solid")
topFrame2.pack(side="top", fill = tk.X)


   

#Text UENUZ sur topFrame2 de la 2eme fenêtre 
accueilText1 = tk.Label(topFrame2,  text="FLSH", font=" ExtraCondensed 13", bg=COLORS["green_dark" ], fg=COLORS ["orange_dark"], height=2,  padx=160)
accueilText1.pack()






#Text Veuillez........sur la 2eme fenêtre 
#accueilText = tk.Label(page_inscription, text="Bienvenue \nFLSH", font=" ExtraCondensed 10", bg="white", fg="gray60",  height=2,  pady=2, relief="ridge")
#accueilText.place(x=150, y= 250)



#bannerText = tk.Label(page_inscription, text="UAS", font=" ExtraCondensed 20", fg="gray90", bg="white", relief="flat")
#bannerText.place(x=290, y= 148)


canvas2 = tk.Canvas(page_inscription, width=396, height=430, bg="white", highlightthickness=0)
canvas2.place(x=340, y=135)

# Exemple : texte incliné de 45°
canvas2.create_text(200, 315, text="..........................................", angle=133, fill=COLORS ["green_dark"], font=("ExtraCondensed", 13), tags="rotated")





canvas = tk.Canvas(page_inscription, width=300, height=430, bg="white", highlightthickness=0)
canvas.place(x=60, y=132)

# Exemple : texte incliné de 45°
canvas.create_text(200, 200, text="..........................................", angle=50, fill=COLORS ["green_dark"], font=("ExtraCondensed", 13), tags="rotated")



# canvas ⬇️
canvas = tk.Canvas(page_inscription, width=600, height=250, bg="gray70",bd=4, relief="sunken", highlightthickness=4, highlightbackground="green")
canvas.place(x=60, y=500)



# photo uas sur page_inscription

navnaFacon = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (1).png')



tk.Button(page_inscription, image=navnaFacon, bg="gray100", width= 630, height=110, bd=0, activebackground="gray100", highlightthickness=-2).place(x=42, y=130)





# canvas ⬇️
canvas = tk.Canvas(page_inscription, width=620, height=100, bg=COLORS ["orange_dark"], bd=5, relief="sunken")
canvas.place(x=35, y=1150)

# photo uas sur page_inscription




bannerText = tk.Label(page_inscription, text="Vos département :", font=" ExtraCondensed 10", fg=COLORS ["orange_dark"], bg="white", bd=0, relief="groove")
bannerText.place(x=35, y= 1100)
'''
navnaDacon = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (1).png')



tk.Button(page_inscription, image=navnaDacon, bg="gray99", width= 250, height=120, bd=0, activebackground="gray100", highlightthickness=-2).place(x=225, y=840)
'''




'''
'''



#Text Login sur la 2eme fenêtre 
'''
bannerText = tk.Label(page_inscription, text="Login....", font=" ExtraCondensed 8", fg="gray55", bg="white", relief="groove")
bannerText.place(x=50, y= 490)       
'''



'''
navOcon = PhotoImage(file='ada.png')

tk.Button(page_inscription, image=navOcon, bg="gray100", width= 750, height=150, activebackground="white", bd=0, highlightthickness=-0).place(x=50, y=396)

canvas = tk.Canvas(page_inscription, width=100, height=130, bg="white", highlightthickness=0)
canvas.place(x=57, y=450)

# Exemple : texte incliné de 45°
canvas.create_text(50, 50, text="Login....", angle=30, fill="black", font=("ExtraCondensed", 8), tags="rotated")

def open_polit():
    webbrowser.open("https://www.google.com")
#button politique de........sur la 2eme fenêtre 
butter = tk.Button(page_inscription, text="Politique de confidentialité ", font=" ExtraCondensed 7",bd=0, fg="sky blue", bg="white", highlightthickness=-2, command=open_polit)
butter.place(x=20, y= 740)



'''






































    


         



















































#fenetre pour la récupération de la carte 
page_RCarte = tk.Frame(app, bg="gray100")
page_RCarte.grid(row=0, column=0, sticky="nsew", rowspan=20)

    
    

    
'''


ImgFond = PhotoImage(file= 'Screenshot_2022-12-16-06-22-38.png')

can = Canvas(page_RCarte, width= 800, height= 1000)
can.create_image(0, -325, anchor=NW, image=ImgFond)
can.pack()


'''

#photo de uas sur page_Rcarte
navRCcon = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (3).png')



tk.Button(page_RCarte, image=navRCcon, bg="gray100", width= 250, height=260, bd=-2, activebackground="gray100", highlightthickness=-2).place(x=245, y=435)





#canvas sur la fenêtre "page_RCarte"
canvas = tk.Canvas(page_RCarte, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=4, relief='groove', width=750, height=500)
canvas.place(x=-5, y=710)


#canvas sur la fenêtre "page_RCarte"
canvas = tk.Canvas(page_RCarte, borderwidth=1, bg="gray68", highlightthickness=4, relief='groove', width=450, height=120)
canvas.place(x=265, y=1260)









# text 

bannerText = tk.Label(page_RCarte, text="Entrer votre N° de Carte :", font=" ExtraCondensed 9", fg="white", bg=COLORS ["green_dark"], relief="flat")
bannerText.place(x=190, y= 728)

# text 

bannerTe = tk.Label(page_RCarte, text="Bienvenue.\n Ici vous pouvez Visualiser et Archiver votre Carte.", font=" ExtraCondensed 5", fg="white", bg="gray68", relief="flat")
bannerTe.place(x=290, y= 1288)





#placeholder sur la page_RCarte
RR = tk.Entry(page_RCarte, placeholder="N° de Carte", highlightthickness = 8, bg="gray100", fg="gray70", font="ExtraCondensed 18", bd=8, width=16, relief="solid")
RR.place(x=40, y=790)









#Checkbox sur la page_RCarte
check = tk.Checkbutton(page_RCarte, text="Confirmer ", bg=COLORS["green_dark"], fg=COLORS ["orange_dark"], font="ExtraCondensed 10", activebackground="orange", width=12, height=1)
check.place(x=40, y=915)



#ImgFono = PhotoImage(file= 'Screenshot_2022-12-16-06-22-38.png', height=750)





ba = tk.Label(page_RCarte, height=100, fg="white", bg="green")
ba.pack()


navSCcon = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (3).png')


def afficher_text_entrer():
    
    
    
    ba.config(text=f"       Bonjour  !\n Scolarité centrale vous souhaite  la bienvenue\n\n Votre N° de carte est *******\nNom : Daouda Sani Fari Abdoul Malik {RR.get()} 1830-22" , bg="green", fg="white", height=45, width=39)
    #ba.config(image=navSCcon, width=609, height=1205)
    #ba.place(x=-5, y=-220)
    



btn_C = tk.Button(
    page_RCarte,
    text="Connectez", activebackground=COLORS["green_dark"], padx=150, pady=30, bd=5, relief="solid",
    command=afficher_text_entrer, 
    bg="white", fg="green", font=("Arial", 6)
)
btn_C.place(x=150, y=1020)





bottom_frameS = tk.Frame(page_RCarte, bg=COLORS["green_dark"], relief="solid", bd=0)
bottom_frameS.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frameS,
         text="© 2026 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vides



# Label j'ai perdu ma Carte

    
N = tk.Button(page_inscription, text="J'ai perdu ma Carte ?", font=" ExtraCondensed 8",bd=0, relief="ridge", fg="red", bg="white", highlightthickness=-1, command=lambda: afficher_page(page_RCarte))
N.place(x=380, y= 920)




# Les canvas de "j'ai perdu ma Carte"




canvas2 = tk.Canvas(page_inscription, width=106, height=158, bg="white", highlightthickness=0)
canvas2.place(x=432, y=993)

# Exemple : texte incliné de 45°
canvas2.create_text(200, 215, text="||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||", angle=135, fill=COLORS["orange_dark"], font=("ExtraCondensed", 13), tags="rotated")




canvas2 = tk.Canvas(page_inscription, width=106, height=158, bg="white", highlightthickness=0)
canvas2.place(x=550, y=990)

# Exemple : texte incliné de 45°
canvas2.create_text(35, 80, text="||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||", angle=47, fill=COLORS["orange_dark"], font=("ExtraCondensed", 13), tags="rotated")









N2 = tk.Button(page_RCarte, text="⬅", font=" ExtraCondensed 17",bd=8, relief="groove", fg="gray30", bg="orange", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_inscription))
N2.place(x=0, y= 1270)


'''
 
#Text Direction de la........sur la 2eme fenêtre 
bannerText = tk.Label(page_inscription, text="DIRECTION DE LA SCOLARITÉ CENTRALE", font=" ExtraCondensed 10", fg="green", bg="white", relief="solid")
bannerText.place(x=10, y= 1350)

'''
'''
# --- Cadre du bas (Bottom Frame) ---j
#sur la 2eme fenêtre ---------_----------
bottom_frame = tk.Frame(page_inscription, bg=COLORS["green_dark"])
bottom_frame.pack(side="bottom", fill=tk.X)



tk.Label(bottom_frame,
         text="© 2026 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vides

'''















# les canvas en bas de la page inscription 
canva = tk.Canvas(page_inscription, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=0, bd =9, relief='sunken', width=610, height=100)
canva.place(x=35, y=1423)


canvas = tk.Canvas(page_inscription, borderwidth=4, bg="gray100", highlightthickness=0, relief='sunken', width=500, height=160)
canvas.place(x=95, y=1260)


#text









'''
#placeholder sur la page_inscription     
NCarte = tk.Entry(page_inscription, highlightthickness=8, bg="gray100", fg="gray30", bd= 8, font="ExtraCondensed 18", width=16, relief="solid")
NCarte.place(x=50, y=550)












#fonction qui permet de voir le contenu de notre placeholder en caractères visibles (lettres, nombres, symboles.......) et invisible ( caractères d'un mot de passe "*****"")


def toggle_visibility():
    if NCarte.cget('show') == '':
        NCarte.config(show='*')
        toggle_btn.config(fg= 'green', text='voir')
    else:
        NCarte.config(show='')
        toggle_btn.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if NCarte.get() == "N° de Carte":
        messagebox.showinfo("Alerte", "Assurez-vous de taper 7 caractères ")
        NCarte.delete(0, tk.END)
        NCarte.config( fg="gray", show="*")  # Afficher les caractères masqués après clic

def add_placeholder(event):
    if not NCarte.get():
        NCarte.config(fg="gray", show="")  # Enlever le masquage pour afficher le texte gris
        NCarte.insert(0, "N° de Carte")
        
        





NCarte.insert(0,  "N° de Carte")  

#Bind des événements
NCarte.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)



def mes_infos():
    
    
    dict = { "1830-22" : "Daouda Sani Fari", "1830-20" : "fati"}
    num = NCarte.get()
   
    if not num.strip():
       
       
           
           messagebox.showwarning("Échec de connexion", " Le N° de Carte n'est pas renseigné.")
           return
           
    
    
    if num == "1830-22" in dict:
                
                
              
              
              
              
              
         showinfo("Connexion réussi", "Bienvenue à la Scolarité Central.")
 #   elif num == NCarte:
     #      showerror("Échec de connexion", "Veuillez entrer votre N° de Carte pour vous connecter.")
      
     
    else:
         showerror(" Échec de connexion !", "     N° de carte incorrect....(×××××××). \n                  Veuillez insérer un\nN° de Carte valide pour vous connecter.")
    if len(num) == 7:
                showinfo("Connexion réussi","N° de Carte validé ")                
    elif len(num) >6:            
             showerror("Valeur Trop Grande ","            Le N° de Carte (×××××××) \n ne peut pas dépasser 7 caractères. \n           \n                  (×××××××)")
    else:
            showerror("Alerte !!!", "  Le N° de Carte doit atteindre 7 caractères")
    
           

          
        
           
           
       
# button qui commande la fonction "toggle_visibility"
toggle_btn = tk.Button(page_inscription, text="(• _ • )", command=toggle_visibility, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn.place(x=510, y=575)



#Checkbox sur la 2eme fenêtre 
check = tk.Checkbutton(page_inscription, text="Confirmer ", bg="white", fg="gray0", font="ExtraCondensed 10", activebackground="white", width=12, height=1)
check.place(x=50, y=680)
            
#Button Connexion sur la 2eme fenêtre             
button1 = tk.Button(page_inscription, text="Connexion", bg="#CE8000", fg="white", bd=5,  activebackground=COLORS ["orange_dark"],font=("Arial", 8), relief="solid", command= mes_infos)
button1.place(x=255, y=820)

'''





#Button d'inscription en ligne uas'
def inscription():
    webbrowser.open("http://postbac.uas.edu.ne")
    
navTcon = PhotoImage(file='Minduka_Present_Blue_pack.png')
tk.Button(page_inscription, image=navTcon, bg="white", width= 120, height=114, bd=0, activebackground="white", highlightthickness=-0).place(x=100, y=900)
#
button5 = tk.Button(page_inscription, text="Inscription",bg="#2980b9", fg="white", highlightthickness=6, padx=10, bd=5, font= ("Arial", 9), command= inscription)
button5.place(x=80, y=650)

#Button Exit

#btn_Exit = tk.Button(page_inscription, text="  Quitter   ", command=app.quit, bg="#e74c3c", fg="white", padx=10, bd=5)
#btn_Exit.place(x=540, y=1180)
# text retour sur le top Frame de la page d'accueil
'''
rt = tk.Label(page_inscription, text="Retour", bg=COLORS["orange_dark"], fg="gray70", font="ExtraCondensed 10", bd=0, highlightthickness=-1).place(x=125, y=40)
'''

Btn_R_P_P = tk.Button(page_inscription, text="⬅",bg=COLORS ["green_dark"], fg="white", activebackground=COLORS["green_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 14", command=lambda: afficher_page(page_accueil))
Btn_R_P_P.place(x=2, y=20)














#------------------3eme fenêtre----------------------
#frame de Réclamation 

page_inscrip= tk.Frame(app, bg="gray10")
page_inscrip.grid(row=0, column=0, sticky="nsew")

#button de réclamation qui enverra vers la 3eme fenêtre "page_inscrip"

recla= tk.Button(page_inscription, highlightthickness=6, text="Réclamation", command=lambda: afficher_page(page_inscrip), bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"],fg="white" , font=("Arial", 9)).place(x=380, y= 650)



























#-------++++4eme frame de "réclamation de ma note" où de Traitement de la réclamation 


page_Tmt= tk.Frame(app, bg="gray68")
page_Tmt.grid(row=0, column=0, sticky="nsew")




topFrame_p_Tmt  = tk.Frame(page_Tmt, bg=COLORS ["green_dark"], relief="raised", bd=0, height=80)
topFrame_p_Tmt.pack(side="top", fill = tk.X)


accueilTextRN = tk.Label(page_Tmt, text="Réclamation de ma note", font="ExtraCondensed 10", bg=COLORS["green_dark"], fg="white")
accueilTextRN.place(x=170, y=15)





bottom_frame2 = tk.Frame(page_Tmt, bg=COLORS["green_dark"], relief="sunken")
bottom_frame2.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame2,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vides


#button de retour à la page "page inscription"


frm_P_inscrip = tk.Button(page_inscrip, text="⬅",bg="gray10", fg=COLORS["orange_dark"], activebackground=COLORS["green_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 15", command=lambda: afficher_page(page_inscription))
frm_P_inscrip.place(x=5, y=40)


#Button de réclamation de mon nom ------------------



btnR= tk.Button(page_inscrip, text="RÉCLAMATION DE MA NOTE", bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"], fg="white"
, font="ExtraCondensed 9", command=lambda: afficher_page(page_Tmt))
btnR.place(x=20, y= 240)    











 # canvasC sur la page_Tmt Carte du Niger 
canvasC = tk.Canvas(page_Tmt, borderwidth=2, bg="orange", highlightthickness=0, width=40, height=5)
canvasC.place(x=655, y=1317)      

 # canvasC sur la page_Tmt
canvasC = tk.Canvas(page_Tmt, borderwidth=2, bg="white", highlightthickness=0, width=40, height=5)
canvasC.place(x=655, y=1325)

 # canvasC sur la page_Tmt
canvasC = tk.Canvas(page_Tmt, borderwidth=2, bg="orange", highlightthickness=0, width=2, height=1)
canvasC.place(x=675, y=1327)       
              
                            
                  
 # canvasC sur la page_Tmt
canvasC = tk.Canvas(page_Tmt, borderwidth=2, bg="green", highlightthickness=0, width=40, height=5)
canvasC.place(x=655, y=1335)           

                         
                                                  
                                                                           
                                                                                                    
                                                                                                                             
                                                                                                                                                                               
   
# canvasC sur la page_Tmt Les deux 
canvasC = tk.Canvas(page_Tmt, borderwidth=5, bg="gray95", highlightthickness=1, relief='sunken', width=30, height=150)
canvasC.place(x=30, y=1390)              
  
                                                                                            
# canvasC sur la page_Tmt Les deux 
canvasC = tk.Canvas(page_Tmt, borderwidth=5, bg="gray95", highlightthickness=1, relief='sunken', width=30, height=150)
canvasC.place(x=655, y=1390)                                    
                                                                                            
                                                                              
   #le Grand canvas                                                                       
                                                                                       
                                                                                                   
                                                                                                               
                                                                                                                           
                                                                                                                                       
                                                                                                                                                   
                                                                                                                                                                           
    
 # grand canvasC sur la page_Tmt
canvasC = tk.Canvas(page_Tmt, borderwidth=12, bg="gray68", highlightthickness=1, relief='sunken', width=668, height=900)
canvasC.place(x=15, y=370)




'''

bannerText = tk.Label(page_Tmt,  text="Assurez-vous de bien remplir \n tous les cases.", font=" ExtraCondensed 12", bg="gray68", fg="white", bd=0, highlightthickness=-1, height=2,  pady=2)
bannerText.place(x=75, y= 150)
'''

UE = tk.Entry(page_Tmt, placeholder = "               UE ", bg="white", fg="gray0", highlightthickness=18, font="ExtraCondensed 18" , bd=8, width=16, relief="solid").place(x=30, y=410)


Num= tk.Entry(page_Tmt, placeholder = "          CODE UE ", bg="white", fg="gray0", highlightthickness=18,font="ExtraCondensed 18" , bd=8, width=16, relief="solid").place(x=30, y=550)


CHARGER = tk.Entry(page_Tmt, placeholder = "     ENSEIGNANT", bg="white", fg="gray0", highlightthickness=18,font="ExtraCondensed 18" , bd=8, width=16, relief="solid").place(x=30, y=690)

NumCt = tk.Entry(page_Tmt, placeholder = "    N° de Carte ", bg="white", fg="gray0", highlightthickness=18,font="ExtraCondensed 18" , show="*", bd=8, width=16, relief="solid").place(x=30, y=830)

checkB = tk.Checkbutton(page_Tmt, bg="gray69", fg="gray100",highlightthickness=-1,  bd=0, font="ExtraCondensed 9", activebackground="white", height=1)
checkB.place(x=30, y=980)

conTr= tk.Label(page_Tmt, font="ExtraCondensed 8",bg ="gray69", fg="gray100", text="J'ai lu et j'accepte les termes et conditions \nde confidentialité.").place(x=80, y=980)


Tr= tk.Label(page_Tmt, font="ExtraCondensed 9",bg ="gray69", fg=COLORS ["green_dark"], text="les termes et conditions").place(x=324, y=975)

def envoyer():
      
     
      
       if not all([UE, Num, CHARGER, NumCt, checkB]) or not confirm:
            messagebox.showwarning("Attention", "\nTous les champs sont obligatoires  \n            et confirmation requise.")
            return
            
            

                
btn_TN = tk.Button(
    page_Tmt,
    text="Connexion", activebackground=COLORS["green_dark"], padx=150, pady=30, bd=5, command=envoyer, relief="raised", 
    bg="white", fg="green", font=("Arial", 6)
)
btn_TN.place(x=150, y=1100)

'''
btnSmtr = tk.Button(page_Tmt, text="Soumettre", font= "ExtraCondensed 15", bg="green", fg="white", bd=9,highlightthickness=0, width=10, command=envoyer)
btnSmtr.place(x=150, y=1000)
'''


frmBtnRecla = tk.Button(page_Tmt, text="⬅",bg=COLORS ["green_dark"], fg="white", activebackground=COLORS ["green_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 13", command=lambda: afficher_page(page_inscrip))
frmBtnRecla.place(x=5, y=-2)













#5eme frame du button "réclamation de mon nom" où de traitement de mon nom


page_TN= tk.Frame(app, bg="gray68")
page_TN.grid(row=0, column=0, sticky="nsew")    
    


btnRN= tk.Button(page_inscrip, text="RÉCLAMATION DE MON NOM", bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"], fg="white"
, font="ExtraCondensed 9", command=lambda: afficher_page(page_TN))
btnRN.place(x=20, y= 350)    
 
frameTN = tk.Frame(page_TN, bg="#FFFFFF", relief="solid", bd=1, height=3)
frameTN.pack(side="top", fill = tk.X)



# Text sur le frame si-haut)
accueilTextTN = tk.Label(frameTN, text="Étudiant", font="ExtraCondensed 25", bg="gray100", fg="gray50")
accueilTextTN.pack(side="right")


 # canvasC sur la page_TN
canvasC = tk.Canvas(page_TN, borderwidth=12, bg="gray69", highlightthickness=1,  relief='raised', width=669, height=900)
canvasC.place(x=15, y=397)








  
#text sur le top Frame
'''
accueilTextRN = tk.Label(frameTN, text="Réclamation de mon nom", font="ExtraCondensed 10", bg="#AC9000", fg="white")
accueilTextRN.place(x=130, y=45)

'''

bottom_frame1 = tk.Frame(page_TN, bg=COLORS["green_dark"], relief="solid", bd=0)
bottom_frame1.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame1,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vides



UE1 = tk.Entry(page_TN, placeholder = "               UE ", bg="white", fg="gray0", highlightthickness=18,font="ExtraCondensed 18" , bd=8, width=16, relief="solid").place(x=30, y=410)


Num1= tk.Entry(page_TN, placeholder = "          CODE UE ", bg="white", fg="gray0", highlightthickness=18,font="ExtraCondensed 18" , bd=8, width=16, relief="solid").place(x=30, y=550)


CHARGER1 = tk.Entry(page_TN, placeholder = "     ENSEIGNANT", bg="white", fg="gray0", highlightthickness=18,font="ExtraCondensed 18" , bd=8, width=16, relief="solid").place(x=30, y=690)

NumCt1 = tk.Entry(page_TN, placeholder = "    N° de Carte ", bg="white", fg="gray0", highlightthickness=18,font="ExtraCondensed 18" , show="*", bd=8, width=16, relief="solid").place(x=30, y=830)

checkB1 = tk.Checkbutton(page_TN, bg="gray69", fg="gray0",highlightthickness=-1,  bd=0, font="ExtraCondensed 10", activebackground="white", height=1)
checkB1.place(x=30, y=980)

conTr1= tk.Label(page_TN, font="ExtraCondensed 8",bg ="gray69", fg="gray100", text="J'ai lu et j'accepte les termes et conditions \nde confidentialité.").place(x=80, y=980)

Tr1= tk.Label(page_TN, font="ExtraCondensed 9",bg ="gray69", fg=COLORS ["green_dark"], text="les termes et conditions").place(x=325, y=975)
'''
btnSmtr1 = tk.Button(page_TN, text="Soumettre", font= "ExtraCondensed 15", bg="green", fg="white", bd=9,highlightthickness=0, width=10)
btnSmtr1.place(x=160, y=1050)
'''
btn_TN = tk.Button(
    page_TN,
    text="Connexion", activebackground=COLORS["green_dark"], padx=150, pady=30, bd=5, relief="sunken", 
    bg="white", fg="green", font=("Arial", 6)
)
btn_TN.place(x=160, y=1100)




#button de retour sur la "page_inscrip" qui nous renvoye à la fenêtre "page_inscription"

retour_Recla= tk.Button(
    page_TN, highlightthickness=-1,
   text="⬅",
    command=lambda: afficher_page(page_inscrip),
    bg="gray100", bd=0, activebackground="#AC9000", fg="gray50"
, font="ExtraCondensed 14")
retour_Recla.place(x=10, y= 30)



#__________---limite des éléments sur la page inscription 




















































#------------ les fenêtre -------------#

 #---------- Page department de Geo----------
page_Geo = tk.Frame(app, bg="white")
page_Geo.grid(row=0, column=0, sticky="nsew")

#btn 
 
btn_G = tk.Button(page_inscription, text="     ", font=" ExtraCondensed 13",bd=5, relief="sunken", fg="white", bg="#4CAF50", highlightthickness=-1, activebackground="#CE8000", command=lambda: afficher_page(page_Geo))
btn_G.place(x=95, y= 1380)


topFrame2 = tk.Frame(page_Geo, bg=COLORS ["green_dark"], relief="solid")
topFrame2.pack(side="top", fill = tk.X)


   
#Text UENUZ sur topFrame2 de la 2eme fenêtre 
accueilText1 = tk.Label(topFrame2,  text="Géographie", font=" ExtraCondensed 13", bg=COLORS["green_dark" ], fg=COLORS ["orange_dark"], height=2,  padx=160)
accueilText1.pack()


#Text Veuillez........sur la 2eme fenêtre 
accueilText = tk.Label(page_Geo, text="Veillez Renseigner votre \n N° de Carte", font=" ExtraCondensed 10", bg="white", fg="gray60",  height=2,  pady=2, relief="ridge")
accueilText.place(x=150, y= 250)



bannerText = tk.Label(page_Geo, text="FLSH", font=" ExtraCondensed 20", fg="gray90", bg="white", relief="flat")
bannerText.place(x=290, y= 148)


#photo

navOcon3 = PhotoImage(file='ada.png')

tk.Button(page_Geo, image=navOcon3, bg="gray100", width= 750, height=150, activebackground="white", bd=0, highlightthickness=-0).place(x=50, y=396)

canvas = tk.Canvas(page_Geo, width=100, height=130, bg="white", highlightthickness=0)
canvas.place(x=57, y=465)

# Exemple : texte incliné de 45°
canvas.create_text(50, 50, text="Login....", angle=0, fill="black", font=("ExtraCondensed", 8), tags="rotated")

def open_polit():
    webbrowser.open("https://www.google.com")
#button politique de........sur la 2eme fenêtre 
butter1 = tk.Button(page_Geo, text="Politique de confidentialité ", font=" ExtraCondensed 7",bd=0, fg="sky blue", bg="white", highlightthickness=-2, command=open_polit)
butter1.place(x=20, y= 740)



#---------- Page de récupération de carte----------
page_RC = tk.Frame(app, bg="white")
page_RC.grid(row=0, column=0, sticky="nsew")

# button j'ai perdu ma carte 
    
N1 = tk.Button(page_Geo, text=" J'ai Perdu ma Carte ? ", font=" ExtraCondensed 7",bd=0, relief="ridge", fg="red", bg="white", highlightthickness=-1, command=lambda: afficher_page(page_RC))
N1.place(x=400, y= 670)

# button de retour 
N3 = tk.Button(page_RC, text="⬅", font=" ExtraCondensed 15",bd=0, relief="groove", fg="gray30", bg="white", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_Geo))
N3.place(x=20, y= 40)


#placeholder sur la page_inscription     
NCarte1 = tk.Entry(page_Geo, highlightthickness=8, bg="gray100", fg="gray30", bd= 8, font="ExtraCondensed 18", width=16, relief="solid")
NCarte1.place(x=50, y=550)





def toggle_visibility():
    if NCarte1.cget('show') == '':
        NCarte1.config(show='*')
        toggle_btn1.config(fg= 'green', text='voir')
    else:
        NCarte1.config(show='')
        toggle_btn1.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if NCarte1.get() == "N° de Carte":
        messagebox.showinfo("Alerte", "Assurez-vous de taper 7 caractères ")
        NCarte1.delete(0, tk.END)
        NCarte1.config( fg="gray", show="*")  # Afficher les caractères masqués après clic
'''
def add_placeholder(event):
    if not NCarte.get():
        NCarte.config(fg="gray", show="")  # Enlever le masquage pour afficher le texte gris
        NCarte.insert(0, "N° de Carte")
        
        '''      





NCarte1.insert(0,  "N° de Carte")  

#Bind des événements
NCarte1.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)



def mes_infos1():
    
    
    dict1 = { "1830-22" : "Daouda Sani Fari", "1830-20" : "fati"}
    num1 = NCarte1.get()
   
    if not num1.strip():
       
       
           
           messagebox.showwarning("Échec de connexion", " Le N° de Carte n'est pas renseigné.")
           return
           
    
    
    if num1 == "1830-22" in dict1:
                
                
                
              
              
              
              
              
         showinfo("Connexion réussi", "Bienvenue à la Scolarité Central.")
 #   elif num == NCarte:
     #      showerror("Échec de connexion", "Veuillez entrer votre N° de Carte pour vous connecter.")
      
     
    else:
         showerror(" Échec de connexion !", "     N° de carte incorrect....(×××××××). \n                  Veuillez insérer un\nN° de Carte valide pour vous connecter.")
    if len(num1) == 7:
                showinfo("Connexion réussi","N° de Carte validé ")                
    elif len(num1) >6:            
             showerror("Valeur Trop Grande ","            Le N° de Carte (×××××××) \n ne peut pas dépasser 7 caractères. \n           \n                  (×××××××)")
    else:
            showerror("Alerte !!!", "  Le N° de Carte doit atteindre 7 caractères")
    
           

          
        
           
           
       
# button qui commande la fonction "toggle_visibility"
toggle_btn1 = tk.Button(page_Geo, text="(• _ • )", command=toggle_visibility, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn1.place(x=510, y=575)



#Checkbox sur la 2eme fenêtre 
check1 = tk.Checkbutton(page_Geo, text="Confirmer ", bg="white", fg="gray0", font="ExtraCondensed 10", activebackground="white", width=12, height=1)
check1.place(x=50, y=680)
            
#Button Connexion sur la 2eme fenêtre             
button6 = tk.Button(page_Geo, text="Connexion", bg=COLORS["orange_dark"], fg="white", bd=5,  activebackground=COLORS ["orange_dark"],font=("Arial", 8), relief="solid", command=mes_infos1)
button6.place(x=255, y=820)

#Button d'inscription en ligne uas'
def inscription1():
    webbrowser.open("http://postbac.uas.edu.ne")
    
navTcon1 = PhotoImage(file='Minduka_Present_Blue_pack.png')
tk.Button(page_Geo, image=navTcon1, bg="gray100", width= 120, height=114, bd=0, activebackground="gray100", highlightthickness=-0).place(x=560, y=1110)
#
button5 = tk.Button(page_Geo, text="Inscription",bg="#2980b9", fg="white", highlightthickness=-1, padx=10, bd=5, font= ("Arial", 9), command= inscription1)
button5.place(x=20, y=1170)

#Button Exit

btn_Exit = tk.Button(page_Geo, text="  Quitter   ", command=app.quit, bg="#e74c3c", fg="white", padx=10, bd=5)
btn_Exit.place(x=540, y=1260)
# text retour sur le top Frame de la page d'accueil
'''
rt = tk.Label(page_inscription, text="Retour", bg=COLORS["orange_dark"], fg="gray70", font="ExtraCondensed 10", bd=0, highlightthickness=-1).place(x=125, y=40)
'''

Btn_1= tk.Button(page_Geo, text="⬅",bg=COLORS ["green_dark"], fg="white", activebackground=COLORS["orange_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 14", command=lambda: afficher_page(page_inscription))
Btn_1.place(x=2, y=20)



#------------------3eme fenêtre----------------------
#frame de Réclamation "page_Geo'

page_Rcla= tk.Frame(app, bg="gray10")
page_Rcla.grid(row=0, column=0, sticky="nsew")

#button de réclamation qui enverra vers la 3eme fenêtre "page_inscrip"

recla_Geo = tk.Button(page_Geo, highlightthickness=-1,text="Réclamation", command=lambda: afficher_page(page_Rcla), bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"],fg="white" , font=("Arial", 8)).place(x=20, y= 1260)


#Text Direction de la........sur la 2eme fenêtre 
bannerText_G = tk.Label(page_Geo, text="DIRECTION DE LA SCOLARITÉ CENTRALE", font=" ExtraCondensed 10", fg="green", bg="white", relief="solid")
bannerText_G.place(x=10, y= 1350)



bottom_frame_Geo = tk.Frame(page_Geo, bg=COLORS["green_dark"], relief="solid", bd=0)
bottom_frame_Geo.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame_Geo,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vide
         # label geo 
bannerText = tk.Label(page_inscription, text="Géo", font=" ExtraCondensed 6", fg="white", bg="#4CAF50")
bannerText.place(x=136, y= 1430)
         
         
         


#________---limite PageGeo---_______________




















































#------------ les fenêtre -------------#

 #---------- Page department de Histoire----------
page_His = tk.Frame(app, bg="white")
page_His.grid(row=0, column=0, sticky="nsew")

#btn 
 
btn_H = tk.Button(page_inscription, text="     ", font=" ExtraCondensed 13",bd=5, relief="sunken", fg="white", bg="#4CAF50", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_His))
btn_H.place(x=190, y= 1310)


topFrame_H= tk.Frame(page_His, bg=COLORS ["green_dark"], relief="solid")
topFrame_H.pack(side="top", fill = tk.X)


   
#Text UENUZ sur topFrame2 de la 2eme fenêtre 
accueilText_H = tk.Label(topFrame_H,  text="Histoire", font=" ExtraCondensed 13", bg=COLORS["green_dark" ], fg=COLORS ["orange_dark"], height=2,  padx=160)
accueilText_H.pack()


#Text Veuillez........sur la 2eme fenêtre 
accueilText_H1 = tk.Label(page_His, text="Veillez Renseigner votre \n N° de Carte", font=" ExtraCondensed 10", bg="white", fg="gray60",  height=2,  pady=2, relief="ridge")
accueilText_H1.place(x=150, y= 250)



bannerText_H = tk.Label(page_His, text="FLSH", font=" ExtraCondensed 20", fg="gray90", bg="white", relief="flat")
bannerText_H.place(x=270, y= 148)


#photo

navOcon_H = PhotoImage(file='ada.png')

tk.Button(page_His, image=navOcon_H, bg="gray100", width= 750, height=150, activebackground="white", bd=0, highlightthickness=-0).place(x=50, y=396)

canvas = tk.Canvas(page_His, width=100, height=130, bg="white", highlightthickness=0)
canvas.place(x=57, y=465)

# Exemple : texte incliné de 45°
canvas.create_text(50, 50, text="Login....", angle=0, fill="black", font=("ExtraCondensed", 8), tags="rotated")

def open_polit():
    webbrowser.open("https://www.google.com")
#button politique de........sur la 2eme fenêtre 
butter_H = tk.Button(page_His, text="Politique de confidentialité ", font=" ExtraCondensed 7",bd=0, fg="sky blue", bg="white", highlightthickness=-2, command=open_polit)
butter_H.place(x=20, y= 740)



#---------- Page de récupération de carte Histoire----------
page_HR = tk.Frame(app, bg="white")
page_HR.grid(row=0, column=0, sticky="nsew")

# button j'ai perdu ma carte 
    
N_H= tk.Button(page_His, text=" J'ai Perdu ma Carte ? ", font=" ExtraCondensed 7",bd=0, relief="ridge", fg="red", bg="white", highlightthickness=-1, command=lambda: afficher_page(page_HR))
N_H.place(x=400, y= 670)

# button de retour 
N_H1 = tk.Button(page_HR, text="⬅", font=" ExtraCondensed 15",bd=0, relief="groove", fg="gray30", bg="white", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_His))
N_H1.place(x=20, y= 40)


#placeholder sur la page_inscription     
NCarte_H = tk.Entry(page_His, highlightthickness=8, bg="gray100", fg="gray30", bd= 8, font="ExtraCondensed 18", width=16, relief="solid")
NCarte_H.place(x=50, y=550)


#_______-----_______________-------_________

def toggle_visibility():
    if NCarte_H.cget('show') == '':
        NCarte_H.config(show='*')
        toggle_btn_H.config(fg= 'green', text='voir')
    else:
        NCarte_H.config(show='')
        toggle_btn_H.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if NCarte_H.get() == "N° de Carte":
        messagebox.showinfo("Alerte", "Assurez-vous de taper 7 caractères ")
        NCarte_H.delete(0, tk.END)
        NCarte_H.config( fg="gray", show="*")  # Afficher les caractères masqués après clic






NCarte_H.insert(0,  "N° de Carte")  

#Bind des événements
NCarte_H.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)



def mes_infos2():
    
    
    dict2 = { "1830-22" : "Daouda Sani Fari", "1830-20" : "fati"}
    num2 = NCarte1.get()
   
    if not num2.strip():
       
       
           
           messagebox.showwarning("Échec de connexion", " Le N° de Carte n'est pas renseigné.")
           return
           
    
    
    if num2 == "1830-22" in dict2:
                
                
                
              
              
              
              
              
         showinfo("Connexion réussi", "Bienvenue à la Scolarité Central.")
 #   elif num == NCarte:
     #      showerror("Échec de connexion", "Veuillez entrer votre N° de Carte pour vous connecter.")
      
     
    else:
         showerror(" Échec de connexion !", "     N° de carte incorrect....(×××××××). \n                  Veuillez insérer un\nN° de Carte valide pour vous connecter.")
    if len(num2) == 7:
                showinfo("Connexion réussi","N° de Carte validé ")                
    elif len(num2) >6:            
             showerror("Valeur Trop Grande ","            Le N° de Carte (×××××××) \n ne peut pas dépasser 7 caractères. \n           \n                  (×××××××)")
    else:
            showerror("Alerte !!!", "  Le N° de Carte doit atteindre 7 caractères")
    
           

          
        
           
           
       
# button qui commande la fonction "toggle_visibility"
toggle_btn_H = tk.Button(page_His, text="(• _ • )", command=toggle_visibility, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn_H.place(x=510, y=575)



#Checkbox sur la 2eme fenêtre 
check_H = tk.Checkbutton(page_His, text="Confirmer ", bg="white", fg="gray0", font="ExtraCondensed 10", activebackground="white", width=12, height=1)
check_H.place(x=50, y=680)
            
#Button Connexion sur la 2eme fenêtre             
button_H = tk.Button(page_His, text="Connexion", bg=COLORS["orange_dark"], fg="white", bd=5,  activebackground=COLORS ["orange_dark"],font=("Arial", 8), relief="solid", command=mes_infos2)
button_H.place(x=255, y=820)

#Button d'inscription en ligne uas'
def inscription2():
    webbrowser.open("http://postbac.uas.edu.ne")
    
navTcon_H = PhotoImage(file='Minduka_Present_Blue_pack.png')
tk.Button(page_His, image=navTcon_H, bg="gray100", width= 120, height=114, bd=0, activebackground="gray100", highlightthickness=-0).place(x=560, y=1110)
#
button_H1 = tk.Button(page_His, text="Inscription",bg="#2980b9", fg="white", highlightthickness=-1, padx=10, bd=5, font= ("Arial", 9), command= inscription2)
button_H1.place(x=20, y=1170)

#Button Exit

btn_Exit_H = tk.Button(page_His, text="  Quitter   ", command=app.quit, bg="#e74c3c", fg="white", padx=10, bd=5)
btn_Exit_H.place(x=540, y=1260)
# text retour sur le top Frame de la page d'accueil
'''
rt = tk.Label(page_inscription, text="Retour", bg=COLORS["orange_dark"], fg="gray70", font="ExtraCondensed 10", bd=0, highlightthickness=-1).place(x=125, y=40)
'''

Btn_H2= tk.Button(page_His, text="⬅",bg=COLORS ["green_dark"], fg="white", activebackground=COLORS["orange_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 14", command=lambda: afficher_page(page_inscription))
Btn_H2.place(x=2, y=20)



#------------------3eme fenêtre----------------------
#frame de Réclamation "page_Geo'

page_Rcla_H= tk.Frame(app, bg="gray10")
page_Rcla_H.grid(row=0, column=0, sticky="nsew")

#button de réclamation qui enverra vers la 3eme fenêtre "page_inscrip"

recla_H= tk.Button(page_His, highlightthickness=-1,text="Réclamation", command=lambda: afficher_page(page_Rcla_H), bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"],fg="white" , font=("Arial", 8)).place(x=20, y= 1260)





#Text Direction de la........sur la 2eme fenêtre 
bannerText = tk.Label(page_His, text="DIRECTION DE LA SCOLARITÉ CENTRALE", font=" ExtraCondensed 10", fg="green", bg="white", relief="solid")
bannerText.place(x=10, y= 1350)


bottom_frame_H = tk.Frame(page_His, bg=COLORS["green_dark"], relief="solid", bd=0)
bottom_frame_H.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame_H,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vide


#________---limite page Histoire---_______________





bannerText = tk.Label(page_inscription, text="Histoire", font=" ExtraCondensed 5", fg="white", bg="#4CAF50")
bannerText.place(x=220, y= 1360)












#------------ les fenêtre -------------#

 #---------- Page department de Scio----------
page_Lac = tk.Frame(app, bg="white")
page_Lac.grid(row=0, column=0, sticky="nsew")

#btn 
 
btn_L = tk.Button(page_inscription, text="     ", font=" ExtraCondensed 13",bd=5, relief="sunken", fg="green", bg="#4CAF50", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_Lac))
btn_L.place(x=352, y= 1310)


topFrame_L = tk.Frame(page_Lac, bg=COLORS ["green_dark"], relief="solid")
topFrame_L.pack(side="top", fill = tk.X)


   
#Text UENUZ sur topFrame2 de la 2eme fenêtre 
accueilText_L = tk.Label(topFrame_L,  text="Lac", font=" ExtraCondensed 13", bg=COLORS["green_dark" ], fg=COLORS ["orange_dark"], height=2,  padx=160)
accueilText_L.pack()


#Text Veuillez........sur la 2eme fenêtre 
accueilText_L1 = tk.Label(page_Lac, text="Veillez Renseigner votre \n N° de Carte", font=" ExtraCondensed 10", bg="white", fg="gray60",  height=2,  pady=2, relief="ridge")
accueilText_L1.place(x=150, y= 250)



bannerText_L = tk.Label(page_Lac, text="FLSH", font=" ExtraCondensed 20", fg="gray90", bg="white", relief="flat")
bannerText_L.place(x=290, y= 148)


#photo

navOcon_L = PhotoImage(file='ada.png')

tk.Button(page_Lac, image=navOcon_L, bg="gray100", width= 750, height=150, activebackground="white", bd=0, highlightthickness=-0).place(x=50, y=396)

canvas = tk.Canvas(page_Lac, width=100, height=130, bg="white", highlightthickness=0)
canvas.place(x=57, y=465)

# Exemple : texte incliné de 45°
canvas.create_text(50, 50, text="Login....", angle=0, fill="black", font=("ExtraCondensed", 8), tags="rotated")

def open_polit():
    webbrowser.open("https://www.google.com")
#button politique de........sur la 2eme fenêtre 
butter_L = tk.Button(page_Lac, text="Politique de confidentialité ", font=" ExtraCondensed 7",bd=0, fg="sky blue", bg="white", highlightthickness=-2, command=open_polit)
butter_L.place(x=20, y= 740)



#---------- Page de récupération de carte Histoire----------
page_LR = tk.Frame(app, bg="white")
page_LR.grid(row=0, column=0, sticky="nsew")

# button j'ai perdu ma carte 
    
N_L = tk.Button(page_Lac, text=" J'ai Perdu ma Carte ? ", font=" ExtraCondensed 7",bd=0, relief="ridge", fg="red", bg="white", highlightthickness=-1, command=lambda: afficher_page(page_LR))
N_L.place(x=400, y= 670)

# button de retour 
N_L1 = tk.Button(page_LR, text="⬅", font=" ExtraCondensed 15",bd=0, relief="groove", fg="gray30", bg="white", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_Lac))
N_L1.place(x=20, y= 40)


#placeholder sur la page_inscription     
NCarte_L = tk.Entry(page_Lac, highlightthickness=8, bg="gray100", fg="gray30", bd= 8, font="ExtraCondensed 18", width=16, relief="solid")
NCarte_L.place(x=50, y=550)



#_______-----_______________-------_________

def toggle_visibility():
    if NCarte_L.cget('show') == '':
        NCarte_L.config(show='*')
        toggle_btn_L.config(fg= 'green', text='voir')
    else:
        NCarte_L.config(show='')
        toggle_btn_L.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if NCarte_L.get() == "N° de Carte":
        messagebox.showinfo("Alerte", "Assurez-vous de taper 7 caractères ")
        NCarte_L.delete(0, tk.END)
        NCarte_L.config( fg="gray", show="*")  # Afficher les caractères masqués après clic






NCarte_L.insert(0,  "N° de Carte")  

#Bind des événements
NCarte_L.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)



def mes_infos4():
    
    
    dict4 = { "1830-22" : "Daouda Sani Fari", "1830-20" : "fati"}
    num4 = NCarte_L.get()
   
    if not num4.strip():
       
       
           
           messagebox.showwarning("Échec de connexion", " Le N° de Carte n'est pas renseigné.")
           return
           
    
    
    if num4 == "1830-22" in dict4:
                
                
                
              
              
              
              
              
         showinfo("Connexion réussi", "Bienvenue à la Scolarité Central.")
 #   elif num == NCarte:
     #      showerror("Échec de connexion", "Veuillez entrer votre N° de Carte pour vous connecter.")
      
     
    else:
         showerror(" Échec de connexion !", "     N° de carte incorrect....(×××××××). \n                  Veuillez insérer un\nN° de Carte valide pour vous connecter.")
    if len(num4) == 7:
                showinfo("Connexion réussi","N° de Carte validé ")                
    elif len(num4) >6:            
             showerror("Valeur Trop Grande ","            Le N° de Carte (×××××××) \n ne peut pas dépasser 7 caractères. \n           \n                  (×××××××)")
    else:
            showerror("Alerte !!!", "  Le N° de Carte doit atteindre 7 caractères")
    
           

          
        
           
           
       
# button qui commande la fonction "toggle_visibility"
toggle_btn_L = tk.Button(page_Lac, text="(• _ • )", command=toggle_visibility, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn_L.place(x=510, y=575)



#Checkbox sur la 2eme fenêtre 
check_L = tk.Checkbutton(page_Lac, text="Confirmer ", bg="white", fg="gray0", font="ExtraCondensed 10", activebackground="white", width=12, height=1)
check_L.place(x=50, y=680)
            
#Button Connexion sur la 2eme fenêtre             
button_L = tk.Button(page_Lac, text="Connexion", bg=COLORS["orange_dark"], fg="white", bd=5,  activebackground=COLORS ["orange_dark"],font=("Arial", 8), relief="solid", command=mes_infos4)
button_L.place(x=255, y=820)

#Button d'inscription en ligne uas'
def inscription4():
    webbrowser.open("http://postbac.uas.edu.ne")
    
navTcon_L = PhotoImage(file='Minduka_Present_Blue_pack.png')
tk.Button(page_Lac, image=navTcon_L, bg="gray100", width= 120, height=114, bd=0, activebackground="gray100", highlightthickness=-0).place(x=560, y=1110)
#
button_L1 = tk.Button(page_Lac, text="Inscription",bg="#2980b9", fg="white", highlightthickness=-1, padx=10, bd=5, font= ("Arial", 9), command= inscription4)
button_L1.place(x=20, y=1170)

#Button Exit

btn_Exit_L = tk.Button(page_Lac, text="  Quitter   ", command=app.quit, bg="#e74c3c", fg="white", padx=10, bd=5)
btn_Exit_L.place(x=540, y=1260)
# text retour sur le top Frame de la page d'accueil
'''
rt = tk.Label(page_inscription, text="Retour", bg=COLORS["orange_dark"], fg="gray70", font="ExtraCondensed 10", bd=0, highlightthickness=-1).place(x=125, y=40)
'''

Btn_L2= tk.Button(page_Lac, text="⬅",bg=COLORS ["green_dark"], fg="white", activebackground=COLORS["orange_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 14", command=lambda: afficher_page(page_inscription))
Btn_L2.place(x=2, y=20)



#------------------3eme fenêtre----------------------
#frame de Réclamation "page_Geo'

page_Rcla_L = tk.Frame(app, bg="gray10")
page_Rcla_L.grid(row=0, column=0, sticky="nsew")

#button de réclamation qui enverra vers la 3eme fenêtre "page_inscrip"

recla_L= tk.Button(page_Lac, highlightthickness=-1,text="Réclamation", command=lambda: afficher_page(page_Rcla_L), bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"],fg="white" , font=("Arial", 8)).place(x=20, y= 1260)





#Text Direction de la........sur la 2eme fenêtre 
bannerText_L= tk.Label(page_Lac, text="DIRECTION DE LA SCOLARITÉ CENTRALE", font=" ExtraCondensed 10", fg="green", bg="white", relief="solid")
bannerText_L.place(x=10, y= 1350)


bottom_frame_L = tk.Frame(page_Lac, bg=COLORS["green_dark"], relief="solid", bd=0)
bottom_frame_L.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame_L,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vide''


#text


bannerText = tk.Label(page_inscription, text="LAC", font=" ExtraCondensed 5", fg="white", bg="#4CAF50")
bannerText.place(x=395, y= 1360)





#________---limite page Lac--_______________




















































#------------ les fenêtre -------------#

 #---------- Page department de Scio----------
page_Soc = tk.Frame(app, bg="white")
page_Soc.grid(row=0, column=0, sticky="nsew")

#btn 
 
btn_S = tk.Button(page_inscription, text="     ", font=" ExtraCondensed 13",bd=5, relief="sunken", fg="orange", bg="#4CAF50", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_Soc))
btn_S.place(x=470, y= 1380)


topFrame_S = tk.Frame(page_Soc, bg=COLORS ["green_dark"], relief="solid")
topFrame_S.pack(side="top", fill = tk.X)


   
#Text UENUZ sur topFrame2 de la 2eme fenêtre 
accueilText_S = tk.Label(topFrame_S,  text="Sociologie", font=" ExtraCondensed 13", bg=COLORS["green_dark" ], fg=COLORS ["orange_dark"], height=2,  padx=160)
accueilText_S.pack()


#Text Veuillez........sur la 2eme fenêtre 
accueilText_S1 = tk.Label(page_Soc, text="Veillez Renseigner votre \n N° de Carte", font=" ExtraCondensed 10", bg="white", fg="gray60",  height=2,  pady=2, relief="ridge")
accueilText_S1.place(x=150, y= 250)



bannerText_S = tk.Label(page_Soc, text="FLSH", font=" ExtraCondensed 20", fg="gray90", bg="white", relief="flat")
bannerText_S.place(x=290, y= 148)


#photo

navOcon_S = PhotoImage(file='ada.png')

tk.Button(page_Soc, image=navOcon_S, bg="gray100", width= 750, height=150, activebackground="white", bd=0, highlightthickness=-0).place(x=50, y=396)

canvas = tk.Canvas(page_Soc, width=100, height=130, bg="white", highlightthickness=0)
canvas.place(x=57, y=465)

# Exemple : texte incliné de 45°
canvas.create_text(50, 50, text="Login....", angle=0, fill="black", font=("ExtraCondensed", 8), tags="rotated")

def open_polit():
    webbrowser.open("https://www.google.com")
#button politique de........sur la 2eme fenêtre 
butter_S = tk.Button(page_Soc, text="Politique de confidentialité ", font=" ExtraCondensed 7",bd=0, fg="sky blue", bg="white", highlightthickness=-2, command=open_polit)
butter_S.place(x=20, y= 740)



#---------- Page de récupération de carte Histoire----------
page_SR = tk.Frame(app, bg="white")
page_SR.grid(row=0, column=0, sticky="nsew")

# button j'ai perdu ma carte 
    
N_S= tk.Button(page_Soc, text=" J'ai Perdu ma Carte ? ", font=" ExtraCondensed 7",bd=0, relief="ridge", fg="red", bg="white", highlightthickness=-1, command=lambda: afficher_page(page_SR))
N_S.place(x=400, y= 670)

# button de retour 
N_S1 = tk.Button(page_SR, text="⬅", font=" ExtraCondensed 15",bd=0, relief="groove", fg="gray30", bg="white", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_Soc))
N_S1.place(x=20, y= 40)


#placeholder sur la page_inscription     
NCarte_S = tk.Entry(page_Soc, highlightthickness=8, bg="gray100", fg="gray30", bd= 8, font="ExtraCondensed 18", width=16, relief="solid")
NCarte_S.place(x=50, y=550)





#_______-----_______________-------_________

def toggle_visibility():
    if NCarte_S.cget('show') == '':
        NCarte_S.config(show='*')
        toggle_btn_S.config(fg= 'green', text='voir')
    else:
        NCarte_S.config(show='')
        toggle_btn_S.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if NCarte_S.get() == "N° de Carte":
        messagebox.showinfo("Alerte", "Assurez-vous de taper 7 caractères ")
        NCarte_S.delete(0, tk.END)
        NCarte_S.config( fg="gray", show="*")  # Afficher les caractères masqués après clic






NCarte_S.insert(0,  "N° de Carte")  

#Bind des événements
NCarte_S.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)



def mes_infos3():
    
    
    dict3 = { "1830-22" : "Daouda Sani Fari", "1830-20" : "fati"}
    num3 = NCarte_S.get()
   
    if not num3.strip():
       
       
           
           messagebox.showwarning("Échec de connexion", " Le N° de Carte n'est pas renseigné.")
           return
           
    
    
    if num3 == "1830-22" in dict3:
                
                
                
              
              
              
              
              
         showinfo("Connexion réussi", "Bienvenue à la Scolarité Central.")
 #   elif num == NCarte:
     #      showerror("Échec de connexion", "Veuillez entrer votre N° de Carte pour vous connecter.")
      
     
    else:
         showerror(" Échec de connexion !", "     N° de carte incorrect....(×××××××). \n                  Veuillez insérer un\nN° de Carte valide pour vous connecter.")
    if len(num3) == 7:
                showinfo("Connexion réussi","N° de Carte validé ")                
    elif len(num3) >6:            
             showerror("Valeur Trop Grande ","            Le N° de Carte (×××××××) \n ne peut pas dépasser 7 caractères. \n           \n                  (×××××××)")
    else:
            showerror("Alerte !!!", "  Le N° de Carte doit atteindre 7 caractères")
    
           

          
        
           
           
       
# button qui commande la fonction "toggle_visibility"
toggle_btn_S = tk.Button(page_Soc, text="(• _ • )", command=toggle_visibility, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn_S.place(x=510, y=575)



#Checkbox sur la 2eme fenêtre 
check_S = tk.Checkbutton(page_Soc, text="Confirmer ", bg="white", fg="gray0", font="ExtraCondensed 10", activebackground="white", width=12, height=1)
check_S.place(x=50, y=680)
            
#Button Connexion sur la 2eme fenêtre             
button_S = tk.Button(page_Soc, text="Connexion", bg=COLORS["orange_dark"], fg="white", bd=5,  activebackground=COLORS ["orange_dark"],font=("Arial", 8), relief="solid", command=mes_infos3)
button_S.place(x=255, y=820)

#Button d'inscription en ligne uas'
def inscription3():
    webbrowser.open("http://postbac.uas.edu.ne")
    
navTcon_S = PhotoImage(file='Minduka_Present_Blue_pack.png')
tk.Button(page_Soc, image=navTcon_S, bg="gray100", width= 120, height=114, bd=0, activebackground="gray100", highlightthickness=-0).place(x=560, y=1110)
#
button_S1 = tk.Button(page_Soc, text="Inscription",bg="#2980b9", fg="white", highlightthickness=-1, padx=10, bd=5, font= ("Arial", 9), command= inscription3)
button_S1.place(x=20, y=1170)

#Button Exit

btn_Exit_S = tk.Button(page_Soc, text="  Quitter   ", command=app.quit, bg="#e74c3c", fg="white", padx=10, bd=5)
btn_Exit_S.place(x=540, y=1260)
# text retour sur le top Frame de la page d'accueil
'''
rt = tk.Label(page_inscription, text="Retour", bg=COLORS["orange_dark"], fg="gray70", font="ExtraCondensed 10", bd=0, highlightthickness=-1).place(x=125, y=40)
'''

Btn_S2= tk.Button(page_Soc, text="⬅",bg=COLORS ["green_dark"], fg="white", activebackground=COLORS["orange_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 14", command=lambda: afficher_page(page_inscription))
Btn_S2.place(x=2, y=20)



#------------------3eme fenêtre----------------------
#frame de Réclamation "page_Geo'

page_Rcla_S = tk.Frame(app, bg="gray10")
page_Rcla_S.grid(row=0, column=0, sticky="nsew")

#button de réclamation qui enverra vers la 3eme fenêtre "page_inscrip"

recla_S = tk.Button(page_Soc, highlightthickness=-1,text="Réclamation", command=lambda: afficher_page(page_Rcla_S), bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"],fg="white" , font=("Arial", 8)).place(x=20, y= 1260)





#Text Direction de la........sur la 2eme fenêtre 
bannerText_S = tk.Label(page_Soc, text="DIRECTION DE LA SCOLARITÉ CENTRALE", font=" ExtraCondensed 10", fg="green", bg="white", relief="solid")
bannerText_S.place(x=10, y= 1350)


bottom_frame_S = tk.Frame(page_Soc, bg=COLORS["green_dark"], relief="solid", bd=0)
bottom_frame_S.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame_S,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vide
         
         

#text


bannerText = tk.Label(page_inscription, text="Socio", font=" ExtraCondensed 5", fg="white", bg="#4CAF50")
bannerText.place(x=507, y= 1430)
         


#________---limite pas Sociologie---_______________





































#------------ les fenêtre -------------#

 #---------- Page department de PCC---------
page_PCC = tk.Frame(app, bg="#FFFFFF")
page_PCC.grid(row=0, column=0, sticky="nsew")

#btn 
 
btn_P = tk.Button(page_inscription, text="     ", font=" ExtraCondensed 12",bd=5, relief="sunken", fg="green", bg="#4CAF50", highlightthickness=5, activebackground="#CE8000", command=lambda: afficher_page(page_PCC))
btn_P.place(x=352, y= 1210)


topFrame_P = tk.Frame(page_PCC, bg=COLORS ["green_dark"], relief="solid")
topFrame_P.pack(side="top", fill = tk.X)


   
#Text UENUZ sur topFrame2 de la 2eme fenêtre 
accueilText_P = tk.Label(topFrame_P,  text="PCC", font=" ExtraCondensed 13", bg=COLORS["green_dark" ], fg=COLORS ["orange_dark"], height=2,  padx=160)
accueilText_P.pack()


#Text Veuillez........sur la 2eme fenêtre 
accueilText_P1 = tk.Label(page_PCC, text="Veillez Renseigner votre \n N° de Carte", font=" ExtraCondensed 10", bg="white", fg="gray60",  height=2,  pady=2, relief="ridge")
accueilText_P1.place(x=150, y= 250)



bannerText_P = tk.Label(page_PCC, text="FLSH", font=" ExtraCondensed 20", fg="gray90", bg="white", relief="flat")
bannerText_P.place(x=290, y= 148)


#photo

navOcon_P = PhotoImage(file='ada.png')

tk.Button(page_PCC, image=navOcon_P, bg="gray100", width= 750, height=150, activebackground="white", bd=0, highlightthickness=-0).place(x=50, y=396)

canvas = tk.Canvas(page_PCC, width=100, height=130, bg="white", highlightthickness=0)
canvas.place(x=57, y=465)

# Exemple : texte incliné de 45°
canvas.create_text(50, 50, text="Login....", angle=0, fill="black", font=("ExtraCondensed", 8), tags="rotated")

def open_polit():
    webbrowser.open("https://www.google.com")
#button politique de........sur la 2eme fenêtre 
butter_P = tk.Button(page_Soc, text="Politique de confidentialité ", font=" ExtraCondensed 7",bd=0, fg="sky blue", bg="white", highlightthickness=-2, command=open_polit)
butter_P.place(x=20, y= 740)



#---------- Page de récupération de carte Histoire----------
page_PR = tk.Frame(app, bg="white")
page_PR.grid(row=0, column=0, sticky="nsew")

# button j'ai perdu ma carte 
    
N_P= tk.Button(page_PCC, text=" J'ai Perdu ma Carte ? ", font=" ExtraCondensed 7",bd=0, relief="ridge", fg="red", bg="white", highlightthickness=-1, command=lambda: afficher_page(page_PR))
N_P.place(x=400, y= 670)

# button de retour 
N_P1 = tk.Button(page_PR, text="⬅", font=" ExtraCondensed 15",bd=0, relief="groove", fg="gray30", bg="white", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_PCC))
N_P1.place(x=20, y= 40)


#placeholder sur la page_inscription     
NCarte_P = tk.Entry(page_PCC, highlightthickness=8, bg="gray100", fg="gray30", bd= 8, font="ExtraCondensed 18", width=16, relief="solid")
NCarte_P.place(x=50, y=550)





#_______-----_______________-------_________

def toggle_visibility4():
    if NCarte_P.cget('show') == '':
        NCarte_P.config(show='*')
        toggle_btn_P.config(fg= 'green', text='voir')
    else:
        NCarte_P.config(show='')
        toggle_btn_P.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if NCarte_P.get() == "N° de Carte":
        messagebox.showinfo("Alerte", "Assurez-vous de taper 7 caractères ")
        NCarte_P.delete(0, tk.END)
        NCarte_P.config( fg="gray", show="*")  # Afficher les caractères masqués après clic






NCarte_P.insert(0,  "N° de Carte")  

#Bind des événements
NCarte_P.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)



def mes_infos4():
    
    
    dict4 = { "1830-22" : "Daouda Sani Fari", "1830-20" : "fati"}
    num4 = NCarte_P.get()
   
    if not num4.strip():
       
       
           
           messagebox.showwarning("Échec de connexion", " Le N° de Carte n'est pas renseigné.")
           return
           
    
    
    if num4 == "1830-22" in dict4:
                
                
                
              
              
              
              
              
         showinfo("Connexion réussi", "Bienvenue à la Scolarité Central.")
 #   elif num == NCarte:
     #      showerror("Échec de connexion", "Veuillez entrer votre N° de Carte pour vous connecter.")
      
     
    else:
         showerror(" Échec de connexion !", "     N° de carte incorrect....(×××××××). \n                  Veuillez insérer un\nN° de Carte valide pour vous connecter.")
    if len(num4) == 7:
                showinfo("Connexion réussi","N° de Carte validé ")                
    elif len(num4) >6:            
             showerror("Valeur Trop Grande ","            Le N° de Carte (×××××××) \n ne peut pas dépasser 7 caractères. \n           \n                  (×××××××)")
    else:
            showerror("Alerte !!!", "  Le N° de Carte doit atteindre 7 caractères")
    
           

          
        
           
           
       
# button qui commande la fonction "toggle_visibility"
toggle_btn_P = tk.Button(page_PCC, text="(• _ • )", command=toggle_visibility4, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn_P.place(x=510, y=575)



#Checkbox sur la 2eme fenêtre 
check_P = tk.Checkbutton(page_PCC, text="Confirmer ", bg="white", fg="gray0", font="ExtraCondensed 10", activebackground="white", width=12, height=1)
check_P.place(x=50, y=680)
            
#Button Connexion sur la 2eme fenêtre             
button_P = tk.Button(page_PCC, text="Connexion", bg=COLORS["orange_dark"], fg="white", bd=5,  activebackground=COLORS ["orange_dark"],font=("Arial", 8), relief="solid", command=mes_infos4)
button_P.place(x=255, y=820)

#Button d'inscription en ligne uas'
def inscription4():
    webbrowser.open("http://postbac.uas.edu.ne")
    
navTcon_P = PhotoImage(file='Minduka_Present_Blue_pack.png')
tk.Button(page_PCC, image=navTcon_P, bg="gray100", width= 120, height=114, bd=0, activebackground="gray100", highlightthickness=-0).place(x=560, y=1110)
#
button_P1 = tk.Button(page_PCC, text="Inscription",bg="#2980b9", fg="white", highlightthickness=-1, padx=10, bd=5, font= ("Arial", 9), command= inscription4)
button_P1.place(x=20, y=1170)

#Button Exit

btn_Exit_S = tk.Button(page_PCC, text="  Quitter   ", command=app.quit, bg="#e74c3c", fg="white", padx=10, bd=5)
btn_Exit_S.place(x=540, y=1260)
# text retour sur le top Frame de la page d'accueil
'''
rt = tk.Label(page_inscription, text="Retour", bg=COLORS["orange_dark"], fg="gray70", font="ExtraCondensed 10", bd=0, highlightthickness=-1).place(x=125, y=40)
'''

Btn_P2= tk.Button(page_PCC, text="⬅",bg=COLORS ["green_dark"], fg="white", activebackground=COLORS["orange_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 14", command=lambda: afficher_page(page_inscription))
Btn_P2.place(x=2, y=20)



#------------------3eme fenêtre----------------------
#frame de Réclamation "page_Pcc'

page_Rcla_P = tk.Frame(app, bg="gray10")
page_Rcla_P.grid(row=0, column=0, sticky="nsew")

#button de réclamation qui enverra vers la 3eme fenêtre "page_inscrip"

recla_P = tk.Button(page_PCC, highlightthickness=-1,text="Réclamation", command=lambda: afficher_page(page_Rcla_P), bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"],fg="white" , font=("Arial", 8)).place(x=20, y= 1260)





#Text Direction de la........sur la 2eme fenêtre 
bannerText_S = tk.Label(page_PCC, text="DIRECTION DE LA SCOLARITÉ CENTRALE", font=" ExtraCondensed 10", fg="green", bg="white", relief="solid")
bannerText_S.place(x=10, y= 1350)


bottom_frame_P = tk.Frame(page_PCC, bg=COLORS["green_dark"], relief="solid", bd=0)
bottom_frame_P.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame_P,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vide
         
         
#label PCC         

bannerText = tk.Label(page_inscription, text="PCC", font=" ExtraCondensed 6", fg="white", bg="#4CAF50")
bannerText.place(x=395, y= 1265)         
         
         
         


#________---limite page PCC---_______________
































#------------ les fenêtre -------------#

 #---------- Page department de Anglais----------
page_AG = tk.Frame(app, bg="white")
page_AG.grid(row=0, column=0, sticky="nsew")

#btn 
 
btn_A = tk.Button(page_inscription, text="     ", font=" ExtraCondensed 12",bd=5, relief="sunken", fg="orange", bg="#4CAF50", highlightthickness=5, activebackground="#CE8000", command=lambda: afficher_page(page_AG))
btn_A.place(x=190, y= 1210)


topFrame_A = tk.Frame(page_AG, bg=COLORS ["green_dark"], relief="solid")
topFrame_A.pack(side="top", fill = tk.X)


   
#Text UENUZ sur topFrame2 de la 2eme fenêtre 
accueilText_A = tk.Label(topFrame_A,  text="Anglais", font=" ExtraCondensed 13", bg=COLORS["green_dark" ], fg=COLORS ["orange_dark"], height=2,  padx=160)
accueilText_A.pack()


#Text Veuillez........sur la 2eme fenêtre 
accueilText_A1 = tk.Label(page_AG, text="Veillez Renseigner votre \n N° de Carte", font=" ExtraCondensed 10", bg="white", fg="gray60",  height=2,  pady=2, relief="ridge")
accueilText_A1.place(x=150, y= 250)



bannerText_A = tk.Label(page_AG, text="FLSH", font=" ExtraCondensed 20", fg="orange", bg="white", relief="flat")
bannerText_A.place(x=270, y= 128)


#photo

navOcon_A = PhotoImage(file='ada.png')

tk.Button(page_AG, image=navOcon_P, bg="gray100", width= 750, height=150, activebackground="white", bd=0, highlightthickness=-0).place(x=50, y=396)

canvas = tk.Canvas(page_AG, width=100, height=130, bg="white", highlightthickness=0)
canvas.place(x=57, y=465)

# Exemple : texte incliné de 45°
canvas.create_text(50, 50, text="Login....", angle=0, fill="black", font=("ExtraCondensed", 8), tags="rotated")

def open_polit5():
    webbrowser.open("https://www.google.com")
#button politique de........sur la 2eme fenêtre 
butter_A = tk.Button(page_AG, text="Politique de confidentialité ", font=" ExtraCondensed 7",bd=0, fg="sky blue", bg="white", highlightthickness=-2, command=open_polit5)
butter_A.place(x=20, y= 740)



#---------- Page de récupération de carte Histoire----------
page_AR = tk.Frame(app, bg="white")
page_AR.grid(row=0, column=0, sticky="nsew")

# button j'ai perdu ma carte 
    
N_A= tk.Button(page_AG, text=" J'ai Perdu ma Carte ? ", font=" ExtraCondensed 7",bd=0, relief="ridge", fg="red", bg="white", highlightthickness=-1, command=lambda: afficher_page(page_AR))
N_A.place(x=400, y= 670)

# button de retour 
N_A1 = tk.Button(page_AR, text="⬅", font=" ExtraCondensed 15",bd=0, relief="groove", fg="gray30", bg="white", highlightthickness=-1, activebackground="white", command=lambda: afficher_page(page_AG))
N_A1.place(x=20, y= 40)


#placeholder sur la page_inscription     
NCarte_A = tk.Entry(page_AG, highlightthickness=8, bg="gray100", fg="gray30", bd= 8, font="ExtraCondensed 18", width=16, relief="solid")
NCarte_A.place(x=50, y=550)





#_______-----_______________-------_________

def toggle_visibility5():
    if NCarte_A.cget('show') == '':
        NCarte_A.config(show='*')
        toggle_btn_A.config(fg= 'green', text='voir')
    else:
        NCarte_A.config(show='')
        toggle_btn_A.config(text='Cacher')

# fonction qui décrit le comportement d'un placeholder avant et après le click 
def clear_placeholder(event):
    if NCarte_A.get() == "N° de Carte":
        messagebox.showinfo("Alerte", "Assurez-vous de taper 7 caractères ")
        NCarte_A.delete(0, tk.END)
        NCarte_A.config( fg="gray", show="*")  # Afficher les caractères masqués après clic






NCarte_A.insert(0,  "N° de Carte")  

#Bind des événements
NCarte_A.bind("<FocusIn>", clear_placeholder)
#NCarte.bind("<FocusOut>", add_placeholder)



def mes_infos5():
    
    
    dict5 = { "1830-22" : "Daouda Sani Fari", "1830-20" : "fati"}
    num5 = NCarte_A.get()
   
    if not num5.strip():
       
       
           
           messagebox.showwarning("Échec de connexion", " Le N° de Carte n'est pas renseigné.")
           return
           
    
    
    if num5 == "1830-22" in dict5:
                
                
                
              
              
              
              
              
         showinfo("Connexion réussi", "Bienvenue à la Scolarité Central.")
 #   elif num == NCarte:
     #      showerror("Échec de connexion", "Veuillez entrer votre N° de Carte pour vous connecter.")
      
     
    else:
         showerror(" Échec de connexion !", "     N° de carte incorrect....(×××××××). \n                  Veuillez insérer un\nN° de Carte valide pour vous connecter.")
    if len(num5) == 7:
                showinfo("Connexion réussi","N° de Carte validé ")                
    elif len(num5) >6:            
             showerror("Valeur Trop Grande ","            Le N° de Carte (×××××××) \n ne peut pas dépasser 7 caractères. \n           \n                  (×××××××)")
    else:
            showerror("Alerte !!!", "  Le N° de Carte doit atteindre 7 caractères")
    
           

          
        
           
           
       
# button qui commande la fonction "toggle_visibility"
toggle_btn_A = tk.Button(page_Soc, text="(• _ • )", command=toggle_visibility5, bd=0, highlightthickness=-2, bg="white", pady=10, activebackground="gray85")
toggle_btn_A.place(x=510, y=575)



#Checkbox sur la 2eme fenêtre 
check_A = tk.Checkbutton(page_AG, text="Confirmer ", bg="white", fg="gray0", font="ExtraCondensed 10", activebackground="white", width=12, height=1)
check_A.place(x=50, y=680)
            
#Button Connexion sur la 2eme fenêtre             
button_A = tk.Button(page_AG, text="Connexion", bg=COLORS["orange_dark"], fg="white", bd=5,  activebackground=COLORS ["orange_dark"],font=("Arial", 8), relief="solid", command=mes_infos5)
button_A.place(x=255, y=820)

#Button d'inscription en ligne uas'
def inscription5():
    webbrowser.open("http://postbac.uas.edu.ne")
    
navTcon_A = PhotoImage(file='Minduka_Present_Blue_pack.png')
tk.Button(page_AG, image=navTcon_A, bg="gray100", width= 120, height=114, bd=0, activebackground="gray100", highlightthickness=-0).place(x=560, y=1110)
#
button_A1 = tk.Button(page_AG, text="Inscription",bg="#2980b9", fg="white", highlightthickness=-1, padx=10, bd=5, font= ("Arial", 9), command= inscription5)
button_A1.place(x=20, y=1170)

#Button Exit

btn_Exit_A = tk.Button(page_AG, text="  Quitter   ", command=app.quit, bg="#e74c3c", fg="white", padx=10, bd=5)
btn_Exit_A.place(x=540, y=1260)
# text retour sur le top Frame de la page d'accueil
'''
rt = tk.Label(page_inscription, text="Retour", bg=COLORS["orange_dark"], fg="gray70", font="ExtraCondensed 10", bd=0, highlightthickness=-1).place(x=125, y=40)
'''

Btn_A2= tk.Button(page_AG, text="⬅",bg=COLORS ["green_dark"], fg="white", activebackground=COLORS["green_dark"], bd=0,highlightthickness=-5, font ="ExtraCondensed 14", command=lambda: afficher_page(page_inscription))
Btn_A2.place(x=2, y=20)



#------------------3eme fenêtre----------------------
#frame de Réclamation "page_Geo'

page_Rcla_A = tk.Frame(app, bg="gray10")
page_Rcla_A.grid(row=0, column=0, sticky="nsew")

#button de réclamation qui enverra vers la 3eme fenêtre "page_inscrip"

recla_A = tk.Button(page_AG, highlightthickness=-1,text="Réclamation", command=lambda: afficher_page(page_Rcla_R), bg=COLORS["green_dark" ], bd=5, activebackground=COLORS["orange_dark"],fg="white" , font=("Arial", 8)).place(x=20, y= 1260)





#Text Direction de la........sur la 2eme fenêtre 
bannerText_A = tk.Label(page_AG, text="DIRECTION DE LA SCOLARITÉ CENTRALE", font=" ExtraCondensed 10", fg="green", bg="white", relief="solid")
bannerText_A.place(x=10, y= 1350)


bottom_frame_A = tk.Frame(page_AG, bg=COLORS["green_dark"], relief="solid", bd=0)
bottom_frame_A.pack(side="bottom", fill=tk.X)

tk.Label(bottom_frame_A,
         text="© 2027 Scolarité Centrale. Tous droits réservés.",
         font=("ExtraCondensed", 6),
         bg=COLORS["green_dark"], fg=COLORS["orange_dark"],
         height=4).pack() # Texte de copyright au lieu de labels vide



#les textes

bannerText = tk.Label(page_inscription, text="Anglais", font=" ExtraCondensed 5", fg="white", bg="#4CAF50")
bannerText.place(x=220, y= 1270)
#text


#________---limite pas AGLAIS---_______________





















# ---------- Affichage initial ----------
afficher_page(page_accueil)

# frame qui ouvre la commutation par le button "||||"

navEtat = False
def switch_nav():
    global navEtat
    if navEtat:
        navLateral.place(x=-600, y=0)
        navEtat = False
    else:
        navLateral.place(x=0, y=0)
        navEtat = True

navLateral = tk.Frame(page_accueil, bg="gray92", width=600, height=1320)
navLateral.place(x=-600, y=0)

#boite
'''
navScon = PhotoImage(file='ada.png')

tk.Button(navLateral, image=navScon, bg="gray30", width= 500, height=800, activebackground="gray30", bd=0, highlightthickness=-0).place(x=70, y=146)
'''

navUAScon = PhotoImage(file='Screenshot_2022-12-16-06-22-38_3 (3).png')



tk.Button(navLateral, image=navUAScon, bg="gray98", width= 495, height=267, bd=-2, activebackground="gray100", highlightthickness=-2).place(x=-100, y=130)




# photo télé 
navUAS = PhotoImage(file='Screenshot_20260215-232043_1 (3).png')



tk.Button(navLateral, image=navUAS, bg="gray98", width= 170, height=167, bd=5, activebackground="gray100", highlightthickness=-2).place(x=405, y=145)




# button Évidemment 

btn_E = tk.Button(navLateral, fg=COLORS ["orange_dark"], text ="Événements", bg="gray95", font= "ExtraCondensed 5", highlightthickness=9,  bd = 5)
btn_E.place(x=400, y= 320)



#canvas sur la navLateral en haut '
canvas = tk.Canvas(navLateral, borderwidth=1, bg="gray100", highlightthickness=0, relief='groove', width=600, height=10)
canvas.place(x=0, y=388)







#canvas sur la navLateral d'en bas '
canvas = tk.Canvas(navLateral, borderwidth=1, bg="#0e6647", highlightthickness=0, relief='groove', width=498, height=90)
canvas.place(x=-10, y=1150)

#canvas sur la navLateral  
canvas = tk.Canvas(navLateral, borderwidth=1, bg="#0e6647", highlightthickness=0, relief='groove', width=599, height=200)
canvas.place(x=-1, y=-66)


#canvas sur la navLateral en bas.............. '
canvas = tk.Canvas(navLateral, borderwidth=1, bg=COLORS["green_dark"], highlightthickness=0, relief='groove', width=600, height=6)
canvas.place(x=0, y=1310)






# photo accueil 
navUA = PhotoImage(file='Screenshot_20260215-233221_1 (1).png')



tk.Button(navLateral, image=navUA, bg="gray98", width= 95, height=80, bd=0, activebackground="gray100", highlightthickness=-2).place(x=455, y=398)



#tk.Button(navLateral, image=navUA, bg="gray98", width= 90, height=90, bd=0, activebackground="gray100", highlightthickness=-2).place(x=245, y=470)
   # y_pos += 110

y= 470

#les options dans la navLateral 

option = ["ACCUEIL", "PAGES", "PROFIL", "PARAMÈTRES", "AIDES"]

for i in range(5):
    tk.Button(navLateral, text=option[i], font="ExtraCondensed 10", highlightbackground= "gray70", highlightthickness=8, bg= "#CE8000", fg="white", activebackground="gray30", bd=5).place(x=50, y=y)
    
    y +=115
    






# boîte de messages
navBcon = PhotoImage(file='Minduka_Present_Blue_pack.png')



tk.Button(navLateral, image=navBcon, bg="gray92", width= 190, height=120, bd=0, activebackground="gray95", highlightthickness=-0).place(x=400, y=868)

#label message 
fr = tk.Label(navLateral, text="Message", bg="gray92", fg="#2980b9", font="ExtraCondensed 7", bd=0, highlightthickness=-1).place(x=440, y=990)





#Button de fermeture  de la commutation 
fermeBtn = tk.Button(navLateral, text="⬅", bg="#0e6647", fg="white", activebackground=COLORS ["green_dark"], bd=0, highlightthickness=-1, font ="ExtraCondensed 15", command=switch_nav)
fermeBtn.place(x=440, y=20)

#------- Label en bas du button qui ferme la commutation 
fr = tk.Label(navLateral, text="FERMER", bg="#0e6647", fg="white", font="ExtraCondensed 6", bd=0, highlightthickness=-1).place(x=455, y=95)

def open_website():
    webbrowser.open("https://www.educt.az")
    
#Button https......sur la navLateral 
tk.Button(navLateral,  text="https://www.educt.az", bg=COLORS["green_dark"], fg="white", activebackground=COLORS["green_dark"],font="ExtraCondensed 11", bd=0, highlightthickness=-2,pady = 15, command=open_website).place(x=-10, y= 1152)

nav = PhotoImage(file='Screenshot_20260215-233721_1 (1).png')



tk.Button(navLateral, image=nav, bg="gray98", width= 85, height=90, bd=-2, activebackground="gray100", highlightthickness=-2).place(x=490, y=1150)

#label web

tk.Label(navLateral, text= "web" ,bg="gray98", font="ExtraCondensed 5", fg="green").place(x=512, y=1215)




    
#tk.Button(navLateral, text="FERMER", bg="green", fg="white", bd=0, command=switch_nav).place(x=385, y=95)

# button qui ouvre la commutation "||||"
navbarBtn = tk.Button(frame, text="|ll|ll|", font= "ExtraCondensed 15", bg="#005747", fg="#05ee92", relief = "raised", highlightbackground= "green", activebackground=COLORS["green_dark"], bd=2,highlightthickness=-1, command=switch_nav)
navbarBtn.place(x=31, y=17)



















#Petite fenêtre sur la navLateral -----button service client 

btnEtat1= False 
def switch():
    global btnEtat1
    if btnEtat1:
        navLateral1.place(x=800, y=0)
        btnEtat1 = False
    else:
        navLateral1.place(x=50, y=200)
        btnEtat1 = True
    

navLateral1 = tk.Frame(page_accueil, bg="#FFFFFF",highlightthickness=9, width=640, height=1200)
navLateral1.place(x=-800, y=200)

assis = tk.Label(navLateral1, text= "Besoin d'assistance ?", font= "ExtraCondensed 10", bg= "white", fg= "gray0").place(x=140, y= 110)

assis1= tk.Label(navLateral1, font="ExtraCondensed 7",bg ="white", fg="gray30", text="Nous sommes disponibles pour vous aider !\n Contactez l'un des numéros ci-dessous pour une \n assistance immédiate.").place(x=10, y=190)


#button 403
btn_assis= tk.Button(navLateral1, font="ExtraCondensed 14",bg ="#CE8000", fg="white", text="Contacter le 402",  highlightthickness=9, highlightbackground="gray80", bd =5).place(x=70, y=490)

# button 88999999
btn_assis= tk.Button(navLateral1, font="ExtraCondensed 13",bg ="red", fg="white", text="Contacter le 88999999",  highlightthickness=9, highlightbackground="gray80", bd =5).place(x=10, y=610)


#button 
btn_assis= tk.Button(navLateral1, font="ExtraCondensed 12",bg ="white", fg="red", text="Envoyez-nous un e-mail",  highlightthickness=9, highlightbackground="gray80", bd =5).place(x=25, y=730)



#text n'hésitez 

btn_assis= tk.Label(navLateral1, font="ExtraCondensed 7",bg ="white", fg="gray30", text="N'hésitez pas à nous contacter pour tout question \noù tout problème concernant nos services.").place(x=10, y=900)







fermeBtn1 = tk.Button(navLateral1, text="Annuler", bg="gray100", fg="#CE8000", activebackground="white", bd=0,highlightthickness=-1, font ="ExtraCondensed 9", command=switch)
fermeBtn1.place(x=5, y=1050)

#button service client 
serviceBtn= tk.Button(navLateral, text="Service d'assistance", font= "ExtraCondensed 6", bg="red", fg="white", bd=5,highlightthickness=8, highlightbackground="orange", command=switch)
serviceBtn.place(x=220, y=1050)











if __name__ == "__main__":
   app.mainloop()
   
    











