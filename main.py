#function that compute the total charge for each category
def compute_category_total_expense(categories):
    total_for_category = []
    for category in categories:
        total_for_category.append(sum(categories[category]))
    return total_for_category


def categories_ls():
    category_list = ['lodging', 'transportation', 'meals', 'entertainment']
    return category_list

#print the total for each category computed by function 'compute_category_total_expense'
def print_total_for_category(categories):
    total_for_category = compute_category_total_expense(categories)
    category_list = categories_ls()
    index = 0
    for total_for_category_index in range(0, len(total_for_category)):
        print(f'Your {category_list[index]} total charge is: €{total_for_category[total_for_category_index]}')
        index += 1


def grand_total(categories):
    grandtotal = float(sum(compute_category_total_expense(categories)))
    return grandtotal

#if user want to change a single charge in a category, this function compute the new total 
def update(categories, category_to_change, day_to_change):
    new_total = []
    for find_day in range(0, len(categories[category_to_change])):
        if day_to_change == find_day + 1:
            categories[category_to_change][day_to_change - 1] = 0
            categories[category_to_change][day_to_change - 1] += new_charge
            new_total = compute_category_total_expense(categories)
    return new_total


days = int(input('How many days do you want to stay? '))
while days <= 0:
    print('Incorrect value or trip too short.')
    days = int(input('How many days do you want to stay? '))

budget = float(input('Enter your total budget:  €'))
while budget <= 0:
    print('Incorrect value. Please enter a positive number.')
    budget = float(input('Enter your total budget:  €'))

categories = {'lodging': [],
              'transportation': [],
              'meals': [],
              'entertainment': []
              }

for day in range(1, days + 1):
    print(f'Day {day}: ')
    for category in categories:
        expense = float(input(f'Enter your {category} expenses for this day: '))
        categories[category].append(expense)

compute_category_total_expense(categories)
print_total_for_category(categories)
print(f'Your grandtotal is: {grand_total(categories)}')

change = str(input('Do you want to make any change? (yes/no) ')).lower()
while change == 'yes':
    category_to_change = str(input('Which category do you want to change? (lodging/transportation/meals/entertainment) ')).lower()
    if category_to_change in categories.keys():
        day_to_change = int(input('Enter the day: '))
        if day_to_change > days or day_to_change <= 0:
            print('Error. Incorrect day.')
        else:
            new_charge = float(input('Enter your new charge: '))
            while new_charge < 0:
                print('You cannot enter a negative number.')
                new_charge = float(input('Enter your new charge: '))
            update(categories, category_to_change, day_to_change)
            change = str(input('Do you want to continue? (yes/no) '))
            global total_update_global
            total_update_global = update(categories, category_to_change, day_to_change)
    else:
        print('Category not found.')
        change = str(input('Do you want to continue? (yes/no) '))


category_ls = categories_ls()
index = 0
for total_update_index in range(0, len(total_update_global)):
    print(f'Your new {category_ls[index]} total charge is: €{total_update_global[total_update_index]}')
    index += 1

grand_total = float(sum(total_update_global))
print(f'Your new grand total is: €{grand_total}')

if grand_total > budget:
    print('You exceed your budget. Pay attention.')