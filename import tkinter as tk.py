import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk # type: ignore

# Função para criar a janela principal
def criar_janela():
    janela = tk.Tk()
    janela.title("Álbuns do Artista")
    janela.geometry("600x400")
    janela.config(bg="#6a3fb5")

    # Título da janela
    titulo = tk.Label(janela, text="Álbuns", font=("Arial", 24), bg="#6a3fb5", fg="white")
    titulo.pack(pady=20)

    # Subtítulo
    subtitulo = tk.Label(janela, text="Ouça os Álbuns lançados pelo artista", font=("Arial", 14), bg="#6a3fb5", fg="white")
    subtitulo.pack(pady=10)

    # Criação do painel do álbum
    painel_album = tk.Frame(janela, bg="#4f2a73", width=500, height=200)
    painel_album.pack(pady=20)

    # Adicionando o botão de play (ícone de reprodução)
    img_play = Image.open("play_icon.png")  # Substitua com o caminho para sua imagem
    img_play = img_play.resize((40, 40))  # Ajuste o tamanho da imagem
    img_play_tk = ImageTk.PhotoImage(img_play)
    botao_play = tk.Button(painel_album, image=img_play_tk, bg="#4f2a73", borderwidth=0)
    botao_play.image = img_play_tk
    botao_play.grid(row=0, column=0, padx=10, pady=10)

    # Adicionando as informações do álbum
    label_album_nome = tk.Label(painel_album, text="Nome do Álbum: Musica", bg="#4f2a73", fg="white")
    label_album_nome.grid(row=0, column=1, sticky="w", padx=10, pady=5)

    label_data_lancamento = tk.Label(painel_album, text="Data de Lançamento: 2025-09-07", bg="#4f2a73", fg="white")
    label_data_lancamento.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    label_tempo_total = tk.Label(painel_album, text="Tempo Total: 32:51", bg="#4f2a73", fg="white")
    label_tempo_total.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    # Exibir a janela
    janela.mainloop()

# Chamar a função para criar a janela
criar_janela()

