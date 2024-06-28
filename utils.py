import csv
import json

def read_csv_to_json(file_name):
    data = []
    with open(file_name, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

def get_element_by_index(data, index):
    if 0 <= index < len(data):
        filtered_data = {
            "woComment": data[index].get("woComment", ""),
            "woComment1": data[index].get("woComment1", ""),
            "woComment2": data[index].get("woComment2", ""),
            "woComment3": data[index].get("woComment3", ""),
            "woComment4": data[index].get("woComment4", ""),
            "mfgCode": data[index].get("mfgCode", ""),
            "mfg": data[index].get("mfg", ""),
            "mfgName": data[index].get("mfgName", ""),
            "mfgDescription": data[index].get("mfgDescription", ""),
            "itemNo": data[index].get("itemNo", ""),
            "ItemDescription": data[index].get("ItemDescription", ""),
            "equipTypeDescription": data[index].get("equipTypeDescription", ""),
            "model": data[index].get("model", ""),
        }
        return json.dumps(filtered_data, indent=2)
    else:
        return json.dumps({"error": "Index out of range"})


