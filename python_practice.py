greeting = 'Hello, World!'
name = 'Julius Kevin Lugya'

def validate_and_greet(greeting, name):
    if not isinstance(greeting, str):
        return "greeting must be a string"
    if not isinstance(name, str):
        return "name must be a string"
    return f"{greeting} {name}!"
print(validate_and_greet(greeting, name))
print(name + (' is saying ' + greeting))
place = f' is from kampala, {name}.'
print(place)
print('Hello' in greeting)
numbers = 5, 2, 7, 3, 1, 4, 6
sorted_numbers = sorted(numbers)
print(sorted_numbers)
for number in sorted_numbers:
    print(number)
data_analytics = 'Julius Kevin Lugya'    
data_analytics = list(data_analytics)
data_analytics.insert(0, 'Mr. ')
print(''.join(data_analytics))

Data_analytics = ['Julius Kevin Lugya', 27, 'Data cleaning']
name, age, task = Data_analytics
print(f'Name: {name}\nAge: {age}\nTask: {task}')