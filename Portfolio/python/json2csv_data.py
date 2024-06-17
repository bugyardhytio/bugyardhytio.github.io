import json
import pandas as pd

with open("Portfolio/python/sumut.json", encoding="utf-8-sig") as jsonfile:
    sumut_json = json.load(jsonfile)

table = pd.DataFrame.from_dict(sumut_json["data"])
#table.to_csv("sumut.csv")