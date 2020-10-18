# -*- coding: utf-8 -*-
import requests as r
import os
import sys
import subprocess

def startup_linux():
  os.system('sudo apt install -y python3 python3-pip')
  os.system('pip3 install setuptools telebot telethon flask pytelegrambotapi requests')

def startup_termux():
  os.system('apt install -y python python2')
  os.system('pip install setuptools telebot telethon flask pytelegrambotapi requests')

def get_ver():
  os.system('termux-info | grep Linux>f.txt || echo not>f.txt')
  versio = str(open('f.txt').read())
  if 'Linux' in versio:
    startup_termux()
    start_example()
  else:
    startup_linux()
    lol = start_example() 
    sleep(5)
    killprocess(lol)

def start_example():
  starting_command = subprocess.run(["python3", "lo.py"], capture_output=True)
  print(starting_command)
  return(starting_command)

def killprocess(starting):
  starting.kill
  

get_ver()