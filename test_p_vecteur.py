#%%
from p_vecteur import t_vecteur


# === JEU DE DONNÉES GLOBAL ===
VECTEUR_A = t_vecteur([1, 2, 3])
VECTEUR_B = t_vecteur([3, 4, 5])
VECTEUR_C = t_vecteur([1, 2, 3])

VECTEUR_D = t_vecteur([1, 2, 3])
VECTEUR_E = t_vecteur([4, 5, 6])

FAMILLE_TEST = [
    t_vecteur([1, 2, -3]),
    t_vecteur([7, 0, -3]),
    t_vecteur([0, 4, 5]),
]


# === TESTS BASIQUES ===
print("\n# === TESTS BASIQUES ===")
print("Vecteur A :", VECTEUR_A)
print("Composante d'indice 1 de A :", VECTEUR_A[1])
print("Dimension de A :", VECTEUR_A.dimension())
print("Vecteur B :", VECTEUR_B)
print("A + B =", VECTEUR_A + VECTEUR_B)


# === TEST D'ENCAPSULATION ===
print("\n# === TEST D'ENCAPSULATION ===")
print("Avant modification :")
print("A =", VECTEUR_A)
print("C =", VECTEUR_C)

VECTEUR_C.coordonnees[1] = -3

print("Après modification de C.coordonnees[1] :")
print("A =", VECTEUR_A)
print("C =", VECTEUR_C)


# === TESTS DES OPÉRATIONS ===
print("\n# === TESTS DES OPÉRATIONS ===")
print("3 * A =", VECTEUR_A * 3)
print("A et B ont même dimension ?", VECTEUR_A.meme_dim(VECTEUR_B))
print("D @ E =", VECTEUR_D @ VECTEUR_E)
print("Norme carrée de A =", VECTEUR_A.norme_carre())
print("Norme de A =", VECTEUR_A.norme())
print("A normalisé =", VECTEUR_A.normalise())
print("D et E sont orthogonaux ?", VECTEUR_D.est_orthogonal(VECTEUR_E))


# === TESTS SUR UNE FAMILLE DE VECTEURS ===
print("\n# === TESTS SUR UNE FAMILLE DE VECTEURS ===")
for i, vect in enumerate(FAMILLE_TEST):
    print("Vecteur", i, ":", vect)

print("v1 + v0 =", FAMILLE_TEST[1] + FAMILLE_TEST[0])
print("2 * v2 =", FAMILLE_TEST[2] * 2)
print("v0 @ v1 =", FAMILLE_TEST[0] @ FAMILLE_TEST[1])
print("Norme de v2 =", FAMILLE_TEST[2].norme())
print("v2 normalisé =", FAMILLE_TEST[2].normalise())

# %%
