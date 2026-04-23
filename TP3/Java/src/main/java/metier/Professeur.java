// metier/Professeur.java — Couche 2 : Modèles métier
package metier;

/**
 * Représente un professeur.
 */
public class Professeur extends Personne {

    private String numeroProfesseur;
    private String cours;

    public Professeur(String nom, int age, String numeroProfesseur, String cours) {
        super(nom, age);
        this.numeroProfesseur = numeroProfesseur;
        this.cours            = cours;
    }

    public String getNumeroProfesseur() { return numeroProfesseur; }
    public String getCours()            { return cours; }

    @Override
    public String afficher() {
        return String.format("Professeur: %s | Âge: %d | N°: %s | Cours: %s",
                nom, age, numeroProfesseur, cours);
    }
}
