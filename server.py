from flask import Flask, request, jsonify
import os

# Render busca esta variable "app"
app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Servidor funcionando correctamente 🚀"}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Ejemplo simple de respuesta
    if "cáncer" in user_message.lower():
        respuesta = "Puedo ayudarte con información sobre síntomas y prevención del cáncer. ¿Qué deseas saber en específico?"
    else:
        respuesta = "Soy un asistente médico. Pregúntame sobre síntomas relacionados con el cáncer."

    return jsonify({"response": respuesta})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
