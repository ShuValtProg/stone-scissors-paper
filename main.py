# камень ножницы бумага
import random

player_input = str(input("камень/ножницы/бумага? "))

count = 0

bot_list = ["камень", "ножницы", "бумага"]

while True:

    bot_choice = random.choice(bot_list)

    if player_input == bot_choice:
        print(f"{player_input} VS {bot_choice}, Ничья! Никто не получает очков!")


    elif player_input == "ножницы":

        if bot_choice == "бумага":
            print(f"{player_input} VS {bot_choice}, Вы выиграли! ")
            count += 1

        else:
            print(f"{player_input} VS {bot_choice}, Вы проиграли!")
            count -= 1

        print(f"Кол-во ваших очков: {count}")


    elif player_input == "камень":

        if bot_choice == "бумага":
            print(f"{player_input} VS {bot_choice}, Вы проиграли! ")
            count -= 1

        else:
            print(f"{player_input} VS {bot_choice}, Вы выиграли!")
            count += 1

        print(f"Кол-во ваших очков: {count}")

    elif player_input == "бумага":

        if bot_choice == "ножницы":
            print(f"{player_input} VS {bot_choice}, Вы проиграли! ")
            count -= 1

        else:
            print(f"{player_input} VS {bot_choice}, Вы выиграли!")
            count += 1

        print(f"Кол-во ваших очков: {count}")

    play_again = str(input("Сыграем еще? (д/н): "))
    if play_again.lower() != "д":
        print("Игра окончена! ")
        break
    else:
        player_input = str(input("камень/ножницы/бумага? "))
