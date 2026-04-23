"""
metier.py — Couche 2 : Modèles métier
Importe uniquement : interfaces.py
"""

from __future__ import annotations
from abc import abstractmethod
from interfaces import Observable


class Personne:
    """Classe abstraite de base représentant une personne."""

    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    @abstractmethod
    def afficher(self) -> str:
        pass

    def __str__(self) -> str:
        return self.afficher()


class Etudiant(Personne, Observable):
    """Représente un étudiant."""

    def __init__(self, nom: str, age: int, numero_etudiant: str,
                 moyenne: float = 0.0, liste_cours: list = None):
        Personne.__init__(self, nom, age)
        Observable.__init__(self)
        self.numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.liste_cours = liste_cours if liste_cours is not None else []

    def ajouter_cours(self, cours: str) -> None:
        self.liste_cours.append(cours)

    def set_moyenne(self, moyenne: float) -> None:
        """Modifie la moyenne et notifie les observateurs (pattern Observer)."""
        self.moyenne = moyenne
        self.notifier_observateurs()

    def afficher(self) -> str:
        cours_str = ", ".join(self.liste_cours) if self.liste_cours else "Aucun"
        return (f"Étudiant: {self.nom} | Âge: {self.age} | "
                f"N°: {self.numero_etudiant} | Moyenne: {self.moyenne} | "
                f"Cours: {cours_str}")


class Professeur(Personne):
    """Représente un professeur."""

    def __init__(self, nom: str, age: int, numero_professeur: str, cours: str):
        super().__init__(nom, age)
        self.numero_professeur = numero_professeur
        self.cours = cours

    def afficher(self) -> str:
        return (f"Professeur: {self.nom} | Âge: {self.age} | "
                f"N°: {self.numero_professeur} | Cours: {self.cours}")


class Cours:
    """Unité d'enseignement."""

    def __init__(self, nom: str, professeur: str):
        self.nom = nom
        self.professeur = professeur

    def __str__(self) -> str:
        return f"Cours: {self.nom} | Professeur: {self.professeur}"
