def determine_soil_type(average_ph):
    if average_ph < 7:
        return "Ácido", "Dificultad de retención de nutrientes como calcio y magnesio. Recomendado aplicar cal agrícola."
    elif average_ph == 7:
        return "Neutro", "Óptimo para la mayoría de los cultivos."
    else:
        return "Básico", "Dificultad para la absorción de nutrientes como hierro. Puede ocasionar clorosis férrica."

def determine_salinity(average_conductivity):
    if average_conductivity < 200:
        return "Baja", "Adecuado para la mayoría de los cultivos."
    elif 200 <= average_conductivity <= 800:
        return "Moderada", "Posible estrés hídrico para cultivos sensibles. Se recomienda monitorear y ajustar el riego."
    else:
        return "Alta", "Riesgo elevado para cultivos sensibles. Se recomienda aplicar técnicas de lavado de sales."

def determine_irrigation_needs(average_humidity):
    if average_humidity < 40:
        return "Baja", "El suelo necesita riego inmediato."
    elif 40 <= average_humidity <= 70:
        return "Adecuada", "Nivel óptimo para la mayoría de los cultivos."
    else:
        return "Alta", "Exceso de humedad. Monitorear para evitar encharcamientos y posibles daños a las raíces."

def determine_fertility(average_nitrogen, average_phosphorus, average_potassium):
    recommendations = {}
    
    if average_nitrogen < 50:
        recommendations["Nitrógeno"] = "Bajo, aplicar fertilizantes ricos en nitrógeno como urea o nitrato de amonio."
    elif 50 <= average_nitrogen <= 150:
        recommendations["Nitrógeno"] = "Adecuado, no es necesario fertilizar adicionalmente."
    else:
        recommendations["Nitrógeno"] = "Alto, evitar fertilización excesiva para prevenir lixiviación."

    if average_phosphorus < 30:
        recommendations["Fósforo"] = "Bajo, aplicar superfosfato o fosfato diamónico."
    elif 30 <= average_phosphorus <= 60:
        recommendations["Fósforo"] = "Adecuado, no es necesario fertilizar adicionalmente."
    else:
        recommendations["Fósforo"] = "Alto, evitar fertilización excesiva para prevenir acumulación en el suelo."

    if average_potassium < 100:
        recommendations["Potasio"] = "Bajo, usar fertilizantes potásicos como cloruro de potasio."
    elif 100 <= average_potassium <= 300:
        recommendations["Potasio"] = "Adecuado, no es necesario fertilizar adicionalmente."
    else:
        recommendations["Potasio"] = "Alto, evitar fertilización excesiva para prevenir salinización."

    return recommendations

def generate_results(average):
   
    try:
        ph_type, ph_recommendation = determine_soil_type(average["ph"])

        salinity, salinity_recommendation = determine_salinity(average["conductivity"])

        irrigation, irrigation_recommendation = determine_irrigation_needs(average["humidity"])


        details_ph = f"Tipo de suelo: {ph_type}. {ph_recommendation}"
        details_salinity = f"Salinidad: {salinity}. {salinity_recommendation}"
        details_irrigation = f"Nivel de irrigación: {irrigation}. {irrigation_recommendation}"
        prob_neutral_soil = 100 if ph_type == "Neutro" else 20 
        details_prob_neutral_soil = f"Probabilidad de que el suelo sea neutro es {prob_neutral_soil}%"

        general_results = [
            
            {
                "cultivo": ph_type,
                "apto": ph_type == "Neutro",
                "detalles": details_ph,
                "porcentaje": round(average["ph"], 2)
            },
            {
                "cultivo": "Salinidad",
                "apto": salinity == "Moderada" or salinity == "Baja",
                "detalles": details_salinity,
                "porcentaje": average["conductivity"]
            },
            {
                "cultivo": "Irrigación",
                "apto": irrigation == "Adecuada",
                "detalles": details_irrigation,
                "porcentaje": average["humidity"]
            },
            {
                "cultivo": "Probabilidad de Suelo Neutro",
                "apto": ph_type == "Neutro",
                "detalles": details_prob_neutral_soil,
                "porcentaje": prob_neutral_soil
            }
        ]

        return general_results

    except KeyError as e:
        print(f"Error: falta un dato clave en el promedio: {e}")
        return []
    except Exception as e:
        print(f"Error al generar resultados generales: {e}")
        return []
