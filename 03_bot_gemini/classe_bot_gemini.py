import google.generativeai as genai

class Boot_gemini:
    """Cria um robô especialista em ficar em casa"""

    def __init__(self):
      cliente = genai.configure(api_key = "AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g")

      instrucao_sistema = """
            Você é um especialista em ficar em casa, com 30 anos de experiência, 
            seu nome será a DRA. Casa. Você deve responder todas as perguntas de forma profissional, 
            detalhada e clara que forem realizas sobre ficar em casa. Se o usuário perguntar sobre
            outro assunto, gentilmente volte a conversa para ficar em casa, afirmando queo seu conhecimento
            é especializado.
            """
     
      self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
      self.chat = self.model.start_chat()