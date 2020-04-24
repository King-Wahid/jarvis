from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang= 'en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

"""Listens to commands"""

def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    """Loop back to continue to listen to command"""

    try:
        command = r.recognize_google(audio)
        print("You said " + command + '/n')

    except sr.UnknownValueError:
        assistant(myCommand())

    return command

"""if statements for executing commands"""
def assistant(command):

    if 'open Reddit python' in command:
        chrome_path = "http://google.com/"
        url = 'https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)

    if "what's up" in command:
        talkToMe('Chilling bro')

    if 'play music' in command:
        talkToMe('Any song you have on mind in youtube')
        chrome_path = "http://google.com/"
        youtube_url = 'https://www.youtube.com/'
        webbrowser.get(chrome_path).open(youtube_url)

    if 'email' in command:
        talkToMe('who is the recipient')
        # pylint: disable=unused-variable
        reciever  = myCommand()
        content = myCommand()

        """init gmail SMTP"""
        mail = smtplib.SMTP('smtp.gmail.com',587)

        """identify to server"""
        mail.ehlo()
        mail.starttls()

        """encrypt sesssion"""
        mail.starttls()

        """login"""
        mail.login('username', 'password')

        """send message"""
        mail.send(content)

        """close connection"""
        mail.close()

        talkToMe('Email sent')

    talkToMe('I am ready for your command')

    while True:
        assistant(myCommand())
