from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json

#accéder à un fichier .json se trouvant dans le dossier /donnees
with open("donnees/BDD_Articles_USA.json") as f:
    Articles = json.load(f)

with open("donnees/BDD_OperationsCommerciales_USA.json") as f:
    OperationsCommerciales = json.load(f)

with open("donnees/BDD_Personnels_USA.json") as f:
    Personnels = json.load(f)

with open("donnees/BDD_ReleveSanitaires_USA.json") as f:
    ReleveSanitaires = json.load(f)

with open("donnees/BDD_SurveillanceZone_USA.json") as f:
    SurveillanceZone = json.load(f)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "привет"}


#Afficher les articles avec le moins de collisions
@app.get("/Commercial/A")
async def less_collisions():
    # Vérifier s'il y a des articles dans la liste
    if not Articles:
        return {"message": "No articles available."}

    # Trouver le minimum de collisions parmi les articles
    min_collisions = min(a.get('Collisions', float('inf')) for a in Articles)

    # Filtrer les articles ayant le nombre minimum de collisions
    filtered_articles = [a for a in Articles if a['Collisions'] == min_collisions]

    return filtered_articles if filtered_articles else {"message": "No articles found."}

#Afficher le responsable de l'opération commercial ayant la marge la plus importante
@app.get("/Commercial/B")
async def max_marge():
    # Vérifier s'il y a des operations commerciales dans la liste
    if not OperationsCommerciales:
        return {"message": "No commercial operations available."}

    # Trouver le maximum de marge parmi les operations commerciales
    max_marge = max(o.get('MargeDegagee', float('-inf')) for o in OperationsCommerciales)

    # Filtrer les operations commerciales ayant la marge maximale
    filtered_operations = [o for o in OperationsCommerciales if o['MargeDegagee'] == max_marge]

    responsable_ids = []
    for operation in filtered_operations:
        RespID = operation["Responsable"]
        responsable_ids.append(RespID)  # Ajouter l'ID à la liste
        print(RespID)

     # Trouver le responsable de l'opération commerciale
    responsables = [p for p in Personnels if p['Identifiant'] in responsable_ids]

    return responsables if responsables else {"message": "No responsables found."}

# Afficher les zones avec le moins d'oxyde de carbone
@app.get("/AssisatnceCommerciale/A")
async def less_Carbone():
    # Vérifier s'il y a des releve sanitaires dans la liste
    if not ReleveSanitaires:
        return {"message": "No Releve sanitaires available."}

    # Trouver la zone avec le moins d'oxyde de carbone
    min_carbone = min(r.get('OxydeCarbone', float('inf')) for r in ReleveSanitaires)

    # Filtrer les zones ayant le nombre minimum d'oxyde de carbone
    filtered_zones = [r for r in ReleveSanitaires if r['OxydeCarbone'] == min_carbone]

    return filtered_zones if filtered_zones else {"message": "No Releve sanitaires found."}


# Afficher le responsable de l'opération commercial ayant le type vente
@app.get("/AssisatnceCommerciale/B")
async def Resp_vente():
    # Vérifier s'il y a des operations commerciales dans la liste
    if not OperationsCommerciales:
        return {"message": "No commercial operations available."}

    # Filtrer les operations commerciales ayant le type vente
    Rvente = [o for o in OperationsCommerciales if o['Type'] == 'Vente']

    responsable_ids = []
    for operation in Rvente:
        RespID = operation["Responsable"]
        responsable_ids.append(RespID)  # Ajouter l'ID à la liste
        print(RespID)

     # Trouver le responsable de l'opération commerciale
    responsables = [p for p in Personnels if p['Identifiant'] in responsable_ids]

    return responsables if responsables else {"message": "No responsables found."}


#Afficher les articles avec le moins de collisions et qui sont déformés
@app.get("/RechercheEtDevloppement/A")
async def deform_with_no_collision():
    # Vérifier s'il y a des articles dans la liste
    if not Articles:
        return {"message": "No articles available."}

    # Trouver le minimum de collisions parmi les articles
    min_collisions = min(a.get('Collisions', float('inf')) for a in Articles)
    print(min_collisions)
    # Filtrer les articles ayant le nombre minimum de collisions et qui sont déformés
    filtered_articles = [a for a in Articles if (a['Collisions'] == min_collisions and a['EtatEmballage']=='Deforme')]

    return filtered_articles if filtered_articles else {"message": "No articles found."}





# @app.get("/personnes/{nom}")
# async def get_personne(nom):
#     for p in personnes:
#         if p.nom == nom:
#             return p
    
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.post("/personnes")
# async def create_personne(p: Personne):
#     wasFound = False
#     for x in personnes:
#         if x.nom == p.nom:
#             wasFound = True

#     if wasFound == False:
#         personnes.append(p)
#     return f"La liste a maintenant {len(personnes)} objet(s) de type Personne"

# ## Ajoutez l'opération Delete

# @app.delete("/personnes/{nom}")
# def delete_personne(nom):
#     wasFound = False
#     for x in personnes:
#         if x.nom == nom:
#             wasFound = True
#             personnes.remove(x)
#             return f"La liste a maintenant {len(personnes)} objet(s) de type Personne"

        
    

    

