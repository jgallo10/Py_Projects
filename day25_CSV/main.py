#with open("./weather_data.csv") as weather_data:
 #   data = weather_data.readlines()
  #  print(data)


# import csv

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data_file)
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()

# avarage = data["temp"].mean()
# max_val = data["temp"].max()

#Get Data in Columns
# print(data["condition"])
# print(data.condition)


#Get Data in Row
#print(data[data.day == "Monday"])
#print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# fahrenheit = (monday.temp * (9/5)) + 32
# print(fahrenheit)


#Create a datafram from scratch 
data_dict = {
    "student" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
