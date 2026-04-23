// pat_structure/EtudiantDecorator.java — Couche 3 : Patterns structurels
package pat_structure;

import interfaces.Observateur;
import metier.Etudiant;
import java.util.List;

/**
 * Classe de base des décorateurs d'Etudiant.
 * Enveloppe un Etudiant et délègue tous les appels à lui.
 */
public abstract class EtudiantDecorator extends Etudiant {

    protected Etudiant etudiant;

    public EtudiantDecorator(Etudiant etudiant) {
        // On appelle le constructeur parent avec les données de l'étudiant enveloppé
        super(etudiant.getNom(), etudiant.getAge(),
              etudiant.getNumeroEtudiant(), etudiant.getMoyenne(),
              etudiant.getListeCours());
        this.etudiant = etudiant;
    }

    // --- Délégation vers l'étudiant enveloppé ---

    @Override
    public String getNom()              { return etudiant.getNom(); }
    @Override
    public int getAge()                 { return etudiant.getAge(); }
    @Override
    public double getMoyenne()          { return etudiant.getMoyenne(); }
    @Override
    public String getNumeroEtudiant()   { return etudiant.getNumeroEtudiant(); }
    @Override
    public List<String> getListeCours() { return etudiant.getListeCours(); }

    @Override
    public void setMoyenne(double moyenne) {
        etudiant.setMoyenne(moyenne);
    }

    @Override
    public void ajouterCours(String cours) {
        etudiant.ajouterCours(cours);
    }

    @Override
    public void ajouterObservateur(Observateur obs) {
        etudiant.ajouterObservateur(obs);
    }

    @Override
    public String afficher() {
        return etudiant.afficher();
    }
}
