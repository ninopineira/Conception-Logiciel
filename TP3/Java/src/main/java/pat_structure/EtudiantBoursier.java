// pat_structure/EtudiantBoursier.java — Couche 3 : Patterns structurels
package pat_structure;

import metier.Etudiant;

/**
 * Décorateur : ajoute la notion de bourse à un étudiant.
 */
public class EtudiantBoursier extends EtudiantDecorator {

    private double montantBourse;

    public EtudiantBoursier(Etudiant etudiant, double montantBourse) {
        super(etudiant);
        this.montantBourse = montantBourse;
    }

    public double getMontantBourse() { return montantBourse; }

    @Override
    public String afficher() {
        return String.format("%s | Boursier: %.0f€/an",
                etudiant.afficher(), montantBourse);
    }
}
