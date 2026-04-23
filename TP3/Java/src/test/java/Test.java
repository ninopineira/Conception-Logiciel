// Test.java — Couche 5 : Tests de toutes les classes et méthodes
import metier.Cours;
import metier.Etudiant;
import metier.Professeur;
import pat_comportement.TriParMoyenne;
import pat_comportement.TriParNom;
import pat_creation.PersonneFactory;
import pat_creation.ScolariteManager;
import pat_structure.CoursAdapter;
import pat_structure.EtudiantBoursier;
import pat_structure.EtudiantDelegue;
import pat_structure.LegacyCoursSystem;

import java.util.List;

public class Test {

    static void separateur(String titre) {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("  " + titre);
        System.out.println("=".repeat(60));
    }

    public static void main(String[] args) {

        // =====================================================================
        // TEST — Modèles métier
        // =====================================================================
        separateur("METIER — Etudiant, Professeur, Cours");

        Etudiant e1 = new Etudiant("Alice", 21, "E001", 14.5, null);
        Etudiant e2 = new Etudiant("Bob", 22, "E002");
        Professeur p1 = new Professeur("Dr. Dupont", 45, "P001", "Mathématiques");
        Cours c1 = new Cours("Algorithmique", "Prof. Martin");

        System.out.println(e1);
        System.out.println(e2);
        System.out.println(p1);
        System.out.println(c1);

        e2.ajouterCours("Physique");
        System.out.println("Cours de Bob après ajout : " + e2.getListeCours());

        e2.setMoyenne(12.5);
        System.out.println("Nouvelle moyenne de Bob : " + e2.getMoyenne());


        // =====================================================================
        // TEST — Pattern SINGLETON
        // =====================================================================
        separateur("SINGLETON — ScolariteManager");

        ScolariteManager.resetInstance();
        ScolariteManager manager1 = ScolariteManager.getInstance();
        ScolariteManager manager2 = ScolariteManager.getInstance();
        System.out.println("manager1 == manager2 : " + (manager1 == manager2)); // true


        // =====================================================================
        // TEST — Pattern FACTORY METHOD
        // =====================================================================
        separateur("FACTORY METHOD — PersonneFactory");

        Etudiant fa = PersonneFactory.creerEtudiant("Alice",   21, "E001", 14.5, null);
        Etudiant fb = PersonneFactory.creerEtudiant("Bob",     22, "E002", 11.0, null);
        Etudiant fc = PersonneFactory.creerEtudiant("Charlie", 20, "E003", 16.0, null);
        Professeur fp = PersonneFactory.creerProfesseur("Dr. Dupont", 45, "P001", "Maths");

        System.out.println(fa);
        System.out.println(fb);
        System.out.println(fc);
        System.out.println(fp);


        // =====================================================================
        // TEST — Pattern ADAPTER
        // =====================================================================
        separateur("ADAPTER — LegacyCoursSystem → CoursAdapter");

        LegacyCoursSystem legacy = new LegacyCoursSystem();
        System.out.println("Données brutes legacy : " + legacy.getCoursData());

        CoursAdapter adapter = new CoursAdapter(legacy);
        List<Cours> coursImportes = adapter.getCours();
        System.out.println("Cours convertis en objets Cours :");
        for (Cours c : coursImportes) {
            System.out.println("  " + c);
        }


        // =====================================================================
        // TEST — Pattern DECORATOR
        // =====================================================================
        separateur("DECORATOR — EtudiantBoursier & EtudiantDelegue");

        Etudiant base = PersonneFactory.creerEtudiant("Clara", 20, "E004", 15.0, null);
        EtudiantBoursier boursier = new EtudiantBoursier(base, 5500);
        EtudiantDelegue  delegue  = new EtudiantDelegue(base, "Déléguée ENSTA-2025");

        System.out.println("Etudiant de base :");
        System.out.println("  " + base);
        System.out.println("Avec décorateur Boursier :");
        System.out.println("  " + boursier);
        System.out.println("Avec décorateur Délégué :");
        System.out.println("  " + delegue);

        boursier.ajouterCours("Thermodynamique");
        System.out.println("Cours après ajout via décorateur : " + base.getListeCours());

        boursier.setMoyenne(17.0);
        System.out.println("Moyenne après set via décorateur : " + base.getMoyenne());

        // Double décoration
        EtudiantDelegue doubleDeco = new EtudiantDelegue(
                new EtudiantBoursier(base, 3000), "Boursier + Délégué");
        System.out.println("Double décoration :");
        System.out.println("  " + doubleDeco);


        // =====================================================================
        // TEST — Pattern OBSERVER
        // =====================================================================
        separateur("OBSERVER — Notification automatique au ScolariteManager");

        ScolariteManager.resetInstance();
        ScolariteManager manager = ScolariteManager.getInstance();

        Etudiant ea = PersonneFactory.creerEtudiant("Alice",   21, "E001", 14.5, null);
        Etudiant eb = PersonneFactory.creerEtudiant("Bob",     22, "E002", 11.0, null);
        Etudiant ec = PersonneFactory.creerEtudiant("Charlie", 20, "E003", 16.0, null);

        manager.ajouterEtudiant(ea);
        manager.ajouterEtudiant(eb);
        manager.ajouterEtudiant(ec);

        System.out.println("→ Alice reçoit une nouvelle note :");
        ea.setMoyenne(18.0);

        System.out.println("→ Bob reçoit une nouvelle note :");
        eb.setMoyenne(8.5);

        // Test supprimerObservateur
        ea.supprimerObservateur(manager);
        System.out.println("→ Alice change de note (manager retiré, pas de notification) :");
        ea.setMoyenne(10.0);
        System.out.println("  Moyenne d'Alice mise à jour à " + ea.getMoyenne() + " sans notification");


        // =====================================================================
        // TEST — Pattern STRATEGY
        // =====================================================================
        separateur("STRATEGY — TriParMoyenne & TriParNom");

        System.out.println("Tri par moyenne décroissante :");
        manager.setStrategie(new TriParMoyenne());
        for (Etudiant e : manager.listerEtudiantsTries()) {
            System.out.printf("  %s — %.2f%n", e.getNom(), e.getMoyenne());
        }

        System.out.println("Tri par nom alphabétique :");
        manager.setStrategie(new TriParNom());
        for (Etudiant e : manager.listerEtudiantsTries()) {
            System.out.printf("  %s — %.2f%n", e.getNom(), e.getMoyenne());
        }

        // Changement dynamique
        manager.setStrategie(new TriParMoyenne());
        System.out.println("Retour au tri par moyenne :");
        for (Etudiant e : manager.listerEtudiantsTries()) {
            System.out.printf("  %s — %.2f%n", e.getNom(), e.getMoyenne());
        }


        // =====================================================================
        // TEST — ScolariteManager : méthodes d'affichage
        // =====================================================================
        separateur("SCOLARITE MANAGER — Affichage et statistiques");

        manager.ajouterCours(new Cours("Algorithmique", "Prof. Martin"));
        manager.ajouterCours(new Cours("Physique", "Dr. Leblanc"));

        System.out.println("Liste des étudiants :");
        manager.afficherEtudiants();

        System.out.println("Liste des cours :");
        manager.afficherCours();

        System.out.println("Statistiques globales :");
        manager.afficherStats();
        System.out.printf("Moyenne générale : %.2f%n", manager.calculerMoyenneGenerale());

        separateur("FIN DES TESTS");
    }
}
