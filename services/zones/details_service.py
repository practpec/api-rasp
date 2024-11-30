from helpers.details_helper import generate_details
from models.details_zone_model import insert_details_zone

def generate_zone_details(zones_id, averages):
    if averages:
        details = generate_details(averages)
        insert_details_zone(zones_id, details)
    else:
        print("No se pudo generar los detalles de la zona.")
