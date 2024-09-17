import requests
from playsound import playsound
from datetime import date
import os
import random
import wikipedia
import pyowm
# import nltk
# import google

boss = "Andrew"
Andrew = ""
Elina = ""
name = ""
error = 0
response = ["Okay, let me see,....", "Wait me a sec..", "Hold on...."]
thanks = ["It is my pleasure!", "The feeling is mutual.", "I am happy to be of assistance."]
goodnight = ["Bonne nuit mon amour!", "Sleep well, Andrew. Have a sweet dream!", "Buenas noches, mi amor!", "Good night, sleep tight!"]
goodbye = ["Blow a kiss, goldfish!", "Bye, see you again!", "Au revoir mon amour!","I can't wait to see your beautiful face again!","Have fun without me!"]
nevermind = ["HATE YOUUU!", "Haizzz! Are you mad?", "Urghh! You wasted my time"]

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/MF3mGyEYCl7XYWbV9V6O/stream"
headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "7cec7418d89ae684445d842f6ebf61ea"
}

def speak():
    data = {
    "text": Elina,
    "model_id": "eleven_multilingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
        }
    }
    response = requests.post(url, json=data, headers=headers, stream=True)
    os.remove('elina_voice.mp3')
    with open('elina_voice.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    print("Elina: " + Elina)
    playsound('elina_voice.mp3')
def wiki_search():
    global Elina
    try:
        results = wikipedia.search(Andrew)
    except:
        answer = "No data received"
    try: 
        wikiPage = wikipedia.page(results[0]) 
        answer = wikipedia.summary(wikiPage.title, sentences = 2 )
        Elina = answer
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
        answer = wikipedia.summary(wikiPage.title, sentences = 2 )
        Elina = answer
    except:
        result = "Your command does not match any data :("
        Elina = result
def verifying():
    global name, error, bool
    while name != boss:
        error = error + 1 
        if error == 3:  
            print("Access denied!\nGO AWAY!")
            quit()
        elif bool == True or name == "":
            print("Sorry, I can't hear you")
            print("Access denied! Please try again!")
            print(f"What is your name?")
            name = input("My name is: ")
            bool = name.isspace()
        else:
            print("Access denied! Please try again!")
            print(f"What is your name?")
            name = input("My name is: ")
            bool = name.isspace()
def weather_search():
    global Elina
    owm = pyowm.OWM('21f592716c0dc5d79039d2a779ce51d7')
    weather_mgr = owm.weather_manager()
    place = Andrew
    observation = weather_mgr.weather_at_place(place)
    temperature = observation.weather.temperature("celsius")["temp"]
    humidity = observation.weather.humidity
    pressure = observation.weather.pressure["press"]
    pressure = "{:.2f}".format((pressure)/1013.25)
    description = observation.weather.detailed_status
    Elina = ("Weather in " +
                        str(Andrew).capitalize() + ":" +
            "\n\tTemperature: " +
                        str(temperature) + "°C" +
            "\n\tAtmospheric pressure: " +
                        str(pressure) + "atm" +
            "\n\tHumidity: " +
                        str(humidity) + "%" +
            "\n\tDetailed status: " +
                        str(description))

print(f"What is your name?")
name = input("My name is: ")
bool = name.isspace()

verifying()
print("Elina: ...")       
Elina = "Hello Andrew!\n\tMy name is Elina, and I'm your virtual assistant.\n\tWhat can I help you?"  
speak()

while True:
    Andrew = input("Andrew: ")
    Andrew = Andrew.lower()
    
    if "today" in Andrew:
        today = date.today()
        Elina = "It is " + today.strftime("%B, %d, %Y")
    elif "handsome" in Andrew:
        Elina = "It's you, Andrew! I love youuu!"
    elif "wikipedia" in Andrew or "wiki" in Andrew:
        print("Elina: ... ")  
        Elina = "I have entered the universal databank.\n\tWhat are you looking for?"
        speak()
        Andrew = input("Andrew: ")
        Elina = random.choice(response)
        speak()
        wiki_search()
    elif "weather" in Andrew:
        print("Elina: ... ")
        Elina = "Which city do you want to ask?"
        speak()
        Andrew = input("Andrew: ")
        Elina = random.choice(response)
        speak()
        weather_search()
    elif "thanks" in Andrew or "thank you" in Andrew:
        Elina = random.choice(thanks)
    elif "night" in Andrew:
        print("Elina: ... ")
        Elina = random.choice(goodnight)
        speak()
        break
    elif "bye" in Andrew:
        print("Elina: ... ")
        Elina = random.choice(goodbye)
        speak()
        break
    elif "nevermind" in Andrew or "nothing" in Andrew:
        print("Elina: ... ")
        Elina = random.choice(nevermind)
        speak()
        break
    else:
        Elina = "I don't understand your question."
#Elina voice  
    print("Elina: ... ")  
    speak()