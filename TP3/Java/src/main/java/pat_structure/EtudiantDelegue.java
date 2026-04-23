// pat_structure/EtudiantDelegue.java — Couche 3 : Patterns structurels
package pat_structure;

import metier.Etudiant;

/**
 * Décorateur : ajoute le rôle de délégué à un étudiant.
 */
public class EtudiantDelegue extends EtudiantDecorator {

    private String roleDelegue;

    public EtudiantDelegue(Etudiant etudiant, String roleDelegue) {
        super(etudiant);
        this.roleDelegue = roleDelegue;
    }

    public String getRoleDelegue() { return roleDelegue; }

    @Override
    public String afficher() {
        return String.format("%s | Délégué: %s",
                etudiant.afficher(), roleDelegue);
    }
}
