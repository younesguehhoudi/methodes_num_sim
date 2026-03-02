#%%
# test de la classe t_application_lineaire
from module.applications_lineaires.p_application_lineaire import t_application_lineaire
from module.algebre_lineaire.p_matrice import t_matrice
from module.algebre_lineaire.p_vecteur import t_vecteur

print("test de la classe t_application_lineaire")
print("=" * 50)

# creation d'une aplication lineaire simple
# matrice 2x2 : [[1, 2], [3, 4]]
m1 = t_matrice([t_vecteur([1, 2]), t_vecteur([3, 4])])
f = t_application_lineaire(m1)

print("aplication lineaire f:")
print(f)
print()

# test dim depart et arivée
print("dimension de l'espace de depart:", f.dimension_depart())
print("dimension de l'espace d'arivée:", f.dimension_arrivee())
print()

# test appliquer
v = t_vecteur([1, 0])
print("aplication de f sur", v)
resultat = f.appliquer(v)
print("f(v) =", resultat)
print()

v2 = t_vecteur([0, 1])
print("aplication de f sur", v2)
resultat2 = f(v2)  # test __call__
print("f(v2) =", resultat2)
print()

# %%
# test rang et dimensions
print("rang de f:", f.rang())
print("dimension de l'image:", f.dimension_image())
print("dimension du noyau:", f.dimension_noyau())
print()

# %%
# test injectivité surjectivité
print("f est injective?", f.est_injective())
print("f est surjective?", f.est_surjective())
print("f est bijective?", f.est_bijective())
print("f est un endomorphisme?", f.est_endomorphisme())
print("f est un automorphisme?", f.est_automorphisme())
print()

# %%
# test addition de 2 aplications
m2 = t_matrice([t_vecteur([2, 0]), t_vecteur([0, 2])])
g = t_application_lineaire(m2)

print("aplication g:")
print(g)
print()

h = f + g
print("f + g:")
print(h)
print()

# %%
# test multiplication par scalaire
f2 = f * 2
print("2 * f:")
print(f2)
print()

# %%
# test composition
print("composition g o f:")
composee = f @ g
print(composee)
print()

# test sur un vecteur
v3 = t_vecteur([1, 1])
print("(g o f)(v3) =", composee(v3))
print("g(f(v3)) =", g(f(v3)))
print()

# %%
# test avec une aplication injective mais pas surjective
# matrice 3x2 : [[1, 0], [0, 1], [0, 0]]
m3 = t_matrice([t_vecteur([1, 0]), t_vecteur([0, 1]), t_vecteur([0, 0])])
f3 = t_application_lineaire(m3)

print("aplication f3 (3x2):")
print(f3)
print("dim depart:", f3.dimension_depart())
print("dim arivée:", f3.dimension_arrivee())
print("rang:", f3.rang())
print("est injective?", f3.est_injective())
print("est surjective?", f3.est_surjective())
print("est bijective?", f3.est_bijective())
print()

# %%
# test avec une aplication surjective mais pas injective
# matrice 2x3 : [[1, 0, 1], [0, 1, 1]]
m4 = t_matrice([t_vecteur([1, 0, 1]), t_vecteur([0, 1, 1])])
f4 = t_application_lineaire(m4)

print("aplication f4 (2x3):")
print(f4)
print("dim depart:", f4.dimension_depart())
print("dim arivée:", f4.dimension_arrivee())
print("rang:", f4.rang())
print("dim noyau:", f4.dimension_noyau())
print("dim image:", f4.dimension_image())
print("est injective?", f4.est_injective())
print("est surjective?", f4.est_surjective())
print("est bijective?", f4.est_bijective())
print()

# %%
# test image
print("calcul d'une base de l'image de f4:")
base_image = f4.image()
print(base_image)
print()

# %%
# test avec une matrice identité (automorphisme)
id_mat = t_matrice([t_vecteur([1, 0, 0]), t_vecteur([0, 1, 0]), t_vecteur([0, 0, 1])])
id_app = t_application_lineaire(id_mat)

print("aplication identité:")
print(id_app)
print("est bijective?", id_app.est_bijective())
print("est automorphisme?", id_app.est_automorphisme())
print("est inversible?", id_app.est_inversible())
print()

# %%
