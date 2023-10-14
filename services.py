from random import choice

quest_dict = {
    "first": {
        "t": True,
        "ff": False,
        "sf": False,
        "c": 1,
    },
    
    "second": {
        "t": True,
        "ff": False,
        "sf": False,
        "c": 2,
    },
    "therd": {
        "t": True,
        "ff": False,
        "sf": False,
        "c": 3,
    },
} 

def take_question ():
    return choice(list(quest_dict.items()))




# def Comparison (answer, right_answer, points, delta_points):
#     if answer == right_answer:
#         points = points + delta_points
#     else:
#         points = points - delta_points

