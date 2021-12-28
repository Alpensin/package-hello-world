import gtts
from playsound import playsound
from sys import argv

def hello_world(text = "Всем Привет!"):
    tts = gtts.gTTS(text, lang="ru")
    tts.save("hello.mp3")
    playsound("hello.mp3")


def main():
    try:
        text = argv[1]
    except IndexError:
        text  = "Ничего не ввели"
    hello_world(text)


if __name__ == '__main__':
    main()