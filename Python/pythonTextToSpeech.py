import pyttsx3


engine = pyttsx3.init()

engine.say("I will not speak this text")
engine.runAndWait()

rate = engine.getProperty('rate')
engine.setProperty('rate', 155)

volume = engine.getProperty('volume')
engine.setProperty('volume',2.0)

# engine.say("This is the new python library, that specifically work for text to speech.")
engine.save_to_file('This is the new python library, that specifically work for text to speech.', 'test.mp3')
engine.say('My current speaking rate is ' + str(rate))
engine.say("Hello World!")
engine.runAndWait()
engine.stop()