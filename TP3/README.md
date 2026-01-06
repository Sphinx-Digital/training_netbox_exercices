# 🧱 TP n°3 : IPAM & VLAN

**🎯 Objectifs**

- Créer des VRFs et des VLANs
- Créer des prefix
- Créer des IP
---

**📘 Consignes**

Pour chaque site, créer :

**VRF**

- GLOBAL
- Sales
- Students

**VLAN**

| VLAN | Nom | VRF |
| --- | --- | --- |
| 10 | MGMT | GLOBAL |
| 20 | SERVERS | Sales |
| 30 | USERS | Students |

**Préfixes**

- 10.0.X.0/24 (MGMT)
- 10.1.X.0/24 (SERVERS)
- 10.2.X.0/24 (USERS)

(X = numéro du site)
