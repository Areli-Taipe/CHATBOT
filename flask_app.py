import nltk
from flask import Flask, request, jsonify,render_template
from nltk.chat.util import Chat, reflections
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import requests
from bs4 import BeautifulSoup
import json

# Descargar recursos necesarios de nltk
nltk.download('punkt')  # Descargar un tokenizador de oraciones
nltk.download('stopwords')  # Descargar un conjunto de datos de palabras vacías (stopwords)

app = Flask(__name__)
app.static_folder = 'static'

# Información de la institución
institucion = {
    "nombre": "José Gálvez",
    "ubicacion": "Jr las Begonias, Rio negro, Perú",
    "telefono": "964073785",
    "horario": "Lunes a viernes de 8am a 3pm"
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    userInput = request.json.get('message', '')
    response = ""
# Funciones de operaciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

# Función para resumir texto
def resumir_texto(texto, num_oraciones=2):
    oraciones = sent_tokenize(texto, language="spanish")
    palabras = word_tokenize(texto.lower())
    stop_words = set(stopwords.words('spanish'))
    palabras_filtradas = [palabra for palabra in palabras if palabra.isalnum() and palabra not in stop_words]
    frecuencia = Counter(palabras_filtradas)

    puntuacion_oraciones = {}
    for oracion in oraciones:
        for palabra in word_tokenize(oracion.lower()):
            if palabra in frecuencia:
                if oracion not in puntuacion_oraciones:
                    puntuacion_oraciones[oracion] = 0
                puntuacion_oraciones[oracion] += frecuencia[palabra]

    oraciones_resumidas = sorted(puntuacion_oraciones, key=puntuacion_oraciones.get, reverse=True)[:num_oraciones]
    return ' '.join(oraciones_resumidas)

# Función para extraer contenido de una página web
def fetch_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = []
        for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
            content.append(tag.get_text())
        return ' '.join(content)
    except requests.RequestException as e:
        print(f"Error al acceder a la web: {e}")
        return ""

# Definición de pares de conversación
pares = [
    [
        r"hola",
        ["Hola mucho gusto, soy tu chatbot personal 😊, estoy aquí para contestar tus preguntas."]
    ],
    [
        r"como estas",
        ["Estoy bien y feliz de ser tu chatbot personal 😁."]
    ],
    [
        r"nombre",
        ["El nombre de la Institución Educativa es José Gálvez."]
    ],
    [
        r"niveles",
        ["El colegio José Galvez cuenta con 2 niveles Primaria y Secundaria."]
    ],
    [
        r"ubicacion",
        ["La ubicación del colegio José Gálvez es Jr. Las Begonias (secundaria) y Jr. Las Orquídeas (primaria) Río Negro-Satipo."]
    ],
    [
        r"lugar",
        ["La institución se encuentra en Calle Jr las Begonias, Rio negro, Perú."]
    ],
    [
        r"historia",
        ["La Institución Educativa José Gálvez, fue creada con la Resolución Directoral-005-82-La Merced, jurisdicción de la tercera Región de Educación de Junín, el 02 de mayo de 1982, en tanto la Escuela Rural PRE vocacional N°5204 del anexo de Rio Negro, Distrito de Satipo, fue creado mediante una R.D.N° 97458 del 09 de junio de 1942. La iniciativa de la integración por parte del presidente de APAFA del nivel primaria señor Victor Astoray Castillo, en coordinación con la Dirección del nivel primaria y el nivel secundaria el presidente de APAFA el señor Hernan Garcia, siendo el director el profesor Gilberto Bendezú Montero, en una reunión de docentes y directivos se logra la aceptación por parte de su mayoría. Obteniéndose una primera R.D. en el mes de febrero de 1994, comenzando la unificación como Centro Educativo Integrado de los niveles de primaria y secundaria. Desde entonces somos una Institución Educativa Integrado, con las especialidades de Industrias Alimentarias y Computación."]
    ],
    [
        r"director",
        ["El director del colegio José Galvez es Melgar Quispe José Fernando."]
    ],
    [
        r"telefono",
        ["El teléfono es 964073785."]
    ],
    [
        r"correo",
        ["El correo es ieijosegalvez@gmail.com."]
    ],
    [
        r"horario",
        ["El horario es de lunes a viernes de 8am a 3pm."]
    ],
    [
        r"salir",
        ["¡Adiós! Espero haberte ayudado."]
    ],
    [
        r"descripcion",
        ["Somos una institucion publica trabajamos con 29 años en el sector publico "]
    ]
]

# Función del chatbot
def chatbot():
    print("¡Hola! Soy el chatbot de la institución educativa José Gálvez. ¿En qué puedo ayudarte? (Escribe 'salir' para terminar)")

    while True:
        user_input = input("> ")

        # Respuestas sobre la institución
        for pattern, responses in pares:
            if nltk.re.search(pattern, user_input):
                print(responses[0])
                break
        else:
            # Manejo de resumen de texto
            if user_input.lower().startswith("resumir"):
                texto_a_resumir = user_input[8:]  # Extraer el texto después de "resumir "
                if texto_a_resumir.strip():  # Verificar que no esté vacío
                    resumen = resumir_texto(texto_a_resumir)
                    print("Resumen:", resumen)
                else:
                    print("Por favor, proporciona un texto para resumir.")
            # Manejo de extracción de contenido web
            elif user_input.lower().startswith("extraer"):
                url = user_input[8:]  # Extraer la URL después de "extraer "
                web_content = fetch_web_content(url)
                if web_content:
                    resumen = resumir_texto(web_content)
                    print("Resumen del contenido web:", resumen)
                else:
                    print("No se pudo extraer contenido de la web.")
            else:
                # Manejo de operaciones matemáticas
                try:
                    result = eval(user_input)
                    print(result)
                except Exception as e:
                    print("Lo siento, no entiendo esa operación. Asegúrate de usar el formato correcto.")

        if user_input.lower() == "salir":
            break

# Ejecutar el chatbot
if __name__ == "__main__":
    app.run(chatbot())

