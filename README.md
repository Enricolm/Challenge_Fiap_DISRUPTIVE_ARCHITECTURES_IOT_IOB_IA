# Challenge_Fiap_DISRUPTIVE_ARCHITECTURES_IOT_IOB_IA
Documentação do código
Este código é um exemplo de como utilizar a API da OpenAI para realizar uma sugestão de destino de viagem baseado em informações inseridas pelo usuário.

Dependências
os: biblioteca nativa do Python para trabalhar com sistema operacional;
openai: biblioteca para trabalhar com a API da OpenAI;
dotenv: biblioteca para carregar variáveis de ambiente a partir de um arquivo .env;
tkinter: biblioteca nativa do Python para criar interfaces gráficas.
Como usar
Para utilizar o código, siga os passos abaixo:

Instale as dependências: pip install openai dotenv tkinter
Crie uma conta na OpenAI e obtenha uma chave de API válida.
Crie um arquivo .env na raiz do projeto com a chave da API obtida na etapa anterior, no seguinte formato: API_KEY=<chave da API>
Rode o script: python nome_do_arquivo.py
Ao rodar o script, uma janela com um campo de texto e um botão será exibida. Insira as informações desejadas no campo de texto e clique no botão "Processar". O sistema irá gerar uma sugestão de destino de viagem baseado nas informações inseridas e exibir o resultado na tela.

Funções
validador_pergunta(texto)
Esta função recebe como parâmetro um texto inserido pelo usuário e utiliza a API da OpenAI para gerar uma sugestão de destino de viagem baseado nas informações contidas no texto. Retorna uma string com a sugestão gerada.

processar_texto(texto)
Esta função recebe como parâmetro um texto inserido pelo usuário, chama a função validador_pergunta para gerar a sugestão de destino de viagem e exibe o resultado na tela em uma nova janela.

janela_principal()
Esta função cria a janela principal da aplicação, que contém um campo de texto e um botão para processar a sugestão de destino de viagem. Inicia o loop principal da janela.
