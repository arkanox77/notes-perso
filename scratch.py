"""
Petit script de tri que je réutilise de temps en temps.
Rien de spécial, juste pratique pour trier une liste de fichiers par date.
"""

import os


def trier_par_date(dossier):
    fichiers = [os.path.join(dossier, f) for f in os.listdir(dossier)]
    fichiers.sort(key=os.path.getmtime)
    return fichiers


if __name__ == "__main__":
    for f in trier_par_date("."):
        print(f)
