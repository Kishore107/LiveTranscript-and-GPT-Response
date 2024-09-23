import pyaudio
import speech_recognition as sr
import queue

class AudioRecorder:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def record_audio(self, audio_queue):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while True:
                audio = self.recognizer.listen(source)
                audio_queue.put(audio)
