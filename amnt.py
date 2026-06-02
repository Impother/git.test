'''

import tkinter as tk
from tkinter import messagebox
btnEtatF= False
# --- Placeholder ---
def add_placeholder(event=None):
    if entry.get() == "":
        entry.insert(0, "Entrer votre numéro...")
        entry.config(fg="gray")

def remove_placeholder(event=None):
    if entry.get() == "Entrer votre numéro...":
        entry.delete(0, tk.END)
        entry.config(fg="black")

# --- Vérification ---
def verifier():
    valeur = entry.get()

    if valeur == "Entrer votre numéro...":
        valeur = ""

    longueur = len(valeur)

    if longueur == 0:
        messagebox.showerror("Erreur", "Le champ est vide.")
        return
    elif longueur < 3:
        messagebox.showwarning("Attention", "Le numéro est trop court (moins de 3 caractères).")
        return
    elif longueur > 7:
        messagebox.showwarning("Attention", "Le numéro est trop long (plus de 7 caractères).")
        return
    else:
        # Numéro valide → lancer le chargement
        lancer_chargement()

# --- Animation de chargement ---
def lancer_chargement():
    loading_label.config(text="Chargement....")
    loading_label.pack(pady=10)

    # Animation (points qui tournent)
    animer_points(0)

    # Après 2 secondes → ouvrir nouvelle fenêtre
    root.after(2000, ouvrir_fenetre_suivante)

def animer_points(i):
    points = "." * (i % 4)
    loading_label.config(text=f"Chargement{points}")
    root.after(300, lambda: animer_points(i + 1))

btnEtatF = False
# --- Nouvelle fenêtre ---
def ouvrir_fenetre_suivante():
    loading_label.pack_forget()
    

    
    #def switchF():
    global btnEtatF
    
    if btnEtatF:
            
            
            navLateralF.place(x=800, y=0)
            btnEtatF = False
            
    else:
            
            navLateralF.place(x=30, y=20)
            btnEtatF = True
            

    navLateralF = tk.Frame(root, bg="gray30", width=670, height=1390)
    navLateralF.place(x=-800, y=200)


    


# --- Interface principale ---
root = tk.Tk()
root.title("Connexion")
root.geometry("320x250")

label = tk.Label(root, text="Tapez votre numéro :", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack()

add_placeholder()
entry.bind("<FocusIn>", remove_placeholder)
entry.bind("<FocusOut>", add_placeholder)

btn = tk.Button(root, text="Valider", font=("Arial", 12), command=verifier)
btn.pack(pady=20)

# Label invisible pour le chargement
loading_label = tk.Label(root, font=("Arial", 12))

    
root.mainloop()


'''

import customtkinter as ctk
# Plus spécifiques
import webbrowser
import os
import re
import sqlite3
from datetime import datetime
import smtplib
from PIL import Image
from customtkinter import *
# --- Dictionnaire de couleurs pour une gestion facile ---
COLORS = {
    "nero": "#252726",
    "purple": "#800080",
    "white": "#FFFFFF",
    "green_dark": "#006400",  # Un vert plus foncé pour les cadres
    "orange_dark": "#FF8C00" } # Un orange plus foncé pour les bannières et boutons

def afficher_page(page):
    page.tkraise()
    
       
        

ctk.set_appearance_mode("blue")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("600x400")
# Configuration du système de "pages"
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)



import urllib.request

def check_internet():
    try:
        urllib.request.urlopen("http://www.google.com", timeout=5)
        return True 
    except:
        return False 



page_accueil = ctk.CTkFrame(root, fg_color=COLORS ["orange_dark"], corner_radius=115, border_color= "gray85", border_width=3, bg_color="gray100")
page_accueil.grid(row=0, column=0, sticky="nsew", rowspan=20)



#le frame du top sur la page_accueil
frame = ctk.CTkFrame(master=page_accueil, corner_radius=50, border_color="gray100", fg_color="gray80",
bg_color="gray100", border_width=20)
frame.pack(pady=10, padx=10, fill="both", expand=True)






# label time




'''
canvas2 = ctk.CTkFrame(master=page_accueil,bg= COLORS["green_dark"], width=450, height=300)
canvas2.place(x=130, y=105)

'''


Cadrant = ctk.CTkFrame(master=frame, fg_color=COLORS ["orange_dark"], corner_radius=110, border_width= 20, border_color= "white", width=620, height=470)
Cadrant.place(x=38, y= 300)




framm_niger = ctk.CTkFrame(master=page_accueil, fg_color="gray100", bg_color=COLORS ["orange_dark"], corner_radius=60, border_width= 30,  border_color= "gray98", width=490, height=340)
framm_niger.place(x=110, y= 477)


accueilText2 = ctk.CTkLabel(page_accueil,text_color=COLORS ["green_dark"], height = 200, bg_color= "gray100", fg_color= COLORS ["green_dark"], text="Ny-Niger International Tranfert d'Argent\n\n\n Transfert d'argent", corner_radius= 70, font=("Arial", 15))
accueilText2.place(x=155, y=560)




# Text sur le frame si-haut)

accueilText = ctk.CTkLabel(master=page_accueil, text_color="gray100", bg_color="white", corner_radius= 30, fg_color= COLORS ["orange_dark"], text="My-Nita", font=("Arial", 70))
accueilText.place(x=225, y= 477)



accueilText_T = ctk.CTkLabel(master=page_accueil, text_color="gray100", bg_color=COLORS ["green_dark"], corner_radius= 30, fg_color= COLORS ["green_dark"], text="TRANSFERT D'ARGENT", font=("Arial", 30))
accueilText_T.place(x=185, y= 570)






#accueilText2 = ctk.CTkLabel(Cadrant ,text_color="green", text="      INSCRIPTION\n\n• My-Nita\n\n• Moov-Africa\n\n• Airtel-Money\n\n• Zamani-Cash\n\n• My-Amanata\n", font=("Arial", 30))
    #accueilText2.place(x=150, y=30)

champ= ctk.CTkEntry(master=page_accueil, width =580, height=110, placeholder_text="          +227 ^  XXXXXXXX", font=("ExtraCondensed", 28),bg_color="gray80", corner_radius=25, border_color= "gray100", border_width=6)
champ.place(x=65, y= 760)


champ1= ctk.CTkEntry(master=page_accueil, placeholder_text="Mot de passe",
 bg_color="gray80", 
 width =580,height=110, border_color= "white", border_width=6, 
  corner_radius=22,
  show="*", font=("Arial", 33))
champ1.place(x=65, y= 900)





#cadrant logo niger



Cadrant_niger = ctk.CTkFrame(master=page_accueil, fg_color="gray100", bg_color= "gray100", corner_radius=30, width=70, height=90)
Cadrant_niger.place(x=85, y= 803)



Cadrant_niger = ctk.CTkFrame(master=page_accueil, fg_color="orange", bg_color= "gray100", corner_radius=10, width=70, height=20)
Cadrant_niger.place(x=85, y= 783)




Cadrant_niger = ctk.CTkFrame(master=page_accueil, fg_color="green", bg_color= "gray100", corner_radius=10, width=70, height=20)
Cadrant_niger.place(x=85, y= 823)

# disc orange 
Cadrant_niger = ctk.CTkFrame(master=page_accueil, fg_color="orange", bg_color= "gray100", corner_radius=30, width=15, height=15)
Cadrant_niger.place(x=113, y= 806)

accueilText2 = ctk.CTkLabel(page_accueil,text_color="red", bg_color= "gray80", fg_color= "gray85", text="Version : 3.2.6", corner_radius= 70, font=("ExtraCondensed", 30))
accueilText2.place(x=250, y=1472)










    
    
    
    

    
    
btn = ctk.CTkButton(
    page_accueil,
    text="Se connecter",
    width=560,
    height=120, 
    border_color=COLORS ["green_dark"],
     border_width=8, 
     hover_color=COLORS ["green_dark"],
    corner_radius=40,
    fg_color=COLORS ["green_dark"],
    text_color="white",
    bg_color= "gray80", font=("Arial", 28),
    command= lambda: afficher_page(page_Matricule)
)
btn.place(x=76, y=1150)    














#page mot de passe oublié 

page_M_O = ctk.CTkFrame(root, fg_color="gray100")
page_M_O.grid(row=0, column=0, sticky="nsew", rowspan=20)






# Mot de passe oublié 

btn_M = ctk.CTkButton(page_accueil, text_color=COLORS ["green_dark"], fg_color="gray80", bg_color="gray80", text="Mot de passe oublié ?", font=("Arial", 26), hover_color= "gray60", command=lambda: afficher_page(page_M_O))
btn_M.place(x=360, y=1030)




#cadran canvas en bas du champ
canvas1 = ctk.CTkCanvas (page_accueil, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=-20,highlightbackground="gray86", relief='groove', width=242, height=0)
canvas1.place(x=368, y=1059)



# frame du placeholder page_M_O
fram = ctk.CTkFrame(page_M_O, fg_color="gray85", corner_radius=60, width=720, height=1750)
fram.place(x=0, y= 400)



L_R_M= ctk.CTkLabel(page_M_O, text= "Mot de passe oublié", bg_color= "gray100",
font=("Arial", 25),
 text_color="green", fg_color= "gray100")
L_R_M.place(x=250, y= 245)



L_R_P= ctk.CTkLabel(page_M_O, text= "Récupération de mot de passe", bg_color= "gray100",
font=("Arial", 37),
 text_color=COLORS ["green_dark"]
 , fg_color= "gray100")
L_R_P.place(x=100, y= 285)





L_R = ctk.CTkLabel(fram, text= "Entrer le numéro de téléphone", bg_color= "gray75",
font=("Arial", 36),
 text_color="green", fg_color= "gray85")
L_R.place(x=100, y= 120)




Nr= ctk.CTkEntry(master=fram, width =640, height=115, placeholder_text="+227 | XXXXXXXX", font=("Arial", 28), border_color= "gray100", border_width=4, bg_color="gray85", corner_radius=25)
Nr.place(x=40, y= 230)



btn_M_O= ctk.CTkButton(
     fram,
    text="Suivant",
    width=640,
    height=120,
    corner_radius=30,
    fg_color=COLORS ["green_dark"],
    text_color="white",
    bg_color="gray75", font=("Arial", 27),
    command=lambda: afficher_page(page_accueil)
)
btn_M_O.place(x=40, y=390)







Rtr= ctk.CTkButton(page_M_O, text="⬅", text_color="gray100", fg_color="gray70", bg_color="gray100", font=("Arial", 54), corner_radius=80, command=lambda: afficher_page(page_accueil))
Rtr.place(x=30, y= 40)

    
  
    
  
    
    



# page enter matrícule


page_Matricule = ctk.CTkFrame(root, fg_color="gray65")
page_Matricule.grid(row=0, column=0, sticky="nsew", rowspan=20)




#le frame du top sur la page_Matricule
Cadrant1 = ctk.CTkFrame(master=page_Matricule, corner_radius=60)
Cadrant1.pack(pady=70, padx=40, fill="both", expand=True)



Text = ctk.CTkLabel(Cadrant1, text_color="gray25", text="Entrer votre Matricule.", font=("Arial", 34))
Text.place(x=80, y=690)





#entry
champ_M= ctk.CTkEntry(master=page_Matricule, placeholder_text="Matricule", border_color= "gray100", border_width=4, 
 bg_color="gray88", 
 width =500,height=100,
  corner_radius=20,
  show="*", font=("Arial", 33))
champ_M.place(x=100, y= 830)





#Button de fermeture  page_Matricule 
fermeBtn = ctk.CTkButton(master=page_Matricule, text="Annuler", bg_color="gray90", height =50,
 font=("Arial", 30), fg_color="green", corner_radius=50,  command=lambda: afficher_page(page_accueil))
fermeBtn.place(x=90, y=1350)









btn_M = ctk.CTkButton(
    page_Matricule,
    text="Valider",
    width=500,
    height=110,
    corner_radius=40,
    fg_color=COLORS ["green_dark"],
    text_color="white",
    bg_color="gray90", font=("Arial", 23),
    command=lambda: afficher_page(page_Matricule)
)
btn_M.place(x=100, y=1000)









 

# ---------- Page compte ----------
page_compte = ctk.CTkFrame(root, bg_color="gray100")
page_compte.grid(row=0, column=0, sticky="nsew", rowspan=20)


text_l = ctk.CTkLabel(page_compte,text_color=COLORS["green_dark"], text="Créer un compte", font=("Arial", 45))
text_l.place(x=210, y=42)






text_C = ctk.CTkLabel(frame,text_color="green", text="Vous n'avez pas de Compte ?", font=("Arial", 29))
text_C.place(x=80, y=1299)




OUVRIR = ctk.CTkButton(page_accueil, text=" Créer un\n", text_color=COLORS["green_dark"], hover_color="gray60", fg_color="gray80", bg_color="gray80", 
font=("Arial", 38), command=lambda: afficher_page(page_compte))
OUVRIR.place(x=470, y= 1295)

#cadran canvas en bas du champ
canvas_S= ctk.CTkCanvas (page_accueil, borderwidth=1, bg=COLORS ["green_dark"], highlightthickness=-20,highlightbackground="green", relief='flat', width=139, height=0)
canvas_S.place(x=487, y=1335)






OUVRIR1 = ctk.CTkButton(page_accueil, text="compte", text_color = COLORS["green_dark"], hover_color="#ce8000", fg_color="gray80", bg_color="gray80", font=("Arial", 38), command=lambda: afficher_page(page_compte))
OUVRIR1.place(x=310, y= 1345)



#cadran canvas en bas du champ
canvas_S1= ctk.CTkCanvas(page_accueil, borderwidth=1, bg=COLORS["green_dark"], highlightthickness=-20,highlightbackground="gray86", relief='flat', width=129, height=0)
canvas_S1.place(x=317, y=1386)




PN= ctk.CTkEntry(master=page_compte, width =630, height=110, border_color= "gray100", border_width=4, placeholder_text="Entrer votre prénom", font=("Arial", 28), bg_color="gray88", fg_color= "gray100", corner_radius=20)
PN.place(x=50, y= 160)


PP= ctk.CTkEntry(master=page_compte, placeholder_text="Entrer votre nom",border_color= "gray100", border_width=4,  bg_color="gray88", fg_color= "gray100",
 width =630,height=110,
  corner_radius=20,
  font=("Arial", 28))
PP.place(x=50, y= 290)




PN= ctk.CTkEntry(master=page_compte, width =630, height=110, placeholder_text="Entrer votre N° de téléphone", font=("Arial", 28), 
border_color= "gray100", border_width=4, bg_color="gray88", fg_color= "gray100", corner_radius=20)
PN.place(x=50, y= 420)




PE= ctk.CTkEntry(master=page_compte, width =630, height=110, placeholder_text="Entrer votre email", font=("Arial", 28), bg_color="gray88", border_color= "gray100", border_width=4,  fg_color= "gray100",  corner_radius=20)
PE.place(x=50, y= 550)


PM= ctk.CTkEntry(master=page_compte, placeholder_text="Mot de passe",  bg_color="gray88", fg_color= "gray100", border_color= "gray100", border_width=4, 
 width =630,height=110,
  corner_radius=20,
  show="*", font=("Arial", 28))
PM.place(x=50, y= 680)



PC= ctk.CTkEntry(master=page_compte,placeholder_text="Confirmez le mot de passe",bg_color="gray88", fg_color= "gray100", border_color= "gray100", border_width=4, 
 width =630,height=110,
  corner_radius=20,
  show="*", font=("Arial", 28))
PC.place(x=50, y= 810)

text_P = ctk.CTkLabel(page_compte,text_color=COLORS["green_dark"], text="Code de parrainage", font=("Arial", 27))
text_P.place(x=50, y=970)


check = ctk.CTkCheckBox(page_compte,text_color=COLORS["green_dark"], checkbox_height = 30, checkbox_width= 30, text="J'ai lu et j'accepte les termes et\n conditions de confidentialité", font=("Arial", 38))
check.place(x=80, y=1190) 


text_T = ctk.CTkLabel(page_compte,text_color=COLORS["orange_dark"], text="Termes et", font=("Arial", 38))
text_T.place(x=475, y=1190)



text_C = ctk.CTkLabel(page_compte,text_color=COLORS["orange_dark"], text="conditions", font=("Arial", 38))
text_C.place(x=123, y=1235)








PM= ctk.CTkEntry(master=page_compte, placeholder_text="00227XXXXXXXX",
 bg_color="gray88", border_color= "gray100", border_width=4, 
 width =630,height=120,
  corner_radius=20, font=("Arial", 28))
PM.place(x=50, y= 1020)









FERMER = ctk.CTkButton(page_compte, text="⬅", text_color="gray100", fg_color="gray70", corner_radius=80, bg_color="gray85", font=("Arial", 54), command=lambda: afficher_page(page_accueil))
FERMER.place(x=30, y= 40)


btn_S = ctk.CTkButton(
    page_compte,
    text="Suivant",
    width=600,
    height=130,
    corner_radius=40,
    fg_color=COLORS ["green_dark"],
    text_color="white",
    bg_color="gray85", font=("Arial", 33)
)
btn_S.place(x=60, y=1350)






afficher_page(page_accueil)




# frame qui ouvre la commutation par le button "||||"

navEtat = False
def switch_nav():
    global navEtat
    if navEtat:
        navLateral.place(x=-900, y=0)
        navEtat = False
    else:
        navLateral.place(x=0, y=0)
        navEtat = True

navLateral = ctk.CTkFrame(master=page_accueil, bg_color="gray0", corner_radius=30, border_color= "gray0", border_width=5, fg_color="gray100", width=722, height=1700)
navLateral.place(x=-800, y=0)




assis = ctk.CTkLabel(navLateral, text= "Besoin d'aide ?", bg_color= "gray90",
font=("Arial", 50),
 text_color="gray0", fg_color= "gray100")
assis.place(x=210, y= 300)


assis2 = ctk.CTkLabel(navLateral, text= "Questions les plus fréquemment posées par\n les utilisateurs.", bg_color= "gray95",
font=("Arial", 30),
 text_color="gray50", fg_color= "gray100")
assis2.place(x=60, y= 400)


comb = ctk.CTkComboBox(navLateral, values = ["Qu'est-ce que le service MYNITA ?", "MYNITA est une application de monnaie électronique permettant d'envoyer, de recevoir et de gérer divers paiement en toute", "sécurité. Elle offre des transactions rapides et fiables."], font=("Arial", 28), corner_radius= 30, fg_color="gray80", bg_color="gray100", dropdown_fg_color= "white", width=630, height= 140)
comb.place(x=40, y=510)

comb2 = ctk.CTkComboBox(navLateral, values = ["Qui peut utiliser le service MYNITA ?"], font=("Arial", 28),  corner_radius= 30, fg_color= "gray80", width=630, height= 140)
comb2.place(x=40, y=700)

comb3 = ctk.CTkComboBox(navLateral, values = ["Quelle sont les avantages d'utiliser L'application MYNITA ?"], font=("Arial", 28),  corner_radius= 30, fg_color= "gray80", width=630, height= 140)
comb3.place(x=40, y=900)


comb4 = ctk.CTkComboBox(navLateral, values = ["Comment créer un compte ?"], font=("Arial", 28),  corner_radius= 30, fg_color= "gray80", width=630, height= 140)
comb4.place(x=40, y=1100)








assis1= ctk.CTkLabel(navLateral, bg_color ="gray95", fg_color="gray100", font=("Arial", 32), text_color="gray50", text="N'hésitez à nous contacter pour toute question\nou problème concernant nos services.")
assis1.place(x=35, y=1370)











#⬅




#Button de fermeture  de la commutation 
fermeBtn = ctk.CTkButton(master=navLateral, text="⬅", bg_color="gray95",
 font=("Arial", 56), fg_color="gray70", corner_radius=80, command=switch_nav)
fermeBtn.place(x=530, y=50)

#------- Label en bas du button qui ferme la commutation 



    
#tk.Button(navLateral, text="FERMER", bg="green", fg="white", bd=0, command=switch_nav).place(x=385, y=95)

# button qui ouvre la commutation "||||"
navbarBtn = ctk.CTkButton(master=frame, text=" Aide  ?",  text_color= "#ffffff", bg_color="gray80", fg_color="#CE8000", border_color="gray100", border_width=8, width =70, height =90,  font=("Arial", 25), corner_radius=40,  hover_color="#CE8000", command=switch_nav)
navbarBtn.place(x=30, y=40)









navEtat1 = False
def switch_nav2():
    global navEtat1
    if navEtat1:
        navLateral3.place(x=-900, y=0)
        navEtat1 = False
    else:
        navLateral3.place(x=0, y=0)
        navEtat1 = True

navLateral3 = ctk.CTkFrame(master=page_accueil, bg_color="gray0", corner_radius=30, border_color= "gray0", border_width=10, fg_color="gray95", width=722, height=1700)
navLateral3.place(x=-800, y=0)


assis5= ctk.CTkLabel(navLateral3, bg_color ="gray0", fg_color="gray95", font=("Arial", 49), text_color="gray0", text="Besoin d'assistance ?")
assis5.place(x=160, y=470)


assis7= ctk.CTkLabel(navLateral3, bg_color ="gray0", fg_color="gray95", font=("Arial", 30), text_color="gray60", text="Nous sommes disponibles pour vous aider !\n Contacter l'un des numéros ci-dessous pour\n une assistance immédiate")
assis7.place(x=60, y=560)



assis9= ctk.CTkLabel(navLateral3, bg_color ="gray0", fg_color="gray95", font=("Arial", 30), text_color="gray60", text="N'hésitez pas à nous contacter pour toute question\n ou problème concernant nos services")
assis9.place(x=20, y=1430)






btn_C = ctk.CTkButton(
    navLateral3,
    text="Contacter le 401",
    width=640,
    height=140,
    corner_radius=40,
    fg_color="#065799",
    text_color="white",
    bg_color="gray95", font=("Arial", 33)
)
btn_C.place(x=40, y=720)



btn_N = ctk.CTkButton(
    navLateral3,
    text="Contacter le 80787878",
    width=640,
    height=140,
    corner_radius=40,
    fg_color="#ee3333",
    text_color="white",
    bg_color="gray95", font=("Arial", 33)
)
btn_N.place(x=40, y=890)


btn_L = ctk.CTkButton(
    navLateral3,
    text="Message WhatsApp",
    width=640,
    height=140,
    corner_radius=40,
    fg_color="#059999",
    text_color="white",
    bg_color="gray95", font=("Arial", 33)
)
btn_L.place(x=40, y=1060)


btn_H = ctk.CTkButton(
    navLateral3,
    text="Envoyez-vous un e-mail",
    width=640,
    height=140,
    corner_radius=40,
    fg_color="#ee6666",
    text_color="white",
    bg_color="gray95", font=("Arial", 33)
)
btn_H.place(x=40, y=1230)














#Button de fermeture  de la commutation 
fermeBtn1 = ctk.CTkButton(master=navLateral3, text="⬅", bg_color="gray95",
 font=("Arial", 56), fg_color="gray70", corner_radius=80, command=switch_nav2)
fermeBtn1.place(x=530, y=50)







# button qui ouvre la commutation "||||"
navbarBtn1 = ctk.CTkButton(master=frame, text="Service Client",  text_color= "#ffffff", border_color="gray100", border_width=8, bg_color="gray80", fg_color="red", hover_color= "red", width =70, height =90,  command=switch_nav2, font=("Arial", 24), corner_radius=40)
navbarBtn1.place(x=430, y=40)




root.mainloop()