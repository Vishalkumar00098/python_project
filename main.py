import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

text_to_speech("Hello, vishal.")


# project 2



# import os
#
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1 Created by vishal")
#     while True:
#         x = input("Enter what you want me to spreak: ")
#         if x == "q":
#             os.system("say bye bye friend")
#             break
#         command = f"say {x}"
#         os.system(command)