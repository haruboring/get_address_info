import json
import os

import pandas as pd

address_info_data: pd.DataFrame = pd.read_csv("data/x-ken-all.csv", encoding="utf-8")
address_info_data.fillna("", inplace=True)
print(address_info_data.head())

zipcodes: set[str] = set()
duplicate_zipcodes: set[str] = set()

for zipcode in address_info_data["zipcode"]:
    if zipcode in zipcodes:
        duplicate_zipcodes.add(zipcode)

    zipcodes.add(zipcode)

unique_zipcodes: set[str] = zipcodes - duplicate_zipcodes

unique_address_info_data: list[dict[str, str]] = []

for address_idx in range(len(address_info_data)):
    address_info: pd.Series = address_info_data.iloc[address_idx]
    if address_info["zipcode"] in unique_zipcodes:
        unique_address_info_data.append(address_info.to_dict())

print(unique_address_info_data[:5])

with open("output/unique_address_info.json", "w", encoding="utf-8") as f:
    json.dump(unique_address_info_data, f, ensure_ascii=False, indent=4)
