import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel
from googletrans import Translator
import speech_recognition as sr

def transcrever_audio():

    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        status_label.config(text="Executando...")
        audio=recognizer.listen(source)
    status_label.config(text="Processando...")
    try:

        texto_transcrito = recognizer.recognize_google(audio, language='pt-BR')
        texto_transcrito_html = f"<p style='margin-bottom:10px'><b>Texto em Português:</b> {texto_transcrito}</p>"
        
        # Traduz o texto para o inglês
        translator = Translator()
        texto_traduzido = translator.translate(texto_transcrito, src='pt', dest='en').text
        texto_traduzido_html = f"<p style='margin-top:20px;margin-bottom:10px'><b>Texto em Inglês:</b> <span style='font-weight:bold'>{texto_traduzido}</span></p>"
        
        texto_html = texto_transcrito_html + texto_traduzido_html
        texto_transcrito_area.set_html(texto_html)
        
        status_label.config(text="Transcrição e tradução concluídas")
    except sr.UnknownValueError:
        status_label.config(text="Não foi possível entender o áudio")
    except sr.RequestError as e:
        status_label.config(text="Erro ao acessar o serviço de reconhecimento de fala do Google; {0}".format(e))

root=tk.Tk()
root.title("Inicie")
root.geometry("300x200")

fonte_roboto=("Roboto",12)

texto_transcrito_area = HTMLLabel(root, html="", font=fonte_roboto)
texto_transcrito_area.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

linha_separator = ttk.Separator(root, orient="horizontal")
linha_separator.grid(row=1, column=0, sticky="ew", pady=10)


frame_botao=tk.Frame(root)
frame_botao.grid(row=2, column=0, padx=10, pady=(0, 10))

botao_transcrever = tk.Button(frame_botao, text="Transcrever e Traduzir Áudio", command=transcrever_audio, font=fonte_roboto,
                              bg="#5F9EA0", fg="white", highlightbackground="white", highlightcolor="white",
                              activebackground="#00CED1", activeforeground="white", relief=tk.FLAT)
botao_transcrever.pack(expand=True, fill="x")

status_label = tk.Label(root, text="", fg="blue", font=fonte_roboto)
status_label.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="ew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

root.mainloop()