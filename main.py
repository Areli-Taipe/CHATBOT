import json
from flask import Flask, request, jsonify,render_template
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import requests
from bs4 import BeautifulSoup

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    userInput = request.json.get('message', '')
    response = ""

    # Lógica para resolver operaciones matemáticas
    try:
        # Evaluar expresiones matemáticas simples
        if userInput.lower().startswith("calcular "):
            expression = userInput[9:].strip()  # Extraer la expresión
            result = eval(expression)  # Evaluar la expresión
            response = f"El resultado de {expression} es {result}."
        else:
            # Lógica para respuestas del chatbot
            if 'ubicacion' in userInput.lower():
                response = "La ubicación del colegio José Gálvez es Jr. Las Begonias (secundaria) y Jr. Las Orquídeas (primaria) Río Negro-Satipo."
            elif 'hola' in userInput.lower():
                response = "Hola mucho gusto, soy tu chatbot personal 😊, estoy aquí para contestar tus preguntas."
            elif 'como estas' in userInput.lower():
                response = "Estoy bien y feliz de ser tu chatbot personal 😁."
            elif 'que haces' in userInput.lower():
                response = "Puedo contestar tus preguntas sobre la información del colegio José Galvez y también puedo resolver problemas matemáticos básicos."
            elif 'nombre' in userInput.lower():
                response = "José Galvez"
            elif 'niveles' in userInput.lower():
                response = "El colegio José Galvez cuenta con 2 niveles Primaria y Secundaria."
            elif 'telefono' in userInput.lower():
                response = "El teléfono es 964073785."
            elif 'director' in userInput.lower():
                response = "El director del colegio José Galvez es Melgar Quispe José Fernando."
            elif 'correo' in userInput.lower():
                response = "El correo es ieijosegalvez@gmail.com."
            elif 'horario' in userInput.lower():
                response = "El horario es de lunes a viernes de 8am a 3pm."
            elif 'historia' in userInput.lower():
                response = "La Institución Educativa José Gálvez, fue creada con la Resolución Directoral-005-82-La Merced, jurisdicción de la tercera Región de Educación de Junín, el 02 de mayo de 1982, en tanto la Escuela Rural PRE vocacional N°5204 del anexo de Rio Negro, Distrito de Satipo, fue creado mediante una R.D.N° 97458 del 09 de junio de 1942. La iniciativa de la integración por parte del presidente de APAFA del nivel primaria señor Victor Astoray Castillo, en coordinación con la Dirección del nivel primaria y el nivel secundaria el presidente de APAFA el señor Hernan Garcia, siendo el director el profesor Gilberto Bendezú Montero, en una reunión de docentes y directivos se logra la aceptación por parte de su mayoría. Obteniéndose una primera R.D. en el mes de febrero de 1994, comenzando la unificación como Centro Educativo Integrado de los niveles de primaria y secundaria. Desde entonces somos una Institución Educativa Integrado, con las especialidades de Industrias Alimentarias y Computación."
            else:
                # Intentar evaluar la expresión matemática directamente
                try:
                    result = eval(userInput)  # Evaluar la expresión
                    response = f"El resultado de {userInput} es {result}."
                except Exception:
                    response = "Lo siento, no entiendo esa operación. Asegúrate de usar el formato correcto."

    except Exception as e:
        response = f"Ocurrió un error al calcular: {str(e)}"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=False)