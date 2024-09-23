
# Live Transcript and GPT Response

The Live Transcription with ChatGPT project is an application designed to provide real-time audio transcription and interactive responses using OpenAI's GPT technology. It enhances communication accessibility by converting spoken language into text instantly and generating meaningful replies based on the transcribed content.


## 🚀 Getting Started

Follow these steps to set up and run Live Transcript on your local machine.
## 📋 Prerequisites

- Python >=3.8.0
- An OpenAI API key (set up a paid OpenAI account)
- Windows OS (Not tested on others)
- FFmpeg (for audio processing)

### Installing FFmpeg on Windows 

1. Install Chocolatey by opening PowerShell as Administrator and running:
```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
2. Install FFmpeg with:
```
choco install ffmpeg
```





## 🔧 Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/livetranscript
```

2. Navigate to the project folder:
```
cd livetranscript
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Create a keys.py file and add your OpenAI API key:
```
OPENAI_API_KEY="YOUR_API_KEY"
```
## 🎬 Running Live Transcript

Run the main script:
```
python main.py
```

For enhanced performance with the Whisper API:
```
python main.py --api
```
This will start real-time transcription from your microphone and speaker.
## ⚠️ Limitations

- Default Device: Only the default microphone and speaker are supported.
- Whisper Model: The 'tiny' version of the Whisper ASR model is used for speed but may have lower accuracy.
- Language Support: Transcription is primarily in English unless the --api flag is used.
## 📖 License

This project is licensed under the MIT License - see the LICENSE file for details.
## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve Live Transcript.


Feel free to customize any part to better fit your project's specifics!
