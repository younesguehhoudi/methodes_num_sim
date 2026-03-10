#%%
from p_vecteur import t_vecteur
from p_matrice import t_matrice
from p_application_lineaire import t_application_lineaire


# === JEU DE DONNÉES GLOBAL : APPLICATIONS R2 -> R2 ===
MAT_IDENTITE_2 = t_matrice([
    t_vecteur([1, 0]),
    t_vecteur([0, 1]),
])
MAT_PROJECTION_X = t_matrice([
    t_vecteur([1, 0]),
    t_vecteur([0, 0]),
])
MAT_F = t_matrice([
    t_vecteur([1, 1]),
    t_vecteur([2, 0]),
])

APP_IDENTITE = t_application_lineaire(MAT_IDENTITE_2)
APP_PROJECTION_X = t_application_lineaire(MAT_PROJECTION_X)
APP_F = t_application_lineaire(MAT_F)

V_TEST_2D = t_vecteur([3, 4])


# === JEU DE DONNÉES GLOBAL : APPLICATION R3 -> R2 ===
MAT_2X3 = t_matrice([
    t_vecteur([1, 2, 3]),
    t_vecteur([4, 5, 6]),
])
APP_2X3 = t_application_lineaire(MAT_2X3)
V_TEST_3D = t_vecteur([2, 3, 4])


# === TESTS BASIQUES ===
print("\n# === TESTS BASIQUES ===")
print("Application identité :\n", APP_IDENTITE)
print("Dimension de départ (identité) :", APP_IDENTITE.dimension_depart())
print("Dimension d'arrivée (identité) :", APP_IDENTITE.dimension_arrivee())
print("f_identite([3,4]) =", APP_IDENTITE(V_TEST_2D))

print("\nApplication 2x3 :\n", APP_2X3)
print("Dimension de départ (2x3) :", APP_2X3.dimension_depart())
print("Dimension d'arrivée (2x3) :", APP_2X3.dimension_arrivee())
print("f_2x3([2,3,4]) =", APP_2X3(V_TEST_3D))


# === TESTS DES OPÉRATIONS ENTRE APPLICATIONS ===
APP_SOMME = APP_IDENTITE + APP_F
APP_DOUBLE = APP_F * 2
APP_COMPOSITION = APP_F @ APP_IDENTITE

print("\n# === TESTS DES OPÉRATIONS ENTRE APPLICATIONS ===")
print("(identité + F)([3,4]) =", APP_SOMME(V_TEST_2D) if APP_SOMME is not None else None)
print("(2 * F)([3,4]) =", APP_DOUBLE(V_TEST_2D))
print("(F o identité)([3,4]) =", APP_COMPOSITION(V_TEST_2D) if APP_COMPOSITION is not None else None)


# === TESTS DES PROPRIÉTÉS (IDENTITÉ) ===
print("\n# === TESTS DES PROPRIÉTÉS (IDENTITÉ) ===")
print("Rang :", APP_IDENTITE.matrice.rang())
print("Dimension image :", APP_IDENTITE.dimension_image())
print("Dimension noyau :", APP_IDENTITE.dimension_noyau())
print("Est injective ? :", APP_IDENTITE.est_injective())
print("Est surjective ? :", APP_IDENTITE.est_surjective())
print("Est bijective ? :", APP_IDENTITE.est_bijective())
print("Est endomorphisme ? :", APP_IDENTITE.est_endomorphisme())
print("Est automorphisme ? :", APP_IDENTITE.est_automorphisme())
print("Est inversible ? :", APP_IDENTITE.est_inversible())


# === TESTS DES PROPRIÉTÉS (PROJECTION) ===
print("\n# === TESTS DES PROPRIÉTÉS (PROJECTION SUR x) ===")
print("Rang :", APP_PROJECTION_X.matrice.rang())
print("Dimension image :", APP_PROJECTION_X.dimension_image())
print("Dimension noyau :", APP_PROJECTION_X.dimension_noyau())
print("Est injective ? :", APP_PROJECTION_X.est_injective())
print("Est surjective ? :", APP_PROJECTION_X.est_surjective())
print("Est bijective ? :", APP_PROJECTION_X.est_bijective())


# === TESTS NOYAU / IMAGE / THÉORÈME DU RANG ===
NOYAU_IDENTITE = APP_IDENTITE.matrice.noyau()
IMAGE_IDENTITE = APP_IDENTITE.matrice.image()

NOYAU_PROJECTION = APP_PROJECTION_X.matrice.noyau()
IMAGE_PROJECTION = APP_PROJECTION_X.matrice.image()

print("\n# === TESTS NOYAU / IMAGE / THÉORÈME DU RANG ===")
print("Noyau de l'identité :", NOYAU_IDENTITE)
print("Image de l'identité :", NOYAU_IDENTITE if False else IMAGE_IDENTITE)
print("Noyau de la projection :", NOYAU_PROJECTION)
print("Image de la projection :", IMAGE_PROJECTION)

dim_noyau = APP_2X3.dimension_noyau()
dim_image = APP_2X3.dimension_image()
dim_depart = APP_2X3.dimension_depart()
print("\nThéorème du rang pour APP_2X3 :")
print("dim(Ker) + dim(Im) =", dim_noyau, "+", dim_image, "=", dim_noyau + dim_image)
print("dim(E) =", dim_depart)


# === TESTS D'INVERSE ===
APP_INV_IDENTITE = APP_IDENTITE.matrice.inverse()
APP_INV_PROJECTION = APP_PROJECTION_X.matrice.inverse()

print("\n# === TESTS D'INVERSE ===")
print("Inverse de l'identité :", APP_INV_IDENTITE)
print("Inverse de la projection :", APP_INV_PROJECTION)

if APP_INV_IDENTITE is not None:
    composition_retour = APP_IDENTITE(APP_INV_IDENTITE @ V_TEST_2D)
    print("identité(inverse_identité([3,4])) =", composition_retour)
# %%
