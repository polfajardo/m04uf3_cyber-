import urllib.request, json

lugares = {
    "1": ("Barcelona", 41.38879, 2.15899),
    "2": ("Almería", 36.8340, -2.4637),
    "3": ("Jaén", 37.7796, -3.7849)
}

print("Elige ciudad:")
for clave, (nombre, _, _) in lugares.items():
    print(f"{clave}. {nombre}")

opcion = input("Opción: ")

if opcion in lugares:
    nombre, lat, lon = lugares[opcion]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
    
    with urllib.request.urlopen(url) as datos:
        info = json.load(datos)
        tiempo = info["current"]

        print(f"\n{nombre} -> Temperatura: {tiempo['temperature_2m']}°C | Viento: {tiempo['wind_speed_10m']} km/h | Humedad: {tiempo['relative_humidity_2m']}%")
else:
    print("Opción no válida.")
