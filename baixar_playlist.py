from email.mime import audio
from pytube import YouTube, Playlist
import os
from email.mime import base
import os
from moviepy.editor import *
from playsound import playsound

# Link da playlist que vc deseja baixar
yt = Playlist("https://youtube.com/playlist?list=PL2YYLURySKW7Rua6ht7eAdJDSuf1wUFQ_")

# Pega o Título da playlist para guardar dados
titulo = yt.title

print(f'fazendo o download de {titulo}')

# Cria uma pasta com o nome da playlist que você deseja baixar
os.mkdir(titulo)

# Salva o caminho para onde deseja baixar a playlist
base_dir ="C:/Users/Bacel/Desktop/musicas python/" + titulo

i = 1

#=====================================================================
#                       BAIXAR AS MÚSICAS
#=====================================================================

# For encarregado de baixar as músicas utilizando a biblioteca pytube
for url in yt:
    print(f'A {i} música está sendo baixada')
    # Pega a url do vídeo
    video = YouTube(url)
    # Pega a melhor qualidade que o vídeo pode estar
    stream = video.streams.get_highest_resolution()
    # Faz o download com a melhor versão do vídeo
    stream.download(output_path=titulo)
    i = i + 1

print("O download foi terminado, agora irá ocorrer a conversão em mp4 para mp3. Aguarde um instante.")

#=====================================================================
#                       CONVERTER AS MÚSICAS
#=====================================================================

# Faz a listagem da pasta com os vídeos
arr = [os.path.abspath(x) for x in os.listdir(base_dir)]

# For encarregado de fazer a conversão de mp4 para mp3
for tit in arr:
    # Faz a troca da barras invertidas para as normais. Essencial para o chegar no lugar.
    titulo = tit.replace('\\', "/")
    # Pega o título do vídeo
    t1 = titulo.split("/")[5]
    # Pega todo o caminho do vídeo
    titulo_mp4 = base_dir + "/" + t1

    # Tranforma esse caminho em mp3 para a conversão
    titulo_mp3 = titulo_mp4.replace("mp4", "mp3")

    # Salva o vídeo em um clipe
    video = VideoFileClip(titulo_mp4)

    # Transforma em áudio 
    audioclip = video.audio

    # Cria o arquivo na pasta
    audioclip.write_audiofile(titulo_mp3)


# Encerra o processo de tranformar em áudio
audioclip.close()
# Encerra o processo de salvar o vídeo
video.close()
