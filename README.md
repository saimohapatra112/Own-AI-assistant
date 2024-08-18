Sai's Personal AI Assistant
Welcome to Sai's Personal AI Assistant, a Python-based project designed to be a voice-activated assistant that can perform various tasks like opening applications, searching Wikipedia, and interacting with the user. This is my first Python project, and it's continuously evolving to include new features and improvements.

Features
Voice Commands: The assistant can recognize and respond to voice commands using the speech_recognition library.
Greetings: Based on the time of day, the assistant greets the user appropriately (morning, afternoon, or evening).
Wikipedia Search: You can ask the assistant to search Wikipedia for information on a given topic.
Open Websites and Applications: The assistant can open popular websites like YouTube, Google, Instagram, and even desktop applications like Google Chrome, Word, and VS Code.
Play Music: The assistant can open a Spotify playlist when you ask for music.
Interactive Responses: The assistant has some basic conversational abilities, like responding to greetings or questions about its mood.
How It Works
Speech Recognition: The assistant uses the speech_recognition library to listen to the user’s commands via a microphone.
Text-to-Speech: Using the pyttsx3 library, the assistant can speak out responses and confirmations.
Command Processing: Based on the user's input, the assistant processes commands to perform tasks like opening apps, searching Wikipedia, or interacting with the user.
Setup
Prerequisites
Python 3.x

The following Python libraries need to be installed:

pyttsx3
speech_recognition
wikipedia
webbrowser
os
smtplib
You can install the required libraries using pip:
