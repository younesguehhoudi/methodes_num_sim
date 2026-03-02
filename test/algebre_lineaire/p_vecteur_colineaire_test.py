#%%
# test de la methode est_colineaire améliorée
from module.algebre_lineaire.p_vecteur import t_vecteur

print("test de la methode est_colineaire")
print("=" * 50)

# test avec vecteurs colineaire
v1 = t_vecteur([1, 2, 3])
v2 = t_vecteur([2, 4, 6])

print("v1 =", v1)
print("v2 =", v2)
print("v1 et v2 sont colineaire?", v1.est_colineaire(v2))
print()

# test avec vecteurs non colineaire
v3 = t_vecteur([1, 0, 0])
v4 = t_vecteur([0, 1, 0])

print("v3 =", v3)
print("v4 =", v4)
print("v3 et v4 sont colineaire?", v3.est_colineaire(v4))
print()

# test avec vecteur nul
v5 = t_vecteur([0, 0, 0])
v6 = t_vecteur([5, 7, 9])

print("v5 =", v5, "(vecteur nul)")
print("v6 =", v6)
print("v5 et v6 sont colineaire?", v5.est_colineaire(v6))
print()

# test autre cas colineaire
v7 = t_vecteur([3, 6])
v8 = t_vecteur([-1, -2])

print("v7 =", v7)
print("v8 =", v8)
print("v7 et v8 sont colineaire?", v7.est_colineaire(v8))
print()

# %%
