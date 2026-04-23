// pat_structure/CoursAdapter.java — Couche 3 : Patterns structurels
package pat_structure;

import metier.Cours;
import java.util.ArrayList;
import java.util.List;

/**
 * Adapter : convertit la chaîne du système legacy en objets Cours
 * compatibles avec le système actuel.
 */
public class CoursAdapter {

    private LegacyCoursSystem legacySystem;

    public CoursAdapter(LegacyCoursSystem legacySystem) {
        this.legacySystem = legacySystem;
    }

    public List<Cours> getCours() {
        String[] parties = legacySystem.getCoursData().split(",");
        List<Cours> coursList = new ArrayList<>();
        for (int i = 0; i + 1 < parties.length; i += 2) {
            String nom  = parties[i].trim();
            String prof = parties[i + 1].trim();
            coursList.add(new Cours(nom, prof));
        }
        return coursList;
    }
}
