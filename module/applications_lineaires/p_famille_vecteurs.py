import sys
sys.path.append('..')
from algebre_lineaire.p_matrice import t_matrice
from algebre_lineaire.p_vecteur import t_vecteur

class t_famille_vecteurs:

    def __init__(self, liste_vecteurs):
        """Constructeur qui prend une liste de t_vecteur et cree une fammile"""
        self.vecteurs = liste_vecteurs[:]
    
    def __del__(self):
        """Detruit l'attribut vecteurs de self"""
        del self.vecteurs
    
    def __repr__(self):
        try :
            return "famille_vecteurs(" + str(self.vecteurs) + ")"
        except AttributeError :
            return "famille non existante"
    
    def __str__(self):
        """Affichage pour humain"""
        chaine = "{"
        i = 0
        for i in range(len(self.vecteurs)):
            chaine += str(self.vecteurs[i])
            if i < len(self.vecteurs) - 1:
                chaine += ", "
        chaine += "}"
        return chaine
    
    def __getitem__(self, key):
        """retorune le vecteur a l'indice key"""
        return self.vecteurs[key]
    
    def nombre_vecteurs(self):
        """retorune le nombre de vecteur dans la fammile"""
        return len(self.vecteurs)
    
    def dimension_vecteurs(self):
        """retorune la dimension des vecteurs (si ils sont de meme dim)"""
        if len(self.vecteurs) == 0:
            return 0
        return self.vecteurs[0].dimension()
    
    def vers_matrice(self):
        """converti la fammile en matrice (chaque vecteur devient une ligne)"""
        if len(self.vecteurs) == 0:
            return None
        mat = t_matrice(self.vecteurs)
        return mat
    
    def rang_famille(self):
        """calcule le rang de la fammile (nombre max de vecteurs independant)"""
        mat = self.vers_matrice()
        if mat is None:
            return 0
        return mat.rang()
    
    def est_libre(self):
        """retorune True si la fammile est lineairement independante"""
        rg = self.rang_famille()
        nb = self.nombre_vecteurs()
        if rg == nb:
            return True
        else :
            return False
    
    def est_liee(self):
        """retorune True si la fammile est lineairement dependante"""
        return not self.est_libre()
    
    def sont_colineaires(self):
        """retorune True si 2 vecteurs sont colineaire (fammile liée avec 2 vecteurs)
        marche seulemnt pour une fammile de 2 vecteurs"""
        if self.nombre_vecteurs() != 2:
            print("la methode sont_colineaires marche seulemnt pour 2 vecteurs")
            return None
        # si le rang est 1 alors les vecteurs sont colineaire
        # si le rang est 2 alors ils sont independant
        rg = self.rang_famille()
        if rg == 1:
            return True
        else :
            return False
    
    def est_generatrice(self, dimension_espace):
        """retorune True si la fammile engendre l'espace de dimension_espace"""
        rg = self.rang_famille()
        if rg == dimension_espace:
            return True
        else :
            return False
    
    def est_base(self, dimension_espace):
        """retorune True si la fammile est une base (libre ET generatrice)"""
        if self.est_libre() and self.est_generatrice(dimension_espace):
            return True
        else :
            return False
    
    def dimension_vect(self):
        """retorune la dimension de l'espace vectoriel engendré par la fammile"""
        return self.rang_famille()
    
    def extraire_base(self):
        """extrai une base de la fammile (enleve les vecteurs en trop)"""
        # on garde les vecteurs qui sont independant
        vecteurs_base = []
        i = 0
        for i in range(len(self.vecteurs)):
            temp_vecteurs = vecteurs_base[:]
            temp_vecteurs.append(self.vecteurs[i])
            temp_famille = t_famille_vecteurs(temp_vecteurs)
            if temp_famille.est_libre():
                vecteurs_base.append(self.vecteurs[i])
        resultat = t_famille_vecteurs(vecteurs_base)
        return resultat
    
    def contient_vecteur_nul(self):
        """retorune True si la fammile contient le vecteur nul"""
        i = 0
        for i in range(len(self.vecteurs)):
            temp = self.vecteurs[i]
            est_nul = True
            j = 0
            for j in range(temp.dimension()):
                if temp[j] != 0:
                    est_nul = False
                    break
            if est_nul:
                return True
        return False
