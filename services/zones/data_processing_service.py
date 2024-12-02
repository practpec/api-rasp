from models.data_model import insert_result_zone
from models.details_zone_model import insert_details_zone
from helpers.compare_helper import check_crops


def process_zone_averages(id_analysis, id_zone, averages):
    if averages:
        insert_result_zone(id_analysis, id_zone, averages)
    else:
        print(f"No se pudo calcular e insertar promedios para la zona {id_zone}.")

def compare_crops(id_analysis, id_zone, averages):
    if averages:
        crops_zone = check_crops(averages)
        insert_details_zone(id_analysis, id_zone, crops_zone)
    else:
        print("No se pudo comprobar los cultivos.")
