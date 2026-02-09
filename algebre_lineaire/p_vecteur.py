class t_vecteur:

    def __init__(self, coordonnees):
        """Constructeur qui place dans l'attribut de <self> les_coordonnees le tuple
        contenant les valeurs de <coordonnees>"""
        self.coordonnees = coordonnees[:]

    def __del__(self):
        """Détruit l'attribut <les_coordonnees> de <self>"""
        del self.coordonnees
    
    def __repr__(self):
        try :
            return "t_vecteur(" + str(self.coordonnees) + ")"
        except AttributeError :
            return "vecteur non existantq"

    def __str__(self):
        """Converti <self> en une chaine de caractères pour l'affichage pour une
        utilisateur humain."""
        chaine = str(self.coordonnees)
        return chaine

    def __getitem__(self, key):
        """retourne la composante d'indice <key> dans le vecteur <self>"""
        composante = self.coordonnees[key]
        return composante
    
    def dimension(self):
        """Fournit le nombre de coordonnées du vecteur <self>"""
        x = len(self.coordonnees)
        return x
        
    def __add__(self, other):
        """retorune la somme de <self> et <other>"""
        tab = []
        i = 0
        for i in range(len(self.coordonnees)):
            tab.append(self.coordonnees[i] + other[i])
        return tab
        
    def __mul__(self, coefficient):
        """retorune <coefficient> fois le vecteur <self> (sic l'ordre)"""
        tab = []
        i = 0
        for i in range(len(self.coordonnees)):
            tab.append(coefficient * self.coordonnees[i])
        return tab

    def meme_dim(self, other):
        """retourne un bool : true -> les 2 vecteur sont de meme dimension
                              false -> les 2 vecteur ne sont pas de meme dimension"""
        return self.dimension() == other.dimension()

    def add_elmts_tab(x):
        """ ajoute tout les element d'un tableau et retourn un int"""
        i = 0
        temp = 0
        for i in range(len(x)):
            temp += x[i]
        return temp

    def __matmul__(self, other):
        """retorune le produit scalaire de <self> et de <other>"""
        if (self.meme_dim(other) == True):
            tab = []
            i = 0
            for i in range(len(self.coordonnees)):
                x = self.coordonnees[i]*other[i]
                tab.append(x)
            temp = t_vecteur.add_elmts_tab(tab)
            return temp
        else :
            print("les 2 vecteur ne sons pas de meme dimension")
        
    def norme_carre(self):
        """retorune le carré de la norme de <self>"""
        return (self.__matmul__(self))
        
    def norme(self):
        """retorune la norme de <self>"""
        return (self.norme_carre()) ** 0.5
        
    def normalise(self):
        """retourne un vecteur ayant même direction et même sens que <self> mais dont la
        norme vaut 1."""
        temp = self.norme()
        i = 0
        temp2 = []
        if (temp != 1):
            while(i != len(self.coordonnees)):
                temp3 = self.coordonnees[i]
                temp2.append(temp3 * (1 / temp ))
                i += 1
            return temp2
        else : 
            return self.coordonnees
        
    def est_colineaire(self, other):
        """retourne True si <self> et <other> sont colinéaires"""
        i = 0
        while(i != len(self.coordonnees) -1 ):
            temp = self.coordonnees[i] / other[i]
            temp2 = self.coordonnees[i+1] / other[i+1]
            if (temp == temp2):
                i += 1
            else:
                return False
        return True 
    
    def est_orthogonal(self, other):
        """retourne True si <self> et <other> sont orthogonaux"""
        if (self.__matmul__(other) == 0):
            return True
        else : 
            return False