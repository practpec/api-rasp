from models.details_general_model import insert_details_general
from helpers.details_helper import generate_results

def details(result_id, averages):
    if averages:
        details =  generate_results(averages)
        insert_details_general(result_id, details)
    else:
        print("No se pudo generar los detalles generales")   
