# Author: Yiwen Zhou
# Date: 3/4/2025
# Description: quiz about python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

def quiz():
    print("Welcome to the python quiz!")
    print("Amswer the following questions:")

    questions = [
        "1.Which of the following is not a python data type?a.int, b.float, c.rational, d.string, e.bool"
        "2.Which of the following is not a built-in operation in python?a.+, b.%, c.abs(), d.sqrt"
        "3.In a mixed-type expression involving ints and floats, python will convert:a.floats to ints, b.ints to strings, c.floats and ints to strings, d.ints to floats"
        "4.The best structure for implementing a multi-way decision in python is:a.if, b.if-else, c.if-elif-else, d.try"
        "5.What statement can be executed in the body of a loop to cause it to terminate?a.if, b.exit, c.continue, d.break"
        ]
    answer = [
        "rational"
        "sqrt()"
        "ints to floats"
        "if-elif-else"
        "continue"
        ]
    score = 0

    for i in range(len(questions)):
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        user_answer = input(questions[i]).strip().lower()
        if user_answer == answers[i]:
            print("Correct!")
            GPIO.output(17, GPIO.HIGH)
            score += 1
        else:
            print("Incorrect!")
            GPIO.output(18, GPIO.HIGH)

        time.sleep(1)

        GPIO.cleanup()

    print("\nQuiz completed!")
    print(f"You got {score}/{len(quesions)} questions correct.")

quiz()
