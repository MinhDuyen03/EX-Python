#!/usr/bin/env python3


def solve(text):
    """Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
    -> [60, 20, 0]

    NOTE: không dùng `re` library
    """

    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError("Học viên chưa làm bài này")

    return result

s = 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu9'
ls = list()
cr = ''
idx = 0
leng = len(s)
for i in s:
    idx += 1
    if i.isdigit():
        cr += i
        if idx == leng:
            ls.append(cr)
    else:
        if cr:
            ls.append(cr)
            cr = ''
ls = [int(i) for i in ls]
print(ls)  