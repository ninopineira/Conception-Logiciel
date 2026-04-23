"""
test.py — Couche 5 : Tests de toutes les classes et méthodes
Importe : pat_creation.py (qui tire toute la chaîne de dépendances)
"""

from metier import Etudiant, Professeur, Cours
from interfaces import Observable
from pat_comportement import TriParMoyenne, TriParNom
from pat_structure import (EtudiantBoursier, EtudiantDelegue,
                            LegacyCoursSystem, CoursAdapter)
from pat_creation import ScolariteManager, PersonneFactory

# Réinitialise le singleton entre les tests (utile en contexte de test)
ScolariteManager._instance = None


def separateur(titre: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {titre}")
    print('=' * 60)


# =============================================================================
# TEST — Modèles métier (metier.py)
# =============================================================================
separateur("METIER — Etudiant, Professeur, Cours")

e1 = Etudiant("Alice", 21, "E001", 14.5, ["Maths"])
e2 = Etudiant("Bob", 22, "E002", 11.0)
e3 = Etudiant("Charlie", 20, "E003", 16.0)
p1 = Professeur("Dr. Dupont", 45, "P001", "Mathématiques")
c1 = Cours("Algorithmique", "Prof. Martin")

print(e1)
print(e2)
print(p1)
print(c1)

# Test ajouter_cours
e2.ajouter_cours("Physique")
print(f"Cours de Bob après ajout : {e2.liste_cours}")

# Test set_moyenne (sans observateur pour l'instant)
e2.set_moyenne(12.5)
print(f"Nouvelle moyenne de Bob : {e2.moyenne}")


# =============================================================================
# TEST — Pattern SINGLETON (pat_creation.py)
# =============================================================================
separateur("SINGLETON — ScolariteManager")

ScolariteManager._instance = None  # reset pour test propre
manager1 = ScolariteManager()
manager2 = ScolariteManager()
print(f"manager1 is manager2 : {manager1 is manager2}")  # Doit être True


# =============================================================================
# TEST — Pattern FACTORY METHOD (pat_creation.py)
# =============================================================================
separateur("FACTORY METHOD — PersonneFactory")

fa = PersonneFactory.creer_personne("etudiant", "Alice", 21, "E001", 14.5, [])
fb = PersonneFactory.creer_personne("etudiant", "Bob", 22, "E002", 11.0, [])
fc = PersonneFactory.creer_personne("etudiant", "Charlie", 20, "E003", 16.0, [])
fp = PersonneFactory.creer_personne("professeur", "Dr. Dupont", 45, "P001", cours="Maths")
print(fa)
print(fb)
print(fc)
print(fp)

try:
    PersonneFactory.creer_personne("inconnu", "X", 0, "X000")
except ValueError as err:
    print(f"Erreur attendue : {err}")


# =============================================================================
# TEST — Pattern ADAPTER (pat_structure.py)
# =============================================================================
separateur("ADAPTER — LegacyCoursSystem → CoursAdapter")

legacy = LegacyCoursSystem()
print(f"Données brutes legacy : {legacy.get_cours_data()}")

adapter = CoursAdapter(legacy)
cours_importes = adapter.get_cours()
print("Cours convertis en objets Cours :")
for c in cours_importes:
    print(f"  {c}")


# =============================================================================
# TEST — Pattern DECORATOR (pat_structure.py)
# =============================================================================
separateur("DECORATOR — EtudiantBoursier & EtudiantDelegue")

base = PersonneFactory.creer_personne("etudiant", "Clara", 20, "E004", 15.0, [])
boursier  = EtudiantBoursier(base, montant_bourse=5500)
delegue   = EtudiantDelegue(base, role_delegue="Déléguée ENSTA-2025")

print("Etudiant de base :")
print(f"  {base}")
print("Avec décorateur Boursier :")
print(f"  {boursier}")
print("Avec décorateur Délégué :")
print(f"  {delegue}")

# Test que les décorateurs délèguent bien les méthodes
boursier.ajouter_cours("Thermodynamique")
print(f"Cours après ajout via décorateur : {base.liste_cours}")

boursier.set_moyenne(17.0)
print(f"Moyenne après set via décorateur : {base.moyenne}")

# Double décoration
double = EtudiantDelegue(EtudiantBoursier(base, 3000), "Délégué + Boursier")
print("Double décoration :")
print(f"  {double}")


# =============================================================================
# TEST — Pattern OBSERVER (interfaces.py + metier.py + pat_creation.py)
# =============================================================================
separateur("OBSERVER — Notification automatique au ScolariteManager")

ScolariteManager._instance = None
manager = ScolariteManager()

ea = PersonneFactory.creer_personne("etudiant", "Alice", 21, "E001", 14.5, [])
eb = PersonneFactory.creer_personne("etudiant", "Bob",   22, "E002", 11.0, [])
ec = PersonneFactory.creer_personne("etudiant", "Charlie", 20, "E003", 16.0, [])

manager.ajouter_etudiant(ea)
manager.ajouter_etudiant(eb)
manager.ajouter_etudiant(ec)

print("→ Alice reçoit une nouvelle note :")
ea.set_moyenne(18.0)

print("→ Bob reçoit une nouvelle note :")
eb.set_moyenne(8.5)

# Test supprimer_observateur
ea.supprimer_observateur(manager)
print("→ Alice reçoit une note (manager retiré, pas de notification) :")
ea.set_moyenne(10.0)
print(f"  Moyenne d'Alice mise à jour à {ea.moyenne} sans notification")


# =============================================================================
# TEST — Pattern STRATEGY (pat_comportement.py)
# =============================================================================
separateur("STRATEGY — TriParMoyenne & TriParNom")

print("Tri par moyenne décroissante :")
manager.set_strategie(TriParMoyenne())
for e in manager.lister_etudiants_tries():
    print(f"  {e.nom} — {e.moyenne:.2f}")

print("Tri par nom alphabétique :")
manager.set_strategie(TriParNom())
for e in manager.lister_etudiants_tries():
    print(f"  {e.nom} — {e.moyenne:.2f}")

# Changement dynamique de stratégie
manager.set_strategie(TriParMoyenne())
print("Retour au tri par moyenne :")
for e in manager.lister_etudiants_tries():
    print(f"  {e.nom} — {e.moyenne:.2f}")


# =============================================================================
# TEST — ScolariteManager : méthodes d'affichage
# =============================================================================
separateur("SCOLARITE MANAGER — Méthodes d'affichage et stats")

manager.ajouter_cours(Cours("Algorithmique", "Prof. Martin"))
manager.ajouter_cours(Cours("Physique", "Dr. Leblanc"))

print("Liste des étudiants :")
manager.afficher_etudiants()

print("Liste des cours :")
manager.afficher_cours()

print("Statistiques globales :")
manager.afficher_stats()
print(f"Moyenne générale : {manager.calculer_moyenne_generale():.2f}")


separateur("FIN DES TESTS")
