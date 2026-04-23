// pat_creation/PersonneFactory.java — Couche 4 : Patterns de création
package pat_creation;

import metier.Etudiant;
import metier.Professeur;
import java.util.ArrayList;
import java.util.List;

/**
 * Factory centralisée pour créer des Personnes.
 * Le client ne connaît pas les détails d'instanciation.
 */
public class PersonneFactory {

    /**
     * Crée un Etudiant.
     */
    public static Etudiant creerEtudiant(String nom, int age,
                                          String numero, double moyenne,
                                          List<String> listeCours) {
        return new Etudiant(nom, age, numero, moyenne,
                listeCours != null ? listeCours : new ArrayList<>());
    }

    /**
     * Crée un Etudiant sans cours ni moyenne (valeurs par défaut).
     */
    public static Etudiant creerEtudiant(String nom, int age, String numero) {
        return new Etudiant(nom, age, numero);
    }

    /**
     * Crée un Professeur.
     */
    public static Professeur creerProfesseur(String nom, int age,
                                              String numero, String cours) {
        return new Professeur(nom, age, numero, cours);
    }
}
