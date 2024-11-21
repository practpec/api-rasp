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

def generate_details(average):
    try:
        ph_type, ph_recommendation = determine_soil_type(average["ph"])
        salinity, salinity_recommendation = determine_salinity(average["conductivity"])
        irrigation, irrigation_recommendation = determine_irrigation_needs(average["humidity"])
        fertility_recommendations = determine_fertility(
            average["nitrogen"], average["phosphorus"], average["potassium"]
        )
        
        details = (
            f"{ph_type} (pH): {ph_recommendation}\n"
            f"Salinidad: {salinity}. {salinity_recommendation}\n"
            f"Nivel de Irrigación: {irrigation}. {irrigation_recommendation}\n"
            "Fertilidad del suelo:\n"
            f"Nitrógeno: {fertility_recommendations['Nitrógeno']}\n"
            f"Fósforo: {fertility_recommendations['Fósforo']}\n"
            f"Potasio: {fertility_recommendations['Potasio']}\n"
        )
        
        return details
    
    except KeyError as e:
        return f"Error: falta un dato clave en el promedio: {e}"
    except Exception as e:
        return f"Error al generar detalles: {e}"
