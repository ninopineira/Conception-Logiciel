// metier/Etudiant.java — Couche 2 : Modèles métier
package metier;

import interfaces.Observable;
import java.util.ArrayList;
import java.util.List;

/**
 * Représente un étudiant.
 * Hérite de Personne et d'Observable (héritage multiple impossible en Java :
 * on hérite de la classe concrète Observable et on étend Personne via composition).
 *
 * Solution Java : Etudiant étend Observable (classe abstraite),
 * et réimplémente les comportements de Personne directement
 * car Java ne supporte pas l'héritage multiple de classes.
 * On garde Personne comme classe abstraite pour le polymorphisme.
 */
public class Etudiant extends Observable {

    private String nom;
    private int age;
    private String numeroEtudiant;
    private double moyenne;
    private List<String> listeCours;

    public Etudiant(String nom, int age, String numeroEtudiant,
                    double moyenne, List<String> listeCours) {
        this.nom            = nom;
        this.age            = age;
        this.numeroEtudiant = numeroEtudiant;
        this.moyenne        = moyenne;
        this.listeCours     = listeCours != null ? listeCours : new ArrayList<>();
    }

    // Constructeur simplifié sans cours ni moyenne
    public Etudiant(String nom, int age, String numeroEtudiant) {
        this(nom, age, numeroEtudiant, 0.0, new ArrayList<>());
    }

    // --- Getters ---

    public String getNom()            { return nom; }
    public int getAge()               { return age; }
    public String getNumeroEtudiant() { return numeroEtudiant; }
    public double getMoyenne()        { return moyenne; }
    public List<String> getListeCours() { return listeCours; }

    // --- Méthodes métier ---

    public void ajouterCours(String cours) {
        listeCours.add(cours);
    }

    /**
     * Modifie la moyenne et notifie les observateurs (pattern Observer).
     */
    public void setMoyenne(double moyenne) {
        this.moyenne = moyenne;
        notifierObservateurs();
    }

    public String afficher() {
        String cours = listeCours.isEmpty() ? "Aucun" : String.join(", ", listeCours);
        return String.format("Étudiant: %s | Âge: %d | N°: %s | Moyenne: %.2f | Cours: %s",
                nom, age, numeroEtudiant, moyenne, cours);
    }

    @Override
    public String toString() {
        return afficher();
    }
}
