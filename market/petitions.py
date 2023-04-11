import requests

def getproducts():
    url = 'http://localhost:5001/getproducts' # URL del endpoint Flask que devuelve la lista de objetos JSON
    response = requests.get(url)
    if response.status_code == 200: # Si la respuesta es exitosa (200)
        datos = response.json() # Convertir la respuesta en un objeto Python
        return datos
    else:
        return None