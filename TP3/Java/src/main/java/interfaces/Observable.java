// interfaces/Observable.java — Couche 1 : Abstractions pures
package interfaces;

import java.util.ArrayList;
import java.util.List;

/**
 * Sujet observable : peut notifier des observateurs.
 * N'importe rien d'autre du projet.
 */
public abstract class Observable {

    private List<Observateur> observateurs = new ArrayList<>();

    public void ajouterObservateur(Observateur obs) {
        observateurs.add(obs);
    }

    public void supprimerObservateur(Observateur obs) {
        observateurs.remove(obs);
    }

    public void notifierObservateurs() {
        for (Observateur obs : observateurs) {
            obs.mettreAJour(this);
        }
    }
}
