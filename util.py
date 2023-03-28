import random


def generate_random_w_limit(start, end):
    return random.randint(start, end)

def generate_steps_by_number(step_number, start_rand, end_rand):
    
    steps_dict = dict()
    steps_rand_list = list()
    
    steps_rand_list = [generate_random_w_limit(start_rand, end_rand) for x in range(0, step_number)]
    steps_rand_list.sort()

    for i in range(0, step_number):
        steps_dict[i] = steps_rand_list[i]
        
    return steps_dict