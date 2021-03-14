#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_hack_tree(program):

    current_dmg = 0
    power = 1
    command_potential = []
    hack_efficiencies = []

    for command in program:
        if command == "C":
            command_potential.append(power)
            power = power * 2
        else:
            current_dmg += power
            hack_efficiencies.append(command_potential)
            command_potential = []

    return hack_efficiencies, current_dmg

def calculate_number_hacks(d, current_dmg, hack_efficiencies):

    nodes_after = 0
    num_hacks = 0

    for node in reversed(hack_efficiencies):
        for hack_efficiency in reversed(node):

            for i in range(0, nodes_after + 1):
                current_dmg -= hack_efficiency
                #print(hack_efficiency)
                num_hacks += 1
                if current_dmg <= d:
                    return num_hacks

        nodes_after += 1

    return -1


testcases = int(input())

for caseNr in range(1, testcases + 1):

    num_hacks = 0
    d, program = input().split()
    d = int(d)

    hack_efficiencies, current_dmg = build_hack_tree(program)

    if current_dmg <= d:
        print("Case #" + str(caseNr) + ": 0")
    else:
        num_hacks = calculate_number_hacks(d, current_dmg, hack_efficiencies)

        if num_hacks == -1:
            print("Case #" + str(caseNr) + ": IMPOSSIBLE")
        else:
            print("Case #" + str(caseNr) + ": " + str(num_hacks))

