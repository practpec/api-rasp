from models.crops_result_model import insert_crops_result
from helpers.compare_helper import check_crops

def compare_crops(result_id, averages):
    if averages:
        crops_zone = check_crops(averages)
        insert_crops_result(result_id, crops_zone)
    else:
        print("No se pudo comprobar los cultivos")
