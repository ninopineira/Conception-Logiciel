"""
pat_structure.py — Couche 3 : Patterns de structure
Importe : interfaces.py, metier.py
Contient : EtudiantDecorator, EtudiantBoursier, EtudiantDelegue,
           LegacyCoursSystem, CoursAdapter
"""

from __future__ import annotations
from typing import List
from metier import Etudiant, Cours


# =============================================================================
# PATTERN DECORATOR
# =============================================================================

class EtudiantDecorator(Etudiant):
    """
    Classe de base des décorateurs d'Etudiant.
    Enveloppe un Etudiant et délègue tous les appels à lui.
    """

    def __init__(self, etudiant: Etudiant):
        # On ne rappelle pas super().__init__() : on délègue à l'étudiant enveloppé
        self._etudiant = etudiant

    # --- Délégation des propriétés ---

    @property
    def nom(self) -> str:
        return self._etudiant.nom

    @property
    def age(self) -> int:
        return self._etudiant.age

    @property
    def moyenne(self) -> float:
        return self._etudiant.moyenne

    @property
    def numero_etudiant(self) -> str:
        return self._etudiant.numero_etudiant

    @property
    def liste_cours(self) -> list:
        return self._etudiant.liste_cours

    # --- Délégation des méthodes ---

    def set_moyenne(self, moyenne: float) -> None:
        self._etudiant.set_moyenne(moyenne)

    def ajouter_cours(self, cours: str) -> None:
        self._etudiant.ajouter_cours(cours)

    def ajouter_observateur(self, obs) -> None:
        self._etudiant.ajouter_observateur(obs)

    def afficher(self) -> str:
        return self._etudiant.afficher()


class EtudiantBoursier(EtudiantDecorator):
    """Décorateur : ajoute la notion de bourse à un étudiant."""

    def __init__(self, etudiant: Etudiant, montant_bourse: float):
        super().__init__(etudiant)
        self.montant_bourse = montant_bourse

    def afficher(self) -> str:
        return f"{self._etudiant.afficher()} | Boursier: {self.montant_bourse:.0f}€/an"


class EtudiantDelegue(EtudiantDecorator):
    """Décorateur : ajoute le rôle de délégué à un étudiant."""

    def __init__(self, etudiant: Etudiant, role_delegue: str = "Délégué de classe"):
        super().__init__(etudiant)
        self.role_delegue = role_delegue

    def afficher(self) -> str:
        return f"{self._etudiant.afficher()} | Délégué: {self.role_delegue}"


# =============================================================================
# PATTERN ADAPTER
# =============================================================================

class LegacyCoursSystem:
    """Ancien système retournant les cours en chaîne concaténée."""

    def get_cours_data(self) -> str:
        """Retourne des cours sous format 'NomCours,Professeur,...'"""
        return ("Mathématiques Avancées,Dr. Dupont,"
                "Algorithmique,Prof. Martin,"
                "Physique Quantique,Dr. Leblanc")


class CoursAdapter:
    """
    Adapter : convertit la chaîne du système legacy en objets Cours
    compatibles avec le système actuel.
    """

    def __init__(self, legacy_system: LegacyCoursSystem):
        self._legacy = legacy_system

    def get_cours(self) -> List[Cours]:
        parties = self._legacy.get_cours_data().split(",")
        cours_list = []
        for i in range(0, len(parties) - 1, 2):
            nom = parties[i].strip()
            prof = parties[i + 1].strip()
            cours_list.append(Cours(nom, prof))
        return cours_list
