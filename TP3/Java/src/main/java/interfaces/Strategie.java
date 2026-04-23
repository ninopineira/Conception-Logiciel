// interfaces/Strategie.java — Couche 1 : Abstractions pures
package interfaces;

import java.util.List;

/**
 * Interface commune à toutes les stratégies de tri.
 * Utilise un générique T pour rester indépendante d'Etudiant.
 */
public interface Strategie<T> {
    List<T> trier(List<T> elements);
}
