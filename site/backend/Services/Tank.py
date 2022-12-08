from Data.TankData import TankData
from Utils.DB import DB

class Tank:

    def __init__(self):
        self.db = DB()

    def get(self, min_date=None, max_date=None):
        req = "SELECT * FROM TankData"
        if min_date is not None and max_date is not None:
            req += f" WHERE date >= '{min_date}' AND date <= '{max_date}'"
        elif min_date is not None:
            req += f" WHERE date >= '{min_date}'"
        elif max_date is not None:
            req += f" WHERE date <= '{max_date}'"
        return self.db.get(req)