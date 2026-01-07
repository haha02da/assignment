{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c9be4832-a2aa-401e-90fd-93f4130b2760",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Down\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요:  19\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Down\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요:  18\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Down\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요:  17\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Down\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "정수를 입력하세요:  16\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Down\n",
      "실패\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "num =  random.randint(1,21)\n",
    "\n",
    "for i in range(5):\n",
    "\n",
    "    user=int(input(\"정수를 입력하세요: \"))\n",
    "     \n",
    "    if user>num :\n",
    "        print(\"Down\")\n",
    "    elif user < num : \n",
    "        print(\"Up\")\n",
    "    else:\n",
    "        print(\"정답\")\n",
    "        break\n",
    "\n",
    "else : print(\"실패\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "45210a0b-e05f-4c60-b221-4ee9736deeda",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19c7f05b-0a99-46c3-a07c-1a8488975ed6",
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
