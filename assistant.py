import speech_recognition
import pyttsx3
from datetime import date

today = date.today()
d2 = today.strftime("%B %d, %Y")
print("d2 =",d2)

robot_ear = speech_recognition.Recognizer()
you = ""
robot_brain = ""
engine = pyttsx3.init()

while TRUE:
    with speech_recognition.Microphone() as mic:
        print("Robo: I'm Listening...")
        audio = robot_ear.listen(mic)

    try:
        print("Robo:...")
        you = robot_ear.recognize_google(audio)
    except:
        you = ""


    if you =="":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Dung Lai"
    elif "today" in you:
        robot_brain = "thu 6"
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot_brain ="Donald Trump"
    elif "thank":
        robot_brain = "I'm fine thank you and you"
    elif "bye":
        robot_brain = "I'm fine thank you and you"
        print("Robot:" + robot_brain)
        engine.say(robot_brain)
        engine.runAndWait()
    else:
        robot_brain = "I don't know"

    print("You:" + you)
    print("Robot:" + robot_brain)


    engine.say(robot_brain)
    engine.runAndWait()
