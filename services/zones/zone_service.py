from models.zones_model import verify_zone_exists, create_zone

def ensure_zone_exists(zones_id, monitoring_id):
    if not verify_zone_exists(zones_id):
        print(f"Zona {zones_id} no existe. Creando zona...")
        create_zone(zones_id, monitoring_id)
    else:
        print(f"Zona {zones_id} ya existe.")
