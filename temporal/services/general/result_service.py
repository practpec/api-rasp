from models.result_models import create_result

def ensure_result_exist(monitoring_id, averages):
    create_result(monitoring_id, averages)