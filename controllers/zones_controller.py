from services.zones.monitoring_service import ensure_monitoring_exists
from services.zones.zone_service import ensure_zone_exists
from services.zones.sensor_service import collect_sensor_data
from services.zones.data_processing_service import process_zone_averages, compare_crops
from services.zones.details_service import generate_zone_details
from models.reads_model import calculate_averages

def handle_zone_action(message):
    try:
        monitoring_id = message["monitoring_id"]
        projects_id = message["projects_id"]
        technical_managers_id = message["technical_managers_id"]
        status = message["status"]
        zones_id = message["id_zone"]

        
        ensure_monitoring_exists(monitoring_id, projects_id, technical_managers_id, status)
        ensure_zone_exists(zones_id, monitoring_id)
        collect_sensor_data(zones_id)

        # Procesar promedios y detalles
        averages = calculate_averages(zones_id)
        process_zone_averages(zones_id, averages)
        compare_crops(zones_id, averages)
        generate_zone_details(zones_id, averages)

    except KeyError as e:
        print(f"Error en los datos del mensaje: falta el campo {e}.")
    except Exception as e:
        print(f"Error al procesar la acción por zona: {e}")
