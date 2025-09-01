import time

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
    print("You Died".center(50))
    print(f"Twój wynik: ✨ {experience}/{level_cap} EXP | 🧝 {level} LVL".center(50))
    print()
    print("#" * 50)


