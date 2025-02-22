

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_drink_choice(MENU, resources):
    drink = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    if drink not in MENU:
        print("Sorry, we don't have this drink.")
        return None  # Geçersiz seçim durumunda None döndürüyoruz.

    # Kaynakları düşelim
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if ingredient in resources:
            resources[ingredient] -= amount
    return drink

#Kullanıcı bir sonraki kahve istemesi


# Kullanıcının seçimini alın
selected_drink = get_drink_choice(MENU, resources)
if selected_drink is None:
    # Geçersiz seçim durumunda işlemi sonlandırabilirsiniz
    exit()


# Para işlemleri
def process_coins():
    coin1 = int(input("How many quarters?: "))
    coin2 = int(input("How many dimes?: "))
    coin3 = int(input("How many nickles?: "))
    coin4 = int(input("How many pennies?: "))
    return coin1 * 0.25 + coin2 * 0.10 + coin3 * 0.05 + coin4 * 0.01


total_inserted = process_coins()
drink_cost = MENU[selected_drink]["cost"]
change = round(total_inserted - drink_cost, 2)

if total_inserted >= drink_cost:
    print(f"Please take your {selected_drink}. This is your change {change}")
else:
    print("Insufficient funds.")


while True:
    answer = input("Would you like to make another drink? (yes/no): ").lower()
    if answer == "yes":
        get_drink_choice(MENU, resources)
        process_coins()
    elif answer == "no":
        print("Thank you for your business.")
        break
    else:
        print("Please enter yes or no.")


