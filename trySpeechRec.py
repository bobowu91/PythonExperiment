'''
This file has to be run in python 3.6 because some of the python packages are
not up to date for the most recent release of python.
'''
import re
import speech_recognition as sr
# take a look at the module and use.__version__ to see their version.
# import pyaudio
# print(pyaudio)
# print(sr)

r = sr.Recognizer()  # initiate a recognizer class object
mic = sr.Microphone()  # assign Microphone() method to mic
# mic_names = sr.Microphone.list_microphone_names()
# print(mic_names)

with mic as source:  # use context manager to take audio input
    r.adjust_for_ambient_noise(source)  # to handle ambient noise
    audio = r.listen(source)

# help(r.recognize_google)
# help(r.recognize_bing)

# for i in dir(r):
#     if re.search('recognize', i):
#         print(i)

# Chinese
# speech_text = r.recognize_google(audio, language='zh-CN')
# print(speech_text)  # print speech text

# English - US
speech_text = r.recognize_google(audio)
print(speech_text)  # print speech text

# French
# speech_text = r.recognize_google(audio, language='fr-FR')
# print(speech_text)  # print speech text


# API by Microsoft Azure; charging for usage
# speech_text = r.recognize_bing(audio,
#                                key='2e8124872dd346d2bb2d0d5ff126c56c',
#                                language='zh-CN')
# print(speech_text)  # print speech text
