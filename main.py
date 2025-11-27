#### Imports et définition des variables globales
"""Encodage ASCII"""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
        passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)."""
    c=[s[0]]
    occ=[1]
    k=1
    for elt in s[k:]:
        if elt == s[k-1]:
            occ[-1]+=1
        else:
            c.append(s[k])
            occ.append(1)
        k=k+1
    return list(zip(c,occ))



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences) """
    # cas de base
    if s=="":
        return []
    # recherche nombre de caractères identiques au premier
    occ = 1
    while occ < len(s) and s[occ] == s[0]:
        occ += 1
    # appel récursif
    pair=(s[0],occ)
    return [pair] + artcode_r(s[occ:])
    #### Fonction principale


def main():
    """Fonction principale"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
