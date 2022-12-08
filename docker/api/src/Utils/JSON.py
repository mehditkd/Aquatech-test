from flask import jsonify
import datetime

class JSON:

    def __parse_rec(data):
        if isinstance(data, list):
            if len(data) > 0:
                list_parsed = list(map(JSON.__parse_rec, data))
                return list_parsed
            else:
                return []
        if isinstance(data, dict):
            for key, value in data.items():
                data[key] = JSON.__parse_rec(value)
            return data
        if isinstance(data, dict) or isinstance(data, (str, int, float, bool, datetime.datetime, datetime.date)):
            return data
        return data.__dict__

    def parse(data):
        return jsonify(JSON.__parse_rec(data))
