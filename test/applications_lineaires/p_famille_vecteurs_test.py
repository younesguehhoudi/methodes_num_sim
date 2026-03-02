#%%
# test de la classe t_famille_vecteurs
from module.applications_lineaires.p_famille_vecteurs import t_famille_vecteurs
from module.algebre_lineaire.p_vecteur import t_vecteur

# creation de quelques vecteurs pour les test
v1 = t_vecteur([1, 0, 0])
v2 = t_vecteur([0, 1, 0])
v3 = t_vecteur([0, 0, 1])
v4 = t_vecteur([2, 3, 1])

print("test de la classe t_famille_vecteurs")
print("=" * 50)

# test constructeur et affichage
fam1 = t_famille_vecteurs([v1, v2, v3])
print("fammile 1 (base canonique de R3):")
print(fam1)
print()

# test nombre de vecteurs
print("nombre de vecteurs dans fam1:", fam1.nombre_vecteurs())
print("dimension des vecteurs:", fam1.dimension_vecteurs())
print()

# test rang
print("rang de la fammile:", fam1.rang_famille())
print()

# test si libre
print("est ce que la fammile est libre?", fam1.est_libre())
print("est ce que la fammile est liée?", fam1.est_liee())
print()

# test si base de R3
print("est ce que c'est une base de R3?", fam1.est_base(3))
print()

# %%
# test avec des vecteurs colineaire
v5 = t_vecteur([1, 2, 3])
v6 = t_vecteur([2, 4, 6])

fam2 = t_famille_vecteurs([v5, v6])
print("fammile 2 (2 vecteurs colineaire):")
print(fam2)
print("sont ils colineaire?", fam2.sont_colineaires())
print("est ce que la fammile est libre?", fam2.est_libre())
print("est ce que la fammile est liée?", fam2.est_liee())
print("rang de la fammile:", fam2.rang_famille())
print()

# %%
# test avec des vecteurs non colineaire
v7 = t_vecteur([1, 0])
v8 = t_vecteur([0, 1])

fam3 = t_famille_vecteurs([v7, v8])
print("fammile 3 (2 vecteurs non colineaire):")
print(fam3)
print("sont ils colineaire?", fam3.sont_colineaires())
print("est ce que la fammile est libre?", fam3.est_libre())
print("rang:", fam3.rang_famille())
print()

# %%
# test extraire base
v9 = t_vecteur([1, 0, 0])
v10 = t_vecteur([0, 1, 0])
v11 = t_vecteur([2, 3, 0])

fam4 = t_famille_vecteurs([v9, v10, v11])
print("fammile 4 (3 vecteurs dont 1 depend des autres):")
print(fam4)
print("rang:", fam4.rang_famille())
print("est libre?", fam4.est_libre())
print()

print("extraction d'une base:")
base = fam4.extraire_base()
print(base)
print("rang de la base:", base.rang_famille())
print("est libre?", base.est_libre())
print()

# %%
# test dimension vect
print("dimension de l'espace vectoriel engendré par fam4:", fam4.dimension_vect())
print()

# %%
# test avec le vecteur nul
v_nul = t_vecteur([0, 0, 0])
fam5 = t_famille_vecteurs([v1, v2, v_nul])
print("fammile 5 (contient le vecteur nul):")
print(fam5)
print("contient le vecteur nul?", fam5.contient_vecteur_nul())
print("est libre?", fam5.est_libre())
print()

# %%
