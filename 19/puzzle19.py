import numpy as np
from collections import defaultdict
import re
import intervals as I

with open('19/input.txt', 'r') as f:
    workflows, parts = f.read().split('\n\n')

    workflow_map = {}
    for i, workflow in enumerate(workflows.split('\n')):
        name, rules = workflow.split('{')
        rules = rules.replace('}', '')
        rules = rules.split(',')
        el = rules[-1]
        rules = [[rule[0],rule[1], *rule[2:].split(':')] for rule in rules[:-1]]
        rules.append(['else',el])
        workflow_map[name] = rules

    parts = [re.findall(r'\d+',part) for part in parts.split('\n')]

ind_map = {
    'x': 0,
    'm': 1,
    'a': 2,
    's': 3
}

total = 0
for part in parts:
    current_state = 'in'

    while current_state not in ['A','R']:
        ruleset = workflow_map[current_state]
        for rule in ruleset:
            if rule[0] == 'else':
                current_state = rule[1]
                break
            ind = ind_map[rule[0]]
            if rule[1] == '<' and int(part[ind]) < int(rule[2]):
                current_state = rule[3]
                break
            if rule[1] == '>' and int(part[ind]) > int(rule[2]):
                current_state = rule[3]
                break
    
    if current_state == 'A':
        total += sum(int(a) for a in part)
print(total)

#Part 2
# Still have to refactor this function
def find_all_ranges(current_state='in', x_range=(1,4000), m_range=(1,4000), a_range=(1,4000), s_range=(1,4000)):
    if current_state == 'A':
        return (x_range[1]-x_range[0]+1)*(m_range[1]-m_range[0]+1)*(a_range[1]-a_range[0]+1)*(s_range[1]-s_range[0]+1)
    if current_state == 'R':
        return 0
    
    ruleset = workflow_map[current_state]
    total = 0
    for rule in ruleset:
        if rule[0] == 'else':
            total += find_all_ranges(rule[1], x_range, m_range, a_range, s_range)
        
        elif rule[0] == 'x':
            if x_range[0] <= int(rule[2]) <= x_range[1]:
                if rule[1] == '<':
                    total += find_all_ranges(rule[3],(x_range[0],int(rule[2])-1),m_range,a_range,s_range)
                    x_range = (int(rule[2]),x_range[1])
                else:
                    total += find_all_ranges(rule[3],(int(rule[2])+1,x_range[1]),m_range,a_range,s_range)
                    x_range = (x_range[0],int(rule[2]))
        elif rule[0] == 'm':
            if m_range[0] <= int(rule[2]) <= m_range[1]:
                if rule[1] == '<':
                    total += find_all_ranges(rule[3],x_range,(m_range[0],int(rule[2])-1),a_range,s_range)
                    m_range = (int(rule[2]),m_range[1])
                else:
                    total += find_all_ranges(rule[3],x_range,(int(rule[2])+1,m_range[1]),a_range,s_range)
                    m_range = (m_range[0],int(rule[2]))

        elif rule[0] == 'a':
            if a_range[0] <= int(rule[2]) <= a_range[1]:
                if rule[1] == '<':
                    total += find_all_ranges(rule[3],x_range,m_range,(a_range[0],int(rule[2])-1),s_range)
                    a_range = (int(rule[2]),a_range[1])
                else:
                    total += find_all_ranges(rule[3],x_range,m_range,(int(rule[2])+1,a_range[1]),s_range)
                    a_range = (a_range[0],int(rule[2]))
        
        elif rule[0] == 's':
            if s_range[0] <= int(rule[2]) <= s_range[1]:
                if rule[1] == '<':
                    total += find_all_ranges(rule[3],x_range,m_range,a_range,(s_range[0],int(rule[2])-1))
                    s_range = (int(rule[2]),s_range[1])
                else:
                    total += find_all_ranges(rule[3],x_range,m_range,a_range,(int(rule[2])+1,s_range[1]))
                    s_range = (s_range[0],int(rule[2]))
    return total


print(find_all_ranges())
            



