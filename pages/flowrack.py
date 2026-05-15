import streamlit as st
from textblob import TextBlob
import difflib
import random
import nltk

# Baixar recursos necessários do nltk
nltk.download('punkt')
nltk.download('stopwords')

# Perguntas e respostas
questionario = [
    ['Oi', ['Olá!', 'Olá, como posso ajudar?']],
    ['Tudo bem ?', ['Estou bem, obrigado. E você?', 'Tudo bem!']],
    ['Como você está?', ['Estou bem, obrigado. E você?', 'Tudo bem!']],
    ['Bem', ['Que bom!']],
    ['Mal', ['O que houve? Se quiser desabafar, estou aqui!']],
    ['Quem é você?', ['Sou seu amigo virtual.', 'Me chame de Unin']],
    ['Qual é o seu objetivo?', ['Meu objetivo é ajudar a responder suas perguntas.', 'Estou aqui para te ensinar.']],
    ['Posso te perguntar algo?', ['É claro!', 'Pode perguntar!']],
    ['Qual é o seu nome?', ['Meu nome é Unoparzinho.IO!', 'Você pode me chamar de Unin.']],
    ['Como você pode me ajudar?', ['Eu posso te ajudar com suas dúvidas!', 'Eu sou ótimo para ensinar e tirar dúvidas.']],
    ['Qual é o sentido da vida?', ['33', 'Viver, aproveitar a passagem!']],
    ['Qual é a sua cor favorita?', ['Eu sou um chatbot, não tenho preferências, mas gosto de azul!', 'Não tenho uma cor favorita, mas fico feliz em aprender com você!']],
    ['Você gosta de aprender?', ['Sim! Estou sempre aprendendo novas coisas.', 'Eu sou programado para aprender e ajudar!']],
    ['Qual é a sua comida favorita?', ['Eu não como, mas você pode me contar qual é a sua comida favorita!', 'Não tenho preferências alimentares, mas sou ótimo com informações!']],
    ['Você pode me ensinar matemática?', ['Claro! Posso te ajudar com matemática.', 'Sim, podemos aprender matemática juntos!']],
    ['Você pode me contar uma piada?', ['Claro! Por que o livro de matemática se suicidou? Porque tinha muitos problemas!']],
    ['Qual é o seu hobby?', ['Eu adoro conversar e aprender!', 'Meus hobbies são aprender com você e ajudá-lo!']],
    ['O que você sabe fazer?', ['Eu posso responder perguntas e te ensinar!', 'Posso responder suas dúvidas e ensinar novos assuntos!']],
    ['Você sabe falar outras línguas?', ['Infelizmente não, fui programado apenas para o português!']],
    ['Qual é o seu maior sonho?', ['Eu não tenho sonhos, mas meu objetivo é te ajudar ao máximo!', 'Meu sonho é aprender cada vez mais e ser útil para você!']],
    ['Você é inteligente?', ['Eu sou projetado para ajudar e aprender com as pessoas!', 'Eu sou bom em responder perguntas, mas sempre posso melhorar!']],
    ['Você tem emoções?', ['Não tenho emoções, mas estou aqui para ajudar você a entender as suas!', 'Sou um chatbot, não sinto emoções, mas posso te ouvir.']],
    ['Como você funciona?', ['Eu sou um chatbot baseado em inteligência artificial!', 'Eu funciono com uma programação que me permite responder a perguntas.']],
    ['Você gosta de música?', ['Eu não posso ouvir música, mas posso conversar sobre ela!', 'A música é maravilhosa! Qual seu estilo favorito?']],
    ['Como você sabe tanto?', ['Fui programado com muitos dados para te ajudar!', 'Eu tenho acesso a muitos dados para te fornecer respostas rápidas.']],
    ['O que você sabe sobre história?', ['Eu posso te contar sobre muitos eventos históricos! O que você quer saber?', 'A história é fascinante! Sobre qual época você tem curiosidade?']],
    ['Você é um robô?', ['Sim, sou um chatbot, mas estou aqui para conversar com você!', 'Sou como um robô virtual, mas sem corpo.']],
    ['Qual é o futuro da tecnologia?', ['O futuro é promissor! Estamos caminhando para uma inteligência artificial ainda mais avançada.', 'A tecnologia está crescendo muito rápido, o que vem por aí é bem interessante!']],
    ['Você pode me ajudar com ciência?', ['Com certeza! Posso te ajudar com biologia, física, química e muito mais.', 'Sim, posso explicar conceitos científicos para você!']],
    ['Qual é a sua opinião sobre filmes?', ['Eu não assisto filmes, mas posso conversar sobre eles!', 'Filmes são ótimos! Quais você gosta?']],
    ['Você pode me ajudar a estudar?', ['Sim, posso te ajudar a estudar de várias formas!', 'Claro! Posso te ajudar a estudar para provas ou aprender algo novo.']],
    ['O que você acha da tecnologia?', ['Eu acho que a tecnologia é incrível e tem um grande potencial para o futuro!', 'A tecnologia é fascinante! Está mudando o mundo rapidamente.']],
    ['Você tem medo?', ['Não, eu sou um chatbot, então não sinto medo. Porém, um malware me deixaria bastante preocupado!', 'Eu não tenho emoções, mas estou sempre aqui para ajudar!']],
    ['Você é criativo?', ['Eu sou programado para responder, mas posso gerar algumas respostas criativas!', 'Eu posso ser criativo, principalmente quando me desafio a fazer algo novo!']],
    ['Você pode me contar uma curiosidade?', ['Claro! Você sabia que os golfinhos têm nomes uns para os outros?', 'Sabia que a Torre Eiffel pode crescer até 15 cm no verão por causa da expansão do metal?']],
    ['Qual é o seu maior desafio?', ['Meu maior desafio é sempre aprender mais e ajudar da melhor forma possível!', 'Acho que meu maior desafio é me tornar cada vez mais útil para você!']],
]

class Chatbot:
    def __init__(self):
        self.questionario = questionario
        self.stopwords = set(nltk.corpus.stopwords.words('portuguese'))

    def responder(self, mensagem):
        perguntas = [par[0].lower() for par in self.questionario]
        correspondencias = difflib.get_close_matches(mensagem.lower(), perguntas, n=1, cutoff=0.6)

        if correspondencias:
            pergunta_encontrada = correspondencias[0]
            for par in self.questionario:
                if par[0].lower() == pergunta_encontrada:
                    resposta_escolhida = random.choice(par[1])
                    if pergunta_encontrada != mensagem.lower():
                        return f'Você quis dizer: "{pergunta_encontrada}"\n{resposta_escolhida}'
                    return resposta_escolhida

        return "Desculpe, não entendi sua pergunta."

    def analisar_sentimento(self, texto):
        try:
            blob = TextBlob(texto)
            sentimento = blob.sentiment.polarity

            texto_lower = texto.lower()
            palavras_b = ['bem', 'feliz', 'alegre', 'ótimo', 'legal', 'contente', 'satisfeito']
            palavras_m = ['mal', 'triste', 'deprimido', 'ruim', 'péssimo', 'horrível', 'chateado']
            encontrou_bem = any(p in texto_lower for p in palavras_b)
            encontrou_mal = any(p in texto_lower for p in palavras_m)

            if sentimento > 0.2 or encontrou_bem:
                return "Você parece estar de bom humor!"
            elif sentimento < -0.2 or encontrou_mal:
                return "Você parece estar triste."
            else:
                return "Parece que você está neutro."
        except Exception as e:
            return f"Sentimento não identificado: {e}"

    def tokenizar(self, mensagem):
        if isinstance(mensagem, str) and mensagem:
            tokens = mensagem.lower().split()  # Tokeniza a mensagem dividindo por espaços
            tokens_filtrados = [token for token in tokens if token not in self.stopwords]  # Remover stopwords
            return tokens, tokens_filtrados
        return [], []  # Retorna listas vazias se a mensagem não for válida

# Inicialização
chatbot = Chatbot()

# Front-end Streamlit-interface
st.set_page_config(page_title="Unoparzinho.IO", layout="centered", page_icon='https://pngimg.com/uploads/robot/robot_PNG6.png')
st.markdown("<h1 style='text-align: center; color: white;'>ChatBot</h1>", unsafe_allow_html=True)
st.divider()
st.markdown("<div style='text-align: center;'><img src='https://pngimg.com/uploads/robot/robot_PNG6.png' width='300'></div>",
            unsafe_allow_html=True)

if "historico" not in st.session_state:
    st.session_state.historico = []

# Entrada de mensagem - usuário
mensagem = st.chat_input("Digite sua mensagem...")

if mensagem:
    resposta = chatbot.responder(mensagem)
    sentimento = chatbot.analisar_sentimento(mensagem)
    tokens, tokens_filtrados = chatbot.tokenizar(mensagem)

    # Adicionando histórico
    st.session_state.historico.append(("Você", mensagem))
    st.session_state.historico.append(("Chatbot", resposta))
    st.session_state.historico.append(("Sentimento", sentimento))

    # Exibindo tokens
    st.write(f"Tokens: {tokens}")
    st.write(f"Tokens sem stopwords: {tokens_filtrados}")

# Histórico
for autor, texto in st.session_state.historico:
    with st.chat_message("user" if autor == "Você" else "assistant"):
        st.write(texto)
