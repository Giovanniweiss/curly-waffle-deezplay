#Importar o módulo requests para fazer requisições HTTP
import requests

#Definir o ID da playlist que queremos obter
#Você pode mudar esse valor para qualquer ID válido de uma playlist do Deezer
playlist_id = 908622995

#Construir a URL da API com o ID da playlist
api_url = f"https://api.deezer.com/playlist/{playlist_id}"

#Fazer a requisição GET para a API e obter a resposta em formato JSON
response = requests.get(api_url).json()
print(response)

#Extrair a lista de faixas da resposta
tracks = response["tracks"]["data"]

#Criar uma lista vazia para armazenar as informações das faixas
playlist = []

#Percorrer cada faixa na lista de faixas
for track in tracks:

#Obter o título, o artista e o link da faixa
    title = track["title"]
    artist = track["artist"]["name"]
    link = track["link"]

#Criar um dicionário com as informações da faixa
    track_info = {"title": title, "artist": artist, "link": link}

#Adicionar o dicionário à lista de playlist
    playlist.append(track_info)

#Exibir a lista de playlist
print(playlist)