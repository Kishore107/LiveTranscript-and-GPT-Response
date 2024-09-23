import customtkinter as ctk

def create_ui(transcription_callback, response_callback):
    root = ctk.CTk()
    root.title("Live Transcription and GPT Response")

    transcript_textbox = ctk.CTkTextbox(root, width=400, height=300)
    transcript_textbox.pack(pady=20)

    response_textbox = ctk.CTkTextbox(root, width=400, height=300)
    response_textbox.pack(pady=20)

    def update_ui():
        transcript_textbox.insert(ctk.END, transcription_callback())
        response_textbox.insert(ctk.END, response_callback())
        root.after(1000, update_ui)

    update_ui()
    root.mainloop()
