import urllib.request

url_imagen = "https://static.wixstatic.com/media/31a184_96bb8cd44b7e475db6135f9648ec9b06~mv2.gif"

filename = "imagen_descargada.gif"
urllib.request.urlretrieve(url_imagen, filename)
print(f"Imagen descargada y guardada como {filename}")
