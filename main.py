from monster import Monster
from player import Player
import visuals
import random

monsters_file_path = "monsters.json"



while True:
    visuals.start_screen()
    print("\nWybierz jedną z opcji:")
    print("1. Zacznij grać")
    print("2. Kto stworzył to cudo?")
    print("3. Wyjdź")
    try:
        player_choice = int(input("> "))
    except ValueError:
        visuals.clear_console()
        print("Nie ma takiej opcji")
        continue

    visuals.clear_console()

    if player_choice == 1:
        break
    elif player_choice == 2:
        visuals.credit_screen()
        visuals.clear_console()
    elif player_choice == 3:
        visuals.clear_console()
        visuals.end_screen()
        exit(0)
    else:
        print("Nie ma takiej opcji")


while True:
    print("Wpisz nazwę swojego bohatera:")
    player_name = input("> ")

    print(f"Czy twój bohater nazywa się \"{player_name}\"")
    print("Wpisz 1 by zatwierdzić")
    try:
        player_accept = int(input("> "))
    except ValueError:
        visuals.clear_console()
        print("Spróbuj jeszcze raz")
        continue

    visuals.clear_console()

    if player_accept == 1:
        break
    else:
        print("Spróbuj jeszcze raz")

start_player_hp = 100
start_player_power = 20
player = Player(player_name, start_player_hp, start_player_power)

enemy_test = Monster.load_monster_from_json(monsters_file_path, player.level)


while True:
    if not player.is_alive():
        visuals.death_screen(player.experience, player.level, player.level_cap)
        break


    player.show_info()
    enemy_test.show_info()
    print("\n\nWybierz jedną z opcji:")
    print("1. Atakuj")
    print("2. Wylecz się")
    try:
        player_choice = int(input("> "))
    except ValueError:
        visuals.clear_console()
        print("Nie ma takiej opcji")
        continue
    visuals.clear_console()

    if player_choice == 1:
        player.deal_damage(enemy_test)
    elif player_choice == 2:
        player.heal_damage(10)
    else:
        print("Nie ma takiej opcji")
        continue

    if not enemy_test.is_alive():
        enemy_test = Monster.load_monster_from_json(monsters_file_path, player.level)
        print(f"Pojawia się nowy przeciwnik {enemy_test.name}")
        continue

    enemy_choice = random.choice([1, 2])

    if enemy_choice == 1:
        enemy_test.deal_damage(player)
    elif enemy_choice == 2:
        enemy_test.heal_damage(10)


