import openpyxl, json

# # def benchmark(func):
#     import time
#     def wrappper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"Время выполнения {func}: {end - start} секунд")
#     return wrappper



list_users = dict()
# @benchmark
def convertation_file_to_dict():
    book = openpyxl.open("contacts/All_contacts.xlsx", read_only=True)
    sheet = book.active

    list_users = {sheet[row][2].value: sheet[row][1].value for row in range(1, sheet.max_row + 1)
                  if sheet[row][0].value in ["Skype", "SkypeSuggested", "SkypeOneWay"]}

    with open('my_data.json', 'w') as file:
        json.dump(list_users, file, indent=3)

list_search = [] # list contats after filters    

def create_users_for_find(country, black_list):
    """
    :param country: enter country for search
    :param black_list: users in block search
    :return: list_search with all users after filters
    """

    with open("my_data.json", 'r') as file:
        data = json.load(file)
    print(len(data))

    for keys in data:
        if (country.lower() in keys.lower()) and black_list.lower() == '':
                list_search.append(data[keys])
        elif (country.lower() in keys.lower()) and (black_list.lower() not in keys.lower()):
                list_search.append(data[keys])
    return list_search




