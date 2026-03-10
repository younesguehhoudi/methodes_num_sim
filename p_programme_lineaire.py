from p_matrice import t_matrice
from p_vecteur import t_vecteur

class t_programme_lineaire:
    """
    Résout un programme linéaire de la forme :
    minimiser/maximiser c^T * x,
    sous contraintes A*x <= b, x >= 0,
    via l'algorithme du simplexe.
    """
    
    def __init__(self, c, A, b, minimiser=True):
        """
        Constructeur du programme linéaire
        c : vecteur de coûts (t_vecteur)
        A : matrice de contraintes (t_matrice)
        b : vecteur B des contraintes (t_vecteur)
        minimiser : True pour minimisation, False pour maximisation
        """
        self.c = c if isinstance(c, t_vecteur) else t_vecteur(c)
        if isinstance(A, t_matrice):
            self.A = A
        else:
            self.A = t_matrice([t_vecteur(row) for row in A])
        self.b = b if isinstance(b, t_vecteur) else t_vecteur(b)
        self.minimiser = minimiser

    def _construire_tableau_initial(self, m, n, nb_ecart):
        """Construit le tableau initial du simplexe."""
        lignes = []

        for i in range(m):
            ligne = []
            for j in range(n):
                ligne.append(self.A[i][j])
            for j in range(nb_ecart):
                ligne.append(1.0 if i == j else 0.0)
            ligne.append(self.b[i])
            lignes.append(t_vecteur(ligne))

        ligne_zero = []
        for j in range(n):
            coeff = -self.c[j] if self.minimiser else self.c[j]
            ligne_zero.append(coeff)
        for j in range(nb_ecart):
            ligne_zero.append(0.0)
        ligne_zero.append(0.0)
        lignes.append(t_vecteur(ligne_zero))

        return t_matrice(lignes)

    def _choisir_colonne_pivot(self, tableau, ligne_obj, nb_colonnes, epsilon):
        """Retourne la colonne pivot ou -1 si l'optimum est atteint."""
        col_pivot = -1
        min_coeff = -epsilon

        for j in range(nb_colonnes):
            coeff = tableau[ligne_obj][j]
            if coeff < min_coeff:
                min_coeff = coeff
                col_pivot = j

        return col_pivot

    def _choisir_ligne_pivot(self, tableau, m, col_pivot, epsilon):
        """Retourne la ligne pivot ou -1 si le problème est non borné."""
        ligne_pivot = -1
        ratio_min = float('inf')

        for i in range(m):
            if tableau[i][col_pivot] > epsilon:
                ratio = tableau[i][-1] / tableau[i][col_pivot]
                if ratio >= 0 and ratio < ratio_min:
                    ratio_min = ratio
                    ligne_pivot = i

        return ligne_pivot

    def _extraire_solution(self, tableau, m, n, nb_ecart, epsilon):
        """Extrait la solution du tableau final."""
        solution = [0.0] * n

        for i in range(m):
            col_nonzero = -1
            count = 0
            for j in range(n + nb_ecart):
                if abs(tableau[i][j]) >= epsilon:
                    count += 1
                    col_nonzero = j

            if count == 1 and col_nonzero < n and abs(tableau[i][col_nonzero] - 1.0) < epsilon:
                solution[col_nonzero] = tableau[i][-1]

        return t_vecteur(solution)
    
    def resoudre(self):
        """
        Résout le programme linéaire avec l'algorithme du Simplexe.
        Retourne un tuple (solution, valeur_optimale)
        """
        epsilon = 1e-10
        m, n = self.A.dimension()
        nb_ecart = m
        tableau = self._construire_tableau_initial(m, n, nb_ecart)

        iterations = 0
        max_iterations = 10000
        ligne_obj = m
        nb_colonnes = n + nb_ecart

        while iterations < max_iterations:
            iterations += 1

            col_pivot = self._choisir_colonne_pivot(tableau, ligne_obj, nb_colonnes, epsilon)
            if col_pivot == -1:
                break

            ligne_pivot = self._choisir_ligne_pivot(tableau, m, col_pivot, epsilon)
            if ligne_pivot == -1:
                return None, None

            tableau.pivot_gauss(ligne_pivot, col_pivot, 0, m + 1, epsilon)

        solution = self._extraire_solution(tableau, m, n, nb_ecart, epsilon)
        valeur_optimale = tableau[m][-1]
        return solution, valeur_optimale
