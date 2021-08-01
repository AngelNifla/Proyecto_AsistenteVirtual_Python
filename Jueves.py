import speech_recognition as sr
import pyttsx3, pywhatkit

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
            rec = listener.recognize_google(pc)     #convierte nuestra voz y la convierte a texto
            rec = rec.lower()       #convierte el texto en minusculas
            if name in rec:         
                rec = rec.replace(name,'')

    except:
        pass
    return rec      #retorna lo recocnocido

#funcion principal
def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce','')
        print("Reproduciendo"+ music)
        talk("Reproduciendo"+ music)
        pywhatkit.playonyt(music)

if __name__ == '__main__':
    run()

