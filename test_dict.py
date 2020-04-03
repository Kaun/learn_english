teacher = {
        "id": 0,
        "name": "Morris Simmmons",
        "about": "Репетитор американского английского языка. Структурированная система обучения. Всем привет! Я предпочитаю называть себя «тренером» английского языка. Мои занятия похожи на тренировки",
        "rating": 4.2,
        "picture": "https://i.pravatar.cc/300?img=20",
        "price": 900,
        "goals": ["travel", "relocate", "study"],
        "free": {

            "mon": {"8:00": False, "10:00": True, "12:00": True, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "tue": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "wed": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "thu": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "fri": {"8:00": True, "10:00": True, "12:00": False, "14:00": False, "16:00": False, "18:00": False,
                    "20:00": False, "22:00": False},
            "sat": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": False},
            "sun": {"8:00": False, "10:00": False, "12:00": False, "14:00": False, "16:00": True, "18:00": True,
                    "20:00": True, "22:00": False},
        }
    }

mydict = {}
for day, hours in teacher["free"].items():
    free_hours = {}
    for hour, stat in hours.items():
        if stat:
            free_hours[hour] = stat
            # print(free_hours)
    mydict[day] = free_hours
print(mydict)
# mydict = {}
# mylist = []
# for day, times in teacher["free"].items():
#     # print(f"{day} {times}")
#     # mylist.clear()
#     # print(mydict)
#     for time, status in times.items():
#         print(day)
#         mylist.append(time)
#         mydict[day]= mylist
#         print(mydict)
#         print(f"{time} {status}")
#         if status == True:
#             print(f"{day} {time} {status}")
            # mylist.append(time)
            # print(mylist)
            # mydict[day] = mylist

            # print(f"{day} {list}")
    # mydict[day] = mylist
    # print(mydict)
    # print("We here", mydict)

# print(mydict)

# dictionary = {}
# list_1=[1,2,3]
# list_2=[1,2,3,4]
# list_2.append('44')
# dictionary['s']=list_1
# dictionary['d']=list_2
# print(dictionary)