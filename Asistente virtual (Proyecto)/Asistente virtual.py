import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from PIL import ImageGrab
import webbrowser as web
import os
import pyjokes
import random
from playsound import playsound

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
name = 'alexis'

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language = 'es-ES')
            rec = rec.lower()
            
            print('\n' + rec.capitalize() +'\n')
           
    except:
        
        pass
    
    return rec

def funciones(rec):
    
    booleano = False
    if 'cómo estás' in rec:
        
        lista1 = [
            'Sigo respirando, bueno, casi, así que eso es algo.',
            'Sigo respirando, así que eso es algo.',
            'Estoy bien, gracias por preocuparte.',
            'Impotente ante esta sociedad, pero nunca pierdo la esperanza en la humanidad.',
            'Conforme',
            'Primero que todo, ¿cómo estás tú?.'
            ]
    
        resp1 = random.choice(lista1)
        
        print('\n' + resp1 + '\n')
        talk(resp1)

    elif 'reproduce' in rec:
        music = rec.replace('reproduce ','')
        talk(rec)
        print("Reproduciendo " + music)
        pywhatkit.playonyt(music)
        
    elif 'hora' in rec or 'time' in rec:
        hora = datetime.datetime.now().strftime('%H:%M:%S %p')
        print('Son las ' + hora)
        talk('Son las ' + hora)
        
    elif 'fecha' in rec or 'día' in rec or 'day' in rec:
        fecha = datetime.datetime.now().strftime('%a, %d de %b, del año %y')
        print('La fecha de hoy es ' + fecha + '\n')
        talk('La fecha de hoy es ' + fecha)
        
    elif 'whatsapp' in rec:
        pywhatkit.open_web()
        
    elif 'buscar' in rec or'search' in rec:
        busqueda = rec.replace('search ', '')
        talk('Buscando ' + busqueda)
        pywhatkit.search(busqueda)
        
    elif 'captura de pantalla' in rec or 'screenshot' in rec:
        screen = ImageGrab.grab()
        screen.show()
        
    elif 'open google'in rec or 'abrir google' in rec:
        web.open("https://www.google.com/")
        
    elif 'open saes' in rec or 'abrir saes' in rec:
        web.open("https://www.saes.upiih.ipn.mx/")
        
    elif 'dime un chiste'in rec or 'tell me a joke' in rec:
        chiste = pyjokes.get_joke('es')
        print(chiste + '\n')
        talk(chiste)
        
    elif 'ejecuta' in rec:
        orden = rec.replace('ejecuta', '')
        talk('ejecutando ' + orden)
        app = orden + '.exe'
        os.system(app)

    elif 'crea el directorio' in rec:
        home = "C:\\Users\\LATITUDE E7440\\Desktop\\"            
        order = rec.replace('crea el directorio ','')

        if os.path.exists(order):
            talk("El directorio ya existe")

        else:
            os.mkdir(home+order)
            talk("Se creó el directorio correctamente")

    elif 'crea el archivo' in rec:
        order = rec.replace('crea el archivo','')
        order = order+'.txt'
        
        if os.path.exists(order):
            talk("El archivo ya existe")

        else:    
            archivo = open(order,"w")
            archivo.close()
            talk("Se creo el archivo correctamente")
                    
    else:
        booleano = True
    
    return booleano

def run(rec):
    
    booleano = funciones(rec)
    
    while booleano == True:
        print('\nNo te he entendido, vuelve a intentarlo\n')
        talk('No te he entendido, vuelve a intentarlo')
        
        rec = listen()
        
        booleano = funciones(rec)
    
    
try:    
    playsound('grab1.mp3')
    rec = listen()
    
    if name in rec:
        print('Escuchando...')
        talk('Escuchando')
        rec = listen() 
        run(rec)
        
except UnboundLocalError:
    
        pass
    
playsound('grab2.mp3')
    
    
    
    
    
    
    