// pat_creation/ScolariteManager.java — Couche 4 : Patterns de création
package pat_creation;

import interfaces.Observable;
import interfaces.Observateur;
import interfaces.Strategie;
import metier.Cours;
import metier.Etudiant;
import pat_comportement.TriParMoyenne;

import java.util.ArrayList;
import java.util.List;

/**
 * Gestionnaire central unique (Singleton).
 * Implémente Observateur : reçoit les notifications des étudiants.
 * Utilise une Strategie pour le tri (Strategy).
 */
public class ScolariteManager implements Observateur {

    // --- Singleton ---
    private static ScolariteManager instance;

    private ScolariteManager() {
        // Constructeur privé : empêche l'instanciation directe
    }

    public static ScolariteManager getInstance() {
        if (instance == null) {
            instance = new ScolariteManager();
        }
        return instance;
    }

    // --- État interne ---

    private List<Etudiant> etudiants = new ArrayList<>();
    private List<Cours>    cours     = new ArrayList<>();
    private Strategie<Etudiant> strategie = new TriParMoyenne();

    // --- Gestion des étudiants ---

    public void ajouterEtudiant(Etudiant etudiant) {
        etudiants.add(etudiant);
        etudiant.ajouterObservateur(this); // s'enregistre comme observateur
    }

    public void ajouterCours(Cours cours) {
        this.cours.add(cours);
    }

    public List<Etudiant> getEtudiants() { return etudiants; }
    public List<Cours>    getCours()     { return cours; }

    // --- Affichage ---

    public void afficherEtudiants() {
        for (Etudiant e : etudiants) {
            System.out.println("  " + e);
        }
    }

    public void afficherCours() {
        for (Cours c : cours) {
            System.out.println("  " + c);
        }
    }

    // --- Statistiques ---

    public double calculerMoyenneGenerale() {
        if (etudiants.isEmpty()) return 0.0;
        double total = 0;
        for (Etudiant e : etudiants) total += e.getMoyenne();
        return total / etudiants.size();
    }

    public void afficherStats() {
        double max = etudiants.stream().mapToDouble(Etudiant::getMoyenne).max().orElse(0);
        double min = etudiants.stream().mapToDouble(Etudiant::getMoyenne).min().orElse(0);
        System.out.printf("  Nb étudiants: %d | Moyenne générale: %.2f | Max: %.2f | Min: %.2f%n",
                etudiants.size(), calculerMoyenneGenerale(), max, min);
    }

    // --- Pattern Observer : réception des notifications ---

    @Override
    public void mettreAJour(Observable sujet) {
        // Cast local vers Etudiant — pat_creation connaît Etudiant (couche haute)
        if (sujet instanceof Etudiant) {
            Etudiant e = (Etudiant) sujet;
            System.out.printf("  [Notification] %s → nouvelle moyenne : %.2f%n",
                    e.getNom(), e.getMoyenne());
            afficherStats();
        }
    }

    // --- Pattern Strategy : tri ---

    public void setStrategie(Strategie<Etudiant> strategie) {
        this.strategie = strategie;
    }

    public List<Etudiant> listerEtudiantsTries() {
        return strategie.trier(etudiants);
    }

    // --- Reset (utile pour les tests) ---

    public static void resetInstance() {
        instance = null;
    }
}
