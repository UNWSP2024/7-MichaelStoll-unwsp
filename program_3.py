#title:US population
#author: michael stoll
#date: 3/6/2025
number_of_cities = int(input('Input number of states:'))

all_states_info = []
filter_year = int(input('Filtered to the year:'))
population_sum = 0
for count in range(number_of_cities):
    state_info = [int(input('year:'))] + [str(input('state:'))] + [int(input('population:'))]
    all_states_info.append(state_info)
    if state_info[0] == filter_year:
        population_sum = population_sum + state_info[2]
print(all_states_info)
print(population_sum)