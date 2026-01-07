students = [("kim", 82), ("lee", 95), ("park", 78), ("choi", 95), ("jung", 60)]

# 1) 학생 수
count = len(students)
print("학생 수:", count)

# 2) 평균 점수
total = sum([score for i, score in students])
avg = total / count
print("평균:", avg)

# 3) 최고점(동점 포함)
top_score = max([score for i, score in students])
top_students = [(name, score) for name, score in students if score == top_score]
print("최고점:", top_score)
print("최고점 학생:", top_students)

# 4) 정렬(점수 내림차순, 이름 오름차순)
sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
print("정렬:", sorted_students)

# 5) 60점 미만 존재 여부
has_fail = any([score < 60 for i, score in students])
print("60점 미만 존재?", has_fail)

# 6) 전원 합격 여부
all_pass = all([score >= 60 for i, score in students])
print("전원 합격?", all_pass)

