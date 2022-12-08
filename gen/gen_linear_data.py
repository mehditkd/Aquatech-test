from datetime import datetime, timedelta
import json

def main():
    datas = []
    date_format = "%Y:%m:%d %H:%M"
    date = datetime.now()
    for i in range(10000):
        datas.append({
            "qte": i,
            "level": i * 2,
            "pressure": i * 3,
            "date": date.strftime(date_format)
        })
        date += timedelta(minutes=1)
    with open("gen/all_tank_info.json", "w") as f:
        json.dump(datas, f, indent=4)

if __name__ == '__main__':
    main()