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

- Créer un agrégat racine
- Créer plusieurs VRFs isolées
- Créer des groupes VLAN et des VLANs
- Créer des préfixes associés aux VLANs
- Créer des plages IP (pools DHCP)
- Créer des adresses IP individuelles

---

## 📋 Consignes

### Contexte

Tu es administrateur réseau de la société **Sphinx Digital**.  
Le site principal est **Paris-01**. Tu dois documenter l'intégralité du plan
d'adressage dans NetBox.

---

### Étape 1 — Agrégat

| Préfixe      | RIR      | Description               |
|--------------|----------|---------------------------|
| 10.0.0.0/8   | RFC 1918 | Espace privé Sphinx Digital |

> 💡 Crée le RIR **RFC 1918** s'il n'existe pas encore.

---

### Étape 2 — VRFs

| Nom         | RD          | Description                        |
|-------------|-------------|------------------------------------|
| GLOBAL      | 65000:0     | Réseau commun (management, infra)  |
| PROD        | 65000:10    | Réseau de production               |
| DEV         | 65000:20    | Réseau de développement            |
| DMZ         | 65000:30    | Zone démilitarisée (accès externe) |

---

### Étape 3 — Groupes VLAN & VLANs

**Groupe VLAN :** `Paris-01`

| VLAN ID | Nom        | VRF    | Description                  |
|---------|------------|--------|------------------------------|
| 10      | MGMT       | GLOBAL | Management équipements réseau|
| 20      | SERVERS    | PROD   | Serveurs de production       |
| 30      | USERS      | PROD   | Postes utilisateurs          |
| 40      | VOIP       | PROD   | Téléphonie IP                |
| 50      | DEV        | DEV    | Serveurs de développement    |
| 60      | STAGING    | DEV    | Environnement de recette     |
| 70      | DMZ-WEB    | DMZ    | Serveurs web exposés         |
| 80      | DMZ-API    | DMZ    | APIs exposées                |

---

### Étape 4 — Préfixes

> X = numéro du site → pour Paris-01, X = **1**

| Préfixe         | VRF    | VLAN       | Statut | Description                  |
|-----------------|--------|------------|--------|------------------------------|
| 10.0.1.0/24     | GLOBAL | 10 - MGMT  | Active | Management Paris-01          |
| 10.1.1.0/24     | PROD   | 20 - SERVERS | Active | Serveurs PROD Paris-01     |
| 10.2.1.0/24     | PROD   | 30 - USERS | Active | Utilisateurs Paris-01        |
| 10.3.1.0/24     | PROD   | 40 - VOIP  | Active | VoIP Paris-01                |
| 10.4.1.0/24     | DEV    | 50 - DEV   | Active | Serveurs DEV Paris-01        |
| 10.5.1.0/24     | DEV    | 60 - STAGING | Active | Staging Paris-01           |
| 10.6.1.0/24     | DMZ    | 70 - DMZ-WEB | Active | DMZ Web Paris-01           |
| 10.7.1.0/24     | DMZ    | 80 - DMZ-API | Active | DMZ API Paris-01           |

---

### Étape 5 — Plages IP (pools DHCP)

| Adresse de début  | Adresse de fin     | Préfixe parent  | Rôle | Description          |
|-------------------|--------------------|-----------------|------|----------------------|
| 10.2.1.50/24      | 10.2.1.200/24      | 10.2.1.0/24     | DHCP | Pool DHCP USERS      |
| 10.3.1.10/24      | 10.3.1.100/24      | 10.3.1.0/24     | DHCP | Pool DHCP VOIP       |
| 10.4.1.50/24      | 10.4.1.150/24      | 10.4.1.0/24     | DHCP | Pool DHCP DEV        |

> ⚠️ Les adresses de début et de fin doivent inclure le masque CIDR (ex: `/24`)

---

### Étape 6 — Adresses IP individuelles

| Adresse IP      | VRF    | Statut   | DNS Name              | Description              |
|-----------------|--------|----------|-----------------------|--------------------------|
| 10.0.1.1/24     | GLOBAL | Reserved | gw-mgmt.paris01.local | Passerelle MGMT          |
| 10.0.1.10/24    | GLOBAL | Active   | sw-core01.paris01.local | Switch core 01         |
| 10.0.1.11/24    | GLOBAL | Active   | sw-core02.paris01.local | Switch core 02         |
| 10.1.1.1/24     | PROD   | Reserved | gw-prod.paris01.local | Passerelle PROD          |
| 10.1.1.10/24    | PROD   | Active   | srv-web01.paris01.local | Serveur web 01         |
| 10.1.1.11/24    | PROD   | Active   | srv-web02.paris01.local | Serveur web 02         |
| 10.1.1.20/24    | PROD   | Active   | srv-db01.paris01.local  | Serveur BDD 01         |
| 10.6.1.1/24     | DMZ    | Reserved | gw-dmz.paris01.local  | Passerelle DMZ           |
| 10.6.1.10/24    | DMZ    | Active   | pub-web01.paris01.local | Serveur web public 01  |

---

## ✅ Vérifications

- [ ] L'agrégat `10.0.0.0/8` est visible dans **IPAM > Agrégats**
- [ ] Les 4 VRFs apparaissent dans **IPAM > VRFs**
- [ ] Le groupe VLAN `Paris-01` contient bien les 8 VLANs
- [ ] Les 8 préfixes sont rattachés à leur VRF et leur VLAN respectifs
- [ ] Les 3 plages IP apparaissent dans **IPAM > Plages d'adresses**
- [ ] Les 9 adresses IP sont créées avec le bon statut et la bonne VRF
- [ ] Les passerelles (`10.x.1.1`) ont toutes le statut **Reserved**

---

## ❓ Questions

> 1. Que se passe-t-il si tu crées une adresse IP `10.2.1.75/24` en VRF **PROD**
>    alors qu'une plage DHCP couvre déjà cette adresse ?

> 2. Pourquoi les préfixes DEV et PROD sont-ils dans des VRFs séparées
>    alors qu'ils pourraient coexister dans la même ?

> 3. Un préfixe `10.1.1.0/24` existe en VRF PROD et un autre `10.1.1.0/24`
>    en VRF DEV — NetBox l'autorise-t-il ? Pourquoi ?
---
