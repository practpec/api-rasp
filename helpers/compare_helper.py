from models.crops_model import get_crops

def check_crops(average):
    
    if not average:
        print("No se proporcionaron datos promedio para comparar.")
        return []

    try:
        crops = get_crops()
        results = []
        parameters = [
            "humidity", "temperature", "conductivity",
            "ph", "nitrogen", "phosphorus", "potassium"
        ]

        for crop in crops:
            missing_params = {}
            matches = 0

            # Iterar sobre los parámetros para verificar rangos
            for param in parameters:
                param_min, param_max = crop[f"{param}_min"], crop[f"{param}_max"]
                if param_min <= average[param] <= param_max:
                    matches += 1
                else:
                    missing_params[param] = {
                        "average": average[param],
                        "required_range": (param_min, param_max)
                    }

            # Calcular porcentaje de adecuación
            suitable = (matches / len(parameters)) * 100

            # Agregar resultado a la lista
            results.append({
                "crops_id": crop["id"],
                "suitable": suitable,
                "details": missing_params if missing_params else "Completamente adecuado"
            })

        return results

    except Exception as e:
        print(f"Error al comparar promedios con cultivos: {e}")
        return []
