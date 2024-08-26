import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('imagenes-todas/audio.wav') as source:
    audio_data = r.record(source)

    texto = r.recognize_google(audio_data, language='es-AR', show_all=True)

    print(texto)