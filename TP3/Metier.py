from abc import ABC, abstractmethod

class Personne(ABC):
    """Classe abstraite de base représentant une personne."""

    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    @abstractmethod
    def afficher(self) -> str:
        pass

    def __str__(self) -> str:
        return self.afficher()

class Etudiant(Personne):
    """Classe représentant un étudiant."""

    def __init__(self, nom: str, age: int, numero_etudiant: str, moyenne: float = 0.0, liste_cours: list = None):
        super().__init__(nom, age)
        self.numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.liste_cours = liste_cours if liste_cours is not None else []

    def afficher(self) -> str:
        return f"Étudiant: {self.nom}, Age: {self.age}, Numéro Étudiant: {self.numero_etudiant}, Moyenne: {self.moyenne}, Cours: {', '.join(self.liste_cours)}"


class Professeur(Personne):
    """Classe représentant un professeur."""

    def __init__(self, nom: str, age: int, numero_professeur: str, cours: str):
        super().__init__(nom, age)
        self.numero_professeur = numero_professeur
        self.cours = cours

    def afficher(self) -> str:
        return f"Professeur: {self.nom}, Age: {self.age}, Numéro Professeur: {self.numero_professeur}, Cours: {self.cours}"

class Cours:
    """Classe représentant un cours."""

    def __init__(self, nom: str, professeur: str):
        self.nom = nom
        self.professeur = professeur

    def __str__(self) -> str:
        return f"Cours: {self.nom}, Professeur: {self.professeur}"