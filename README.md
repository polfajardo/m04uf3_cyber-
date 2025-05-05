# Proyecto: Consulta del Tiempo

Este proyecto es un script en Python que consulta el tiempo actual de diferentes ciudades utilizando la API de Open-Meteo.

## Descripción

El script permite seleccionar una ciudad de un listado predefinido (Barcelona, Almería y Jaén) y luego muestra la temperatura y la velocidad del viento de esa ciudad utilizando la API de Open-Meteo.

## Requisitos

- Python 3.x
- Librerías:
  - `urllib` (para hacer peticiones HTTP)
  - `json` (para procesar la respuesta de la API)

## Funcionamiento

1. El usuario elige una ciudad de una lista.
2. El script utiliza las coordenadas de la ciudad seleccionada para hacer una petición a la API de Open-Meteo.
3. La respuesta de la API contiene datos sobre la temperatura y el viento.
4. El script imprime estos datos en pantalla.

### Código

```python
import urllib.request, json

# Coordenadas de cada ciudad
lugares = {
    "1": ("Barcelona", 41.38879, 2.15899),
    "2": ("Almería", 36.8340, -2.4637),
    "3": ("Jaén", 37.7796, -3.7849)
}

# Mostrar opciones
print("Elige ciudad:")
for clave, (nombre, _, _) in lugares.items():
    print(f"{clave}. {nombre}")

opcion = input("Opción: ")

if opcion in lugares:
    nombre, lat, lon = lugares[opcion]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=te"

    with urllib.request.urlopen(url) as datos:
        info = json.load(datos)
        tiempo = info["current"]

        print(f"\n{nombre} -> Temperatura: {tiempo['temperature_2m']}°C | Viento: {tiempo['windspeed_10m']} km/h")
else:
    print("Opción no válida.")
