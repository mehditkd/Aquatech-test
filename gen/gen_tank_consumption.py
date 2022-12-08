import json
import random
from datetime import datetime, timedelta

def get_tank_info():
    with open("gen/tank_info.json", "r") as f:
        return json.load(f)

def get_gen_choice():
    print("Generation choice: random")
    user_choice = input("What generation choice do you want? [random, real]")
    if user_choice not in ["random", "real"]:
        return "random"
    return user_choice

def random_gen(max_capacity, curr, _):
    sign = random.choice([-1, 1])
    if sign == -1:
        return -random.randint(0, curr)
    return random.randint(0, max_capacity - curr)

def arbitrary_consumption(max_capacity, curr, date):
    consumption = [
        0.5, 0.4, 0.2, 0.1, 0.1, 1,
        1.2, 2.6, 1.1, 1, 1, 0.9,
        1, 1.1, 0.9, 0.8, 1, 3,
        2.8, 2.7, 1.7, 1.3, 0.9, 0.6
    ] # percentage / hour
    arbitrary_factor = max_capacity // 4
    multiplier = -1 if consumption[date.hour] > 1 else 1
    res = (arbitrary_factor * consumption[date.hour] * multiplier) // 60
    print(arbitrary_factor, max_capacity, curr, res)
    if curr + res < 0:
        return -curr
    if curr + res > max_capacity:
        return max_capacity - curr
    return res

def gen_consumption(gen_choice, max_capacity, curr, time):
    choices = {
        "random": random_gen,
        "real": arbitrary_consumption,
    }
    return choices[gen_choice](max_capacity, curr, time)

def generate(tank):
    datas = []
    date_format = "%Y:%m:%d %H:%M"
    date = datetime.now()
    max_capacity = int(tank["dim"]["x"]) * int(tank["dim"]["y"]) * int(tank["dim"]["z"])
    curr_capacity = max_capacity
    print("Max capacity: {}".format(max_capacity))
    gen_choice = get_gen_choice()
    for i in range(60 * 24 * 7):
        d = {
            "date": date.strftime(date_format),
            "consumption": gen_consumption(gen_choice, max_capacity, curr_capacity, date),
        }
        datas.append(d)
        curr_capacity += d["consumption"]
        if curr_capacity < 0:
            curr_capacity = 0
        if curr_capacity > max_capacity:
            curr_capacity = max_capacity
        print(curr_capacity, max_capacity)
        date += timedelta(minutes=1)
        max_capacity
    return datas

def main():
    tank_info = get_tank_info()
    datas = generate(tank_info)
    with open("gen/tank_consumption.json", "w") as f:
        json.dump(datas, f, indent=4)

if __name__ == '__main__':
    main()