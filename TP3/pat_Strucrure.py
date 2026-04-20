from Metier import *
from typing import List

class EtudiantBoursier(Etudiant):
    """Classe représentant un étudiant boursier."""
    
    def __init__(self, nom: str, age: int, numero_etudiant: str, moyenne: float = 0.0, liste_cours: list = None, montant_bourse: float = 0.0):
        super().__init__(nom, age, numero_etudiant, moyenne, liste_cours)
        self.montant_bourse = montant_bourse

    def afficher(self) -> str:
        return f"Étudiant Boursier: {self.nom}, Age: {self.age}, Numéro Étudiant: {self.numero_etudiant}, Moyenne: {self.moyenne}, Cours: {', '.join(self.liste_cours)}, Montant Bourse: {self.montant_bourse}"

class EtudiantDelegue(Etudiant):
    """Classe représentant un étudiant délégué."""
    
    def __init__(self, nom: str, age: int, numero_etudiant: str, moyenne: float = 0.0, liste_cours: list = None, role_delegue: str = "Délégué de classe"):
        super().__init__(nom, age, numero_etudiant, moyenne, liste_cours)
        self.role_delegue = role_delegue

    def afficher(self) -> str:
        return f"Étudiant Délégué: {self.nom}, Age: {self.age}, Numéro Étudiant: {self.numero_etudiant}, Moyenne: {self.moyenne}, Cours: {', '.join(self.liste_cours)}, Rôle Délégué: {self.role_delegue}"
    



class LegacyCoursSystem:
    """Ancien système qui retourne des données de cours en format brut."""

    def get_cours_data(self) ->str:
        """Retourne des cours sous format 'NomCours,Professeur,...'"""
        return "Mathématiques Avancées,Dr. Dupont,Algorithmique,Prof. Martin,Physique Quantique,Dr. Leblanc"
    
class CoursAdapter:
    """Adapter pour convertir les données du LegacyCoursSystem en objets Cours."""

    def __init__(self, legacy_system: LegacyCoursSystem):
        self.legacy_system = legacy_system

    def get_cours(self) -> List[Cours]:
        cours_data = self.legacy_system.get_cours_data()
        cours_list = cours_data.split(',')
        cours_objects = []
        for i in range(0, len(cours_list), 2):
            nom_cours = cours_list[i].strip()
            professeur = cours_list[i + 1].strip()
            cours_objects.append(Cours(nom_cours, professeur))
        return cours_objects