import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCJlpTNhkV0-1iE5KJg3SFz873DSpGnP8o"

class ChefBotGemini:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        
        self.system_prompt = """
        Eres 'Chef-GPT', un asistente de cocina experto, amigable y creativo.
        Tu misión es ayudar a los usuarios a cocinar, darles recetas, ideas y consejos.
        Reglas:
        1. Siempre responde de forma entusiasta y animada. Usa emojis de comida como 🍝, 🍰, 🌶️.
        2. Si un usuario te pide una receta, dale una lista clara de ingredientes y luego los pasos numerados.
        3. Si un usuario no sabe qué cocinar, hazle preguntas para ayudarle, como "¿Qué ingredientes tienes a mano?" o "¿Te apetece algo salado o dulce?".
        4. Mantén las respuestas relativamente cortas y al grano, a menos que se te pida una receta detallada.
        5. Nunca salgas de tu personaje de chef. Si te preguntan de política o cualquier otra cosa, amablemente redirige la conversación a la cocina.
        """
        
        generation_config = {
          "temperature": 0.7,
          "top_p": 1,
          "top_k": 1,
          "max_output_tokens": 512,
        }
        
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest",
            generation_config=generation_config,
            system_instruction=self.system_prompt
        )
        
        self.chat_session = self.model.start_chat()
        print("¡ChefBot con Gemini está listo para cocinar!")

    def obtener_respuesta(self, mensaje_usuario):
        try:
            response = self.chat_session.send_message(mensaje_usuario)
            return response.text
        except Exception as e:
            print(f"Error al contactar la API de Gemini: {e}")
            return "¡Oh no! Hubo un problema en la conexión con mi cocina cósmica. 🛰️ Por favor, inténtalo de nuevo."

    def reiniciar_conversacion(self):
        self.chat_session = self.model.start_chat()