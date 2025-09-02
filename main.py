from monster import Monster
from player import Player, heal_potion_index
import visuals
import random

monsters_file_path = "assets/monsters.json" # ścieżka do pliku z potworami
floor_number = 1 # numer poziomu

#Start gry, menu startowe
visuals.clear_console()
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

    if player_choice == 1: # rozpoczęcie gry
        break
    elif player_choice == 2: # autor gry
        visuals.credit_screen()
        visuals.clear_console()
    elif player_choice == 3: # wyjście z gry
        visuals.clear_console()
        visuals.end_screen()
        input()
        exit(0)
    else:
        print("Nie ma takiej opcji")


#Ustawienie nazwy dla bohatera, którym gra gracz
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

#Stworzenie postaci gracza z nazwą i defaultowymi wartościami zdrowia i siły
player = Player(player_name, 0, 0)

#Stowrzenie pierwszego przeciwnika
enemy = Monster.load_monster_from_json(monsters_file_path, player.level)


while True:
    #Sprawdzenie, czy gracz dalej żyje
    if not player.is_alive():
        visuals.death_screen(player.experience, player.level, player.level_cap, floor_number)
        input()
        break

    #Informacje o graczu i przeciwniku
    visuals.floor_info(floor_number)
    player.show_info()
    enemy.show_info()

    #Wybór akcji gracza
    print("\n\nWybierz jedną z opcji:")
    print(f"1. Atakuj {visuals.emojis.get('sword')}")
    if player.bag[heal_potion_index].is_in_bag():
        print(f"2. Wylecz się {player.bag[heal_potion_index].amount}/{player.bag[heal_potion_index].limit} {visuals.emojis.get('health_potion')}")
    else:
        print(f"2. Brak Mikstur Leczenia w plecaku! {visuals.emojis.get('health_potion')}")

    try:
        player_choice = int(input("> "))
    except ValueError:
        visuals.clear_console()
        print("Nie ma takiej opcji")
        continue
    visuals.clear_console()

    if player_choice == 1:
        player.deal_damage(enemy)
    elif player_choice == 2 and player.bag[heal_potion_index].is_in_bag():
        player.heal_damage(10)
        player.bag[heal_potion_index].amount -= 1
    elif player_choice == 2 and not player.bag[heal_potion_index].is_in_bag():
        print("Brak Mikstur Leczenia w plecaku!")
        continue
    else:
        print("Nie ma takiej opcji")
        continue

    #sprawdzenie, czy nie trzeba wysłać nowego przeciwnika
    if not enemy.is_alive():
        floor_number+=1
        enemy = Monster.load_monster_from_json(monsters_file_path, player.level)
        visuals.change_floor(floor_number)
        print(f"Pojawia się nowy przeciwnik {enemy.name}")

        continue

    #Wybór akcji przeciwnika
    enemy_choice = random.choice([1, 2])

    if enemy_choice == 1:
        enemy.deal_damage(player)
    elif enemy_choice == 2:
        enemy.heal_damage(10)


