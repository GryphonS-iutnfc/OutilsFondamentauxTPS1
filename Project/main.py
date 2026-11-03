import matplotlib.pyplot as plt
import numpy as np
import time, math, unicodedata, random
from collections import Counter

liste_lettres_francais = [
    'E', 'A', 'S', 'T', 'I', 'R', 'N', 'U', 'L', 'O',
    'D', 'M', 'C', 'P', 'V', 'H', 'G', 'F', 'B', 'Q',
    'J', 'X', 'Z', 'Y', 'K', 'W'
]

liste_lettres_anglais = [
    'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D',
    'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P',
    'B', 'V', 'K', 'X', 'Q', 'J', 'Z', 'S',
]

liste_lettres_slovaque = [
    'O', 'A', 'E', 'N', 'I', 'R', 'V', 'S', 'T', 'K',
     'L', 'D', 'P', 'M', 'U', 'C', 'H', 'Z', 'J', 'B',
     'Y', 'F', 'G', 'X', 'W', 'Q'
]



def duree(fonction, argument, argument2):
    """Renvoie le temps d'exécution de fonction(argument), en secondes."""
    debut = time.perf_counter()
    fonction(argument, argument2)
    return (time.perf_counter() - debut) * 1000

def lettre_vers_nombre(c):
    return ord(c) - ord("A")

def nombre_vers_lettre(n):
    return chr(n % 26 + ord("A"))


def nettoyer(texte):
    """Majuscules sans accents, lettres A-Z uniquement."""
    sans_accent = unicodedata.normalize("NFD", texte)
    sans_accent = "".join(c for c in sans_accent if unicodedata.category(c) != "Mn")
    return "".join(c for c in sans_accent.upper() if "A" <= c <= "Z")

def chiffrer(texte):
    secret = []
    cles = []
    for lettre in nettoyer(texte):
        cle = random.randrange(26)
        lettre_nombre = lettre_vers_nombre(lettre)
        secret.append(nombre_vers_lettre((lettre_nombre + cle)))
        cles.append(cle)
    return secret



with open("anglais.txt", "r", encoding="utf-8") as anglais:
    contenu_anglais = anglais.read()
    anglais_2500 = nettoyer(contenu_anglais[:2500])
    anglais_5000 = nettoyer(contenu_anglais[:5000])

with open("francais.txt", "r", encoding="utf-8") as francais:
    contenu_francais = francais.read()
    francais_2500 = nettoyer(contenu_francais[:2500])
    francais_5000 = nettoyer(contenu_francais[:5000])

with open("slovaque.txt", "r", encoding="utf-8") as slovaque:
    contenu_slovaque = slovaque.read()
    slovaque_2500 = nettoyer(contenu_slovaque[:2500])
    slovaque_5000 = nettoyer(contenu_slovaque[:5000])

with open("melange.txt", "r") as melange:
    melange_2000 = nettoyer(melange.read(2000))

def brute_force(secret, texte_long):
    resultat = ''
    for count, lettre in enumerate(secret):
        for i in range(26):
            difference_lettre = lettre_vers_nombre(lettre) - i
            if difference_lettre < 0:
                testn = lettre_vers_nombre(lettre) + abs(difference_lettre)
            elif difference_lettre > 0:
                testn = lettre_vers_nombre(lettre) - abs(difference_lettre)
            else:
                testn = lettre_vers_nombre(lettre)

            if testn == lettre_vers_nombre(texte_long[count]):
                resultat += nombre_vers_lettre(testn)
                break
    return resultat



def analyse_francais(secret, texte_long):
    resultat = ''
    for count, lettre in enumerate(secret):
        for i in range(len(liste_lettres_francais)):
            difference_lettre = lettre_vers_nombre(lettre) - lettre_vers_nombre(liste_lettres_francais[i])
            if difference_lettre < 0:
                testn = lettre_vers_nombre(lettre) + abs(difference_lettre)
            elif difference_lettre > 0:
                testn = lettre_vers_nombre(lettre) - abs(difference_lettre)
            else:
                testn = lettre_vers_nombre(lettre)
            if testn == lettre_vers_nombre(texte_long[count]):
                resultat += nombre_vers_lettre(testn)
                break
    return resultat

def analyse_anglais(secret, texte_long):
    resultat = ''
    for count, lettre in enumerate(secret):
        for i in range(len(liste_lettres_anglais)):
            difference_lettre = lettre_vers_nombre(lettre) - lettre_vers_nombre(liste_lettres_anglais[i])
            if difference_lettre < 0:
                testn = lettre_vers_nombre(lettre) + abs(difference_lettre)
            elif difference_lettre > 0:
                testn = lettre_vers_nombre(lettre) - abs(difference_lettre)
            else:
                testn = lettre_vers_nombre(lettre)
            if testn == lettre_vers_nombre(texte_long[count]):
                resultat += nombre_vers_lettre(testn)
                break
    return resultat

def analyse_slovaque(secret, texte_long):
    resultat = ''
    for count, lettre in enumerate(secret):
        for i in range(len(liste_lettres_slovaque)):
            difference_lettre = lettre_vers_nombre(lettre) - lettre_vers_nombre(liste_lettres_slovaque[i])
            if difference_lettre < 0:
                testn = lettre_vers_nombre(lettre) + abs(difference_lettre)
            elif difference_lettre > 0:
                testn = lettre_vers_nombre(lettre) - abs(difference_lettre)
            else:
                testn = lettre_vers_nombre(lettre)
            if testn == lettre_vers_nombre(texte_long[count]):
                resultat += nombre_vers_lettre(testn)
                break
    return resultat


def detecter_langue(texte_partiel):
    """
    Calcule un score basé sur la position des lettres dans les listes de fréquences
    pour le français, l'anglais et le slovaque. Le score le plus bas gagne.
    """
    score_fr = 0
    score_en = 0
    score_sk = 0

    for c in texte_partiel:
        # Score Français
        if c in liste_lettres_francais:
            score_fr += liste_lettres_francais.index(c)
        else:
            score_fr += 26

        # Score Anglais
        if c in liste_lettres_anglais:
            score_en += liste_lettres_anglais.index(c)
        else:
            score_en += 26

        # Score Slovaque
        if c in liste_lettres_slovaque:
            score_sk += liste_lettres_slovaque.index(c)
        else:
            score_sk += 26

    # Détermination du minimum entre les trois scores
    scores = {'FR': score_fr, 'EN': score_en, 'SK': score_sk}
    return min(scores, key=scores.get)


def analyse_dynamique(secret, texte_long):
    """
    Fonction qui déchiffre lettre par lettre et évalue / met à jour
    la langue probable tous les 20 caractères déchiffrés (FR, EN ou SK).
    """
    resultat = ''
    active_list = liste_lettres_francais  # Liste par défaut au démarrage

    for count, lettre in enumerate(secret):
        # Tous les 20 caractères, on réévalue la langue en fonction du texte déjà trouvé
        if count > 0 and count % 80 == 0:
            langue_detectee = detecter_langue(resultat)
            if langue_detectee == 'FR':
                active_list = liste_lettres_francais
            elif langue_detectee == 'EN':
                active_list = liste_lettres_anglais
            else:
                active_list = liste_lettres_slovaque

        for i in range(len(active_list)):
            difference_lettre = lettre_vers_nombre(lettre) - lettre_vers_nombre(active_list[i])
            if difference_lettre < 0:
                testn = lettre_vers_nombre(lettre) + abs(difference_lettre)
            elif difference_lettre > 0:
                testn = lettre_vers_nombre(lettre) - abs(difference_lettre)
            else:
                testn = lettre_vers_nombre(lettre)

            if testn == lettre_vers_nombre(texte_long[count]):
                resultat += nombre_vers_lettre(testn)
                break
    return resultat


def moyenne_temps(fonction, texte_long, runs=50):
    """Exécute et moyenne le temps d'une fonction de décryptage sur un nombre de runs donné."""
    total = 0
    for _ in range(runs):
        secret = chiffrer(texte_long)
        total += duree(fonction, secret, texte_long)
    return total / runs


def generer_graphiques():
    """Génère les 4 graphiques comparatifs demandés avec matplotlib."""
    algorithms = [
        ("Brute Force", brute_force),
        ("Analyse Français", analyse_francais),
        ("Analyse Anglais", analyse_anglais),
        ("Analyse Slovaque", analyse_slovaque)
    ]

    print("Calcul des temps pour le texte Anglais...")
    temps_anglais = [(moyenne_temps(func, anglais_2500), moyenne_temps(func, anglais_5000)) for _, func in algorithms]

    print("Calcul des temps pour le texte Français...")
    temps_francais = [(moyenne_temps(func, francais_2500), moyenne_temps(func, francais_5000)) for _, func in
                      algorithms]

    print("Calcul des temps pour le texte Slovaque...")
    temps_slovaque = [(moyenne_temps(func, slovaque_2500), moyenne_temps(func, slovaque_5000)) for _, func in
                      algorithms]

    print("Calcul des temps pour le texte Mélangé (2000)...")
    algorithms_melange = algorithms + [("Analyse Dynamique", analyse_dynamique)]
    algo_names_melange = [name for name, _ in algorithms_melange]
    temps_melange_2000 = [moyenne_temps(func, melange_2000) for _, func in algorithms_melange]

    # Création de la figure avec 4 sous-graphiques (2x2)
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))

    # Paramètres pour les graphiques groupés par taille (2500 vs 5000)
    labels_taille = ['2500 caractères', '5000 caractères']
    x = np.arange(len(labels_taille))
    width = 0.18  # Largeur de chaque barre pour qu'elles tiennent toutes les 4
    algo_names = [name for name, _ in algorithms]

    def tracer_groupe_taille(ax, titre, data_tuples):
        num_algos = len(data_tuples)
        total_width = width * num_algos
        start_offset = -total_width / 2 + width / 2

        for i, (algo_name, temps_val) in enumerate(zip(algo_names, data_tuples)):
            offset = start_offset + i * width
            ax.bar(x + offset, temps_val, width, label=algo_name)

        ax.set_title(titre)
        ax.set_xticks(x)
        ax.set_xticklabels(labels_taille)
        ax.set_ylabel('Temps moyen (ms)')
        ax.legend()
        ax.grid(axis='y', linestyle='--', alpha=0.7)

    # 1. Graphique Anglais (Groupé par taille)
    tracer_groupe_taille(axs[0, 0], 'Déchiffrement - Texte Anglais', temps_anglais)

    # 2. Graphique Français (Groupé par taille)
    tracer_groupe_taille(axs[0, 1], 'Déchiffrement - Texte Français', temps_francais)

    # 3. Graphique Slovaque (Groupé par taille)
    tracer_groupe_taille(axs[1, 0], 'Déchiffrement - Texte Slovaque', temps_slovaque)

    # 4. Graphique Mélange (Inchangé car une seule taille de 2000)
    x_melange = np.arange(len(algo_names_melange))
    axs[1, 1].bar(x_melange, temps_melange_2000, color='purple', width=0.5)
    axs[1, 1].set_title('Déchiffrement - Texte Mélangé (2000 caractères)')
    axs[1, 1].set_xticks(x_melange)
    axs[1, 1].set_xticklabels(algo_names_melange, rotation=15)
    axs[1, 1].set_ylabel('Temps moyen (ms)')
    axs[1, 1].grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    generer_graphiques()

