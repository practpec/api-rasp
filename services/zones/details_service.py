from helpers.details_helper import generate_results
from models.details_zone_model import insert_details_zone

def generate_zone_details(id_analysis, id_zone, averages):
    if averages:
        details = generate_results(averages)
        insert_details_zone(id_analysis, id_zone, details)
    else:
        print("No se pudo generar los detalles de la zona.")
