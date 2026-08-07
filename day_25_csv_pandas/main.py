
# #? Reading CSV with [with open()] method
# # with open("weather_data.csv") as weather:
# #     data = weather.readlines()
# #     print(data)


# #? Reading CSV with [import python inbuilt csv] method
# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     print(data)
# #     temperature = []
# #     for row in data:
# #         if row[0] != "day":
# #             temperature.append(int(row[1]))
# #     print(temperature)



# #? Reading CSV with [import pandas library] method
# import pandas

# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # temperature_series = data["temp"]
# # data_series = temperature_series.to_list()

# # total_temp = 0
# # for temp in data_series:
# #     total_temp += temp

# # avg_temp = round(total_temp / len(data_series))
# # print(f"Average Temperature: {avg_temp}")

# # max_temp = temperature_series.max()
# # print(f"Maximum Temperature: {max_temp}")


# #* Get Data in columns
# # print(data["condition"])
# # print(data.condition)

# #* Get Data in row
# # print(data[data["day"] == "Monday"])
# # print(data[data.day == "Thursday"])


# #* Find the row where temperature is maximum
# # print(data[data.temp == data.temp.max()])

# #* Tapping row values
# monday = data[data.day == "Monday"]

# monday.day
# monday_temp = monday.temp[0]
# monday.condition

# #* Get monday Temperature in Farenhiet
# temp_in_farenhiet = round(monday_temp * 9/5) + 32
# # print(f"Temperature in Farenhiet: {temp_in_farenhiet}")


# #* Create a dataframe from scratch

# # student_dict = {
# #     "students":["Soham", "Amitabh", "Akash"],
# #     "score":[67, 77, 98],
# # }

# # student_data = pandas.DataFrame(student_dict)
# # print(student_data)

# # student_data.to_csv("student_data.csv")

# new_student_data = pandas.read_csv("student_data.csv")

# print(new_student_data)


#? ============================ SQUIRREL DATA ============================

import pandas

squirrel_data  =pandas.read_csv("squirrel_data.csv")

gray_count = 0
red_count = 0
black_count = 0

for color in squirrel_data["Primary Fur Color"].to_list():
    if color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        red_count += 1
    elif color == "Black":
        black_count += 1
    else:
        continue

new_data = {}
new_data.update({
    "color":["grey", "red", "black"],
    "count":[gray_count, red_count, black_count]
})

make_csv_data = pandas.DataFrame(new_data)
make_csv_data.to_csv("squirrel_data_by_colors.csv")



