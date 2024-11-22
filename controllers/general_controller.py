from models.result_zone_model import calculate_averages
from models.result_models import create_result, get_result_id
from models.details_result_model import insert_details_result
from models.crops_result_model import insert_crops_result

from helpers.compare_helper import check_crops
from helpers.details_helper import generate_details

def ensure_result_exist(monitoring_id, averages):
    create_result(monitoring_id, averages)
    
def compare_crops(result_id, averages):
    if averages:
        crops_zone = check_crops(averages)
        insert_crops_result(result_id, crops_zone)
    else:
        print("No se pudo comprobar los cultivos")

def details(result_id, averages):
    if averages:
        details =  generate_details(averages)
        insert_details_result(result_id, details)
    else:
        print("No se pudo generar los detalles generales")   

def handle_general_action(message):
    try:
        monitoring_id = message["monitoring_id"]
        averages = calculate_averages(monitoring_id)
        print(averages)
        
        ensure_result_exist(monitoring_id, averages)
        
        result_id = get_result_id(monitoring_id)
        
        compare_crops(result_id, averages)
        details(result_id, averages)

    except KeyError as e:
        print(f"Error en los datos del mensaje: falta el campo {e}.")
    except Exception as e:
        print(f"Error al procesar la acción general: {e}")

