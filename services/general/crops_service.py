from models.details_general_model import insert_details_general
from helpers.compare_helper import check_crops

def compare_crops(result_id, averages):
    if averages:
        crops_zone = check_crops(averages)
        insert_details_general(result_id, crops_zone)
    else:
        print("No se pudo comprobar los cultivos")
