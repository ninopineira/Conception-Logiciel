"""
TP : Architecture Logicielle Avancée
Sujet : Système de Gestion Académique Multi-Patterns

Patterns implémentés :
  Création  : Singleton, Factory Method
  Structure : Decorator, Adapter
  Comportement : Strategy, Observer
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional


# =============================================================================
# MODÈLES DE BASE
# =============================================================================

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


class Cours:
    """Unité d'enseignement."""

    def __init__(self, nom_cours: str, professeur: str):
        self.nom_cours = nom_cours
        self.professeur = professeur

    def __str__(self) -> str:
        return f"{self.nom_cours} (Prof : {self.professeur})"


# =============================================================================
# PATTERN 5 — STRATEGY
# Permet de changer dynamiquement l'algorithme de tri des étudiants.
# Chaque stratégie encapsule un comportement interchangeable.
# =============================================================================

class Strategie(ABC):
    """Interface commune à toutes les stratégies de tri."""

    @abstractmethod
    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        pass


class TriParMoyenne(Strategie):
    """Trie les étudiants par moyenne décroissante."""

    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        return sorted(etudiants, key=lambda e: e.moyenne, reverse=True)


class TriParNom(Strategie):
    """Trie les étudiants par nom alphabétique."""

    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        return sorted(etudiants, key=lambda e: e.nom)


# =============================================================================
# PATTERN 6 — OBSERVER
# Le ScolariteManager observe les étudiants.
# Quand une note est ajoutée, l'étudiant notifie ses observateurs.
# =============================================================================

class Observateur(ABC):
    """Interface observateur."""

    @abstractmethod
    def mettre_a_jour(self, etudiant: "Etudiant") -> None:
        pass


class Observable(ABC):
    """Interface sujet observable."""

    def __init__(self):
        self._observateurs: List[Observateur] = []

    def ajouter_observateur(self, obs: Observateur) -> None:
        self._observateurs.append(obs)

    def notifier_observateurs(self) -> None:
        for obs in self._observateurs:
            obs.mettre_a_jour(self)


# =============================================================================
# CLASSE ETUDIANT
# Hérite de Personne et d'Observable (pour le pattern Observer).
# Utilise une Stratégie pour le tri (pattern Strategy).
# =============================================================================

class Etudiant(Personne, Observable):
    """Représente un étudiant."""

    def __init__(self, nom: str, age: int, numero_etudiant: str, moyenne: float = 0.0):
        Personne.__init__(self, nom, age)
        Observable.__init__(self)
        self.numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.cours: List[Cours] = []
        self._strategie: Optional[Strategie] = TriParMoyenne()  # stratégie par défaut

    def ajouter_cours(self, cours: Cours) -> None:
        self.cours.append(cours)

    def set_moyenne(self, moyenne: float) -> None:
        """Modifie la moyenne et notifie les observateurs (pattern Observer)."""
        self.moyenne = moyenne
        self.notifier_observateurs()

    def set_strategie(self, strategie: Strategie) -> None:
        """Change dynamiquement la stratégie de tri (pattern Strategy)."""
        self._strategie = strategie

    def afficher(self) -> str:
        cours_str = ", ".join(str(c) for c in self.cours) if self.cours else "Aucun"
        return (f"[Étudiant] {self.nom} | Âge: {self.age} | "
                f"N°: {self.numero_etudiant} | Moyenne: {self.moyenne:.2f} | "
                f"Cours: {cours_str}")


class Professeur(Personne):
    """Représente un professeur."""

    def __init__(self, nom: str, age: int, matiere: str):
        super().__init__(nom, age)
        self.matiere = matiere

    def afficher(self) -> str:
        return f"[Professeur] {self.nom} | Âge: {self.age} | Matière: {self.matiere}"


# =============================================================================
# PATTERN 1 — SINGLETON
# ScolariteManager est unique dans toute l'application.
# Il centralise la liste des étudiants et observe leurs changements de note.
# =============================================================================

class ScolariteManager(Observateur):
    """
    Gestionnaire central unique (Singleton).
    Observe les étudiants et met à jour les statistiques globales.
    """

    _instance: Optional["ScolariteManager"] = None

    def __new__(cls) -> "ScolariteManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._etudiants = []
            cls._instance._strategie = TriParMoyenne()
        return cls._instance

    # --- Gestion des étudiants ---

    def ajouter_etudiant(self, etudiant: Etudiant) -> None:
        """Ajoute un étudiant et s'enregistre comme observateur."""
        self._etudiants.append(etudiant)
        etudiant.ajouter_observateur(self)

    def get_etudiants(self) -> List[Etudiant]:
        return self._etudiants

    # --- Pattern Observer : réception de la notification ---

    def mettre_a_jour(self, etudiant: Etudiant) -> None:
        print(f"  [ScolariteManager] Notification reçue : {etudiant.nom} "
              f"a maintenant une moyenne de {etudiant.moyenne:.2f}")
        self._afficher_stats()

    # --- Statistiques globales ---

    def _afficher_stats(self) -> None:
        if not self._etudiants:
            return
        moyennes = [e.moyenne for e in self._etudiants]
        print(f"  [Statistiques] Moyenne générale: {sum(moyennes)/len(moyennes):.2f} | "
              f"Max: {max(moyennes):.2f} | Min: {min(moyennes):.2f}")

    # --- Pattern Strategy : tri de la liste ---

    def set_strategie(self, strategie: Strategie) -> None:
        self._strategie = strategie

    def lister_etudiants_tries(self) -> List[Etudiant]:
        return self._strategie.trier(self._etudiants)


# =============================================================================
# PATTERN 2 — FACTORY METHOD
# PersonneFactory crée des Etudiants ou des Professeurs
# sans exposer la logique de construction au client.
# =============================================================================

class PersonneFactory:
    """
    Factory centralisée pour créer des Personnes.
    Le client ne connaît pas les détails d'instanciation.
    """

    @staticmethod
    def creer(type_personne: str, **kwargs) -> Personne:
        """
        Crée une Personne selon son type.

        Pour un étudiant : type_personne="etudiant", nom, age, numero_etudiant, moyenne (opt.)
        Pour un professeur : type_personne="professeur", nom, age, matiere
        """
        type_personne = type_personne.lower()
        if type_personne == "etudiant":
            return Etudiant(
                nom=kwargs["nom"],
                age=kwargs["age"],
                numero_etudiant=kwargs["numero_etudiant"],
                moyenne=kwargs.get("moyenne", 0.0)
            )
        elif type_personne == "professeur":
            return Professeur(
                nom=kwargs["nom"],
                age=kwargs["age"],
                matiere=kwargs["matiere"]
            )
        else:
            raise ValueError(f"Type de personne inconnu : '{type_personne}'")


# =============================================================================
# PATTERN 3 — DECORATOR
# Ajoute des responsabilités à un Etudiant sans modifier sa classe.
# EtudiantBoursier et EtudiantDelegue "enveloppent" un Etudiant existant.
# =============================================================================

class EtudiantDecorator(Personne, Observable):
    """Classe de base des décorateurs d'Etudiant."""

    def __init__(self, etudiant: Etudiant):
        # On délègue à l'étudiant enveloppé
        self._etudiant = etudiant

    # Délégation des propriétés clés
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

    def afficher(self) -> str:
        return self._etudiant.afficher()

    def set_moyenne(self, moyenne: float) -> None:
        self._etudiant.set_moyenne(moyenne)

    def ajouter_cours(self, cours: Cours) -> None:
        self._etudiant.ajouter_cours(cours)


class EtudiantBoursier(EtudiantDecorator):
    """Décorateur : ajoute la notion de bourse à un étudiant."""

    def __init__(self, etudiant: Etudiant, montant_bourse: float):
        super().__init__(etudiant)
        self.montant_bourse = montant_bourse

    def afficher(self) -> str:
        base = self._etudiant.afficher()
        return f"{base} | 🎓 Boursier ({self.montant_bourse:.0f}€/an)"


class EtudiantDelegue(EtudiantDecorator):
    """Décorateur : ajoute le rôle de délégué à un étudiant."""

    def __init__(self, etudiant: Etudiant, promotion: str):
        super().__init__(etudiant)
        self.promotion = promotion

    def afficher(self) -> str:
        base = self._etudiant.afficher()
        return f"{base} | 🏅 Délégué de promo {self.promotion}"


# =============================================================================
# PATTERN 4 — ADAPTER
# Le système legacy fournit les données de cours sous forme de chaîne
# concaténée "NomCours|Professeur". L'adapter traduit ce format en Cours.
# =============================================================================

class LegacyCoursSystem:
    """Ancien système qui retourne des données de cours en format brut."""

    def get_cours_data(self) -> List[str]:
        """Retourne des cours sous format 'NomCours|Professeur'."""
        return [
            "Mathématiques Avancées|Dr. Dupont",
            "Algorithmique|Prof. Martin",
            "Physique Quantique|Dr. Leblanc",
        ]


class CoursAdapter:
    """
    Adapter : convertit les données legacy en objets Cours
    compatibles avec le système actuel.
    """

    def __init__(self, legacy_system: LegacyCoursSystem):
        self._legacy = legacy_system

    def get_cours(self) -> List[Cours]:
        cours_list = []
        for data in self._legacy.get_cours_data():
            parties = data.split("|")
            if len(parties) == 2:
                cours_list.append(Cours(nom_cours=parties[0], professeur=parties[1]))
        return cours_list


# =============================================================================
# DÉMONSTRATION COMPLÈTE
# =============================================================================

def main():
    separateur = "=" * 65

    print(separateur)
    print("  PATTERN 1 — SINGLETON : ScolariteManager")
    print(separateur)
    manager1 = ScolariteManager()
    manager2 = ScolariteManager()
    print(f"  manager1 is manager2 : {manager1 is manager2}")  # True
    print()

    print(separateur)
    print("  PATTERN 2 — FACTORY METHOD : PersonneFactory")
    print(separateur)
    alice = PersonneFactory.creer("etudiant", nom="Alice", age=21,
                                  numero_etudiant="E001", moyenne=14.5)
    bob   = PersonneFactory.creer("etudiant", nom="Bob",   age=22,
                                  numero_etudiant="E002", moyenne=11.0)
    charlie = PersonneFactory.creer("etudiant", nom="Charlie", age=20,
                                    numero_etudiant="E003", moyenne=16.0)
    prof  = PersonneFactory.creer("professeur", nom="Dr. Dupont", age=45,
                                  matiere="Mathématiques")
    print(f"  {alice}")
    print(f"  {bob}")
    print(f"  {charlie}")
    print(f"  {prof}")
    print()

    print(separateur)
    print("  PATTERN 4 — ADAPTER : LegacyCoursSystem → Cours")
    print(separateur)
    legacy = LegacyCoursSystem()
    adapter = CoursAdapter(legacy)
    cours_disponibles = adapter.get_cours()
    for c in cours_disponibles:
        print(f"  Cours importé : {c}")
    # On attribue des cours aux étudiants
    alice.ajouter_cours(cours_disponibles[0])
    alice.ajouter_cours(cours_disponibles[1])
    bob.ajouter_cours(cours_disponibles[2])
    print()

    print(separateur)
    print("  PATTERN 3 — DECORATOR : EtudiantBoursier & EtudiantDelegue")
    print(separateur)
    alice_boursiere = EtudiantBoursier(alice, montant_bourse=5500)
    bob_delegue     = EtudiantDelegue(bob, promotion="ENSTA-2025")
    print(f"  {alice_boursiere}")
    print(f"  {bob_delegue}")
    print()

    print(separateur)
    print("  PATTERN 1+6 — SINGLETON + OBSERVER : ajout et notification")
    print(separateur)
    # On enregistre les étudiants originaux dans le manager
    manager1.ajouter_etudiant(alice)
    manager1.ajouter_etudiant(bob)
    manager1.ajouter_etudiant(charlie)

    print("\n  → Alice obtient une nouvelle note :")
    alice.set_moyenne(17.5)

    print("\n  → Bob obtient une nouvelle note :")
    bob.set_moyenne(9.0)
    print()

    print(separateur)
    print("  PATTERN 5 — STRATEGY : tri des étudiants")
    print(separateur)

    print("\n  Tri par moyenne (décroissant) :")
    manager1.set_strategie(TriParMoyenne())
    for e in manager1.lister_etudiants_tries():
        print(f"    {e.nom} — {e.moyenne:.2f}")

    print("\n  Tri par nom (alphabétique) :")
    manager1.set_strategie(TriParNom())
    for e in manager1.lister_etudiants_tries():
        print(f"    {e.nom} — {e.moyenne:.2f}")

    print()
    print(separateur)
    print("  FIN DU TP")
    print(separateur)


if __name__ == "__main__":
    main()
    