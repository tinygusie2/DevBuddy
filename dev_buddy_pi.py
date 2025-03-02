import pygame
import random
import time
import pyttsx3
import speech_recognition as sr
import threading
import os
import subprocess
from pystray import Icon as TrayIcon, MenuItem as MenuItem
from PIL import Image, ImageDraw

# Initialize Pygame, Pyttsx3 (text-to-speech), and other required libraries
pygame.init()
engine = pyttsx3.init()

# Screen settings for displaying eyes and facial expressions
WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dev Buddy Eyes")

# Colors and settings for the eye appearance
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PUPIL_COLOR = (0, 0, 0)

EYE_WIDTH, EYE_HEIGHT = 120, 160
EYE_SPACING = 180
PUPIL_RADIUS = 20
BLINK_DURATION = 0.15
GLOW_INTENSITY = 60

left_eye_x = WIDTH // 2 - EYE_SPACING // 2 - EYE_WIDTH
right_eye_x = WIDTH // 2 + EYE_SPACING // 2
eye_y = HEIGHT // 2 - EYE_HEIGHT // 2

# Mood states and their corresponding color
MOODS = ["happy", "neutral", "sad", "angry", "surprised", "bored"]
mood = "neutral"

# Helper function to determine eye color based on mood
def get_eye_color():
    """Return color based on current mood."""
    colors = {
        "happy": (0, 255, 100),
        "neutral": (0, 200, 255),
        "sad": (50, 50, 255),
        "angry": (255, 0, 0),
        "surprised": (255, 255, 0),
        "bored": (100, 100, 100)
    }
    return colors.get(mood, (0, 200, 255))

def draw_eye(x, y, width, height, pupil_x, pupil_y):
    """Draw the eyes with glowing effect."""
    pygame.draw.ellipse(screen, get_eye_color(), (x, y, width, height), border_radius=40)
    pygame.draw.circle(screen, PUPIL_COLOR, (pupil_x, pupil_y), PUPIL_RADIUS)

# Function to change the mood
def change_mood(new_mood):
    """Change Dev Buddy's mood."""
    global mood
    mood = new_mood
    speak(f"Changing mood to {mood}")
    print(f"Mood changed to {mood}")

# Speech-to-text and voice recognition
def listen_for_commands():
    """Listen for voice commands."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for commands...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")
        
        # Execute system commands based on voice input
        if "hello" in command:
            speak("Hello! How can I help you today?")
        elif "open browser" in command:
            open_browser()
        elif "open terminal" in command:
            open_terminal()
        elif "shut down" in command:
            shut_down()
        elif "restart" in command:
            restart_system()
        elif "set mood to happy" in command:
            change_mood("happy")
        elif "set mood to sad" in command:
            change_mood("sad")
        elif "set mood to angry" in command:
            change_mood("angry")
        elif "set mood to surprised" in command:
            change_mood("surprised")
        elif "set mood to bored" in command:
            change_mood("bored")
        elif "shutdown" in command:
            speak("Shutting down now.")
            exit()
    except Exception as e:
        print(f"Error: {e}")

# Function to speak out the text using pyttsx3
def speak(text):
    """Use pyttsx3 to speak the given text."""
    engine.say(text)
    engine.runAndWait()

# Open browser application
def open_browser():
    """Open the default browser."""
    speak("Opening browser...")
    subprocess.run(["chromium-browser"])

# Open terminal application
def open_terminal():
    """Open the terminal application."""
    speak("Opening terminal...")
    subprocess.run(["lxterminal"])

# Shut down the Raspberry Pi
def shut_down():
    """Shut down the Raspberry Pi."""
    speak("Shutting down...")
    os.system("sudo shutdown now")

# Restart the Raspberry Pi
def restart_system():
    """Restart the Raspberry Pi."""
    speak("Restarting system...")
    os.system("sudo reboot")

# System Tray Icon Setup (for easy access)
def setup_tray_icon():
    def on_quit(icon, item):
        icon.stop()

    icon_image = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
    icon = TrayIcon("Dev Buddy", menu=(MenuItem('Quit', on_quit)))
    icon.icon = icon_image
    icon.run()

# Running the voice command listener in the background
def start_listening():
    """Start listening for commands in the background."""
    while True:
        listen_for_commands()
        time.sleep(1)

# Main program loop
if __name__ == "__main__":
    # Start voice command listening in a separate thread
    threading.Thread(target=start_listening, daemon=True).start()

    # System tray and Dev Buddy main loop
    setup_tray_icon()

    # Main loop for the eye animations
    while True:
        # Reset the screen and fill with black background
        screen.fill((0, 0, 0))

        # Randomize pupil movement for a more lifelike experience
        pupil_offset_x = random.randint(-30, 30)
        pupil_offset_y = random.randint(-30, 30)

        # Draw the left and right eye with the pupils
        draw_eye(left_eye_x, eye_y, EYE_WIDTH, EYE_HEIGHT, left_eye_x + pupil_offset_x, eye_y + pupil_offset_y)
        draw_eye(right_eye_x, eye_y, EYE_WIDTH, EYE_HEIGHT, right_eye_x + pupil_offset_x, eye_y + pupil_offset_y)

        # Display the updated screen
        pygame.display.flip()

        # Pause briefly before next frame
        time.sleep(0.1)
