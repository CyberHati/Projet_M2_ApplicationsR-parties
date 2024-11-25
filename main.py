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

print(Articles)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "привет"}

#Afficher tous les articles
@app.get("/Articles")
async def all():
    return Articles

#Afficher les articles avec moins de 2 collisions
@app.get("/Articles/LessCollisions")
async def all():
    filtered_articles = [article for article in Articles if article.get('Collisions', 0) < 2]
    return filtered_articles if filtered_articles else {"message": "No articles found with less than 2 collisions."}



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

        
    

    

