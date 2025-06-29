print('Prices:')
price_list = {'Bubblegum': '$2', 'Toffee': '$0.2', 'Ice cream': '$5', 'Milk chocolate': '$4', 'Doughnut': '$2.5',
              'Pancake': '$3.2'}

for key, val in price_list.items():
    print(key + ': ' + val)

print()
print('Earned amount:')
earned_amount = {'Bubblegum': '202', 'Toffee': '118', 'Ice cream': '2250', 'Milk chocolate': '1680', 'Doughnut': '1075',
                 'Pancake': '80'}

for key1, val1 in earned_amount.items():
    print(key1 + ': $' + val1)

print()
income = 0
for amount in earned_amount.values():
    income += int(amount)
print('Income: ' + '$', end='')
print(float(income))

# Stores total expense before net income
expenses = {'Staff income': 1550.00, 'Electricity': 221.90, 'Security expenses': 126.64}

total_expenses = 0
for expense in expenses.values():
    total_expenses += expense

print('Total expenses:' + '$', end='')
print(round(total_expenses, 2))  # Prints total expenses

net_income = income - total_expenses
print('Net income:' + '$', end='')
print(round(net_income, 2))

