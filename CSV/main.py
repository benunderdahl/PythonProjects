import pandas as pd


data = pd.read_csv("./Squirrel_Data/squirrel.csv")


cinammon= len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinammon, gray, black]
}

df = pd.DataFrame(data_dict)
print(df.to_csv("squirrel_counter"))