#%%
from p_vecteur import t_vecteur

#initialisation des vecteurs pour les tests
mes_coordonnees = [1,2,3]
vecteur1 = t_vecteur(mes_coordonnees)
vecteur2 = t_vecteur((3,4,5))
vecteur3 = t_vecteur(mes_coordonnees)

#tests des methodes de la classe t_vecteur
print("le vecteur 1 est:")
print(vecteur1.__str__())
print("la composante a l'indice 1 du vecteur 1 est:")
print(vecteur1.__getitem__(1))
print("la dimension du vecteur 1 est de:")
print(vecteur1.dimension())
print("le vecteur 2 est:")
print(vecteur2.__str__())
print("le resultat de l'addition du vecteur 1 et 2 est:")
print(vecteur1 + vecteur2)


#test sur la violation d'encapsulation
print("\n")
print("test sur la violation d'encapsulation")
print("fin", vecteur1)
print("fin", vecteur3)

vecteur3.coordonnees[1] = -3

print("fin", vecteur1)
print("fin", vecteur3)
print("fin", mes_coordonnees)

vecteur4 = t_vecteur((1,2,3))
vecteur5 = t_vecteur((4,5,6))

#suite des test des methodes de la classe t_vecteur
print("\n")
print("continuation des test de la classe t_vecteur")
print("le resultat de la multiplication du vecteur 1 par le coefficient 3 est:")
print(vecteur1.__mul__(3))
print(vecteur1.meme_dim(vecteur2))
print("le produit scalaire du vecteur 1 et du vecteur 2 est:")
print(vecteur4.__matmul__(vecteur5))
print("le carre de la norme du vecteur" , vecteur1 , "est:")
print(vecteur1.norme_carre()) 
#    print("la norme du vecteur 1 est:")
#    print(vecteur1.norme())
#    print("le vecteur normalise du vecteur 1 est:")
#    print(vecteur1.normalise())
# %%
