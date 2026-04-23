// metier/Personne.java — Couche 2 : Modèles métier
package metier;

/**
 * Classe abstraite de base représentant une personne.
 */
public abstract class Personne {

    protected String nom;
    protected int age;

    public Personne(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }

    public String getNom() { return nom; }
    public int getAge()    { return age; }

    public abstract String afficher();

    @Override
    public String toString() {
        return afficher();
    }
}
