#%%
from module.algebre_lineaire.p_matrice import t_matrice
from module.algebre_lineaire.p_vecteur import t_vecteur

v1 = t_vecteur([1,2,3])
v2 = t_vecteur([4,5,6])
m = t_matrice([v1,v2])
print(m)
print("la dimension de la matrice m est:")
print(m.dimension())
print("la 1ere colonne de la matrice m est:")
print(m.get_colonne(0))
print("est ce que la matrice m est carrée ?")
print(m.est_carree())
# %%
mes_matrices = []
mes_matrices.append(t_matrice([t_vecteur([1, 2, 3]), t_vecteur([4, 5, 6])]))
mes_matrices.append(t_matrice([t_vecteur([7, 8, 9]), t_vecteur([10, 11, 12])]))
for m in mes_matrices:
    print(m)
    print(m.dimension())
    print(m.get_colonne(1))
    print(m.est_carree())
print(mes_matrices[0] + mes_matrices[1])
print(mes_matrices[0] * 2)
print(mes_matrices[0].transposee())
print(mes_matrices[0] @ mes_matrices[1])
print(mes_matrices[0].est_carree())
# %%
