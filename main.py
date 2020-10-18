# -*- coding: utf-8 -*-
import requests as r
import os
import sys

def startup_linux():
  os.system('sudo apt install -y python3 python3-pip')
  os.system('pip3 install setuptools telebot telethon pytelegrambotapi requests')

def startup_termux():
  os.system('apt install -y python python2')
  os.system('pip install setuptools telebot telethon pytelegrambotapi requests')

def get_ver():
  os.system('termux-info | grep Linux>f.txt || echo not>f.txt')
  versio = str(open('f.txt').read())
  if 'Linux' in versio:
    startup_termux()
  else:
    startup_linux() 

get_ver()