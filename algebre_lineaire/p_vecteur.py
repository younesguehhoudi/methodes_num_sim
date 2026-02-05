class t_vecteur:

    def __init__(self, coordonnees):
        """Constructeur qui place dans l'attribut de <self> les_coordonnees le tuple
        contenant les valeurs de <coordonnees>"""
        self.coordonnees = coordonnees[:]

    def __del__(self):
        """Détruit l'attribut <les_coordonnees> de <self>"""
        del self.coordonnees
    
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
        return t_vecteur.dimension(self.coordonnees) == t_vecteur.dimension(other)

    def add_elmts_tab(x):
        """ ajoute tout les element d'un tableau et retourn un int"""
        i = 0
        temp = 0
        for i in range(len(x)):
            temp += x[i]
        return temp

    def __matmul__(self, other):
        """retorune le produit scalaire de <self> et de <other>"""
        if (t_vecteur.meme_dim(self.coordonnees, other) == True):
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
        pass
        
    def norme(self):
        """retorune la norme de <self>"""
        pass
        
    def normalise(self):
        """retourne un vecteur ayant même direction et même sens que <self> mais dont la
        norme vaut 1."""
        pass