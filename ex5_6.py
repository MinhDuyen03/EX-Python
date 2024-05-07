#!/usr/bin/env python3

term1 = {"math": 3, "python": 5, "data": 2}
term2 = {"math": 7, "python": 9, "SQL": 8, "HTML": 6}
data = [term1, term2]


# def solve(term1, term2):
#     """Trả về result là dict chứa bảng điểm của các môn học sau hai học kỳ.
#     Biết điểm số được chọn là điểm số ở lần học sau cùng.
#     """

#     result = {}
#     # Xoá dòng raise và Viết code vào đây set result làm kết quả
#     raise NotImplementedError("Học viên chưa làm bài này")
#     return result
def solve(term1, term2):
    """Returns result as a dict containing transcripts of subjects after two semesters.
    Know that the selected score is the score from the last study session."""
    
    # Merge the scores from term1 and term2
    merged_scores = {}
    for subject, score in term1.items():
        merged_scores[subject] = score
    for subject, score in term2.items():
        merged_scores[subject] = score
    print(merged_scores)

    # Keep only the last score for each subject
    # final_scores = {}
    # for subject, score in merged_scores.items():
    #     final_scores[subject] = score

    # return final_scores

# # Test the function with the provided data
# term1 = {"math": 3, "python": 5, "data": 2}
# term2 = {"math": 7, "python": 9, "SQL": 8, "HTML": 6}
# data = [term1, term2]

# transcripts = solve(term1, term2)
# print(transcripts)



