""" 
Python program to convert text to speech

win32com library provides a bunch of methods to get excited about and one of them is the Dispatch method 
of the library. Dispatch method when passed with the argument of SAPI.SpVoice It interacts with the Microsoft 
Speech SDK to speak what you type in from the keyboard.

To install the win32com.client module , open terminal and write
    pip install pypiwin32
"""

# import the required module from text to speech conversion 
import win32com.client 

# Calling the Dispatch method of the module which interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
speaker = win32com.client.Dispatch("SAPI.SpVoice") # Initialize the speaker object

voices = speaker.GetVoices()

# Display available voices and their attributes
print("Available voices:")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.GetDescription()}")

# Allow the user to select a voice
choice = int(input("Enter the number of the voice you want to use: "))
speaker.Voice = voices.Item(choice)

speaker.Speak("Good Morning")
while 1:
    # Use the Speak method of the speaker to speak the given input from the keyboard
    print("Enter the word you want to speak it out by computer") 
    speaker.Speak("Enter the word you want to speak it out by computer")
    s = input() 
    speaker.Speak(f"Oh, The Word you have entered is {s}") 

