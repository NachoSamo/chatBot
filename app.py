from flask import Flask, request, jsonify, render_template
from chef_bot_gemini import ChefBotGemini, GOOGLE_API_KEY

app = Flask(__name__)

bot_cocina = ChefBotGemini(api_key=GOOGLE_API_KEY)

@app.route('/')
def index():
    bot_cocina.reiniciar_conversacion()
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    mensaje_usuario = request.json.get('message')
    if not mensaje_usuario:
        return jsonify({'error': 'No se recibió ningún mensaje'}), 400
        
    respuesta_bot = bot_cocina.obtener_respuesta(mensaje_usuario)
    
    return jsonify({'response': respuesta_bot})

if __name__ == '__main__':
    app.run(debug=True, port=5001)