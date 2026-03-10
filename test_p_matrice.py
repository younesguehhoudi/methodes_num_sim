from p_vecteur import t_vecteur
from p_matrice import t_matrice
from p_famille_vecteurs import t_famille_vecteurs


def concatener_matrices(mat1, mat2):
    """Concatène horizontalement deux matrices de même nombre de lignes."""
    lignes = []
    for i in range(mat1.dimension()[0]):
        ligne = list(mat1[i].coordonnees) + list(mat2[i].coordonnees)
        lignes.append(t_vecteur(ligne))
    return t_matrice(lignes)


def resoudre_systeme(A, b):
    """Résout approximativement Ax=b par échelonnement puis remontée."""
    n = A.dimension()[0]
    mat_b_colonne = t_matrice([b]).transposee()
    mat_augmentee = concatener_matrices(A, mat_b_colonne)
    mat_augmentee_copy = mat_augmentee.copy()
    mat_augmentee_copy.forme_echelonnee()

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        somme = 0.0
        for j in range(i + 1, n):
            somme += mat_augmentee_copy[i][j] * x[j]
        x[i] = (mat_augmentee_copy[i][-1] - somme) / mat_augmentee_copy[i][i]
    return x


# === TESTS DES OPÉRATIONS MATRICIELLES ===
V2_A = t_vecteur([1, 2])
V2_B = t_vecteur([3, 4])
V2_C = t_vecteur([5, 6])
V2_D = t_vecteur([7, 8])

V3_A = t_vecteur([1, 2, 3])
V3_B = t_vecteur([4, 5, 6])
V3_C = t_vecteur([7, 8, 9])

MAT_2X2_1 = t_matrice([V2_A, V2_B])
MAT_2X2_2 = t_matrice([V2_C, V2_D])
MAT_2X3 = t_matrice([V3_A, V3_B])
MAT_3X3 = t_matrice([V3_A, V3_B, V3_C])

print("\n# === TESTS DES OPÉRATIONS MATRICIELLES ===")
print("Dimension de MAT_2X3 :", MAT_2X3.dimension())
print("Colonne 0 de MAT_2X3 :", MAT_2X3.get_colonne(0))
print("Est-ce que MAT_2X2_1 est carrée ? :", MAT_2X2_1.est_carree())
print("Est-ce que MAT_2X3 est carrée ? :", MAT_2X3.est_carree())
print("MAT_2X2_1 + MAT_2X2_2 =\n", MAT_2X2_1 + MAT_2X2_2)
print("MAT_2X2_1 * 2 =\n", MAT_2X2_1 * 2)
print("Transposée de MAT_2X3 =\n", MAT_2X3.transposee())


# === TESTS DU PRODUIT MATRICIEL ===
MAT_A = t_matrice([
    t_vecteur([1, 2, 3]),
    t_vecteur([4, 5, 6]),
])
MAT_B = t_matrice([
    t_vecteur([1, 2]),
    t_vecteur([3, 4]),
    t_vecteur([5, 6]),
])

VECT_COL = t_matrice([t_vecteur([1, 2])]).transposee()

print("\n# === TESTS DU PRODUIT MATRICIEL ===")
print("Dimension de A :", MAT_A.dimension())
print("Dimension de B :", MAT_B.dimension())
print("A @ B =\n", MAT_A @ MAT_B)
print("Dimension de A @ B :", (MAT_A @ MAT_B).dimension() if (MAT_A @ MAT_B) is not None else None) # type: ignore
print("MAT_2X2_1 @ vecteur_colonne =\n", MAT_2X2_1 @ VECT_COL)


# === TESTS DU RANG, DÉTERMINANT ET INVERSIBILITÉ ===
MAT_IDENTITE_2 = t_matrice([
    t_vecteur([1, 0]),
    t_vecteur([0, 1]),
])
MAT_NULLE_2 = t_matrice([
    t_vecteur([0, 0]),
    t_vecteur([0, 0]),
])
MAT_LIEE_2 = t_matrice([
    t_vecteur([1, 2]),
    t_vecteur([2, 4]),
])
MAT_TRIANGULAIRE = t_matrice([
    t_vecteur([2, 0]),
    t_vecteur([3, 1]),
])

print("\n# === TESTS DU RANG, DÉTERMINANT ET INVERSIBILITÉ ===")
print("Rang de l'identité 2x2 :", MAT_IDENTITE_2.rang())
print("Rang de la matrice nulle :", MAT_NULLE_2.rang())
print("Rang de la matrice liée :", MAT_LIEE_2.rang())
print("Rang de MAT_3X3 :", MAT_3X3.rang())
print("Déterminant de MAT_TRIANGULAIRE :", MAT_TRIANGULAIRE.determinant())
print("Est-ce que MAT_2X2_1 est inversible ? :", MAT_2X2_1.est_inversible())
print("Est-ce que MAT_LIEE_2 est inversible ? :", MAT_LIEE_2.est_inversible())


# === TESTS DES FAMILLES DE VECTEURS ===
FAM_LIBRE_CANONIQUE = t_famille_vecteurs([
    t_vecteur([1, 0, 0]),
    t_vecteur([0, 1, 0]),
    t_vecteur([0, 0, 1]),
])
FAM_LIEE_EXPLICITE = t_famille_vecteurs([
    t_vecteur([1, 2, 0]),
    t_vecteur([2, 4, 0]),
    t_vecteur([0, 0, 1]),
])

print("\n# === TESTS DES FAMILLES DE VECTEURS ===")
print("Famille libre (base canonique R3) :", FAM_LIBRE_CANONIQUE)
print("Est-ce qu'elle est liée ? :", FAM_LIBRE_CANONIQUE.est_liee())
print("Est-ce qu'elle est libre ? :", FAM_LIBRE_CANONIQUE.est_libre())
print("Rang de la famille libre :", FAM_LIBRE_CANONIQUE.rang_famille())
print("Est-ce une base de R3 ? :", FAM_LIBRE_CANONIQUE.est_base(3))

print("\nFamille liée (v2 = 2 * v1) :", FAM_LIEE_EXPLICITE)
print("Est-ce qu'elle est liée ? :", FAM_LIEE_EXPLICITE.est_liee())
print("Est-ce qu'elle est libre ? :", FAM_LIEE_EXPLICITE.est_libre())
print("Rang de la famille liée :", FAM_LIEE_EXPLICITE.rang_famille())
print("Est-ce une base de R3 ? :", FAM_LIEE_EXPLICITE.est_base(3))
print("Base extraite de la famille liée :", FAM_LIEE_EXPLICITE.extraire_base())


# === TESTS DES SYSTÈMES LINÉAIRES ===
A_2X2 = t_matrice([
    t_vecteur([1, 2]),
    t_vecteur([3, 4]),
])
B_2X2 = t_vecteur([5, 11])

A_3X3 = t_matrice([
    t_vecteur([1, 1, 1]),
    t_vecteur([2, 3, -1]),
    t_vecteur([1, -1, 2]),
])
B_3X3 = t_vecteur([6, 5, 5])

print("\n# === TESTS DES SYSTÈMES LINÉAIRES ===")
print("Système 2x2 :")
print("A =\n", A_2X2)
print("b =", B_2X2)
print("Solution approchée :", resoudre_systeme(A_2X2, B_2X2))

print("\nSystème 3x3 :")
print("A =\n", A_3X3)
print("b =", B_3X3)
print("Solution approchée :", resoudre_systeme(A_3X3, B_3X3))