import speech_recognition
import pyttsx3 as tts
import pywhatkit
import datetime
import wikipedia


listener = speech_recognition.Recognizer()
machine = tts.init()

def talk(text):
    machine.say(text)

machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with speech_recognition.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            if "" in instruction:
                instruction = instruction.replace('', '')
                print(instruction)
            print(instruction)
    
    except:
        pass

    return instruction


def play_me():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time"+ time)

    elif '' in instruction:
        human = instruction.replace('', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info) 
    
    else:
        talk('please repeat')
    


play_me()


# datetime.datetime.now().strftime('%d /%m %Y')