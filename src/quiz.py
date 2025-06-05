# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 11:39:07 2025

@author: Dhara
"""

# quiz.py

def run_quiz():
    score = 0
    questions = [
        {
            "question": "What keyword defines a function in Python?",
            "options": ["a) func", "b) define", "c) def"],
            "answer": "c"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["a) //", "b) #", "c) <!-- -->"],
            "answer": "b"
        },
        {
            "question": "Which data type stores True/False?",
            "options": ["a) string", "b) int", "c) boolean"],
            "answer": "c"
        }
    ]

    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)

        user_answer = input("Your answer: ").lower()

        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print(f"\n🎯 You got {score} out of {len(questions)} correct.")
