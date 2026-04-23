// pat_comportement/TriParNom.java — Couche 3 : Patterns comportementaux
package pat_comportement;

import interfaces.Strategie;
import metier.Etudiant;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Trie les étudiants par nom alphabétique.
 */
public class TriParNom implements Strategie<Etudiant> {

    @Override
    public List<Etudiant> trier(List<Etudiant> elements) {
        List<Etudiant> copie = new ArrayList<>(elements);
        copie.sort(Comparator.comparing(Etudiant::getNom));
        return copie;
    }
}
