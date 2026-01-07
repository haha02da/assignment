students = [("kim",82), ("lee",95), ("park",78), ("choi",95), ("jung",60)]

# 1) 학생 수
count = len(students)
print("학생 수:", count)


# 2) 평균 점수
avg = sum(score for _, score in students) / len(students)
print("avg:", avg)


# 3) 최고점(동점 포함)
top_score = max([score for _, score in students])

top_students = ([(name, score) for name, score in students 
                 if score == top_score])
print("최고점:", top_score)
print("최고점 학생:", top_students)


# 4) 정렬(점수 내림차순, 이름 오름차순)
sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
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




