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

# 🗂️ TP n°3 - advance : Plages IP & Adresses

## 🎯 Objectifs

- Créer un agrégat (bloc IP racine)
- Créer un préfixe et le structurer
- Créer une plage IP (pool DHCP)
- Créer des adresses IP individuelles
- Comprendre la hiérarchie : Agrégat > Préfixe > Plage IP / Adresse IP

---

## 📋 Consignes

### Contexte

Le site **Paris-01** dispose d'un réseau LAN dédié aux utilisateurs.  
Ton rôle est de documenter ce réseau dans NetBox en respectant la hiérarchie complète.

### Agrégat à créer

| Préfixe     | RIR          | Description                  |
|-------------|--------------|------------------------------|
| 10.0.0.0/8  | RFC 1918     | Espace d'adressage privé     |

> 💡 L'agrégat est le bloc racine. Tous les préfixes `10.x.x.x` en dépendent.  
> Le RIR **RFC 1918** est à créer s'il n'existe pas encore dans NetBox.

### Préfixe à créer

| Préfixe       | VRF    | VLAN | Statut | Description        |
|---------------|--------|------|--------|--------------------|
| 10.2.1.0/24   | GLOBAL | 30   | Active | LAN Users Paris-01 |

### Plage IP à créer

| Adresse de début | Adresse de fin | Rôle | Description     |
|------------------|----------------|------|-----------------|
| 10.2.1.50/24     | 10.2.1.200/24  | DHCP | Pool DHCP Users |

> ⚠️ Les adresses de début et de fin doivent inclure le masque CIDR (ex: `/24`)

### Adresses IP individuelles à créer

| Adresse IP    | Statut   | DNS Name         | Description        |
|---------------|----------|------------------|--------------------|
| 10.2.1.1/24   | Reserved | gw-paris01.local | Passerelle VRRP    |
| 10.2.1.10/24  | Active   | pc-user01.local  | Poste fixe User 01 |
| 10.2.1.11/24  | Active   | pc-user02.local  | Poste fixe User 02 |
| 10.2.1.12/24  | Active   | pc-user03.local  | Poste fixe User 03 |

---

## ✅ Vérifications

- [ ] L'agrégat `10.0.0.0/8` apparaît dans **IPAM > Agrégats**
- [ ] Le préfixe `10.2.1.0/24` est rattaché à l'agrégat dans **IPAM > Préfixes**
- [ ] La plage `10.2.1.50 → 10.2.1.200` apparaît dans **IPAM > Plages d'adresses**
- [ ] Les 4 adresses IP apparaissent dans **IPAM > Adresses IP**
- [ ] Le taux d'utilisation du préfixe est visible dans sa vue détail
- [ ] L'adresse `10.2.1.1/24` a bien le statut **Reserved**

---

## ❓ Question

> Si tu crées manuellement l'adresse IP `10.2.1.75/24`,  
> NetBox te laisse faire — mais quel problème cela peut-il poser en production ?
