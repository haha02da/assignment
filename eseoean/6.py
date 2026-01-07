{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2c45f060-d2c1-4862-8087-83579991752c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "학생 수: 5\n",
      "평균: 82.0\n",
      "최고점: 95\n",
      "최고점 학생: [('lee', 95), ('choi', 95)]\n",
      "정렬: [('choi', 95), ('lee', 95), ('kim', 82), ('park', 78), ('jung', 60)]\n",
      "60점 미만 존재? False\n",
      "전원 합격? True\n"
     ]
    }
   ],
   "source": [
    "students = [(\"kim\", 82), (\"lee\", 95), (\"park\", 78), (\"choi\", 95), (\"jung\", 60)]\n",
    "\n",
    "# 1) 학생 수\n",
    "count = len(students)\n",
    "print(\"학생 수:\", count)\n",
    "\n",
    "# 2) 평균 점수\n",
    "total = sum([score for _, score in students])\n",
    "avg = total / count\n",
    "print(\"평균:\", avg)\n",
    "\n",
    "# 3) 최고점(동점 포함)\n",
    "top_score = max([score for _, score in students])\n",
    "top_students = list([(name, score) for name, score in students if score == top_score])\n",
    "print(\"최고점:\", top_score)\n",
    "print(\"최고점 학생:\", top_students)\n",
    "\n",
    "# 4) 정렬(점수 내림차순, 이름 오름차순)\n",
    "sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))\n",
    "print(\"정렬:\", sorted_students)\n",
    "\n",
    "# 5) 60점 미만 존재 여부\n",
    "has_fail = any([score < 60 for _, score in students])\n",
    "print(\"60점 미만 존재?\", has_fail)\n",
    "\n",
    "# 6) 전원 합격 여부\n",
    "all_pass = all([score >= 60 for _, score in students])\n",
    "print(\"전원 합격?\", all_pass)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cac7ef1f-ffcb-45cf-84b1-1161c63eb2fe",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
