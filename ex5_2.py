#!/usr/bin/env python3

"""
Tips: dùng stdlib copy.deepcopy

In [14]: import copy

In [15]: d = [{'name': 'Dung', 'languages': ['C', 'Python']}]

In [16]: dnew = copy.deepcopy(d)

In [18]: dnew[0]['languages'].append('Elixir')

In [19]: dnew
Out[19]: [{'languages': ['C', 'Python', 'Elixir'], 'name': 'Dung'}]

In [20]: d
Out[20]: [{'languages': ['C', 'Python'], 'name': 'Dung'}]
"""


data = [
    {
        "name": "Hoang",
        "phone": "0988888888",
        "languages": [
            "Python",
            "C",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript",
            "Golang",
        ],
    },
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]


# def solve(last_year_data):
"""
    Trả về list thông tin các học viên sau khi đã update sau 1 năm.
    Không thay đổi thông tin năm cũ.

    Biết các học viên đều học được các ngôn ngữ lập trình
    trong "languages" của học viên "Hoang".
    Sau đó "Hoang" học thêm được ngôn ngữ "Elixir", các học
    viên khác không biết ngôn ngữ này.
    "Tu" có bạn gái tên là "Do Anh".
    "Duy" chia thay bạn gái, không còn bạn gái nữa.

    Chú ý: code tránh dựa vào thứ tự cụ thể trong để bài.
    # """
    # result = []

    # # Xoá dòng raise và Viết code vào đây set result làm kết quả
    # raise NotImplementedError("Học viên chưa làm bài này")

    # return result



# Hoang học ngôn ngữ Elixir
def after_1_year(data):
    for student in data:
        if student.get("name") == "Hoang":
             if "Elixir" not in ["languages",[]]:
                student["languages"].append("Elixir")
        # print(student)      
# Update bạn gái Tú
    for girl_friends in data:
        if girl_friends.get("name")  == "Tu":
            girl_friends ["girl_friend"] = "Do Anh"
        # print(girl_friends)
# Remove bạn gái Duy
    for gf in data:
         if gf.get("name") == "Duy":
            gf.pop("girl_friend")
        # print (gf)
#Update thông tin học viên


    



