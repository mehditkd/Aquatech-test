import json
import math

def get_tank_consumption():
    with open("gen/tank_consumption.json", "r") as f:
        return json.load(f)

def get_tank_info():
    with open("gen/tank_info.json", "r") as f:
        return json.load(f)

def get_pressure(cons, height):
    z = height / 100
    pressure = z * 9.81
    return pressure

def gen_tank_info(consumption, tank_data):
    all_infos = []
    curr_consumption = 1000000000
    for c in consumption:
        curr_consumption += c["consumption"]
        height = curr_consumption / int(tank_data["dim"]["x"]) / int(tank_data["dim"]["y"])
        pressure = get_pressure(curr_consumption, height)
        info = {
            "qte": curr_consumption / 1000,
            "date": c["date"],
            "level": height,
            "pressure": pressure
        }
        all_infos.append(info)
    return all_infos

def main():
    consumption = get_tank_consumption()
    tank_data = get_tank_info()
    all_infos = gen_tank_info(consumption, tank_data)
    with open("gen/all_tank_info.json", "w") as f:
        json.dump(all_infos, f, indent=4)

if __name__ == '__main__':
    main()
