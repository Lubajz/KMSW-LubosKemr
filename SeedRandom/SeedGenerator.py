import os
import time
import random
import pyautogui


def collect_seed_data():
    # Získání současného času
    current_time_seed = int(time.time())

    # Získání pozice myši
    mouse_x, mouse_y = pyautogui.position()
    mouse_seed = (mouse_x << 16) + mouse_y

    # Výzva pro uživatele k zadání náhodného vstupu
    user_input_seed = input("Enter something random and press Enter: ")

    return current_time_seed, mouse_seed, hash(user_input_seed)


def generate_seed():
    #Získání dat z různých zdrojů pomocí funkce
    current_time_seed, mouse_seed, user_input_seed = collect_seed_data()

    # Vygenerovaní náhodnych bytů semínka
    random_bytes_seed = os.urandom(16)

    # Zkombinování dat pro vytvoření finálního semínka
    combined_seed = (
        current_time_seed ^ int.from_bytes(
            random_bytes_seed, byteorder='big') ^ mouse_seed ^ user_input_seed
    )

    return combined_seed


# Inicializace random generátorů pomocí vytvořeného semínka
seed = generate_seed()
random.seed(seed)

#Vygenerování náhodného čísla iterací dle zadaného rozsahu od uživatele
min_iterations = int(input("Enter number and press Enter: "))
max_iterations = int(input(f"Enter second number bigger than {min_iterations} and press Enter: "))
num_of_iterations = random.randint(min_iterations, max_iterations)

#Generování pseudonáhodných čísel 
for i in range(num_of_iterations):
    random_number = random.randint(0, 5000)
    print("Pseudorandom number:", random_number)
