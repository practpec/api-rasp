from models.details_result_model import insert_details_result
from helpers.details_helper import generate_details

def details(result_id, averages):
    if averages:
        details =  generate_details(averages)
        insert_details_result(result_id, details)
    else:
        print("No se pudo generar los detalles generales")   
