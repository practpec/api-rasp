from services.general.result_service import ensure_result_exist
from services.general.crops_service import compare_crops
from services.general.details_service import details
from models.result_zone_model import calculate_averages
from models.result_models import get_result_id


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

