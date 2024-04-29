#!/usr/bin/env python3
data = 5


def squared(input_data):
    """Tính bình phương của số đầu vào

    Số đầu vào ở đây được chứa trong tên `input_data`,
    được cung cấp sẵn bởi bài tập. Học viên chỉ cần lo tính toán ra kết quả
    dựa trên `input_data` đã cho.
    Xem video hướng dẫn ở tài liệu hướng dẫn làm bài.
    """
    result = None
    
    with open(r"E:\Python\alo\pymi\exercises\input\input_data.txt", "r") as f:
        da = f.read()
    ls = da.split(' ')
    i = 0
    for i in ls:
        i = int(i)
        print(i * i)
      
    

