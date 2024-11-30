from models.reads_model import calculate_averages
from models.result_zone_model import insert_result_zone
from models.crops_zone_model import insert_crops_zone
from helpers.compare_helper import check_crops

def process_zone_averages(zones_id, averages):
    if averages:
        insert_result_zone(zones_id, averages)
    else:
        print(f"No se pudo calcular e insertar promedios para la zona {zones_id}.")

def compare_crops(zones_id, averages):
    if averages:
        crops_zone = check_crops(averages)
        insert_crops_zone(zones_id, crops_zone)
    else:
        print("No se pudo comprobar los cultivos.")
