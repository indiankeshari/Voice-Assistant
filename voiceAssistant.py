import speech_recognition as sr
import pywhatkit
import pyautogui
import os
import subprocess
import datetime
import time
import pyttsx3


recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("listening....")
    recorded_audio = recognizer.listen(source, timeout=5)
    print("Done recording")
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("Decoded Text : {}".format(text))
    #pint(text)
except Exception as ex:
    print(ex)
    
text = text.lower()
if 'open notepad' in text:
    os.system("notepad")
    print("Done")
    
elif 'open chrome' in text:
    os.system("chrome")
    print("Done")
    
elif 'youtube' in text:
    song = text.replace('song', '')
    pywhatkit.playonyt(song)
        
elif 'turn off wifi' in text:
    mywish=subprocess.run (['netsh', 'interface', 'set', 'interface', "Wi-Fi", "admin=disable"])
    mywish
    
elif 'time' in text:
    time = datetime.datetime.now().strftime('%I:%M %p')
    engine=pyttsx3.init()
    engine.say('Current time is ' + time)
    engine.runAndWait()
        
elif 'open camera' in text:
    os.system("start microsoft.windows.camera:")
    
elif 'shutdown' in text:
    os.system("shutdown -s")
    
elif 'open spotify' in text:
    os.system("spotify")
    time.sleep(2)
    pyautogui.hotkey('ctrl','l')
    pyautogui.write('ya habibi',interval=0.1)
    for key in ['enter','pagedown','tab','enter','enter']:
        time.sleep(2)
        pyautogui.press(key)
        
elif 'do whatsapp'in text:
    engine=pyttsx3.init()
    engine.say("Tell me phone No")
    engine.runAndWait()
    number=input("Number please:")
    engine.say("Write your Messege here:")
    engine.runAndWait()
    messege=input("Messege:")
    pywhatkit.sendwhatmsg_instantly(number,messege)
    engine.say("Done")
    engine.runAndWait()
    
elif 'make folder' in text:
    folder_name=input()
    os.mkdir(folder_name)
    
elif 'remove folder' in text:
    folder_name=input()
    os.rmdir(folder_name)
