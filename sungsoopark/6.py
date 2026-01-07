#과제 6

# 종합 미니 프로젝트(내장함수 올인원)
# “학생 점수 분석기”

# 데이터
# students = [("kim",82), ("lee",95), ("park",78), ("choi",95), ("jung",60)]
'''
요구사항(내장함수 활용):

1. 학생 수 출력 (`len`)
2. 평균 점수 출력 (`sum`)
3. 최고점(동점 포함) 학생 모두 출력 (`max`, `filter`)
4. 점수 내림차순, 이름 오름차순 정렬 (`sorted`, key)
5. 60점 미만이 한 명이라도 있으면 경고 (`any`)
6. 모두 60점 이상이면 “전원 합격” (`all`)
7. 결과를 파일로 저장 (`open`) '''

students = [("kim", 82), ("lee", 95), ("park", 78), ("choi", 95), ("jung", 60)]

# 1) 학생 수
count = len(students)
print("학생 수:", count)

# 2) 평균 점수
total = sum([score for _, score in students])
avg = total / count
print("평균:", avg)

# 3) 최고점(동점 포함)
top_score = max([score for _, score in students])
top_students = [(name, score) for name, score in students if score == top_score]
print("최고점:", top_score)
print("최고점 학생:", top_students)

# 4) 정렬(점수 내림차순, 이름 오름차순)
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("정렬:", sorted_students)

# 5) 60점 미만 존재 여부
has_fail = any([score < 60 for _, score in students])
print("60점 미만 존재?", has_fail)

# 6) 전원 합격 여부
all_pass = all([score >= 60 for _, score in students])
print("전원 합격?", all_pass)

# 7) 파일 저장
with open("report.txt", "w", encoding="utf-8") as f:
    f.write("학생 수: " + str(count) + "\n")
    f.write("평균: " + str(avg) + "\n")
    f.write("최고점: " + str(top_score) + "\n")
    f.write("최고점 학생: " + str(top_students) + "\n")
    f.write("정렬: " + str(sorted_students) + "\n")
    f.write("60점 미만 존재?: " + str(has_fail) + "\n")
    f.write("전원 합격?: " + str(all_pass) + "\n")

print("report.txt 저장 완료")

# #솔루션
# students = [("kim", 82), ("lee", 95), ("park", 78), ("choi", 95), ("jung", 60)]

# # 1) 학생 수
# count = len(students)
# print("학생 수:", count)

# # 2) 평균 점수
# total = sum([score for _, score in students])
# avg = total / count
# print("평균:", avg)

# # 3) 최고점(동점 포함)
# top_score = max([score for _, score in students])
# top_students = list([(name, score) for name, score in students if score == top_score])
# print("최고점:", top_score)
# print("최고점 학생:", top_students)

# # 4) 정렬(점수 내림차순, 이름 오름차순)
# sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
# print("정렬:", sorted_students)

# # 5) 60점 미만 존재 여부
# has_fail = any([score < 60 for _, score in students])
# print("60점 미만 존재?", has_fail)

# # 6) 전원 합격 여부
# all_pass = all([score >= 60 for _, score in students])
# print("전원 합격?", all_pass)

# # 7) 파일 저장
# with open("report.txt", "w", encoding="utf-8") as f:
#     f.write("학생 수: " + str(count) + "\n")
#     f.write("평균: " + str(avg) + "\n")
#     f.write("최고점: " + str(top_score) + "\n")
#     f.write("최고점 학생: " + str(top_students) + "\n")
#     f.write("정렬: " + str(sorted_students) + "\n")
#     f.write("60점 미만 존재?: " + str(has_fail) + "\n")
#     f.write("전원 합격?: " + str(all_pass) + "\n")

# print("report.txt 저장 완료")