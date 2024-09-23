import threading
import tkinter as tk
import customtkinter as ctk
from AudioTranscriber import AudioTranscriber
from GPTResponder import GPTResponder

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

def update_ui(transcriber, responder, response_textbox):
    while True:
        transcript = transcriber.transcribe_audio()
        if transcript:
            print("You said:", transcript)
            response = responder.get_response(transcript)
            # Safely update the UI
            response_textbox.insert(ctk.END, response + "\n")
            response_textbox.see(ctk.END)  # Scroll to the end

def create_ui_components(root):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    root.title("Live Transcription")
    root.geometry("800x600")

    response_textbox = ctk.CTkTextbox(root, width=600, height=400)
    response_textbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    return response_textbox

def main():
    root = ctk.CTk()
    response_textbox = create_ui_components(root)

    # Initialize components
    transcriber = AudioTranscriber()  # Initialize your audio transcriber
    responder = GPTResponder('OPENAI_API_KEY')  # Provide your OpenAI API key

    # Start the update UI thread
    update_thread = threading.Thread(target=update_ui, args=(transcriber, responder, response_textbox))
    update_thread.daemon = True
    update_thread.start()

    root.mainloop()  # Start the Tkinter main loop

if __name__ == "__main__":
    main()
