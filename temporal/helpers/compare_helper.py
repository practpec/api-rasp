from models.crops_model import get_crops

def check_crops(average):
    
    if not average:
        print("No se proporcionaron datos promedio para comparar.")
        return []

    try:
        crops = get_crops()
        results = []
        parameters_in_spanish = {
            "humidity": "Humedad",
            "temperature": "Temperatura",
            "conductivity": "Conductividad",
            "ph": "PH",
            "nitrogen": "Nitrógeno",
            "phosphorus": "Fósforo",
            "potassium": "Potasio"
        }
        parameters = [
            "humidity", "temperature", "conductivity",
            "ph", "nitrogen", "phosphorus", "potassium"
        ]

        for crop in crops:
            missing_params = []
            matches = 0

            for param in parameters:
                param_min, param_max = crop[f"{param}_min"], crop[f"{param}_max"]
                if param_min <= average[param] <= param_max:
                    matches += 1
                else:
                    param_spanish = parameters_in_spanish.get(param, param.capitalize())
                    missing_params.append(f'{param_spanish} requerida: {param_min} - {param_max}.')

            suitable = (matches / len(parameters)) * 100

            details = "Completamente adecuado" if not missing_params else "\n".join(missing_params)

            results.append({
                "crops_id": crop["id"],
                "suitable": suitable,
                "details": details
            })

        return results

    except Exception as e:
        print(f"Error al comparar promedios con cultivos: {e}")
        return []



