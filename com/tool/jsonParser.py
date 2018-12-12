import json

if __name__ == "__main__":
    with open("C://Users//anve//Desktop//orderInfo.txt", "r", encoding="utf-8") as f:
        jsonData = f.read().encode("utf-8")
        print(type(jsonData))
        print("raw data is", jsonData)
        formatData = json.loads(jsonData)
        print("parsed data is: ", formatData)
