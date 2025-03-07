#title:rainfall
#author: michael stoll
#date: 3/6/2025

def rain_stats():
    most_rain = max(rainfall_list)
    least_rain = min(rainfall_list)
    print(f'Average amount of rain is {average_rain:0.1f} inches.')
    print(f'Total rain this year is {sum(rainfall_list)} inches.')
    print(
        f'The month with the most rain has {most_rain} inches of rain and the least has with {least_rain} inches of rain.')

rainfall_list = []
for count in range(0, 12):
    rainfall_list += [int(input('Enter inches of rain:'))]
average_rain = sum(rainfall_list)/12
rain_stats()