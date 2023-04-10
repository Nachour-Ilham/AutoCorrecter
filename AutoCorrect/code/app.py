import tkinter as tk
from manipulation_functions import *


def calculer():
    result=''
    valeur = valeur_entree.get()
    corrections = get_corrections(valeur, probs, vocab, n=2, verbose = True)
    for i, word_prob in enumerate(corrections):
        st = "\n word "+str(i)+" : "+str(word_prob[0])
        result+=st
    etiquette_resultat.config(text=result)


fenetre = tk.Tk()
fenetre.title("Spelling correction")
fenetre.config(bg='white')
fenetre.geometry('640x440')

etiquette_valeur = tk.Label(fenetre, text="Entry a word :")
etiquette_valeur.pack()


valeur_entree = tk.Entry(fenetre)
valeur_entree.pack()


bouton_calculer = tk.Button(fenetre, text="correct",command=calculer , bg='green')
bouton_calculer.pack()


etiquette_resultat = tk.Label(fenetre, text="")
etiquette_resultat.pack()


fenetre.mainloop()