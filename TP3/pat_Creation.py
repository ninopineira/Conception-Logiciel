from Metier import *
from pat_Comportement import *

class ScolaritéManager(Observateur):
    """Singleton pour gérer les opérations de scolarité."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScolaritéManager, cls).__new__(cls)
            cls._instance.etudiants = []
            cls._instance.cours = []
        return cls._instance

    def ajouter_etudiant(self, etudiant: Etudiant):
        self.etudiants.append(etudiant)

    def ajouter_cours(self, cours: Cours):
        self.cours.append(cours)

    def afficher_etudiants(self):
        for etudiant in self.etudiants:
            print(etudiant)

    def afficher_cours(self):
        for cours in self.cours:
            print(cours)
    
    def calculer_moyenne_generale(self):
        if not self.etudiants:
            return 0.0
        total_moyenne = sum(etudiant.moyenne for etudiant in self.etudiants)
        return total_moyenne / len(self.etudiants)

    def afficher_stats(self):
        print(f"Nombre d'étudiants: {len(self.etudiants)}")
        print(f"Nombre de cours: {len(self.cours)}")
        print(f"Moyenne générale des étudiants: {self.calculer_moyenne_generale()}")

    def update(self, message):
        print(f"ScolaritéManager a reçu une mise à jour: {message}")
        self.afficher_stats()

class PersonneFactory:
    """Factory pour créer des instances de Personne."""

    @staticmethod
    def creer_personne(type_personne: str, nom: str, age: int, numero: str, moyenne: float = None, liste_cours: list = None, cours: str = None) -> Personne:
        if type_personne == "etudiant":
            return Etudiant(nom, age, numero, moyenne, liste_cours)
        elif type_personne == "professeur":
            return Professeur(nom, age, numero, cours)
        else:
            raise ValueError("Type de personne inconnu")
        


