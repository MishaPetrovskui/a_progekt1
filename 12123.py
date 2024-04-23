import random

def generate_example():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, num1)
    return num1, num2

def validate_input(user_input, expected_result):
    if user_input.lower() in ["q", "quit", "вихід", "в", "выход"]:
        return "quit"
    elif user_input.isnumeric():
        if int(user_input) == expected_result:
            return "Вірно"
        else:
            return "Невірно"
    else:
        return "Невірно, це не число"

def load_leaderboard():
    leaderboards = []
    with open("leaderboard.txt", "r+", encoding="utf-8") as leaderboard:
        for line in leaderboard:
            if "," in line:
                chet, name = line.split(",")
                leaderboards.append((int(chet), name))
    return leaderboards


def update_leaderboard(chet, name):
    leaderboard = load_leaderboard()
    leaderboard.append((chet, name))
    top_scores = []
    for _ in range(5):
        max_score = -1
        max_entry = None
        for entry in leaderboard:
            if entry[0] > max_score:
                max_score = entry[0]
                max_entry = entry
        if max_entry:
            top_scores.append(max_entry)
            leaderboard.remove(max_entry)
    with open("leaderboard.txt", "w", encoding="utf-8") as file:
        for chet, name in top_scores:
            file.write(f"{chet},{name}\n")


def display_leaderboard():
    leaderboards = load_leaderboard()
    if not leaderboards:
        print("Таблиця лідерів порожня")
    else:
        print("Топ 5 лідерів:")
        for i in range(len(leaderboards)):
            chet, name = leaderboards[i]
            print(f"{i + 1}. {name}: {chet}")

def main():
    chet = 0
    hizni = 3
    while True:
        num1, num2 = generate_example()
        print(f"Життя: {hizni}\nРахунок: {chet}")
        diya = input(f"{num1} + {num2} = ")
        result = validate_input(diya, num1 + num2)
        if result == "quit":
            print(f"Кінцевий рахунок: {chet}")
            display_leaderboard()
            break
        elif result == "Вірно":
            print("Вірно!")
            chet += 1
        elif result == "Невірно":
            print(f"Неправильно, правильна відповідь: {num1 + num2}")
            hizni -= 1
            if hizni == 0:
                print("Життя закінчилися")
                name = input("Ведіть ім'я: ")
                update_leaderboard(chet, name)
                print("Кінець")
                print(f"Рахунок: {chet}")
                display_leaderboard()
                break
        else:
            print("Невірно, це не число")

main()
