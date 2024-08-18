Sai's Personal AI Assistant
Welcome to Sai's Personal AI Assistant, a Python-based project designed to be a voice-activated assistant that can perform various tasks like opening applications, searching Wikipedia, and interacting with the user. This is my first Python project, and it's continuously evolving to include new features and improvements.
Features
•	Voice Commands: The assistant can recognize and respond to voice commands using the speech_recognition library.
•	Greetings: Based on the time of day, the assistant greets the user appropriately (morning, afternoon, or evening).
•	Wikipedia Search: You can ask the assistant to search Wikipedia for information on a given topic.
•	Open Websites and Applications: The assistant can open popular websites like YouTube, Google, Instagram, and even desktop applications like Google Chrome, Word, and VS Code.
•	Play Music: The assistant can open a Spotify playlist when you ask for music.
•	Interactive Responses: The assistant has some basic conversational abilities, like responding to greetings or questions about its mood.

How It Works

1.	Speech Recognition: The assistant uses the speech_recognition library to listen to the user’s commands via a microphone.
2.	Text-to-Speech: Using the pyttsx3 library, the assistant can speak out responses and confirmations.
3.	Command Processing: Based on the user's input, the assistant processes commands to perform tasks like opening apps, searching Wikipedia, or interacting with the user.
Setup
Prerequisites
•	Python 3.x
•	The following Python libraries need to be installed:
•	pyttsx3
•	speech_recognition
•	wikipedia
•	webbrowser
•	os
•	smtplib

You can install the required libraries using pip:
 ![image](https://github.com/user-attachments/assets/9c6e856e-9fc2-4824-98fd-3fe14ab3a27f)

Running the Assistant
To start the assistant, simply run the main.py file:
![image](https://github.com/user-attachments/assets/d9a43c53-0eeb-4aea-b5f6-daf8e51ba02c)

The assistant will greet you based on the current time and start listening for your commands.
Future Improvements
This project is a work in progress. Here are some planned features:
•	Enhanced Conversation: Improving the assistant's conversational abilities.
•	Email Support: Adding functionality to send emails using voice commands.
•	Task Automation: Incorporating automation tasks like setting reminders, calendar integration, etc.
•	Customizable Responses: Allowing users to personalize responses and commands.

Contributing
Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and submit a pull request.



