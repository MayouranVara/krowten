# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:30:20 2020

@author: gilbe
"""

import pandas as pd
import re


def matching(mot1, mot2):
    if (mot1.upper()) == (mot2.upper()):
        return 1
    else:
        return 0


def search_algo(a,question):

    list1 = question
    list1 = list1.strip()
    list1 = re.split("\W", list1)

    compteur = []
    cpt = 0
    candidatPotentiel = []
    candidatSur = []
    data = []

    # On compte tous les mots qui match avec chaque utilisateurs
    for i in range(0, 28):
        for j in range(9, 13):
            for k in list1:
                cpt += matching(a.iloc[i, j], k)
        compteur.append(cpt)
        cpt = 0

    # Premier filtre en fonction du nombre de matching
    for i in range(len(compteur)):
        if (compteur[i] >= 1):
            candidatPotentiel.append(i)

    if not candidatPotentiel:
        print("Personne!")

    # Deuxième filtre en fonction des notes de chaque utilisateurs
    else:
        for i in candidatPotentiel:
            if (a.iloc[i, 5] > 2):
                candidatSur.append(i)

    if not candidatSur:
        print("Personne!")
    else:
        print("Voici ceux qui pourront vous aider:")
        for i in candidatSur:
            data.append(a.iloc[i]['Prénom'])
        return data

    # On active la notification si ce n'est pas fait
    for i in candidatSur:
        if a.iloc[i]['Notification'] == 0:
            a.at[i, 'Notification'] = 1
    a.to_excel("classeur.xlsx", index=False)


df = pd.read_excel("classeur.xlsx")
question = input("Entrer une question:")
data = search_algo(df,question)

print(data)
