import webbrowser
from pystyle import Colors, Colorate
import time
import sys

def prompt_mod_download(mod_name, mod_link):
    while True:
        user_input = input(f"""


Would You Like to Insntall, and Import Spectre Client to your mods folder? (Works with Linux and Windows -- Mac NOT SUPPORTED!!!) y/n

""").strip().lower()
        
        if user_input == 'y':
            print(f"Opening the download link for {mod_name}...")
            webbrowser.open(mod_link)
            break
        elif user_input == 'n':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 'y', 'n'")

def progress_bar(total=50, delay=0.05):
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = '█' * i + '-' * (total - i)
        colored_bar = Colorate.Horizontal(Colors.rainbow, f"|{bar}| {percent:.2f}%")
        sys.stdout.write(f'\r{colored_bar}')
        sys.stdout.flush()
        time.sleep(delay)
    print()

def typing_animation(text, delay=0.05):
    
    gradient_colors = Colors.blue_to_cyan
    colored_text = [Colorate.Vertical(gradient_colors, char) for char in text]
    
    for char in colored_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)   
    print()  

def welcome_message():
  
    time.sleep(1)  
    sys.stdout.write("\033[H\033[J") 

    welcome_text = "Welcome Spectre User, to the Installer"
    typing_animation(welcome_text, delay=0.05)  

progress_bar(total=50, delay=0.05)

welcome_message()

mod_name = "Spectre Client"
mod_link = "https://cdn.discordapp.com/attachments/1221586084845064305/1280327204131176482/Spectre.jar?ex=66d7ad20&is=66d65ba0&hm=2dd61a37ff02be089af7b005345fb2fd1e3c9540bab8358c308a4efd6e85a4d6&"
prompt_mod_download(mod_name, mod_link)
