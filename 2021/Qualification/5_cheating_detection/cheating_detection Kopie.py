#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def generate_candidate_profile(candidate_profiles, candidate_index, answers, questions):

    skill = 0
    int_answers = []

    for a_id, a in enumerate(answers):

        int_answers.append(int(a))
        skill = skill + int(a)
        questions[a_id] = questions[a_id] + float(a)

    candidate_skill = float(skill/len(questions))

    candidate_profiles[candidate_index] = {'Skill': candidate_skill, 'Answers': int_answers, 'Cheater_probability': 0}

    return candidate_profiles, questions


def generate_candidate_skills_and_question_difficulties(num_questions, num_candidates):

    #init
    candidate_profiles={}
    questions=[0.0] * num_questions

    for candidate_index in range(1,num_candidates+1):

        answers = input()

        candidate_profiles, questions = generate_candidate_profile(candidate_profiles, candidate_index, answers, questions)

    return candidate_profiles, questions




def preprocess_candidates(candidate_profiles):
    
    for key in list(candidate_profiles.keys()):
        if candidate_profiles[key]["Skill"] < 0.5:
            del candidate_profiles[key]


def preprocess_question_difficulties(questions, num_candidates):

    for q_id, q in enumerate(questions):
        questions[q_id] = 1 - q/num_candidates

    return questions


def calculate_cheater_probabilities(candidate_profiles, questions):

    profiles = {}

    for profile_key in candidate_profiles.keys():

        cheater_probability = 0.0

        for answer_id, answer in enumerate(candidate_profiles[profile_key]["Answers"]):

            if answer == 1 and candidate_profiles[profile_key]["Skill"] < questions[answer_id]:
                cheater_probability = cheater_probability + (questions[answer_id] - candidate_profiles[profile_key]["Skill"])
            elif answer == 0 and candidate_profiles[profile_key]["Skill"] > questions[answer_id]:
                cheater_probability = cheater_probability + (candidate_profiles[profile_key]["Skill"] - questions[answer_id])

        if cheater_probability > 100:
            candidate_profiles[profile_key]["Cheater_probability"] = cheater_probability
            profiles[profile_key] = candidate_profiles[profile_key]
        else:
            pass

    return candidate_profiles


def get_candidate_with_highest_probability(candidate_profiles):

    profile_number = 0
    profile_probability = 0

    for profile_key in candidate_profiles.keys():
        if candidate_profiles[profile_key]["Cheater_probability"] > profile_probability:
            profile_number = profile_key
            profile_probability = candidate_profiles[profile_key]["Cheater_probability"]

    #print(profile_probability)

    return str(profile_number)




testcases = int(input())

for caseNr in range(1, testcases + 1):

    start = time.time()

    # read input
    num_candidates = 100
    num_questions = 10000
    percentage = int(input())

    # define question difficulties in %
    questions = preprocess_question_difficulties(questions, num_candidates)

    # generate candidate skills and question difficulties
    candidate_profiles, questions = generate_candidate_skills_and_question_difficulties(num_questions, num_candidates)

    # throw away weak candidates with < 0.5
    preprocess_candidates(candidate_profiles)

    # calculate cheater probabilities
    candidate_profiles = calculate_cheater_probabilities(candidate_profiles, questions)


    #print("DER ECHTE CHEATER")
    #print(candidate_profiles[59]["Cheater_probability"])

    #print("DER ECHTE CHEATER")
    #print(candidate_profiles[60]["Cheater_probability"])

    #print(candidate_profiles)
    #print(questions)

    print("Case #" + str(caseNr) + ": " + get_candidate_with_highest_probability(candidate_profiles))

    end = time.time()
    print(end - start)
