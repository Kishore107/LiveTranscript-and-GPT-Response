import speech_recognition as sr

class AudioTranscriber:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()  # You can specify the device_index if needed

    def transcribe_audio(self):
        with self.microphone as source:
            print("Calibrating microphone... Please be quiet.")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            
            audio = self.recognizer.listen(source, phrase_time_limit=10)
            
            try:
                print("Transcribing...")
                text = self.recognizer.recognize_google(audio, language='en-US')
                return text  # Return the transcribed text
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None  # Return None if transcription fails
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return None  # Handle request errors

# Example usage:
if __name__ == "__main__":
    transcriber = AudioTranscriber()
    transcript = transcriber.transcribe_audio()
    if transcript:
        print("You said:", transcript)
