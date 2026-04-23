"""
pat_comportement.py — Couche 3 : Patterns de comportement
Importe : interfaces.py, metier.py
Contient : TriParMoyenne, TriParNom
"""

from interfaces import Strategie
from metier import Etudiant


class TriParMoyenne(Strategie):
    """Trie les étudiants par moyenne décroissante."""

    def trier(self, elements: list) -> list:
        return sorted(elements, key=lambda e: e.moyenne, reverse=True)


class TriParNom(Strategie):
    """Trie les étudiants par nom alphabétique."""

    def trier(self, elements: list) -> list:
        return sorted(elements, key=lambda e: e.nom)
