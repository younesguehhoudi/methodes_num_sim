from p_vecteur import t_vecteur
class t_matrice:

    def __init__(self, vecteurs):
        self.matrice = vecteurs[:]

    def __repr__(self):
        chaine = str(self.matrice)
        return chaine

#%%
v1 = t_vecteur([1,2,3])
v2 = t_vecteur([4,5,6])
m = t_matrice([v1,v2])
print(m)
# %%
