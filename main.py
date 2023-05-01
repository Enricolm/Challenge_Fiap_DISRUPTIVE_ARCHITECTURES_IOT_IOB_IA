# %%
#Api-key: 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  Authorization: Bearer OPENAI_API_KEY


# %%
import os
import openai
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()
openai.api_key = os.getenv("API_KEY")


# %%
def validador_pergunta(texto):
    resposta = openai.Completion.create(
    prompt=f"Realize uma sugestão de destino e local para uma pessoa com essas informações(Crie um mini resumo de pq esse é o destino ideal): {texto}",
    temperature=0.7,
    max_tokens=1000,
    n=1,
    stop=None,
    presence_penalty=0.6,
    frequency_penalty=0.6,
    model="text-davinci-002",
)
    print(resposta)
    return resposta['choices'][0]['text'].strip()
    


validador_pergunta("tenho 3 filhos e gosto de viajar para lugares quentes e dentro do Brasil, pode me falar algum? ")


# %%

def processar_texto(texto):
    root = tk.Tk()
    # Faça aqui o processamento do texto inserido pelo usuário
    label = tk.Label(root, text=str(validador_pergunta(texto=texto)))
    label.pack()
    root.mainloop()



def janela_principal():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Coloque suas informações")

    # Cria o campo de entrada
    campo_texto = tk.Entry(janela, width=50)
    campo_texto.pack(padx=10, pady=10)

    # Cria o botão de processar
    botao_processar = tk.Button(janela, text="Processar", command=lambda: processar_texto(campo_texto.get()))
    botao_processar.pack(padx=10, pady=10)

    # Inicia o loop principal da janela
    janela.mainloop()

janela_principal()

# %%



