from pytube import YouTube

#Link do vídeo e pasta para salvar o vídeo

link = input("Digite o link do vídeo: ")
path = input("Digite a pasta em que deseja salvar o vídeo: ")
yt = YouTube(link)

#Detalhes do vídeo

print("Título: ", yt.title)
print("Views: ", yt.views)
print("Tamanho do vídeo: ", yt.length, "segundos")
print("Avaliação do vídeo: ", yt.rating)

#Resolução

ys = yt.streams.get_highest_resolution()

#Download

print("Baixando...")
ys.download(path)
print("Download completo!")
