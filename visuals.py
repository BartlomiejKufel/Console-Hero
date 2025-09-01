import time
import json

with open("assets/emojis.json", "r", encoding="utf-8") as f:
    emojis = json.load(f)

game_title = "CONSOLE HERO"


def clear_console():
    print("\n" * 100)

def start_screen():
    print("#" * 50)
    print()
    print(game_title.center(50))
    print()
    print("#" * 50)

def credit_screen():
    print("#" * 50)
    print()
    print("Tą grę stworzył Bartłomiej Kufel".center(50))
    print("https://github.com/BartlomiejKufel".center(50))
    print()
    print("#" * 50)

    time.sleep(3)


def end_screen():
    print("#" * 50)
    print()
    print("Nara".center(50))
    print()
    print("#" * 50)

def death_screen(experience, level, level_cap):
    print("#" * 50)
    print()
    print(f"You Died {emojis.get('skull')}".center(50))
    print(f"Twój wynik: {emojis.get('stars')} {experience}/{level_cap} EXP | {emojis.get('hero')} {level} LVL".center(50))
    print()
    print("#" * 50)


