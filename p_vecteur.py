class t_vecteur:
    """Représente un vecteur et ses opérations de base."""

    def __init__(self, coordonnees):
        """Constructeur qui place dans l'attribut de <self> les_coordonnees le tuple
        contenant les valeurs de <coordonnees>"""
        self.coordonnees = coordonnees[:]

    def __del__(self):
        """Détruit l'attribut <les_coordonnees> de <self>"""
        del self.coordonnees
    
    def __repr__(self):
        try :
            return "vecteur(" + str(self.coordonnees) + ")"
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

    def __len__(self):
        return len(self.coordonnees)

    def __iter__(self):
        return iter(self.coordonnees)
    
    def dimension(self):
        """retourne la dimension (nombre de composantes) du vecteur <self>"""

        x = len(self.coordonnees)
        return x
        
    def __add__(self, other):
        """retourne la somme du vecteur <self> et du vecteur <other>.
        Retourne None si les deux vecteurs n'ont pas la même dimension."""

        if not self.meme_dim(other):
            return None
        tab = []
        i = 0
        for i in range(len(self.coordonnees)):
            tab.append(self.coordonnees[i] + other[i])
        return t_vecteur(tab)

    def __mul__(self, coefficient):
        """retourne le vecteur <self> multiplié par le scalaire <coefficient>"""
        tab = []
        i = 0
        for i in range(len(self.coordonnees)):
            tab.append(coefficient * self.coordonnees[i])
        return t_vecteur(tab)

    def meme_dim(self, other):
        """retourne un bool : True si les 2 vecteurs sont de même dimension,
        False sinon."""
        return self.dimension() == other.dimension()

    @staticmethod
    def add_elmts_tab(x):
        """ajoute tous les éléments d'un tableau et retourne leur somme"""
        i = 0
        temp = 0
        for i in range(len(x)):
            temp += x[i]
        return temp

    def __matmul__(self, other):
        """retourne le produit scalaire de <self> et de <other>.
        Affiche un message d'erreur si les deux vecteurs n'ont pas la même dimension."""
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
        return t_vecteur.add_elmts_tab([x * x for x in self.coordonnees])
        
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
            return t_vecteur(temp2)
        else : 
            return t_vecteur(self.coordonnees)
        
    def est_colineaire(self, other):
        """retourne True si <self> et <other> sont colinéaires"""
        #i = 0
        #while(i != len(self.coordonnees) -1 ):
        #    temp = self.coordonnees[i] / other[i]
        #    temp2 = self.coordonnees[i+1] / other[i+1]
        #    if (temp == temp2):
        #        i += 1
        #    else:
        #        return False
        #return True 
        pass
        """ fausse bonne idée d'abord avoir les methode pour faire un pivot de gauss
        et voir si un fammile est lié """
    
    def est_orthogonal(self, other):
        """retourne True si <self> et <other> sont orthogonaux"""
        if (self.__matmul__(other) == 0):
            return True
        else : 
            return False

    def est_nul(self):
        """retourne True si le vecteur est nul"""
        return self.norme_carre() == 0
