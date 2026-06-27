import speech_recognition as sr

recognizer = sr.Recognizer()

print("🎤 Speech-to-Text Converter")
print("Speak something after the prompt...")

with sr.Microphone() as source:
    print("🎙️ Listening...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("\n✅ Recognized Text:")
    print(text)

except sr.UnknownValueError:
    print("❌ Could not understand the audio.")

except sr.RequestError:
    print("❌ Could not connect to the speech recognition service.")
