#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def read_answers_matrix(num_profiles):
    
    answers_matrix = []

    for i in range(num_candidates):
        answers_string = input()
        answers = []

        for a in answers_string:
            answers.append(int(a))

        answers_matrix.append(answers)

    return np.array(answers_matrix)


def get_question_difficulties(answers_matrix):

    return (1 - answers_matrix.sum(axis=0) / len(answers_matrix)) * 6 - 3

def get_profile_skills(answers_matrix):
    return (answers_matrix.sum(axis=1) / len(answers_matrix[0])) * 6 - 3

def calculate_cheater_probabilities(profile_skills, answers, question_difficulties, LUCK_THRESHOLD):

    #print("\nquestion_difficulties")
    #print(question_difficulties)


    #print("\nPROFILE SKILLS")
    #print(profile_skills)

    probabilities = []

    for i in range(len(profile_skills)):
        probabilities.append(1 / (1 + np.exp(-(profile_skills[i] - question_difficulties))))

    # calculate answer probability

    #print("\n\n\nPROBABILITIES")
    #print(np.array(probabilities))

    lucky_guys = 1 - np.array(probabilities) * answers
    lucky_guys = lucky_guys * (lucky_guys < 1)

    lucky_guys = lucky_guys + (np.array(probabilities) * np.logical_not(answers))

    #print("\n\n\n NICHT GESCHAFFTE mit probability")
    #print(lucky_guys)


    # filter out small probabilities (candidates with luck)
    #lucky_guys = lucky_guys * (lucky_guys > LUCK_THRESHOLD)

    # check how much luck they had
    return lucky_guys.sum(axis=1)


def get_candidate_with_highest_probability(cheater_probabilities):

    """
    print()
    print()
    print()
    print("NUM 58 " + str(cheater_probabilities[57]))
    print("NUM 59 " + str(cheater_probabilities[58]))
    print("NUM 60 " + str(cheater_probabilities[59]))
    print("NUM " + str(int(cheater_probabilities.argmax() + 1)) + " " + str(int(cheater_probabilities[cheater_probabilities.argmax() + 1])))
    """

    return str(int(cheater_probabilities.argmax() + 1))


testcases = int(input())
percentage = int(input())

for caseNr in range(1, testcases + 1):

    LUCK_THRESHOLD = 0.1

    # read input
    num_candidates = 100
    num_questions = 10000
    
    # load data
    answers_matrix = read_answers_matrix(num_candidates)

    # calculate question difficulties
    question_difficulties = get_question_difficulties(answers_matrix)

    # calculate profile skills
    profile_skills = get_profile_skills(answers_matrix)


    #LUCK_THRESHOLD = this_i/100
    #print("LUCK THRESHOLD: " + str(LUCK_THRESHOLD))

    # calculate cheater probabilities
    cheater_probabilities = calculate_cheater_probabilities(profile_skills, answers_matrix, question_difficulties, LUCK_THRESHOLD)

    # find the "luckiest"
    print("Case #" + str(caseNr) + ": " + get_candidate_with_highest_probability(cheater_probabilities))   
