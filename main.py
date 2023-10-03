def take_input():
  
  """take in input the number of days and user's budget for their own travel.
  If variables are equal to 0 or negative, this function print an error and ask again for user's data"""
  
  num_days = int(input("How many days do you want to travel? "))
  while num_days <= 0:
    print("Error. Not valid value.")
    num_days = int(input("How many days do you want to travel? "))

  tot_budget = float(input("What's your total budget? €"))
  while tot_budget <= 0:
    print('Error. Negative or too low budget.')
    tot_budget = float(input("What's your total budget? "))
    
  return num_days, tot_budget


def all_categories():

  """generate a dictionary that store the all categories' name 
  and return it"""
  
  categories_dict = {
    1: ['lodging'],
    2: ['transportation'],
    3: ['meals'],
    4: ['entertainment']
  }
  return categories_dict


def updated_daily_expense(categories_dict, num_days):
  """take in input the user's daily expenses for any category and return an updated dictionary with all daily expenses"""
  
  for day in range(1, num_days + 1):
    print(f'\nDay {day} of {num_days}: ')
    for category in categories_dict:
      expense = float(input(f'Your daily {categories_dict[category][0]} expense: €'))
      categories_dict[category].append(expense)
  return categories_dict


def total_for_category(expense_for_category):

  """compute the total charge for any category and store it in a list"""

  total_for_cat = []
  for category in expense_for_category: 
    total_for_cat.append(sum(expense_for_category[category][1:]))  #from index one for any key, sum all categories daily expenses and append to a list
  return total_for_cat


def compute_grand_total(total_category):
  
  """sum all elements contained in total_category"""

  grand_total = sum(total_category)
  return grand_total


def print_total(total_category, categories_dict):
  
  grand_total = compute_grand_total(total_category)
  print('\n')
  for cat_key in categories_dict:
    print(f'Your total charge for {categories_dict[cat_key][0]}: €{total_category[cat_key - 1]}')
  print(f'\nGrandtotal is: €{grand_total}')


def change_choice(categories_dict, num_days, expense_for_category): 
  
  """Allow user to change previous data.
  Then it assign the new value to a variable called 'new_total' and return it"""

  change = input('\nDo you want to make any change? (yes/no) ').lower()
  if change != 'yes':
    print('Exiting . . .')
    return None
  
  key = 1     #Starts from key 1 then iterate through categories_dict
  new_total = 0
  while change == 'yes':
    cat_to_change = input('Which category you want to change (lodging/transportation/meals/entertainment) ').lower()
    while cat_to_change != categories_dict[key][0]:
      key += 1

    if cat_to_change == categories_dict[key][0]:
      day_to_change = int(input(f'Enter the day (total days: {num_days}): '))
      while day_to_change < 1 or day_to_change > num_days:
        print('Days out of range.')
        day_to_change = int(input(f'Enter the day (total days: {num_days}): '))
      new_charge = float(input('Enter the new charge: '))
      while new_charge < 0:
        print('Error. New charge cannot be less than 0.')
        new_charge = float(input('Enter the new charge: '))
      expense_for_category[key][day_to_change] = new_charge   
      new_total = total_for_category(expense_for_category)
    change = input('\nDo you want to continue? (yes/no) ')
  return new_total


def check_budget(total_category, tot_budget):
  
  """check if user exceeded the budget or stayed within it and print an appropriate message"""

  grand_total = compute_grand_total(total_category)
  if grand_total <= tot_budget:
    print('\nYou stayed in your budget!')
  else:
    print('\nYour expenses exceed your budget. Pay attention.')
  
 
def main():
  num_days, tot_budget = take_input()
  categories_dict = all_categories()
  expense_for_category = updated_daily_expense(categories_dict, num_days)
  total_category = total_for_category(expense_for_category)
  print_total(total_category, categories_dict)
  check_budget(total_category, tot_budget)
  total_category = change_choice(categories_dict, num_days, expense_for_category)
  if total_category != None:
    print_total(total_category, categories_dict)
    check_budget(total_category, tot_budget)


if __name__ == '__main__':
  main()