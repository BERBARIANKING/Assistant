import webbrowser
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Specify the keyword to start the bot
keyword = 'start'

print("Say the keyword to start the bot!")

# Initial loop that waits for the keyword
while True:
    with sr.Microphone() as source:
        try:
            input_speech = r.listen(source)
            query = r.recognize_google(input_speech, language='en_gb')
            print(f'The query was: {query}')

            # If keyword is detected, break the loop
            if query.lower() == keyword:
                print("Keyword detected, starting the bot...")
                break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

print("Talk to the bot!")


# The main loop of bot
while True:
    with sr.Microphone() as source:
        input_speech = r.listen(source)
        # Exception handling added to manage errors in speech recognition
        try:
            query = r.recognize_google(input_speech, language='en_gb')
            print("Recognizing...")
            print(f'The query was: {query}')
            if query.lower() == 'hey':
                engine.say('Sup')
                engine.runAndWait()
            elif query.lower() == 'hello':
                engine.say('Hello Nikolas')
                engine.runAndWait()
            elif query.lower() == 'hello my friend':
                 engine.say('Hello boiiii')
                 engine.runAndWait()
            elif query.lower() == 'how are you doing today':
                engine.say('Fantastic')
                engine.runAndWait()
            elif query.lower() == 'tell me a joke':
                engine.say('Roses are Red , Violettes are Blue , input a joke whenever you are ready too')
                engine.runAndWait()
            elif query.lower() == 'tell me another joke':
                engine.say("I'm out")
                engine.runAndWait()
            elif query.lower() == 'search':
                engine.say('What do you want to search for?')
                engine.runAndWait()
                input_speech = r.listen(source)
                search_query = r.recognize_google(input_speech, language='en_gb')
                print(f'Searching for: {search_query}')
                engine.say('Hold on let me check')
                engine.runAndWait()
                url = f"https://www.google.com.tr/search?q={search_query}"
                webbrowser.open_new_tab(url)
            else:
                print('Goodbye')
                break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
