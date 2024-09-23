#🌟 Live Transcript

##🚀 Getting Started
Follow these steps to set up and run Live Transcript on your local machine.

##📋 Prerequisites
Python >=3.8.0
An OpenAI API key (set up a paid OpenAI account)
Windows OS (Not tested on others)
FFmpeg (for audio processing)
Installing FFmpeg on Windows
Install Chocolatey by opening PowerShell as Administrator and running:
powershell

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
Install FFmpeg with:
powershell
Copy code
choco install ffmpeg
##🔧 Installation
Clone the repository:
bash

git clone https://github.com/yourusername/livetranscript
Navigate to the project folder:
bash

cd livetranscript
Install the required packages:
bash

pip install -r requirements.txt
Create a keys.py file and add your OpenAI API key:
python

OPENAI_API_KEY="YOUR_API_KEY"
##🎬 Running Live Transcript
Run the main script:

bash

python main.py
For enhanced performance with the Whisper API:

bash

python main.py --api
This will start real-time transcription from your microphone and speaker.

##⚠️ Limitations
Default Device: Only the default microphone and speaker are supported.
Whisper Model: The 'tiny' version of the Whisper ASR model is used for speed but may have lower accuracy.
Language Support: Transcription is primarily in English unless the --api flag is used.
##📖 License
This project is licensed under the MIT License - see the LICENSE file for details.

##🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve Live Transcript.
