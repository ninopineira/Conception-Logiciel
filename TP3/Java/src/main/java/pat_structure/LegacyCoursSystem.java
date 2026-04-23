// pat_structure/LegacyCoursSystem.java — Couche 3 : Patterns structurels
package pat_structure;

/**
 * Ancien système retournant les cours en chaîne concaténée.
 * Format : "NomCours,Professeur,NomCours,Professeur,..."
 */
public class LegacyCoursSystem {

    public String getCoursData() {
        return "Mathématiques Avancées,Dr. Dupont,"
             + "Algorithmique,Prof. Martin,"
             + "Physique Quantique,Dr. Leblanc";
    }
}
