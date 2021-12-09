from colored.colored import attr
from pypresence import Presence
from colored import fg, bg, attr

import time
import json
import sys
import os
import platform
import ctypes


class colors:
    blue = fg(110)
    white = fg('white')


def typewritter(text):
    for x in text:
        print(x, end="")
        sys.stdout.flush()
        time.sleep(0.1)

def error(text):
    print(f"{colors.blue}[{colors.white}ERROR{colors.blue}]{colors.white} {text}")
    time.sleep(1)
    os.system('CLS')
    menu()

def menu():
    username = os.getlogin()
    operatingsystem =  platform.platform()

    print(
    f"""
    {colors.blue}     ________
    {colors.blue}    /_______/\         {colors.blue}{username}{colors.white}@{colors.blue}boogethook
    {colors.blue}    \ \    / /         {colors.white}==========================
    {colors.blue}  ___\ \__/_/___       {colors.blue}Loading Custom Configs: {colors.white}load <config-name>
    {colors.blue} /____\ \______/\      {colors.blue}Loading Default Config: {colors.white}load default 
    {colors.blue} \ \   \/ /   / /      
    {colors.blue}  \ \  / /\  / /       
    {colors.blue}   \ \/ /\ \/ /        
    {colors.blue}    \_\/  \_\/
    """
    )
    
    try:
        command, arg = input(f" {colors.blue}{username}{colors.white}@{colors.blue}boogehook{colors.white}~{colors.blue}${colors.white} ").split(' ')
    except(ValueError):
        error('Missing a required argument!')
    else:
        if command == "load":
            if arg == "default":
                initRpc('default')
            else:
                if arg is not 'default':
                    if os.path.isfile(f'configs/{arg}.json'):
                        initRpc(arg)
                    else:
                        error('Config was not found!')
        else:
            error('Invalid command! Please try again.')
    

def initRpc(configname):
    with open(f'configs/{configname}.json') as f:
        try:
            data = json.load(f)
        except(ValueError):
            error('The chosen config was not setup in the correct format!')
            menu()

    client_id = data['client_id']
    top_text = data['top_text']
    bottom_text = data['bottom_text']
    large_image_name = data['large_image_name']
    large_image_name_text = data['large_image_name_text']
    include_btn1 = data['include_button1']
    include_btn2 = data['include_button2']
    btn1_text = data['button1_text']
    btn2_text = data['button2_text']
    btn1_link = data['button1_link']
    btn2_link = data['button2_link']
    time_elapse = data['time_elapse']

    if include_btn1 == "false": # No buttons
        nobtn = True

        btn1_text = 'NULL'
        btn2_text = 'NULL'
        btn1_link = 'NULL'
        btn2_link = 'NULL'
    elif include_btn1 == "true": # One button
        if include_btn2 == "false":
            nobtn = False

            buttonforrpc = buttons=[{"label": btn1_text, "url": btn1_link}]

            btn1_text = btn1_text
            btn2_text = 'NULL'
            btn1_link = btn2_link
            btn2_link = 'NULL'
        elif include_btn2 == "true": # Two buttons
            nobtn = False

            buttonforrpc = buttons=[{"label": btn1_text, "url": btn1_link}, {"label": btn2_text, "url": btn2_link}]

            btn1_text = btn1_text
            btn2_text = btn2_text
            btn1_link = btn1_link
            btn2_link = btn2_link
    
    if time_elapse == "true":
        menu_time_elapse = "Using"
    else:
        menu_time_elapse = "Not Using"

    start_time = int(time.time())

    RPC = Presence(client_id, pipe=0)  
    RPC.connect()

    os.system('CLS')

    print(f" {colors.white}RPC has been launched!")
    print(
    f"""
    {colors.blue}     ________
    {colors.blue}    /_______/\         {colors.blue}Top Text: {colors.white}{top_text}
    {colors.blue}    \ \    / /         {colors.blue}Bottom Text: {colors.white}{top_text}
    {colors.blue}  ___\ \__/_/___       {colors.blue}Button 1 Text: {colors.white}{btn1_text} | {colors.blue}Button 1 Link: {colors.white}{btn1_link}
    {colors.blue} /____\ \______/\      {colors.blue}Button 2 Text: {colors.white}{btn2_text} | {colors.blue}Button 2 Link: {colors.white}{btn2_link}
    {colors.blue} \ \   \/ /   / /      {colors.blue}Large Image Name {colors.white}{large_image_name} | {colors.blue}Large Image Text: {colors.white}{large_image_name_text}
    {colors.blue}  \ \  / /\  / /       {colors.blue}Using Time Elapse?: {colors.white}{menu_time_elapse}
    {colors.blue}   \ \/ /\ \/ /        {colors.blue}Client ID: {colors.white}{client_id}
    {colors.blue}    \_\/  \_\/
    """
    )

    if nobtn == True:
        if time_elapse == 'true':
            while 1:
                RPC.update(state=bottom_text, details=top_text, large_image=large_image_name, large_text=large_image_name_text, start=start_time) 
                time.sleep(15)
        else:
            while 1:
                RPC.update(state=bottom_text, details=top_text, large_image=large_image_name, large_text=large_image_name_text) 
                time.sleep(15)
         
    else:
        if time_elapse == 'true':
            while 1:
                RPC.update(state=bottom_text, details=top_text, large_image=large_image_name, large_text=large_image_name_text, buttons=buttonforrpc, start=start_time) 
                time.sleep(15)
        else:
            while 1:
                RPC.update(state=bottom_text, details=top_text, large_image=large_image_name, buttons=buttonforrpc, large_text=large_image_name_text) 
                time.sleep(15)



def init():
    ctypes.windll.kernel32.SetConsoleTitleA("$")

    os.system('CLS')

    username = os.getlogin()
    
    typewritter(" Loading boogethook RPC...")

    time.sleep(0.3)
    os.system('CLS')

    typewritter(f" Welcome {username}!\n\n")

    menu()
    
        
        

if __name__ == "__main__":
    init()