#%%
from p_vecteur import t_vecteur
from p_matrice import t_matrice
from p_programme_lineaire import t_programme_lineaire

def _vers_matrice(A):
    """Convertit `A` en `t_matrice` si nécessaire."""
    if isinstance(A, t_matrice):
        return A
    return t_matrice([t_vecteur(ligne) for ligne in A])


def afficher_resultat_programme(titre, c, A, b, minimiser=True):
    """Construit un programme linéaire, le résout et affiche le résultat."""
    c_vecteur = c if isinstance(c, t_vecteur) else t_vecteur(c)
    A_matrice = _vers_matrice(A)
    b_vecteur = b if isinstance(b, t_vecteur) else t_vecteur(b)

    print("\n---", titre, "---")
    print("Objectif c =", c_vecteur)
    print("Contraintes A =\n", A_matrice)
    print("Second membre b =", b_vecteur)
    print("Type :", "Minimisation" if minimiser else "Maximisation")

    programme = t_programme_lineaire(c_vecteur, A_matrice, b_vecteur, minimiser=minimiser)
    solution, valeur_opt = programme.resoudre()

    print("Solution renvoyée :", solution)
    print("Valeur optimale renvoyée :", valeur_opt)


# === TESTS DES PROGRAMMES LINÉAIRES (SIMPLEXE) ===
print("\n# === TESTS DES PROGRAMMES LINÉAIRES (SIMPLEXE) ===")


# === PROBLÈMES DE BASE ===
print("\n# === PROBLÈMES DE BASE ===")

afficher_resultat_programme(
    "Minimisation simple",
    c=[1, 1],
    A=[[1, 1], [2, 1]],
    b=[3, 4],
    minimiser=True,
)

afficher_resultat_programme(
    "Maximisation simple",
    c=[1, 2],
    A=[[1, 1], [1, 0], [0, 1]],
    b=[4, 2, 3],
    minimiser=False,
)

afficher_resultat_programme(
    "Programme 2x2 avec contrainte >= (réécrite en <=)",
    c=[1, 1],
    A=[[-1, -1]],
    b=[-2],
    minimiser=True,
)


# === PROBLÈMES APPLIQUÉS ===
print("\n# === PROBLÈMES APPLIQUÉS ===")

afficher_resultat_programme(
    "Problème du régime alimentaire",
    c=[2, 3],
    A=[[-5, -10], [-2, -1]],
    b=[-20, -5],
    minimiser=True,
)

afficher_resultat_programme(
    "Problème de planification de production",
    c=[5, 4],
    A=[[2, 3], [1, 0], [0, 1]],
    b=[12, 4, 3],
    minimiser=False,
)

afficher_resultat_programme(
    "Problème du fleuriste",
    c=[40, 50],
    A=[[10, 10], [10, 20], [20, 10]],
    b=[50, 80, 80],
    minimiser=False,
)

afficher_resultat_programme(
    "Problème des pâtes (maximisation de marge)",
    # Variables :
    # x11,x21,x31,x41 (ingrédients I1..I4 pour P1)
    # x12,x22,x32,x42 (ingrédients I1..I4 pour P2)
    # x13,x23,x33,x43 (ingrédients I1..I4 pour P3)
    # Objectif = prix vente produit - coût ingrédient
    c=[
        35, 50, 61, 45,
        30, 45, 56, 40,
        9, 24, 35, 19,
    ],
    A=[
        # Stocks ingrédients
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],   # I1 <= 5200
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],   # I2 <= 8000
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],   # I3 <= 8000
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],   # I4 <= 7500

        # Composition P1 : I1 >= 15%, I2 <= 15%, I4 >= 20%
        [-0.85, 0.15, 0.15, 0.15, 0, 0, 0, 0, 0, 0, 0, 0],
        [-0.15, 0.85, -0.15, -0.15, 0, 0, 0, 0, 0, 0, 0, 0],
        [0.20, 0.20, 0.20, -0.80, 0, 0, 0, 0, 0, 0, 0, 0],

        # Composition P2 : I1 <= 20%, I3 <= 30%, I4 >= 40%
        [0, 0, 0, 0, 0.80, -0.20, -0.20, -0.20, 0, 0, 0, 0],
        [0, 0, 0, 0, -0.30, -0.30, 0.70, -0.30, 0, 0, 0, 0],
        [0, 0, 0, 0, 0.40, 0.40, 0.40, -0.60, 0, 0, 0, 0],

        # Composition P3 : I2 <= 15%, I3 <= 50%, I4 <= 15%
        [0, 0, 0, 0, 0, 0, 0, 0, -0.15, 0.85, -0.15, -0.15],
        [0, 0, 0, 0, 0, 0, 0, 0, -0.50, -0.50, 0.50, -0.50],
        [0, 0, 0, 0, 0, 0, 0, 0, -0.15, -0.15, -0.15, 0.85],
    ],
    b=[
        5200, 8000, 8000, 7500,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
    ],
    minimiser=False,
)


# === CAS LIMITES ===
print("\n# === CAS LIMITES ===")

afficher_resultat_programme(
    "Problème potentiellement non borné",
    c=[1, 1],
    A=[[1, -1]],
    b=[1],
    minimiser=False,
)

afficher_resultat_programme(
    "Aucune contrainte (cas trivial)",
    c=[1, 1],
    A=[],
    b=[],
    minimiser=True,
)


# === TESTS AVEC t_vecteur / t_matrice ===
print("\n# === TESTS AVEC t_vecteur / t_matrice ===")

C_VECT = t_vecteur([1, 1])
A_MAT = t_matrice([
    t_vecteur([1, 1]),
    t_vecteur([2, 1]),
])
B_VECT = t_vecteur([3, 4])

afficher_resultat_programme(
    "Programme linéaire construit avec objets",
    c=C_VECT,
    A=A_MAT,
    b=B_VECT,
    minimiser=True,
)

C_VECT_2 = t_vecteur([2, 3])
A_MAT_2 = t_matrice([
    t_vecteur([1, 0]),
    t_vecteur([0, 1]),
])
B_VECT_2 = t_vecteur([2, 2])

afficher_resultat_programme(
    "Vérification d'un objectif pondéré",
    c=C_VECT_2,
    A=A_MAT_2,
    b=B_VECT_2,
    minimiser=True,
)
# %%
