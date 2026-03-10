from p_matrice import t_matrice

class t_application_lineaire:
    """Représente une application linéaire via sa matrice associée."""

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
    
    def dimension_depart(self):
        """retorune la dimension de l'espace de depart"""
        dim = self.matrice.dimension()
        return dim[1]
    
    def dimension_arrivee(self):
        """retorune la dimension de l'espace d'arivée"""
        dim = self.matrice.dimension()
        return dim[0]
    
    def __call__(self, vecteur):
        """permet d'apeler l'aplication comme une fonction : f(v)"""
        return self.matrice @ vecteur
    
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
    
    def dimension_image(self):
        """retorune la dimension de l'image dim(Im(f))"""
        return self.matrice.rang()
    
    def dimension_noyau(self):
        """retorune la dimension du noyau dim(Ker(f)) par le theoreme du rang"""
        # theoreme du rang : dim(Ker(f)) + dim(Im(f)) = dim(depart)
        return self.dimension_depart() - self.dimension_image()
    
    def est_injective(self):
        """retorune True si l'aplication est injective (Ker(f) = {0})"""
        # injective ssi dim(Ker(f)) = 0 ssi rang = dim(depart)
        return self.dimension_noyau() == 0
    
    def est_surjective(self):
        """retorune True si l'aplication est surjective (Im(f) = espace d'arivée)"""
        # surjective ssi dim(Im(f)) = dim(arivée) ssi rang = dim(arivée)
        return self.matrice.rang() == self.dimension_arrivee()
    
    def est_bijective(self):
        """retorune True si l'aplication est bijective (injective ET surjective)"""
        return self.est_injective() and self.est_surjective()
    
    def est_endomorphisme(self):
        """retorune True si l'aplication est un endomorphisme (depart = arivée)"""
        return self.dimension_depart() == self.dimension_arrivee()
    
    def est_automorphisme(self):
        """retorune True si c'est un automorphisme (endomorphisme bijectif)"""
        return self.est_endomorphisme() and self.est_bijective()
    
    def est_inversible(self):
        """retorune True si l'aplication est inversible (= automorphisme)"""
        return self.est_automorphisme()
    