from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

# Charger les données
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

# Configuration CORS
origins = [
    "http://192.168.200.39",  # IP de ton PC 1 (frontend)
    "http://localhost",  # Localhost si tu veux tester en local
    "http://127.0.0.1",  # Localhost
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Autorise ces origines à accéder à l'API
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permet tous les headers
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


# Commercial: Article ayant subi le moins de collisions
@app.get("/Commercial/A")
async def commercial_a():
    if not Articles:
        return {"message": "No articles available."}
    min_collisions = min(a.get('Collisions', float('inf')) for a in Articles)
    filtered_articles = [a for a in Articles if a['Collisions'] == min_collisions]
    return filtered_articles


# Industriel: Machine ayant la meilleure cadence
@app.get("/Industriel/B")
async def industriel_b():
    if not OperationsCommerciales:
        return {"message": "No operations available."}
    max_cadence = max(o.get('Cadence', float('-inf')) for o in OperationsCommerciales)
    filtered_machines = [o for o in OperationsCommerciales if o['Cadence'] == max_cadence]
    return filtered_machines


# Qualité: Nombre d’articles ayant un emballage correct
@app.get("/Qualite/A")
async def qualite_a():
    if not Articles:
        return {"message": "No articles available."}
    correct_emballage = [a for a in Articles if a['EtatEmballage'] == 'Correct']
    return {"count": len(correct_emballage)}


# Recherche & Développement: Nombre d’articles ayant un emballage déformé sans collision
@app.get("/RechercheEtDevloppement/A")
async def recherche_et_devloppement_a():
    if not Articles:
        return {"message": "No articles available."}
    deformes_sans_collision = [a for a in Articles if a['EtatEmballage'] == 'Deforme' and a['Collisions'] == 0]
    return {"count": len(deformes_sans_collision)}


# Ressources humaines: Formation ayant le pourcentage de motivation le plus élevé
@app.get("/RessourcesHumaines/A")
async def ressources_humaines_a():
    if not Personnels:
        return {"message": "No personnel data available."}
    max_motivation = max(p.get('Motivation', 0) for p in Personnels)
    highest_motivation = [p for p in Personnels if p['Motivation'] == max_motivation]
    return highest_motivation


# Maintenance: Nombre de zones ayant un incendie en cours
@app.get("/Maintenance/B")
async def maintenance_b():
    if not SurveillanceZone:
        return {"message": "No surveillance data available."}
    zones_incendie = [z for z in SurveillanceZone if z['Incendie'] == 'En cours']
    return {"count": len(zones_incendie)}


# Assistance Commerciale: Nombre de responsables en vente
@app.get("/AssistanceCommerciale/B")
async def assistance_commerciale_b():
    if not OperationsCommerciales:
        return {"message": "No operations available."}
    vente_responsables = [o for o in OperationsCommerciales if o['Type'] == 'Vente']
    responsables_ids = {o['Responsable'] for o in vente_responsables}
    responsables = [p for p in Personnels if p['Identifiant'] in responsables_ids]
    return {"count": len(responsables)}
