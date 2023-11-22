def time_to_text (minutes):
    heures = int(minutes / 60)
    minutes_restantes = int(minutes % 60)
    return f"{heures} heures et {minutes_restantes} minutes" 

print(time_to_text(430))
print(time_to_text(68))
print(time_to_text(148))
