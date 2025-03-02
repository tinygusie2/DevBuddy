# Dev Buddy - Virtual Assistant with Animated Face and Voice Commands

Welcome to **Dev Buddy**, a fun and interactive virtual assistant that features animated eyes, mood-based facial expressions, and voice command capabilities. This project is designed to run on both **Raspberry Pi** and **Windows** platforms, offering an engaging development buddy for programmers, creators, and tech enthusiasts.

## Features

- **Voice Command Recognition**: Control your system with commands like opening the browser, terminal, shutdown, restart, and changing moods.
- **Animated Eyes**: The eyes will change based on the mood and respond to random pupil movements for a more lifelike experience.
- **System Tray Icon**: A system tray icon for quick access and control (Windows only).
- **Mood-based Facial Expressions**: The assistant can show different facial expressions based on the selected mood (e.g., happy, sad, angry, surprised).
- **Cross-Platform**: Compatible with both Raspberry Pi and Windows systems.

## Requirements

### Raspberry Pi

1. **Raspberry Pi 4** (recommended for best performance).
2. **Raspberry Pi OS** installed and configured.
3. **Python 3.x** (installed by default).
4. **Pygame** and **Pyttsx3** libraries for voice synthesis and animation handling.
5. **USB Microphone** (for voice commands).
6. **Display** (screen connected to the Raspberry Pi).

### Windows

1. **Windows 10/11** with Python 3.x installed.
2. **Microphone** (for voice commands).
3. **Pygame** and **Pyttsx3** libraries for animation and voice synthesis.

## Installation

### Raspberry Pi

1. **Install Python 3**: (if not already installed):
   ```bash
   sudo apt-get update
   sudo apt-get install python3
   ```

2. Install dependencies:

pip install pyttsx3 pygame SpeechRecognition pystray numpy pillow


3. Enable the microphone: Make sure your microphone is properly connected and recognized.


4. Run the script:

```bash
python3 dev_buddy_rpi.py
```



Windows

1. Install Python 3: (if not already installed): Download and install Python from python.org.


2. Install dependencies: Open a Command Prompt or PowerShell window and run:

pip install pyttsx3 pystray pygame SpeechRecognition numpy pillow


3. Install PyAudio: PyAudio is required for speech recognition. If you encounter issues installing it, download the corresponding wheel file from PyPI and install it using pip:

pip install pyaudio


4. Run the script:

python dev_buddy_win.py



Usage

Once the script is running, Dev Buddy will show an animated face with eyes that change color based on the current mood. You can give voice commands such as:

"Hello"

"Open browser"

"Open terminal"

"Shutdown"

"Restart"

"Set mood to happy"

"Set mood to sad"

"Set mood to angry"

"Set mood to surprised"

"Set mood to bored"


The assistant will respond accordingly, with either a voice reply or by changing the displayed mood.

 # Mood Options

Dev Buddy has the following moods you can set via voice commands:

Happy: Bright and energetic eye color.

Sad: Dimmed eye color.

Angry: Red eyes with a sharp expression.

Surprised: Wide open eyes with a yellow color.

Bored: Dim and unengaged eye color.

Neutral: Default, relaxed look.


# Voice Command Examples

You can say any of the following commands to interact with Dev Buddy:

"Hello" – To greet the assistant.

"Open browser" – To open the default browser (Windows only).

"Open terminal" – To open the command prompt/terminal (Windows only).

"Shutdown" – To shut down the system.

"Restart" – To restart the system.

"Set mood to [mood]" – Change the mood of the assistant (e.g., "Set mood to happy").


# File Structure

Here is the file structure for the Dev Buddy project:

DevBuddy/
│
├── dev_buddy_rpi.py      # Raspberry Pi version script
├── dev_buddy_win.py      # Windows version script
├── README.md             # This README file
├── requirements.txt      # List of Python dependencies
└── assets/               # Folder for assets (optional)
    └── dev_buddy_logo.png

Note:

The assets/ folder is optional and can contain any images or logos you may want to use for the system tray icon (Windows only).

requirements.txt contains the required dependencies, and you can use it to install all dependencies in one go by running:

pip install -r requirements.txt


# Customization

Changing the Mood Colors

You can customize the colors of the eyes and other facial expressions by modifying the color values in the scripts. The colors are defined in the MOODS dictionary for different expressions.

MOODS = {
    "happy": (0, 255, 100),        # Light green for happy
    "neutral": (0, 200, 255),      # Light blue for neutral
    "sad": (50, 50, 255),          # Dark blue for sad
    "angry": (255, 0, 0),          # Red for angry
    "surprised": (255, 255, 0),    # Yellow for surprised
    "bored": (100, 100, 100)       # Grey for bored
}

# Adding New Commands

You can add new voice commands by expanding the listen_for_commands function. Each new command would correspond to a specific function in your system.

if "open code editor" in command:
    open_code_editor()

# Troubleshooting

Microphone Not Detected: Ensure that your microphone is correctly set up and recognized by your system. You can test it using simple Python audio capture scripts.

Voice Recognition Not Working: Make sure your system has a working internet connection for Google’s speech recognition API to function correctly.


# License

This project is open-source under the MIT License. Feel free to modify and distribute it according to your needs.
