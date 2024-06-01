from datetime import datetime
from classes.Projet import Projet
from classes.Membre import Membre
from classes.Tache import Tache
from classes.Jalon import Jalon
from classes.Risque import Risque

date_debut = datetime(2022,3,4)
date_fin = datetime(2023,3,5)
membre1 = Membre("Mouhamed","Chef de projet")
membre2 = Membre("Mamadou","Développeur")
projet1 = Projet("Soumaya", "test", date_debut.date(), date_fin.date())
projet1.definir_budget(350000)
risque1 = Risque("Retard de livraison", 0.4 ,"Elevé")
dateDebut = datetime(2022, 4, 6)
dateFin = datetime(2022 , 7, 6)
tache1 = Tache("Analyse des besoins","test",dateDebut.date(), dateFin.date(), membre2,"Non démarrée")
tache2 = Tache("Développement","test",dateDebut.date(), dateFin.date(), membre1,"Terminée")
date = datetime(2022, 4, 4)
jalon1 = Jalon("phase 1", date.date())
projet1.ajouter_membre_equipe(membre1)
projet1.ajouter_membre_equipe(membre2)
projet1.ajouter_tache(tache1)
projet1.ajouter_tache(tache2)
projet1.ajouter_jalon(jalon1)
projet1.ajouter_risque(risque1)

print(projet1)