import random
import requests
from flask import Flask

app = Flask(__name__)

# Descargar lista de campeones desde Riot
versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
latest_version = versions[0]

champions_data = requests.get(
    f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion.json"
).json()

champions = list(champions_data["data"].keys())

# Asegurar que Yunara esté incluida
if "Yunara" not in champions:
    champions.append("Yunara")

@app.route("/randomchamp")
def random_champ():
    champ = random.choice(champions)
    frases = [
        f"El Chebita ha elegido {champ} support, nuevo meta coreano en su mente.",
        f"{champ} support, el plan maestro de Chebita.",
        f"Chebita pickea {champ} en support... ¿será troleo o innovación?"
    ]
    return random.choice(frases)

@app.route("/")
def home():
    return "API de Chebita Support Activa!"
