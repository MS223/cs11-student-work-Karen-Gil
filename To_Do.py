to_do= raw_input("What do you need to do")
day=raw_input("What day").capitalize()
days_of_week={

    "Monday": [],
    "Tuesday": [],
    "Wednesday":[],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": [],
}

def add(to_do,day):
    days_of_week[day].append(to_do)
def get(day):
    print days_of_week[day]

def choice():
    choice=raw_input("How can I help you?") 
#     Why is is not letting me make the function
# Trying to let user add new to todo

#     # days_of_week[day].append(to_do)
#     days_of_week["day"] = to_do .append()
# def get(day):
#         print get()
add(to_do,day)
print days_of_week
