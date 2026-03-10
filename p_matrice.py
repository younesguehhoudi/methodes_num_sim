from p_vecteur import t_vecteur

class t_matrice:
    """Représentation d'une matrice comme liste de vecteurs lignes."""

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

    def _vers_vecteur(self, ligne):
        """Convertit une ligne en `t_vecteur` si nécessaire."""
        if isinstance(ligne, t_vecteur):
            return ligne
        return t_vecteur(ligne)

    def _ligne_non_nulle(self, ligne, epsilon):
        """Retourne `True` si la ligne contient un coefficient non nul."""
        j = 0
        for j in range(ligne.dimension()):
            if abs(ligne[j]) >= epsilon:
                return True
        return False


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

    def colonnes(self):
        """Retourne la liste des colonnes de la matrice."""
        nb_lignes, nb_colonnes = self.dimension()
        if nb_lignes == 0:
            return []
        return [self.get_colonne(j) for j in range(nb_colonnes)]

    def est_carree(self):
        """Vérifie si la matrice est carrée"""
        nb_lignes, nb_colonnes = self.dimension()
        return nb_lignes == nb_colonnes

    def __add__(self, other):
        """Additionne deux matrices"""
        dimension_self = self.dimension()
        dimension_other = other.dimension()
        if dimension_self != dimension_other:
            return None
        result = []
        i = 0
        for i in range(len(self.matrice)):
            vecteur_somme = self.matrice[i] + other.matrice[i]
            result.append(self._vers_vecteur(vecteur_somme))
        matrice_resultat = t_matrice(result)
        return matrice_resultat

    def __mul__(self, scalaire):
        """Multiplie la matrice par un scalaire"""
        result = []
        i = 0
        for i in range(len(self.matrice)):
            vecteur_multiplie = self.matrice[i] * scalaire
            result.append(self._vers_vecteur(vecteur_multiplie))
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
        if isinstance(other, t_vecteur):
            nb_col_self = self.dimension()[1]
            if nb_col_self != other.dimension():
                return None

            resultat = []
            for i in range(len(self.matrice)):
                resultat.append(self.matrice[i].__matmul__(other))
            return t_vecteur(resultat)

        nb_col_self = self.dimension()[1]
        nb_lignes_other, nb_col_other = other.dimension()
        
        if nb_col_self != nb_lignes_other:
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


    def copy(self):
        """retorune une copie de la matrice"""
        vecteurs_copie = []
        i = 0
        for i in range(len(self.matrice)):
            coord_copie = []
            j = 0
            for j in range(self.matrice[i].dimension()):
                coord_copie.append(self.matrice[i][j])
            vecteurs_copie.append(t_vecteur(coord_copie))
        return t_matrice(vecteurs_copie)

    def echange_lignes(self, i, j):
        """Échange la ligne i et la ligne j (L_i <-> L_j)"""
        temp = self.matrice[i]
        self.matrice[i] = self.matrice[j]
        self.matrice[j] = temp

    def multiplie_ligne(self, i, k):
        """Multiplie la ligne i par un coefficient k (L_i <- k*L_i)"""
        self.matrice[i] = self._vers_vecteur(self.matrice[i] * k)

    def ajoute_ligne(self, i, j, k):
        """Ajoute à la ligne i le produit de la ligne j par k (L_i <- L_i + k*L_j)"""
        vecteur_j = self._vers_vecteur(self.matrice[j] * k)
        resultat = self.matrice[i] + vecteur_j
        self.matrice[i] = self._vers_vecteur(resultat)

    def pivot_gauss(self, ligne_pivot, colonne_pivot, debut=0, fin=None, epsilon=1e-10):
        """Applique un pivot de Gauss sur une colonne donnée."""
        if fin is None:
            fin = len(self.matrice)

        pivot = self.matrice[ligne_pivot][colonne_pivot]
        if abs(pivot) < epsilon:
            return False

        self.multiplie_ligne(ligne_pivot, 1.0 / pivot)

        for i in range(debut, fin):
            if i != ligne_pivot:
                facteur = self.matrice[i][colonne_pivot]
                if abs(facteur) >= epsilon:
                    self.ajoute_ligne(i, ligne_pivot, -facteur)

        return True

    @classmethod
    def identite(cls, n):
        """Construit la matrice identité de taille n."""
        lignes_identite = []
        for i in range(n):
            ligne = [1 if i == j else 0 for j in range(n)]
            lignes_identite.append(t_vecteur(ligne))
        return cls(lignes_identite)

    def concatener_horizontalement(self, other):
        """Concatène horizontalement deux matrices [self | other]."""
        nb_lignes_self, _ = self.dimension()
        nb_lignes_other, _ = other.dimension()
        if nb_lignes_self != nb_lignes_other:
            return None

        lignes = []
        for i in range(nb_lignes_self):
            ligne = list(self[i].coordonnees) + list(other[i].coordonnees)
            lignes.append(t_vecteur(ligne))
        return t_matrice(lignes)

    def extraire_colonnes(self, debut, fin):
        """Extrait les colonnes d'indice debut à fin-1."""
        lignes = []
        for i in range(self.dimension()[0]):
            ligne = [self[i][j] for j in range(debut, fin)]
            lignes.append(t_vecteur(ligne))
        return t_matrice(lignes)

    def forme_echelonnee(self):
        """Applique l'algorithme du Pivot de Gauss pour échelonner la matrice"""
        #foeme echelonnee d'une matrice
        epsilon = 1e-10
        nb_lignes, nb_colonnes = self.dimension()
        for i in range(min(nb_lignes, nb_colonnes)):
            # Trouver le pivot
            pivot = self.matrice[i][i]
            if abs(pivot) < epsilon:
                # Si le pivot est nul, essayer de trouver une ligne en dessous pour échanger
                for j in range(i + 1, nb_lignes):
                    if abs(self.matrice[j][i]) >= epsilon:
                        self.echange_lignes(i, j)
                        pivot = self.matrice[i][i]
                        break
            
            if abs(pivot) >= epsilon:
                self.pivot_gauss(i, i, i + 1, nb_lignes, epsilon)

    def rang(self):
        """Retourne le rang de la matrice"""
        epsilon = 1e-10
        matrice_echelonnee = self.copy()
        matrice_echelonnee.forme_echelonnee()
        nb_lignes, _ = matrice_echelonnee.dimension()
        rang = 0
        for i in range(nb_lignes):
            ligne = matrice_echelonnee.matrice[i]
            if self._ligne_non_nulle(ligne, epsilon):
                rang += 1
        return rang

    def determinant(self):
        """Calcule le déterminant (si carrée)"""
        if not self.est_carree():
            return None
        epsilon = 1e-10
        matrice_temp = self.copy()
        n = matrice_temp.dimension()[0]
        determinant = 1.0
        signe = 1

        for i in range(n):
            ligne_pivot = i
            while ligne_pivot < n and abs(matrice_temp[ligne_pivot][i]) < epsilon:
                ligne_pivot += 1

            if ligne_pivot == n:
                return 0.0

            if ligne_pivot != i:
                matrice_temp.echange_lignes(i, ligne_pivot)
                signe *= -1

            pivot = matrice_temp[i][i]
            determinant *= pivot

            for j in range(i + 1, n):
                facteur = matrice_temp[j][i] / pivot
                matrice_temp.ajoute_ligne(j, i, -facteur)

        return signe * determinant

    def est_inversible(self):
        """Vérifie si la matrice est inversible"""
        return self.rang() == self.dimension()[0]

    def inverse(self):
        """Calcule l'inverse de la matrice si elle existe."""
        if not self.est_inversible():
            return None

        epsilon = 1e-10
        n = self.dimension()[0]
        mat_augmentee = self.concatener_horizontalement(t_matrice.identite(n))
        if mat_augmentee is None:
            return None

        for i in range(n):
            ligne_pivot = i
            while ligne_pivot < n and abs(mat_augmentee[ligne_pivot][i]) < epsilon:
                ligne_pivot += 1

            if ligne_pivot == n:
                return None

            if ligne_pivot != i:
                mat_augmentee.echange_lignes(i, ligne_pivot)

            if not mat_augmentee.pivot_gauss(i, i, 0, n, epsilon):
                return None

        return mat_augmentee.extraire_colonnes(n, 2 * n)

    def colonnes_pivots(self, epsilon=1e-10):
        """Retourne les indices des colonnes pivots de la forme échelonnée."""
        mat_copy = self.copy()
        mat_copy.forme_echelonnee()

        nb_lignes, nb_colonnes = mat_copy.dimension()
        pivots = []
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                if abs(mat_copy[i][j]) >= epsilon:
                    pivots.append(j)
                    break
        return pivots

    def colonnes_libres(self, epsilon=1e-10):
        """Retourne les indices des colonnes libres."""
        _, nb_colonnes = self.dimension()
        pivots = set(self.colonnes_pivots(epsilon))
        return [j for j in range(nb_colonnes) if j not in pivots]

    def noyau(self, epsilon=1e-10):
        """Retourne une base du noyau de la matrice."""
        mat_copy = self.copy()
        mat_copy.forme_echelonnee()

        nb_lignes, nb_colonnes = mat_copy.dimension()
        colonnes_pivots = mat_copy.colonnes_pivots(epsilon)
        colonnes_libres = mat_copy.colonnes_libres(epsilon)

        vecteurs_noyau = []
        for j_libre in colonnes_libres:
            x = [0.0] * nb_colonnes
            x[j_libre] = 1.0

            for i in range(len(colonnes_pivots) - 1, -1, -1):
                col_pivot = colonnes_pivots[i]
                somme = 0.0
                for j in range(col_pivot + 1, nb_colonnes):
                    somme += mat_copy[i][j] * x[j]

                if abs(mat_copy[i][col_pivot]) >= epsilon:
                    x[col_pivot] = -somme / mat_copy[i][col_pivot]

            vecteurs_noyau.append(t_vecteur(x))

        return vecteurs_noyau

    def image(self, epsilon=1e-10):
        """Retourne une base de l'image de la matrice."""
        indices_pivots = self.colonnes_pivots(epsilon)
        return [self.get_colonne(j) for j in indices_pivots]