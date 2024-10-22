def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()  
    str_list = user_input.split(",")  
    float_list = [float(num.strip()) for num in str_list]  
    return float_list

def calc_average_temperature(temperature_list):
    if len(temperature_list) == 0:
        return 0.0  
    average = sum(temperature_list) / len(temperature_list)
    return average

def calc_min_max_temperature(temperature_list):
    if len(temperature_list) == 0:
        return [None, None] 
    minimum = min(temperature_list)
    maximum = max(temperature_list)
    return [minimum, maximum]


def main():
    display_main_menu()
    temperature_list = get_user_input()
    average = calc_average_temperature(temperature_list)
    min_max = calc_min_max_temperature(temperature_list)
    print(f"Average temperature: {average:.2f}")
    print(f"Minimum temperature: {min_max[0]}")
    print(f"Maximum temperature: {min_max[1]}")
main()
