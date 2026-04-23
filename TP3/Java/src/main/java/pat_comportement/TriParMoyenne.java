// pat_comportement/TriParMoyenne.java — Couche 3 : Patterns comportementaux
package pat_comportement;

import interfaces.Strategie;
import metier.Etudiant;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Trie les étudiants par moyenne décroissante.
 */
public class TriParMoyenne implements Strategie<Etudiant> {

    @Override
    public List<Etudiant> trier(List<Etudiant> elements) {
        List<Etudiant> copie = new ArrayList<>(elements);
        copie.sort(Comparator.comparingDouble(Etudiant::getMoyenne).reversed());
        return copie;
    }
}
