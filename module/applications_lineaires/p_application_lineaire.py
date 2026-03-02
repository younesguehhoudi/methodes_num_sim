import sys
sys.path.append('..')
from algebre_lineaire.p_matrice import t_matrice
from algebre_lineaire.p_vecteur import t_vecteur
from p_famille_vecteurs import t_famille_vecteurs

class t_application_lineaire:

    def __init__(self, matrice_associee):
        """Constructeur qui prend une t_matrice comme matrice associé a l'aplication"""
        self.matrice = matrice_associee
    
    def __del__(self):
        """Detruit l'attribut matrice de self"""
        del self.matrice
    
    def __repr__(self):
        try :
            return "application_lineaire(" + str(self.matrice) + ")"
        except AttributeError :
            return "application non existante"
    
    def __str__(self):
        """Affichage pour humain de l'aplication lineaire"""
        chaine = "Application lineaire de matrice :\n"
        chaine += str(self.matrice)
        return chaine
    
    def get_matrice(self):
        """retorune la matrice associé a l'aplication"""
        return self.matrice
    
    def dimension_depart(self):
        """retorune la dimension de l'espace de depart"""
        dim = self.matrice.dimension()
        return dim[1]
    
    def dimension_arrivee(self):
        """retorune la dimension de l'espace d'arivée"""
        dim = self.matrice.dimension()
        return dim[0]
    
    def appliquer(self, vecteur):
        """calcule f(v) = M * v (produit matrice vecteur)"""
        # on converti le vecteur en matrice colonne
        mat_vecteur = t_matrice([vecteur])
        mat_vecteur = mat_vecteur.transposee()
        
        # produit matriciel
        resultat_mat = self.matrice @ mat_vecteur
        
        # on converti le resultat en vecteur
        vecteur_resultat = resultat_mat.get_colonne(0)
        return vecteur_resultat
    
    def __call__(self, vecteur):
        """permet d'apeler l'aplication comme une fonction : f(v)"""
        return self.appliquer(vecteur)
    
    def __add__(self, autre):
        """addition de 2 aplications lineaire (f+g)(v) = f(v) + g(v)"""
        mat_somme = self.matrice + autre.matrice
        if mat_somme is None:
            return None
        resultat = t_application_lineaire(mat_somme)
        return resultat
    
    def __mul__(self, scalaire):
        """multiplication par un scalaire (k*f)(v) = k*f(v)"""
        mat_produit = self.matrice * scalaire
        resultat = t_application_lineaire(mat_produit)
        return resultat
    
    def composer(self, autre):
        """composition de 2 aplications (g o f)(v) = g(f(v))"""
        # la matrice de g o f est le produit matriciel de g * f
        mat_composee = autre.matrice @ self.matrice
        if mat_composee is None:
            return None
        resultat = t_application_lineaire(mat_composee)
        return resultat
    
    def __matmul__(self, autre):
        """permet d'utiliser @ pour la composition"""
        return self.composer(autre)
    
    def rang(self):
        """retorune le rang de l'aplication lineaire"""
        return self.matrice.rang()
    
    def dimension_image(self):
        """retorune la dimension de l'image dim(Im(f))"""
        return self.rang()
    
    def dimension_noyau(self):
        """retorune la dimension du noyau dim(Ker(f)) par le theoreme du rang"""
        # theoreme du rang : dim(Ker(f)) + dim(Im(f)) = dim(depart)
        return self.dimension_depart() - self.dimension_image()
    
    def est_injective(self):
        """retorune True si l'aplication est injective (Ker(f) = {0})"""
        # injective ssi dim(Ker(f)) = 0 ssi rang = dim(depart)
        if self.dimension_noyau() == 0:
            return True
        else :
            return False
    
    def est_surjective(self):
        """retorune True si l'aplication est surjective (Im(f) = espace d'arivée)"""
        # surjective ssi dim(Im(f)) = dim(arivée) ssi rang = dim(arivée)
        if self.rang() == self.dimension_arrivee():
            return True
        else :
            return False
    
    def est_bijective(self):
        """retorune True si l'aplication est bijective (injective ET surjective)"""
        if self.est_injective() and self.est_surjective():
            return True
        else :
            return False
    
    def est_endomorphisme(self):
        """retorune True si l'aplication est un endomorphisme (depart = arivée)"""
        if self.dimension_depart() == self.dimension_arrivee():
            return True
        else :
            return False
    
    def est_automorphisme(self):
        """retorune True si c'est un automorphisme (endomorphisme bijectif)"""
        if self.est_endomorphisme() and self.est_bijective():
            return True
        else :
            return False
    
    def est_inversible(self):
        """retorune True si l'aplication est inversible (= automorphisme)"""
        return self.est_automorphisme()
    
    def inverse(self):
        """calcule l'aplication inverse si elle existe"""
        if not self.est_inversible():
            print("l'aplication n'est pas inversible")
            return None
        
        # pour calculer l'inverse on utilise la methode de gauss-jordan
        # on cree la matrice augmentée [M | I]
        n = self.dimension_depart()
        
        # creation de la matrice identité
        lignes_identite = []
        i = 0
        for i in range(n):
            ligne = []
            j = 0
            for j in range(n):
                if i == j:
                    ligne.append(1)
                else :
                    ligne.append(0)
            lignes_identite.append(t_vecteur(ligne))
        
        matrice_identite = t_matrice(lignes_identite)
        
        # concatenation horizontale [M | I]
        lignes_augmentee = []
        i = 0
        for i in range(n):
            ligne_m = self.matrice[i]
            ligne_i = matrice_identite[i]
            ligne_concat = []
            j = 0
            for j in range(n):
                ligne_concat.append(ligne_m[j])
            for j in range(n):
                ligne_concat.append(ligne_i[j])
            lignes_augmentee.append(t_vecteur(ligne_concat))
        
        mat_augmentee = t_matrice(lignes_augmentee)
        
        # pivot de gauss pour avoir [I | M^-1]
        mat_augmentee.forme_echelonnee()
        
        # extraction de la partie droite (l'inverse)
        lignes_inverse = []
        i = 0
        for i in range(n):
            ligne = []
            j = 0
            for j in range(n, 2*n):
                ligne.append(mat_augmentee[i][j])
            lignes_inverse.append(t_vecteur(ligne))
        
        matrice_inverse = t_matrice(lignes_inverse)
        resultat = t_application_lineaire(matrice_inverse)
        return resultat
    
    def noyau(self):
        """calcule une base du noyau Ker(f) = {v | f(v) = 0}"""
        # pour trouver le noyau on resout le systeme Mv = 0
        # on echelone la matrice et on trouve les variables libres
        
        mat_echelonnee = self.matrice.copy()
        mat_echelonnee.forme_echelonnee()
        
        # on identifie les colonnes pivots et les colonnes libres
        # implementation simplifiée : on retourne juste la dimension du noyau
        # pour l'instant (implementation complete plus complexe)
        print("calcul d'une base du noyau pas encore implementé completement")
        print("dimension du noyau:", self.dimension_noyau())
        return None
    
    def image(self):
        """calcule une base de l'image Im(f)"""
        # l'image est engendré par les colonnes de la matrice
        # on prend les colonnes qui sont linearement independantes
        
        nb_lignes, nb_colonnes = self.matrice.dimension()
        colonnes = []
        i = 0
        for i in range(nb_colonnes):
            col = self.matrice.get_colonne(i)
            colonnes.append(col)
        
        fam = t_famille_vecteurs(colonnes)
        base_image = fam.extraire_base()
        return base_image
