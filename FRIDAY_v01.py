import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os, random
import subprocess
import wolframalpha
import ctypes
import time
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Intro():
    '''
    Program starts with introduction. FRIDAY will give her intro
    '''
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak('Good Morning Sir')

    elif 12 <= hour < 18:
        speak('Good Afternoon Sir')

    else:
        speak('Good Evening Sir')

    speak('I am FRIDAY, your virtual assistant.')
    speak('What can i do for you?')


def InputSpeech():
    '''
    Take input from microphone and convert it into text.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\nListening...')
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')

    except:
        print("Sorry Sir!! I didn't hear properly. Can you say it again?")
        speak("Sorry Sir!! I didn't hear properly. Can you say it again?")
        return 'None'
    return query


def weather_info():
    '''
    Take query from user and extract weather information using openweathermap API
    '''
    api_key = "API-Key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    print("Of which city sir? ")
    speak("Of which city sir? ")
    city_name = InputSpeech()

    if city_name != 'None':
        url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            temp = y["temp"]
            pressure = y["pressure"]
            humidity = y["humidity"]
            z = x["weather"]
            wind_speed = x["wind"]["speed"]
            description = z[0]["description"]
            print(f"Weather Forecast of {city_name}")
            print("Temperature: " + str(round(temp-273,2)) + " °C"
                  "\nPressure: " + str(pressure) + " hPa"
                  "\nHumidity: " + str(humidity) + " %"
                  "\nWind Speed: " + str(wind_speed) + " km/h"
                  "\nDescription: " + str(description))

            speak(f"Weather Forecast of {city_name}")
            speak("Temperature: " + str(round(temp-273,2)) + " °C"
                  "\nPressure: " + str(pressure) + " hPa"
                  "\nHumidity: " + str(humidity) + " %" 
                  "\nWind Speed: " + str(wind_speed) + " km/h"
                  "\nDescription: " + str(description))
        else:
            speak("Sorry sir!! I can't find city")
    else:
        print("Sorry Sir!! I can't understand. Can you repeat your question?")
        speak("Sorry Sir!! I can't understand. Can you repeat your question?")


if __name__ == '__main__':
    Intro()
    while True:
        query = InputSpeech().lower()
        query = query.replace('can you', '')

        # Logics for executing tasks based on input audio

###################################################################################################################
    # wikipedia search

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            query = query.replace('search', '')

            try:
                result = wikipedia.summary(query, sentences=1)
                print('According to Wikipedia')
                speak('According to Wikipedia')
                print(result)
                speak(result)
            except:
                print("Sorry sir!! I can't find result")
                speak("Sorry sir!! I can't find result")

    # wikipedia search
###################################################################################################################
    # date time and weather

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {time}')

        elif 'the date' in query:
            date = str(datetime.datetime.now())[:10]
            speak(f"Today's Date is {date}")

        elif 'weather' in query:
            weather_info()

    # date time and weather
###################################################################################################################
    # about FRIDAY

        elif 'who are you' in query or 'hello friday' in query:
            speak('Hello sir, I am FRIDAY, your virtual assistant.')
            speak('What can i do for you?')

        elif 'how are you' in query:
            speak("I am Fine, How are you sir?")

        elif 'i am good' in query or 'i am fine' in query:
            speak("It's good to know that. How can i help you?")

        elif 'thank you' in query or 'thanks' in query:
            speak("Your Welcome Sir. What else I can do for you?")

###################################################################################################################
    # open websites

        elif 'open youtube' in query:
            print('Opening Youtube...')
            speak('Opening Youtube')
            webbrowser.open('youtube.com')
            time.sleep(8)

        elif 'open gmail' in query:
            print('Opening Gmail...')
            speak('Opening Gmail')
            webbrowser.open('gmail.com')
            time.sleep(8)

        elif 'open dtu' in query:
            print('Opening DTU Website...')
            speak('Opening DTU Website')
            webbrowser.open('dtu.ac.in')
            time.sleep(8)

    # open websites
###################################################################################################################
    # open applications
        elif 'play music' in query or 'play songs' in query:
            print('Playing Songs...')
            speak('Playing Songs')
            music_dir = 'C:\\Users\\vivek\\Music\\New'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))
            time.sleep(10)

        elif 'open ms word' in query or 'open word' in query or 'microsoft word' in query:
            print('Opening Microsoft Word...')
            speak('Opening Microsoft Word')
            file_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word'
            os.startfile(file_path)
            time.sleep(8)

        elif 'open ms ppt' in query or 'open ppt' in query:
            print('Opening Power Point Presentation...')
            speak('Opening Power Point Presentation')
            file_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint'
            os.startfile(file_path)
            time.sleep(8)

        elif 'open ms excel' in query or 'open excel' in query:
            print('Opening Microsoft Excel...')
            speak('Opening Microsoft Excel')
            file_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel'
            os.startfile(file_path)
            time.sleep(8)

        elif 'open google chrome' in query or 'open chrome' in query:
            print('Opening Google Chrome...')
            speak('Opening Google Chrome')
            file_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome'
            os.startfile(file_path)
            time.sleep(8)

        elif 'open wireshark' in query:
            print('Opening Wireshark...')
            speak('Opening Wireshark')
            file_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Wireshark'
            os.startfile(file_path)
            time.sleep(8)

    # open applications
###################################################################################################################
    # system tasks like shutdown, restart, log off, lock screen

        elif 'shutdown' in query:
            speak("Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "restart" in query:
            speak('System is restarting')
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("System is Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif ('lock' in query and 'screen' in query) or ('lock window' in query):
            speak("Locking this device")
            ctypes.windll.user32.LockWorkStation()
            time.sleep(10)

    # system tasks like shutdown, restart, log off, lock screen
###################################################################################################################
    # FRIDAY is sleeping

        elif "wait" in query or "stop listening" in query or 'hold on' in query:
            print("For how much time Sir?")
            speak("For how much time Sir?")
            sleep = False
            while not sleep:
                try:
                    input_time = InputSpeech().replace('seconds', '')
                    sleep_time = int(input_time.replace('second', ''))
                    print(f'I am sleeping for {sleep_time} seconds')
                    speak(f'I am Sleeping for {sleep_time} seconds')
                    time.sleep(sleep_time)
                    sleep = True
                except:
                    print('Please specify time in seconds')
                    speak('Please specify time in seconds')

    # FRIDAY is sleeping
###################################################################################################################
    # Wolfram alpha

        elif "calculate" in query:
            print('Calculating...')
            speak('Calculating')
            app_id = "API-Key"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]

            try:
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except:
                speak("Sorry sir!! I can't calculate")

        elif "what is" in query or "what's" in query or "who is" in query:
            print('Wait!! I am searching for result')
            speak('Wait!! I am searching for result')
            app_id = "API-Key"
            client = wolframalpha.Client(app_id)

            try:
                res = client.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)

            except:
                print("Sorry sir!! There is No result")
                speak("Sorry sir!! There is No result")

    # Wolfram alpha
###################################################################################################################

        elif 'quit' in query or 'exit' in query or 'terminate' in query:
            speak('Terminating program')
            exit()
