from p_vecteur import t_vecteur

class t_matrice:

    # constructeur, destructzur, affichagz
    def __init__(self, vecteurs):
        """Constructeur : prend une liste d'objets t_vecteur"""
        self.matrice = vecteurs[:]

    def __del__(self):
        """Détruit l'attribut matrice de self"""
        del self.matrice
    
    def __repr__(self):
        """Représentation de l'objet"""
        try :
            return "matrice(" + str(self.matrice) + ")"
        except AttributeError :
            return "matrice non existante"

    def __str__(self):
        """Affichage utilisateur (une ligne par vecteur)"""
        chaine = ""
        for v in self.matrice:
            chaine += str(v) + "\n"
        return chaine

    def __getitem__(self, key):
        """Retourne le vecteur à l'indice key"""
        return self.matrice[key]


    def dimension(self):
        """Retourne un tuple (nb_lignes, nb_colonnes)"""
        nb_lignes = len(self.matrice)
        if nb_lignes == 0:
            return (0, 0)
        nb_colonnes = self.matrice[0].dimension()
        return (nb_lignes, nb_colonnes)

    def get_colonne(self, j):
        """Extrait la j-ème colonne sous forme de t_vecteur"""
        if len(self.matrice) == 0:
            return None
        colonne = []
        i = 0
        for i in range(len(self.matrice)):
            composante = self.matrice[i][j]
            colonne.append(composante)
        resultat = t_vecteur(colonne)
        return resultat

    def est_carree(self):
        """Vérifie si la matrice est carrée"""
        nb_lignes, nb_colonnes = self.dimension()
        return nb_lignes == nb_colonnes

    # qlq opeation sur les matrice

    def __add__(self, other):
        """Additionne deux matrices"""
        dimension_self = self.dimension()
        dimension_other = other.dimension()
        if dimension_self != dimension_other:
            print("Les matrices doivent avoir les mêmes dimensions pour être additionnées.")
            return None
        result = []
        i = 0
        for i in range(len(self.matrice)):
            vecteur_somme = self.matrice[i] + other.matrice[i]
            resultat_vecteur = t_vecteur(vecteur_somme)
            result.append(resultat_vecteur)
        matrice_resultat = t_matrice(result)
        return matrice_resultat

    def __mul__(self, scalaire):
        """Multiplie la matrice par un scalaire"""
        result = []
        i = 0
        for i in range(len(self.matrice)):
            vecteur_multiplie = self.matrice[i] * scalaire
            resultat_vecteur = t_vecteur(vecteur_multiplie)
            result.append(resultat_vecteur)
        matrice_resultat = t_matrice(result)
        return matrice_resultat

    def transposee(self):
        """Retourne la transposée de la matrice"""
        nb_lignes, nb_colonnes = self.dimension()
        if nb_lignes == 0:
            return t_matrice([])
        result = []
        j = 0
        for j in range(nb_colonnes):
            colonne = self.get_colonne(j)
            result.append(colonne)
        matrice_transposee = t_matrice(result)
        return matrice_transposee


    def __matmul__(self, other):
        """
        Gère le produit Matrice @ Vecteur 
        OU le produit Matrice @ Matrice
        """
        nb_col_self, _ = (self.dimension()[1], self.dimension()[0])
        nb_lignes_other, nb_col_other = other.dimension()
        
        if nb_col_self != nb_lignes_other:
            print("Les dimensions ne sont pas compatibles pour le produit matriciel")
            return None
        
        result = []
        i = 0
        for i in range(len(self.matrice)):
            ligne_resultat = []
            j = 0
            for j in range(nb_col_other):
                colonne_other = other.get_colonne(j)
                produit_scalaire = self.matrice[i].__matmul__(colonne_other)
                ligne_resultat.append(produit_scalaire)
            vecteur_ligne = t_vecteur(ligne_resultat)
            result.append(vecteur_ligne)
        
        matrice_resultat = t_matrice(result)
        return matrice_resultat

    # outil pivot de gauss

    def echange_lignes(self, i, j):
        """Échange la ligne i et la ligne j (L_i <-> L_j)"""
        temp = self.matrice[i]
        self.matrice[i] = self.matrice[j]
        self.matrice[j] = temp

    def multiplie_ligne(self, i, k):
        """Multiplie la ligne i par un coefficient k (L_i <- k*L_i)"""
        vecteur_multiplie = self.matrice[i] * k
        self.matrice[i] = t_vecteur(vecteur_multiplie)

    def ajoute_ligne(self, i, j, k):
        """Ajoute à la ligne i le produit de la ligne j par k (L_i <- L_i + k*L_j)"""
        vecteur_j_multiplie = self.matrice[j] * k
        vecteur_j = t_vecteur(vecteur_j_multiplie)
        resultat = self.matrice[i] + vecteur_j
        self.matrice[i] = t_vecteur(resultat)

    # autres méthodes

    def forme_echelonnee(self):
        """Applique l'algorithme du Pivot de Gauss pour échelonner la matrice"""
        pass

    def rang(self):
        """Retourne le rang de la matrice"""
        pass

    def determinant(self):
        """Calcule le déterminant (si carrée)"""
        pass

    def est_inversible(self):
        """Vérifie si la matrice est inversible"""
        pass