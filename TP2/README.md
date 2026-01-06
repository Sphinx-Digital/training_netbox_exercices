# 🧱 TP n°2 : Inventaire physique avancé

**🎯 Objectifs**

- Créer devices, interfaces, alimentations
- Câbler les équipements
- Associer les devices aux racks
---

**📘 Consignes**

Pour chaque site, créer :

**🗄️ Racks**

| Nom | Localisation | Rôle |
| --- | --- | --- |
| R001 | Salle server | Baie Operateur |
| R002 | Salle server | Baie Networking |
| R003 | Salle server | Baie Compute |

**🔌 Devices**

| Type | Modèle | Rôle | Quantité |
| --- | --- | --- | --- |
| Routeur | Cisco ASR1001-X | Core | 2 |
| Switch | Cisco Catalyst 9300 | Access | 6 |
| Firewall | Palo Alto PA‑3220 | Security | 2 |
| Serveur | Dell R740 | Compute | 8 |

**🔌 Interfaces**

- Routeurs : 4x 10G
- Switches : 48x 1G
- Firewalls : 8x 10G
- Serveurs : 4x 10G

**🔗 Câblage**

- Routeur1 ↔ Switch1 (10G)
- Routeur2 ↔ Switch2 (10G)
- Firewall1 ↔ Switch3
- Firewall2 ↔ Switch4
- Serveurs ↔ Switches (round‑robin)
