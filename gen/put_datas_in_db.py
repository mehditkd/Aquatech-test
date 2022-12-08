import json
from dotenv import load_dotenv
from DB import DB

def init_env():
    load_dotenv()

def get_datas():
    with open("gen/all_tank_info.json") as f:
        datas = json.load(f)
    return datas

def main():
    db = DB()
    init_env()
    datas = get_datas()
    req = "delete from TankData where 1=1"
    if not db.post(req):
        print("Error")
    req = "insert into TankData (qte, date, level, pressure) values "
    values = [f"({data['qte']}, '{data['date']}', {data['level']}, {data['pressure']})" for data in datas]
    req += ", ".join(values)
    if not db.post(req):
        print("Error")

if __name__ == "__main__":
    main()
