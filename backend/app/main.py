# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data import get_geojson_data, get_density_data

app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update if frontend is hosted elsewhere
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/locations")
async def locations():
    """
    Returns GeoJSON data for locations with pins or tiles.
    """
    return get_geojson_data()  # No need to pass call_data explicitly, it's defaulted in the function

@app.get("/density")
async def density():
    """
    Returns data for heatmap (density of customers).
    """
    return get_density_data()  # No need to pass call_data explicitly, it's defaulted in the function
