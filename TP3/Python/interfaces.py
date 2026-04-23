"""
interfaces.py — Couche 1 : Abstractions pures
N'importe rien d'autre du projet.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Observable(ABC):
    """Sujet observable : peut notifier des observateurs."""

    def __init__(self):
        self._observateurs: List[Observateur] = []

    def ajouter_observateur(self, obs: Observateur) -> None:
        self._observateurs.append(obs)

    def supprimer_observateur(self, obs: Observateur) -> None:
        self._observateurs.remove(obs)

    def notifier_observateurs(self) -> None:
        for obs in self._observateurs:
            obs.mettre_a_jour(self)


class Observateur(ABC):
    """Interface observateur : réagit aux notifications d'un Observable."""

    @abstractmethod
    def mettre_a_jour(self, sujet: Observable) -> None:
        """
        Reçoit l'objet observable qui a changé.
        On ne dépend PAS d'Etudiant ici — on dépend de l'abstraction Observable.
        """
        pass


class Strategie(ABC):
    """Interface commune à toutes les stratégies de tri."""

    @abstractmethod
    def trier(self, elements: list) -> list:
        pass
