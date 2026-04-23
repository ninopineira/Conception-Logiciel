// interfaces/Observateur.java — Couche 1 : Abstractions pures
package interfaces;

/**
 * Interface observateur : réagit aux notifications d'un Observable.
 * Dépend uniquement de Observable, jamais d'Etudiant.
 */
public interface Observateur {

    /**
     * Appelé automatiquement quand un sujet observable change.
     * On reçoit le sujet générique — le cast vers Etudiant
     * se fait dans les implémentations de couche haute.
     */
    void mettreAJour(Observable sujet);
}
