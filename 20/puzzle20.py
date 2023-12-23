import numpy as np
from collections import defaultdict
import re
import intervals as I
import math

class FlipFlop:
    def __init__(self) -> None:
        self.switch = False

    def set_input(self, input):
        return

    def pulse(self, incoming_module, signal):
        if signal == 0:
            self.switch = not self.switch
            return 1 if self.switch else 0
        else:
            return -1
    def reset(self):
        self.switch = False

class Conjunction:
    def __init__(self) -> None:
        self.last_input = {}
    
    def set_input(self, input):
        self.last_input[input] = 0

    def get_inputs(self):
        return self.last_input.keys()
    
    def pulse(self, incoming_module, signal):
        self.last_input[incoming_module] = signal
        return 1 if 0 in self.last_input.values() else 0

    def reset(self):
        self.last_input = dict.fromkeys(self.last_input.keys(),0)



with open('20/input.txt', 'r') as f:
    mapping = {}
    input = [line.split(' -> ') for line in f.read().split('\n')]
    broadcast = []
    rx_input = ''
    for line in input:
        if line[0] == 'broadcaster':
            broadcast = line[1].split(', ')
        else:
            type_mod = line[0][0]
            name_mod = line[0][1:]
            outputs = line[1].split(', ')
            if 'rx' in outputs:
                rx_input = name_mod
            if type_mod == '%':
                mapping[name_mod] = (FlipFlop(), outputs)
            elif type_mod == '&':
                mapping[name_mod] = (Conjunction(), outputs)
    
    for key, value in mapping.items():
        for output in value[1]:
            if output in mapping.keys():
                mapping[output][0].set_input(key)
    for out in broadcast:
        mapping[out][0].set_input('broadcast')
    
    
def press_button_ntimes(n):
    total_low = 0
    total_high = 0
    for _ in range(n):
        queue = [(module, 0, 'broadcast') for module in broadcast]
        count_low = 1
        count_high = 0
        while queue:
            module_name, signal, from_module = queue.pop(0)
            if signal == 0:
                count_low += 1
            elif signal == 1:
                count_high += 1
            if module_name not in mapping:
                continue
            module, outputs = mapping[module_name]
            if signal != -1:
                new_signal = module.pulse(from_module, signal)
                for output in outputs:
                    queue.append((output, new_signal, module_name))
        total_low += count_low
        total_high += count_high
    for mod in mapping.values():
        mod[0].reset()
    return total_high*total_low

def press_until_rx():
    presses = 0
    loops_rx = {}
    inputs_rx = mapping[rx_input][0].get_inputs()
    while len(loops_rx) < len(inputs_rx):
        presses += 1
        queue = [(module, 0, 'broadcast') for module in broadcast]
        while queue:
            module_name, signal, from_module = queue.pop(0)
            if module_name not in mapping:
                continue

            if module_name == rx_input and signal == 1:
                if from_module not in loops_rx.keys():
                    loops_rx[from_module] = presses
            module, outputs = mapping[module_name]
            if signal != -1:
                new_signal = module.pulse(from_module, signal)
                for output in outputs:
                    queue.append((output, new_signal, module_name))
    for mod in mapping.values():
        mod[0].reset()
    return loops_rx

print(press_button_ntimes(1000))
cycles = press_until_rx()
print(math.lcm(*cycles.values()))




    


    

