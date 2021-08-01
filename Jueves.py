import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer

#VARIABLES

#nombre del asistente
name = "Jueves"
#variable que reconoce el audio
listener = sr.Recognizer()
#para modificar las voz del asistente
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#elegir idioma del asistente
engine.setProperty('voices',voices[0].id)

#funcion para que la computadora hable
def talk(text):
    engine.say(text)
    engine.runAndWait()

#funcion para que el asistente escuhe
def listen():
    try:
        with sr.Microphone() as source:   #toma como fuente el microfono 
            print("escuchando...")
            pc = listener.listen(source)    #escucha lo que decimos
            rec = listener.recognize_google(pc, language="es")     #convierte nuestra voz y la convierte a texto
            rec = rec.lower()       #convierte el texto en minusculas
            if name in rec:         
                rec = rec.replace(name,'')

    except:
        pass
    return rec      #retorna lo recocnocido

#funcion principal
def run():
    while True:
        rec = listen()
        #condicional para reconocer "reproduce"
        if 'reproduce' in rec:
            music = rec.replace('reproduce','')
            print("Reproduciendo"+ music)
            talk("Reproduciendo"+ music)
            pywhatkit.playonyt(music)
        #condicional para reconocer "busca"
        elif 'busca' in rec:
            search = rec.replace('busca','')
            wikipedia.set_lang("es")        #la informacion se buscara en español
            wiki = wikipedia.summary(search, 1)     #resume la informacion en una oración
            print(search+ ": " +wiki)
            talk(wiki)
        #condicional para reconocer "alarma"
        elif 'alarma' in rec:
            alam = rec.replace('alarma','')
            alam = alam.strip() 
            talk("Alarma activada a las "+ alam +" horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == alam:
                    print("DESPIERTA!!!")
                    mixer.init()
                    mixer.music.load("alam.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break

if __name__ == '__main__':
    run()

