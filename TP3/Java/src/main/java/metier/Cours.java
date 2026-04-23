// metier/Cours.java — Couche 2 : Modèles métier
package metier;

/**
 * Unité d'enseignement.
 */
public class Cours {

    private String nom;
    private String professeur;

    public Cours(String nom, String professeur) {
        this.nom        = nom;
        this.professeur = professeur;
    }

    public String getNom()        { return nom; }
    public String getProfesseur() { return professeur; }

    @Override
    public String toString() {
        return String.format("Cours: %s | Professeur: %s", nom, professeur);
    }
}
