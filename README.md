# **_Projet_M2_ApplicationsReparties_**
## **Contexte**
### **Niveau serveur**
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
### **Niveau Client**
