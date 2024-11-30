from models.monitoring_model import verify_monitoring_exists, create_monitoring

def ensure_monitoring_exists(monitoring_id, projects_id, technical_managers_id, status):
    if not verify_monitoring_exists(monitoring_id):
        print(f"Monitoreo {monitoring_id} no existe. Creando monitoreo...")
        create_monitoring(monitoring_id, projects_id, technical_managers_id, status)
    else:
        print(f"Monitoreo {monitoring_id} ya existe.")
