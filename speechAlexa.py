# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 18:26:23 2021

@author: User
"""

import speech_recognition as sr
listener= sr.recognize_api()

try:
    with sr.Microphone() as source:
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        print(command)
except:
    pass
        
