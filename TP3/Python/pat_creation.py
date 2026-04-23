"""
pat_creation.py — Couche 4 : Patterns de création
Importe : interfaces.py, metier.py, pat_comportement.py
Contient : ScolariteManager (Singleton + Observateur), PersonneFactory
"""

from __future__ import annotations
from typing import Optional
from interfaces import Observateur, Observable, Strategie
from metier import Etudiant, Professeur, Cours
from pat_comportement import TriParMoyenne


# =============================================================================
# PATTERN SINGLETON + OBSERVATEUR
# =============================================================================

class ScolariteManager(Observateur):
    """
    Gestionnaire central unique (Singleton).
    Implémente Observateur : reçoit les notifications des étudiants.
    Utilise une Strategie pour le tri (Strategy).
    """

    _instance: Optional[ScolariteManager] = None

    def __new__(cls) -> ScolariteManager:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.etudiants = []
            cls._instance.cours = []
            cls._instance._strategie = TriParMoyenne()
        return cls._instance

    # --- Gestion des étudiants ---

    def ajouter_etudiant(self, etudiant: Etudiant) -> None:
        """Ajoute un étudiant et s'enregistre comme observateur."""
        self.etudiants.append(etudiant)
        etudiant.ajouter_observateur(self)

    def ajouter_cours(self, cours: Cours) -> None:
        self.cours.append(cours)

    def afficher_etudiants(self) -> None:
        for etudiant in self.etudiants:
            print(f"  {etudiant}")

    def afficher_cours(self) -> None:
        for cours in self.cours:
            print(f"  {cours}")

    # --- Statistiques ---

    def calculer_moyenne_generale(self) -> float:
        if not self.etudiants:
            return 0.0
        return sum(e.moyenne for e in self.etudiants) / len(self.etudiants)

    def afficher_stats(self) -> None:
        moyennes = [e.moyenne for e in self.etudiants]
        moy_gen = self.calculer_moyenne_generale()
        print(f"  Nb étudiants: {len(self.etudiants)} | "
              f"Moyenne générale: {moy_gen:.2f} | "
              f"Max: {max(moyennes, default=0):.2f} | "
              f"Min: {min(moyennes, default=0):.2f}")

    # --- Pattern Observer : réception des notifications ---

    def mettre_a_jour(self, sujet: Observable) -> None:
        """
        Appelé automatiquement quand un étudiant change de moyenne.
        On cast vers Etudiant ici car pat_creation connaît Etudiant.
        """
        if isinstance(sujet, Etudiant):
            print(f"  [Notification] {sujet.nom} → nouvelle moyenne : {sujet.moyenne:.2f}")
            self.afficher_stats()

    # --- Pattern Strategy : tri ---

    def set_strategie(self, strategie: Strategie) -> None:
        self._strategie = strategie

    def lister_etudiants_tries(self) -> list:
        return self._strategie.trier(self.etudiants)


# =============================================================================
# PATTERN FACTORY METHOD
# =============================================================================

class PersonneFactory:
    """
    Factory centralisée pour créer des Personnes.
    Le client ne connaît pas les détails d'instanciation.
    """

    @staticmethod
    def creer_personne(type_personne: str, nom: str, age: int, numero: str,
                       moyenne: float = 0.0, liste_cours: list = None,
                       cours: str = None):
        type_personne = type_personne.lower()
        if type_personne == "etudiant":
            return Etudiant(nom, age, numero, moyenne, liste_cours or [])
        elif type_personne == "professeur":
            return Professeur(nom, age, numero, cours or "")
        else:
            raise ValueError(f"Type de personne inconnu : '{type_personne}'")
