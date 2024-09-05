import_modules='''
import os # Os Module must be imported first to install any package if not installed in between
import time
#import mysql.connector as sqlcon
import pymysql as sqlcon
import pickle
import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE, K_UP
import csv
import webbrowser
import PySimpleGUI as sg
import subprocess
import wolframalpha
from GoogleNews import GoogleNews as gn
import pandas as pd
import randfacts
import pywhatkit
from num2words import num2words
import random
import wikipedia
import webbrowser
import pyjokes
import smtplib
import ctypes
import requests
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
'''
    
try:
    exec(import_modules)
except:
    print('Installing Required Packages')
    os.system('pip install matplotlib PySimpleGUI mysql-connector wolframalpha pyttsx3 PyAudio SpeechRecognition \
    wikipedia pyjokes requests twilio clint ecapture BeautifulSoup4 GoogleNews Pandas PyWhatKit randfacts num2words pygame')
    os.system('pip3 install matplotlib PySimpleGUI mysql-connector wolframalpha pyttsx3 PyAudio SpeechRecognition \
    wikipedia pyjokes requests twilio clint ecapture BeautifulSoup4 GoogleNews Pandas PyWhatKit randfacts num2words pygame')
    try:
        exec(import_modules)
    except:
        raise Exception('Unable to Install and import some particular Modules')
