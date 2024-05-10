import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import datetime

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def take_command(self):
        with self.microphone as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            print("I'm having trouble accessing the Google API. Please try again later.")
            return ""
        return query.lower()

    def wish_me(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.speak("Good Morning!")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("Hey, how can I assist you today?")

    def search_wikipedia(self, query):
        self.speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia")
            print(results)
            self.speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            self.speak("There are multiple results. Please specify your search.")
        except wikipedia.exceptions.PageError:
            self.speak("Sorry, I couldn't find any information on that topic.")

    def open_website(self, url):
        webbrowser.open(url)

    def toss_coin(self):
        result = random.choice(["Head", "Tail"])
        self.speak(f"The result of the coin toss is {result}")

    def tell_joke(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Parallel lines have so much in common. It's a shame they'll never meet!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ]
        joke = random.choice(jokes)
        self.speak(joke)

    def get_time(self):
        str_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {str_time}")

    def get_date(self):
        str_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today's date is {str_date}")

    def process_query(self, query):
        if 'wikipedia' in query:
            self.search_wikipedia(query)
        elif 'open youtube' in query:
            self.open_website("https://www.youtube.com")
        elif 'open google' in query:
            self.open_website("https://www.google.com")
        elif 'open stackoverflow' in query:
            self.open_website("https://www.stackoverflow.com")
        elif 'play' in query:
            self.open_website(f"https://www.youtube.com/results?search_query={query.replace('play', '')}")
        elif 'search' in query:
            self.open_website(f"https://www.google.com/search?q={query.replace('search', '')}")
        elif 'toss a coin' in query:
            self.toss_coin()
        elif 'tell me a joke' in query:
            self.tell_joke()
        elif 'time' in query:
            self.get_time()
        elif 'date' in query:
            self.get_date()
        else:
            self.speak("Sorry, I didn't understand that command.")

    def run(self):
        self.wish_me()
        while True:
            query = self.take_command()
            if 'bye' in query:
                self.speak("Goodbye!")
                break
            elif 'toru' in query:
                self.process_query(query)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
