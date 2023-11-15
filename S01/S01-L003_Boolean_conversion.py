
choices = ['load data', 'export data', 'analyze & predict']

choice = 'x'
while choice:
    choice = input(f'Choose option or press Enter to finish. Available options: \n1:{choices[0]}, \n2:{choices[1]}, \n3:{choices[2]} \n')
    if choice:
        try:
            choice_num = int(choice) - 1
            print(choice_num)
            if choice_num >= 0 and choice_num < len(choices):
                print(f'Chosen option: {choices[choice_num]}')
        except:
            print('Please enter a number')
    else:
        print('-----END-----')
