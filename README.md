# **_Projet_M2_ApplicationsReparties_**
## **Contexte**
### **Serveur de données**
Nous devons créer un serveur de données permettant d'accéder aux données suivantes :
#### Personnel
- **Identifiant :** Numéro de sécurité sociale
- **Nom-Prénom :** chaîne de caractères
- **État :** actif, repos, arrêt maladie, congé
- **Service :** 
  - commercial
  - finance et gestion
  - ressources humaines
  - juridique
  - logistique
  - assistance commerciale
  - direction générale
  - maintenance
  - achats
  - cyber sécurité
  - recherche et développement
  - informatique
  - qualité
  - collecte
  - marketing
  - industriel
  - assistance technique
  - analyse des données
- **Fréquence cardiaque actuelle :** pulsations/min
- **Position :** coordonnées GPS

#### Opérations commerciales
- **Identifiant :** nombre entier
- **Type :** Achat ou Vente
- **Responsable :** identifiant personnel
- **Marge dégagée :** €
- **Nombre de kilomètres parcourus :** kms
- **Mot clé le plus utilisé par le responsable :** chaîne de caractères
- **Mot clé le plus utilisé par le client/fournisseur :** chaîne de caractères

#### Articles sur la chaîne de montage
- **Identifiant du produit :** nombre entier
- **Zone :** nombre entier unique pour l’ensemble du groupe Innov3D
- **État emballage :** Correct / Déformé
- **Responsable :** identifiant personnel
- **Position :** 3 coordonnées (GPS)
- **Rotation :** 3 angles d'Euler
- **Collisions :** nombre entier

#### Relevés sanitaires d’une zone
- **Zone :** nombre entier unique pour l’ensemble du groupe Innov3D
- **Identifiant du relevé :** nombre entier
- **Température air :** degré Celsius
- **Taux d’humidité :** %
- **Pression air :** bar
- **Oxyde de carbone :** % dans l'air
- **Particules (PM10 et PM2.5) :** % dans l'air

#### Surveillance d’une zone
- **Zone :** nombre entier unique pour l’ensemble du groupe Innov3D
- **Nombre de drones actifs :** nombre entier
- **Nombre de drones en panne :** nombre entier
- **Nombre de drones en rechargement :** nombre entier
- **Détection incendie :** oui / non
- **Détection forme :** 
  - aucune
  - personnel non identifiée
  - objet non identifié
- **Audit de conformité :** oui / non

### **Serveurs applicatifs**
L’ensemble des données des différents sites n’est pas centralisé
sur un seul serveur.
En effet, les accès à ces données sont répartis sur différents
serveurs applicatifs. De plus, un seul serveur applicatif est
présent dans chaque service.
La liste des serveurs applicatifs ci-dessous indique le type de données qui alimente ce serveur applicatif :
#### Commercial
  - Opérations commerciales
  - Articles
#### Assistance Commerciale
  - Opérations commerciales
  - Relevés sanitaires
#### Recherche et développement
  - Articles
  - Machines


La liste suivante indique le type de données que fournira ce serveur applicatif:
#### Assistance commerciale
- **A.** Zone ayant le taux d’oxyde de carbone le plus faible
- **B.** Nombre de responsables en vente

#### Commercial
- **A.** Article ayant subi le moins de collisions
- **B.** Responsable de l’opération ayant eu la marge la plus importante

#### Recherche & développement
- **A.** Nombre d’articles ayant un emballage déformé sans subir aucune collision
- **B.** Machine ayant la plus faible cadence
### **Interface utilisateur**
Nous allons devoir réaliser un tableau de bord pour l'utilisateur "Olivia" qui aura accès à :

#### Commercial
**A.** Article ayant subi le moins de collisions

#### Industriel
**B.** Machine ayant la meilleure cadence

#### Qualité
**A.** Nombre d’articles ayant un emballage correct

#### Recherche & développement
**A.** Nombre d’articles ayant un emballage déformé sans subir aucune collision

#### Ressources humaines
**A.** Formation en ressources humaines ayant le pourcentage de motivation le plus élevé

#### Maintenance
**B.** Nombre de zones ayant un incendie en cours

#### Assistance commerciale
**B.** Nombre de responsables en vente

# **Partie Code**
Les données sont stockées dans des fichiers .json se trouvant dans le dossier "/donnees"

Pour lancer le serveur il faut lancer cette commande depuis le dossier mère :
`uvicorn main:app --reload`


