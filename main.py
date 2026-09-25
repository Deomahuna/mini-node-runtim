from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root()
    # Erreur de syntaxe volontaire (deux-points manquants) : le build Docker
    # réussit (pip install fonctionne), mais le conteneur plante au
    # démarrage lors de l'import du module par uvicorn.
    return {"message": "ne devrait jamais démarrer"}
