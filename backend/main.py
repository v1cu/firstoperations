from fastapi import FastAPI
import scripts

app = FastAPI()

@app.get("/getallplayercharacter")
async def get_all_player_character():
    return scripts.get_all_player_character()
