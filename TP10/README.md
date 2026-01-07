# 🧱 TP n°10 : Utilisation de la librairie PyNetbox

**🎯 Objectifs**

- Pratiquer la librairie PyNetbox grace a des exercices simples
---



🟢 Exercice 1 — Connexion à NetBox et récupération des sites
🎯 Objectif

Se connecter à NetBox et afficher la liste des sites existants.

📝 Énoncé

Écrire un script Python qui :

Se connecte à l’API NetBox

Affiche le nom et le slug de chaque site


🟢 Exercice 2 — Création d’un site
🎯 Objectif

Créer un nouvel objet dans NetBox via l’API.

📝 Énoncé

Créer un site :

Nom : DC-PARIS

Slug : dc-paris

Status : active

🟢 Exercice 3 — Lister les équipements d’un site
🎯 Objectif

Filtrer les objets NetBox.

📝 Énoncé

Afficher tous les équipements (devices) du site DC-PARIS avec :

Nom
Rôle
Type

🟢 Exercice 4 — Création d’un équipement réseau
🎯 Objectif

Créer un device complet (site, rôle, type).

📝 Énoncé

Créer un switch :

Nom : SW-CORE-01

Site : DC-PARIS

Rôle : core-switch

Type : Cisco C9300

🟢 Exercice 5 — Création d’interfaces sur un équipement
🎯 Objectif

Manipuler les interfaces réseau.

📝 Énoncé

Créer les interfaces suivantes sur SW-CORE-01 :

Ethernet1

Ethernet2

Ethernet3

🟢 Exercice 6 — Affecter une IP à une interface
🎯 Objectif

Gérer les adresses IP.

📝 Énoncé

Créer l’IP 192.168.10.1/24

L’associer à Ethernet1

La définir comme IP principale du device


🟢 Exercice 7 — Script d’inventaire automatisé
🎯 Objectif

Automatiser un inventaire réseau.

📝 Énoncé

Créer un script qui exporte dans un fichier texte :

Nom du device

Site

IP principale








