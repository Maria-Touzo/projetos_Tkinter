import google.generativeai as genai

class Boot_gemini:
    """Cria um robô especialista em ficar em casa"""

    def __init__(self):
      #self são atributos 
      cliente = genai.configure(api_key = "AIzaSyChFOsumu35YjUO4V_pEG74ouAbmYeqQ14")

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

      
    def responder(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text
    
#Este if só sera executado se eu rodar o arquivo diretamente,
#caso eu importe essa página não erá executada 
#podemos utilizar isso para teste
if __name__ == "__main__":
   robo = Boot_gemini()
   resposta = robo.responder("Quem é o hamster mais amado do Brasil?")
   print(resposta)
   