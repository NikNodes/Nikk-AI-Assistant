import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import time
import threading
import pywhatkit
import os
import pyautogui
from groq import Groq
from dotenv import load_dotenv
import json
    
load_dotenv()

NOTES_FILE = "notes.txt"
MEMORY_FILE = "memory.txt"
CHAT_HISTORY_FILE = "chat_history.txt"

# Load contacts from contacts.json
with open("contacts.json", "r") as f:
    CONTACTS = json.load(f)


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# save note function
def save_note(note):
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")
    speak("Note saved successfully.")

# save memory function
def save_memory(data):
    with open(MEMORY_FILE, "a", encoding="utf-8") as file:
        file.write(data + "\n")

# read memory function
def read_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:

            return file.read()
    except Exception as e:
        print("Memory error:", e)
        return ""
    
# read notes function
def read_notes():

    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.read()
        if notes.strip() == "":
            speak("No notes found.")
        else:
            speak("Here are your notes.")
            speak(notes)
    except FileNotFoundError:
        speak("No notes found.")
    
# wake word detection function
def listen_for_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        wake_word = recognizer.recognize_google(audio).lower()
        print("Wake word:", wake_word)
        return wake_word
    except Exception as e:
        print("Wake word error:", e)
        return ""
# set reminder function
def set_reminder(minutes):

    def reminder_thread():

        time.sleep(minutes * 60)

        speak(f"Nikunj, this is your {minutes} minute reminder.")

    threading.Thread(target=reminder_thread).start()

# send whatsapp message function
def send_whatsapp_message(phone_number, message):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_number,
            message,
            wait_time=15,
            tab_close=True,
            close_time=3
        )
        speak("Message sent successfully.")
    except Exception as e:
        print("WhatsApp Error:", e)
        speak("Sorry, I could not send the message.")

# text to speech function
def speak(text):
    print("Nikk:", text)

    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print("Speech Error:", e)

# Voice input function
def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command

    except Exception as e:
        print("Error:", e)
        return ""
    
# save chat history function
def save_chat(user_message, ai_response):
    with open(CHAT_HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"User : {user_message}\n")
        file.write(f"Nikk : {ai_response}\n")
        file.write("-" * 50 + "\n")
    
# AI chat function 
def ai_chat(question):

    try:
        memory = read_memory()
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are Nikk, a helpful AI voice assistant.
Here are some facts about the user:
{memory}
Always use these facts while answering.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        answer = response.choices[0].message.content
        speak(answer)
        save_chat(question, answer)

    except Exception as e:
        print("AI Error:", e)
        speak("Sorry, I am unable to answer right now.")

# Main assistant loop
speak("Hello, I am Nikk. How can I help you?")

empty_count = 0
while True:

    wake_word = listen_for_wake_word()

    if "hey nik" in wake_word or "hello nik" in wake_word or "hello" in wake_word or "hey" in wake_word or "hi" in wake_word or wake_word == "wake up" or wake_word == "wake" or wake_word == "wake up nik" or wake_word == "wake nik" or wake_word == "wake up nikk" or wake_word == "wake nikk":
        speak("Yes Nikunj")
        empty_count = 0
        while True:
            command = take_command()
            if command == "":
                empty_count += 1
                if empty_count >= 3:
                    speak("No command detected. Going to sleep.")
                    break
                continue

            empty_count = 0

            if "stop listening" in command:
                speak("Going to sleep")
                break

            elif "stop" in command or "exit" in command:
                speak("Goodbye")
                exit()

            # YAHAN BAKI SAARE COMMANDS
    # Open YouTube
            if "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://youtube.com")

    # Open Google
            elif "open google" in command:
                print("Google command detected")
                speak("Opening Google")
                webbrowser.open("https://google.com")

    # Tell time
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {current_time}")

    # Search Google
            elif "search" in command:
                search_query = command.replace("search", "")
                speak(f"Searching for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")

    # Open Notepad
            elif "open notepad" in command or "open text editor" in command:
                speak("Opening Notepad")
                os.system("notepad")

    # Open Calculator
            elif "open calculator" in command :
                speak("Opening Calculator")
                os.system("calc")

    # open paint
            elif "open paint" in command or "open mspaint" in command:
                speak("Opening Paint")
                os.system("mspaint")

    # open command prompt
            elif "open command prompt" in command or "open cmd" in command:
                speak("Opening Command Prompt")
                os.system("cmd")
    
    # open file explorer
            elif "open file explorer" in command or "open explorer" in command or "open file manager" in command or "open windows explorer" in command:
                speak("Opening File Explorer")
                os.system("explorer")
    
    # open control panel
            elif "open control panel" in command :
                speak("Opening Control Panel")
                os.system("control")
            
    #  open task manager
            elif "open task manager" in command :
                speak("Opening Task Manager")
                os.system("taskmgr")
            
    #  open settings
            elif "open settings" in command or "open system settings" in command or "open windows settings" in command or "open pc settings" in command or "open computer settings" in command or "open setting" in command:
                speak("Opening Settings")
                os.system("ms-settings:")
    
    # open visual studio code
            elif "open visual studio code" in command or "open vscode" in command:
                speak("Opening Visual Studio Code")
                os.system("code")
    
    
    # open yt music
            elif "open youtube music" in command or "open yt music" in command:
                speak("Opening YouTube Music")
                webbrowser.open("https://music.youtube.com/")
            
    # open armory crate
            elif "open armory crate" in command:
                speak("Opening Armory Crate")
                os.system("C:\\Program Files (x86)\\ASUS\\Armoury Crate\\ArmouryCrate.exe") 
    
    # open discord    
            elif "open discord" in command:
                speak("Opening Discord")
                os.system("C:\\Users\\Asus\\AppData\\Local\\Discord\\app-1.0.9235\\Discord.exe")    

    # open google drive
            elif "open google drive" in command:
                speak("Opening Google Drive")
                webbrowser.open("https://drive.google.com/drive/my-drive")

    # open github
            elif "open github" in command:  
                speak("Opening GitHub")
                webbrowser.open("https://github.com")

    # open email
            elif "open email" in command or "open gmail" in command:
                speak("Opening Gmail")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            
    # open pinterest
            elif "open pinterest" in command:
                speak("Opening Pinterest")
                webbrowser.open("https://www.pinterest.com/")
            
    # open amazon
            elif "open amazon" in command:
                speak("Opening Amazon")
                webbrowser.open("https://www.amazon.com/")

    # open flipkart
            elif "open flipkart" in command:
                speak("Opening Flipkart")
                webbrowser.open("https://www.flipkart.com/")    
            
    #  oprn hotstar
            elif "open hotstar" in command:
                speak("Opening Hotstar")
                webbrowser.open("https://www.hotstar.com/in")
    
    #  open linkedin
            elif "open linkedin" in command:
                speak("Opening LinkedIn")
                webbrowser.open("https://www.linkedin.com/")

    # open download folder
            elif "open downloads" in command or "open download folder" in command:
                speak("Opening Downloads folder")
                os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
    
    #  open documents folder
            elif "open documents" in command or "open document folder" in command:  
                speak("Opening Documents folder")
                os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))

    #  open pictures folder
            elif "open pictures" in command or "open picture folder" in command:
                speak("Opening Pictures folder")
                os.startfile(os.path.join(os.path.expanduser("~"), "Pictures"))
            
    #  open videos folder
            elif "open videos" in command or "open video folder" in command:
                speak("Opening Videos folder")
                os.startfile(os.path.join(os.path.expanduser("~"), "Videos"))
            
    # tell me date
            elif "date" in command:
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                speak(f"Today's date is {current_date}")
            
    #  tell me day
            elif "day" in command:
                current_day = datetime.datetime.now().strftime("%A")
                speak(f"Today is {current_day}")
    
    # shutdown computer
            elif "shutdown" in command or "shut down" in command:
                speak("Shutting down the computer")
                os.system("shutdown /s /t 1")
    
    # restart computer
            elif "restart" in command or "reboot" in command:
                speak("Restarting the computer")
                os.system("shutdown /r /t 1")
            
    # lock computer
            elif "lock" in command or "lock computer" in command:
                speak("Locking the computer")
                os.system("rundll32.exe user32.dll,LockWorkStation")

    # take a screenshot
            elif "take screenshot" in command:
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                speak("Screenshot saved successfully")

    # open camera
            elif "open camera" in command or "open webcam" in command:
                speak("Opening Camera")
                os.system("start microsoft.windows.camera:")

    # weather
            elif "weather" in command:
                speak("Opening Weather")
                webbrowser.open("https://www.weather.com/")
            
    # news
            elif "news" in command:
                speak("Opening News")
                webbrowser.open("https://news.google.com/")
            
    # create a text file
            elif "create a text file" in command or "create text file" in command:
                speak("Creating a text file on the desktop")
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                file_path = os.path.join(desktop_path, "New Text File.txt")
                with open(file_path, "w") as file:
                    file.write("This is a new text file created by Nikk.")
                speak("Text file created successfully on the desktop.")

    # create a folder
            elif "create a folder" in command or "create folder" in command:
                speak("Creating a folder on the desktop")
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                folder_path = os.path.join(desktop_path, "New Folder")
                os.makedirs(folder_path, exist_ok=True)
                speak("Folder created successfully on the desktop.")
    
    # delete a file
            elif "delete a file" in command or "delete file" in command:
                speak("Please specify the name of the file to delete")
                file_name = take_command()
                desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                file_path = os.path.join(desktop_path, file_name)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    speak(f"{file_name} has been deleted from the desktop.")
                else:
                    speak(f"{file_name} does not exist on the desktop.")
            
    #  volume up
            elif "volume up" in command:
                speak("Increasing volume")
                pyautogui.press("volumeup")
    
    # volume down
            elif "volume down" in command:
                speak("Decreasing volume")
                pyautogui.press("volumedown")
    
    # mute volume
            elif "mute" in command or "mute volume" in command:
                speak("Muting volume")
                pyautogui.press("volumemute")
            
    # unmute volume
            elif "unmute" in command or "unmute volume" in command:
                speak("Unmuting volume")
                pyautogui.press("volumemute")

    # maximize window
            elif "maximize window" in command:
                speak("Maximizing window")
                pyautogui.hotkey("win", "up")
    
    # minimize window
            elif "minimize window" in command:
                speak("Minimizing window")
                pyautogui.hotkey("win", "down")
            
            elif "remember" in command:
                info = command.replace("remember", "").strip()
                save_memory(info)
                speak(f"I will remember that {info}")

    # Take Note
            elif "write a note" in command or "take a note" in command:
                speak("What should I write?")
                note = take_command()
                if note != "":
                    save_note(note)

    # Read Notes
            elif "read notes" in command:
                read_notes()

            elif "remind me in" in command:
                try:
                    minutes_text = command.replace("remind me in", "").replace("minutes", "").replace("minute", "").strip()
                    minutes = int(minutes_text)
                    speak(f"Okay, I will remind you in {minutes} minutes.")
                    set_reminder(minutes)
                except ValueError:
                    speak("Please tell me the number of minutes.")

    # Send WhatsApp Message
            elif "send whatsapp message" in command or "send a whatsapp message" in command:
                speak("Whom should I send the message to?")
                contact = take_command().lower()
                phone_number = CONTACTS.get(contact)

                if phone_number is None:
                    speak("Contact not found.")
                    continue

                speak("What should I send?")
                message = take_command()
                send_whatsapp_message(phone_number, message)

            elif command != "":
                ai_chat(command)                           