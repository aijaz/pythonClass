# Python Notes

# Introduction

## Printing

- Anything in "quotes" is a _string_
- A whole number is an _integer_
- You can print strings or integers this way

    ```python
    # print a string
    print("Hello, world!")

    # print an integer
    print(2)
    ```

- Anything that can be printed is known as an _expression_
- An expression has a value
- The value of a string is the string
- The value of an integer is the integer

## Operations

- An operator is a verb that operates over one or more nouns (operands)
    + `+` is an operator
        * It operates on strings and integers
        * The value of an expression that has an operator is the value of the operation
        
            ```python
            print("Hello, " + "world")  
            # Prints "Hello, world"
            # The value of the expression is the string "Hello, world"
            # That's what's being printed

            print(2 + 3)
            # The value of the expression being printed is 5
            ```

- Operations can use parentheses, like in Math
    
    ```python
    print(2 * (6 - 2))  # prints 8, not 14
    ```

__Remember: If you can print it, it's an expression.__

## Strings

- Strings can be specified with `'single quotes'`, `"double quotes"`, or `"""triple quotes"""`
- Triple-quoted strings can span multiple lines, like this:

    ```python
    poem = """Roses are red,
    I think I am smitten
    Not by Leo
    But this adorable kitten."""
    ```

- If you want to add newlines into a single- or double-quoted string, use the _escape character_ `\n`: 

    ```python
    haiku = "I code in python\nI'm not sure if this will work\nHelp me, Obi-Wan!"
    ```


## Functions

- Functions are commands that do things
- Sometimes functions take _parameters_, like `print(4)` where `4` is the parameter
- Other times functions operate on things like strings. For example:
    + `"hello world".upper()` evaluates to `"HELLO WORLD"`
    + `"hello world".title()` evaluates to `"Hello World"`
    + `"HeLlo wOrlD".lower()` evaluates to `"hello world"`

## Variables

- Variables are things that hold values
- Variables have names so that you can refer to them
- The values that variables hold can be strings, integers, other types, or the special value `None`
- You can assign a value to a variable this way: `my_name = "Aijaz"` or `number_of_surahs = 114`.

## Variables inside strings

- You can insert the values of variables into strings using _f strings_. 
- F strings work with single-, double-, and triple-quoted strings. Use them this way:

    ```python
    my_name = "Aijaz"
    print(f"Hello, {my_name}")
    ```

- Anything inside braces in an f string will be evaluated. 
- Braces can contain any expression.
- Therefore, this is also valid:

    ```python
    my_name = "Aijaz"
    print(f"Hello, {my_name.upper()}!!!")

    # You could also, do this, but it's not as cool:
    print("Hello, " + my_name.upper() + "!!!")
    ```

## Asking for input

- Use `input` to ask the user to input something:

    ```python
    name = input("What is your name?")
    print(name)
    ```

# Week 1 Homework:

This is week 1's homework:

```python
name = input("What is your name? ")
print(name + " shark! Do do do do do do!")
print(name + " shark! Do do do do do do!")
print(name + " shark! Do do do do do do!")
print(name.upper() + " SHARK!")    
```

# Lists

- Lists are ordered collections of things.
- Lists can contain all sorts of things, strings, integers, `None`, and other things we haven't seen yet.
- Accessing elements with indexes
    + Lists are _zero-indexed_. This means that the first element in a list is item 0
    + Think of the index of an item as the _distance from the first item_
    + The index of the last item is the length of the list - 1
    + Use `len(l)` to calculate the length of the list named `l`.
    + Create a list with square brackets (see below)
    
        ```python
        my_list = [10, 20, 30]
        l = len(my_list)  # l is equal to 3
        my_list[0]
        my_list[1]
        my_list[2]
        my_list[3]  # this will throw an error. There is no element 3. The last element is element 2.
        ```

    - You can also use negative indexes. `-1` for the last item, and so on
    - `last_item = things[-1]`
    - Why `-1`?  Because `-0` doesn't make sense.
- Changing, adding, and removing elements
    + modifying elements 
    + Adding elements `append`
    + `l.insert(2, "abc")` - insert an element into index 2
    + `item = things.pop()` - return the last item in the list (and remove that item from the list)
    + `a = things.pop(3)` - return the item at index 3 (and remove that item from the  list)
    + `things.del("book")` - remove the item at index 3
    + `things.remove('book')` - remove the first item with a value of `"book"` from the list named `things`
    + `l1.extend(l2)` - add one list to another
- Organizing a list
    + Sort permanently with `cars.sort()`
    + Get a sorted copy with `sorted(cars)`
    + Reverse a list with `cars.reverse()`
- Tuples
    + Tuples are comma-separated values
    + They can optionally have parentheses around them. 
    + This makes them look like lists
    + Unlike lists, however, you cannot add or remove an item from a tuple. Nor can you change an item in a tuple.
    + Tuples are useful for creating data structures (groups of things) that will never change.
- Lists containing lists 
    + Lists can contain lists e.g.: `l = [1, 3, 5, ["Book", "Pen", "Pencil"]]`

# Week 2 Homework

1. Make a list of your favorite sports in order of preference (most favorite first)
2. Print the list
3. You learn about a new game called "7 tiles" and suddenly it's your favorite game. Modify the list so that this is new game is now in the first spot, with everything else moving down a spot. Print the list.
4. After a week, "7 tiles" moves to the second spot but the third most favorite game moves to the top spot. Modify the list accordingly, and print the list.
5. After another week, you get bored of "7 tiles" and remove it from your list altogether. Everything else stays the same. Modify the list accordingly, and print the list.
6. Print the list in reverse order

```python
sports = ['Soccer', 'Cricket', 'Tennis']
print(sports)
sports.insert(0, "7 tiles")
print(sports)
sports.insert(0, sports.pop(2))
print(sports)
sports.remove("7 tiles")
print(sports)
sports.reverse()
print(sports)
```

7. I'm creating an Avatar Fandom page. I want to keep track of the following information for each character: Name, Nationality, Children, Bending. 
    - Every character will have a name and nationality
    - We will keep track of the names of the character's children (if any)
    - Some characters may not have children
    - Some characters will have a single bending power
    - Some characters will have more than one bending power
    - Some characters may not have any bending powers
    - Design a data structure for this fandom page
    - Populate your data structure using the data below
    - Print the value of your data structure
    - This is gonna take some thought, so spend some time on this assignment.
    - Data:
        + Name: Aang
            + Nationality: Southern Air Temple
            + Children: 
                * Bumi
                * Kya
                * Tenzin
            + Bending: 
                * Air
                * Water
                * Earth
                * Fire
                * Energy
        - Name: Katara
            + Nationality: Southern Water Tribe
            + Children:
                * Bumi
                * Kya
                * Tenzin
            + Bending: 
                * Water
                * Blood
        - Name: Sokka
            + Nationality: Southern Water Tribe
            + Children: None
            + Bending: None
        - Name: Toph Beifong
            + Nationality: Gaoling, Earth Kingdom
            + Children: 
                * Lin Beifong
                * Suyin Beifong
            + Bending:
                * Earth
                * Metal
        - Name: Zuko
            + Nationality: Fire Nation Capital, Fire Nation
            + Children: 
                * Izumi
                * Kya
            + Bending:
                * Fire
                * Energy
        - Name: Iroh
            + Nationality: Fire Nation Capital, Fire Nation
            + Children: 
                * Lu Ten
            + Bending:
                * Fire
                * Energy
        - Name: Zhao
            + Nationality: Fire Nation Capital, Fire Nation
            + Children: 
                * None
            + Bending:
                * Fire

```python
data = [
    ['Aang', 'Southern Air Temple', ['Bumi', 'Kya', 'Tenzin'], ['Air', 'Water', 'Earth', 'Fire', 'Energy']],
    ['Katara', 'Southern Water Tribe', ['Bumi', 'Kya', 'Tenzin'], ['Water', 'Blood']],
    ['Sokka', 'Southern Water Tribe', [], []], 
    ['Toph Beifong', 'Gaoling, Earth Kingdom', ['Lin Beifong', 'Suyin Beifong'], ['Earth', 'Metal']],
    ['Zuko', 'Fire Nation Capital, Fire Nation', ['Izumi', 'Kya'], ['Fire', 'Energy']],
    ['Iroh', 'Fire Nation Capital, Fire Nation', ['Lu Ten'], ['Fire', 'Energy']],
    ['Zhao', 'Fire Nation Capital, Fire Nation', [], ['Fire']]
]
print(data)
# Note: I'm using empty lists for children and bending
# for Sokka, instead of None. If I used None, I would 
# interpret that as "I don't know if Sokka has children
# or bending skills". Using the empty lists implies: 
# "I know he has 0 children and 0 bending skills"
```

# Working with Lists and Tuples

- Looping through an entire list:

    ```python
    things = ['Raindrops', 'Whiskers', 'Kettles', 'Mittens', 'Packages']
    for thing in things:
        print(thing)
        print(f"{thing} is one of my favorite things")
    ```

- Statements after a for loop

    ```python
    for person in ("Aijaz", "Adel", "Ayesha"):
        print(f"Hello, {person}")
        
    print("It's good to meet all of you.")
        
    the_sum = 0
    for n in (1, 2, 3, 4):
        the_sum = the_sum + n
        
    print(f"The sum of the first 4 integers is {the_sum}")
    ```

- Making Numerical Lists
    + Many reasons exist: games, measurements, etc.
    + Range
        * Two parameters: _start_at_ and _stop_before_
        * Never includes the second parameter

            ```python
            s = 0
            for v in range(1, 4):
                s = s + v
            
            print(f"the sum of the first 3 integers is {s}")
            
            #################################################
            
            s = 0
            n = 4
            for v in range(1, n):
                s = s + v
            
            print(f"the sum of the first {n - 1} integers is {s}")
            
            #################################################
            
            s = 0
            n = 4
            for v in range(1, n):
                s += v
            
            print(f"the sum of the first {n - 1} integers is {s}")
            ```

        * `range` with 1 parameter

            ```python
            for n in range(5):
                print(n)
            ```

        * `range` with 1 parameter - starts at 0, stops at parameter - Works well with list indexes

            ```python
            odds = [1, 3, 5, 7, 9]
            for f in range(len(odds)):
                print(odds[f] + 1)
            ``` 

        * `range` with 3 parameter: increment by parameter 3 instead of 1

            ```python
            for v in range(1, 10, 3):
                print(v)
            ```

        * Using `range` to create lists

            ```python
            l = list(range(1, 10, 3))
            ```

- Functions on lists
    + `min()`
    + `max()`
    + `sum()`
    + `len()`

- List comprehensions
    + Elegant shorthand for the creation of a new list and a `for` loop.

        ```python
        numbers = [1, 2, 3, 4, 5]
        doubles = [x * 2 for x in numbers]
        triples = [item * 3 for item in numbers]
        halves = [item/2 for item in numbers]
        ``` 

    + You can also use ranges with list comprehensions

        ```python
        squares = [x**2 for x in range(1, 10)]
        ```

- List slices
    + A slice is like a range for lists
    + A slice returns a new list
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        first_3 = months[0:3] # ['Jan', 'Feb', 'Mar']
        q2 = months[3:6] # ['Apr', 'May', 'Jun']
        ```
    
    + Omitting the first parameter implies it's 0
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        first_third = months[:4] # ['Jan', 'Feb', 'Mar', 'Apr']
        ```
    
    + Omitting the second parameter implies it's the last index + 1
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        last_third = months[8:4] # ['Sep', 'Oct', 'Nov', 'Dec']
        ```
    
    + Omitting both parameter implies indexes 0 and the last index + 1
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        year = months[:]
        ```
    
    + An index of -1 is the index of the last item
    + An index of -2 is the second-last item, and so on
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        p4 = months[-4:-1] # ['Sep', 'Oct', 'Nov']
        ```

# Week 4 Homework:

1. Create a data structure to represent a planet and it's confirmed number of moons. Create a list of these data structures. You can find the data on [Wikipedia](https://en.wikipedia.org/wiki/Planet#Planetary_attributes)
2. Print the name of each planet along with its number of confirmed moons. 
3. Print the total number of confirmed moons in the solar system. 
4. For each of the the first 4 planets in the solar system, print the planet's name, and it's number of moons. Print the total number of moons for those 4 planets.
5. For each of the the last 3 planets in the solar system, print the planet's name, and it's number of moons. Print the total number of moons for those 3 planets.
6. Use a single Python statement no more than 80 characters long to generate a list of of the reciprocals of the first 1000 positive integers. (Remember: a positive integer is any whole number greater than 0, and the reciprocal of n is 1/n).

```python
# 1
planets_and_moons = [
    ('Mercury', 0),
    ('Venus', 0),
    ('Earth', 1),
    ('Mars', 2),
    ('Jupiter', 80),
    ('Saturn', 83),
    ('Uranus', 27),
    ('Neptune', 14),
]

# 2
total = 0
for planet_name, number_of_moons in planets_and_moons:
    print(f"{planet_name} has {number_of_moons} moons")
    total += number_of_moons

# 3
print(f"The total number of confirmed moons in the solar system is {total}")

# 4
total = 0
for planet_name, number_of_moons in planets_and_moons[:4]:
    print(f"{planet_name} has {number_of_moons} moons")
    total += number_of_moons

print(f"The total number of confirmed moons for these planets is {total}")

# 5
total = 0
for planet_name, number_of_moons in planets_and_moons[-3:]:
    print(f"{planet_name} has {number_of_moons} moons")
    total += number_of_moons

print(f"The total number of confirmed moons for these planets is {total}")

# 6
print([1/x for x in range(1, 1001)])

```

## Alternate method (Aqsa's method)

```python
# 1
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
num_moons = [0, 0, 1, 2, 80, 83, 27, 14]

# 2
for index in range(len(planets)):
    print(f'Planet {planets[index]} has {num_moons[index]} moons')

# 3
print(f'The total number of confirmed moons in the solar system is {sum(num_moons)}')

# 4
print(f'The total number of confirmed moons in the solar system is {sum(num_moons[:4])}')

# 5
num_planets = len(planets)
for index in range(num_planets - 3, num_planets):
    print(f'Planet {planets[index]} has {num_moons[index]} moons')
```

# Conditionals

- Everything after an `if` is a Boolean expression (it evaluates to `True` or `False`)

    ```python
    team = input("What is your favorite NBA team?")
    if team == "Bulls":  # notice 2 equal signs to compare values
        print("They're my favorite team, too!")
    else:
        print("They're not as good as the Bulls, NGL")
    ```

- Assignment vs Test for equality 

    ```python
    team = 'Bulls'     # this is used to set the value of team to 'Bulls'
    team == 'Bulls'    # two equal signs are used to compare values. This is a Boolean expression
    team == 'Nuggets'  # two equal signs are used to compare values. This is a Boolean expression
    ```

- Syntactic VS Semantic equality

    ```python
    team = 'Lakers'
    team == 'Lakers'
    team == 'lakers'
    team.lower() 
    team.lower() == 'lakers'
    team = 'LAKERS'
    team.lower() == 'lakers'
    team = 'lAkERs'
    team.lower() == 'lakers'
    # use .lower() or .upper() or even .title() to compare strings case insensitively
    ```

- Testing for inequality

    ```python
    team = input("What is your favorite NBA team?")
    if team != "Bulls":
        print("They're not as good as the Bulls, NGL")
    else:
        print("They're my favorite team, too!")
    ```

- Testing numbers

    ```python
    age = input('How old are you?')
    age = int(age) # convert the string to an integer
    if age > 17:
        print('You are an adult')
    else: 
        print("You're still a child.")
    ```

- Testing multiple conditions

    ```python
    age = int(input('How old are you?'))  # You can do this all in one statement
    if age < 4: 
        print("You're a baby")
    elif age < 11:
        print("You're a little kid")
    elif age < 13:
        print("You're a tween")
    elif age < 18:
        print("You're a teenager")
    elif age < 20:
        print("You're a teenaged adult")
    else:
        print("You're an adult")
        
    # no else block
    
    if age == 16:
        print("You can drive now!")
    elif age == 18:
        print("You can vote now!")
    ```

- Checking multiple conditions
    - Use `or` if you want to check multiple conditions and want to at least one condition to be True

        ```python
        age = input('How old are you?')
        if age < 13 or age > 19: 
            print("You're not a teenager.")
        ```

    - Use `and` if you want to check multiple conditions and want to all conditions to be True

        ```python
        age = input('How old are you?')
        if age < 20 and age > 17: 
            print("You are a teenaged adult.")
        ```
- Everything between the `if` and the `:` is called a Boolean expression
- A boolean expression can be composed of other Boolean expressions (like we just saw with `or` and `and`)
- Other boolean tests
    + `"Feb" in ["Jan", "Feb", "Mar"]`
    + `"Jun" in ["Jan", "Feb", "Mar"]`
    + `"feb" not in ["Jan", "Feb", "Mar"]`
    + `"ear" in "hearing"`
    + `5 >= 4`
- Describe the modulo operator (`%`)
    + `5 % 3` has the value of the _remainder_ when you divide 5 by 3 (in this case: 2)
    + if `x % y == 0` it means that `x` is a multiple of `y`
    + this is often used to test if a number is odd or even. If that number % 2 is 0, then it is a multiple if 2. Which makes it even. Otherwise that number % 2 is 1, and that makes it odd.
    + The value of `x % y` is always a number >= 0 and less than `y`
- Knowing this, now you can also limit which items make it into a comprehension using a comprehension condition:

    ```python
    squares_of_evens = [x**2 for x in range(1,10) if x%2 == 0]
    ```

# Week 5 Homework

1. Continuing with last week's homework on the number of moons each planet has, print the names of the planets that more than 20 moons, as well as the number of moons they have. 
2. According to this page (https://en.wikipedia.org/wiki/List_of_landings_on_extraterrestrial_bodies) three other planets in our solar system (Mercury, Venus, and Mars) have human-made machines on their surface. Loop through the list of planets. If a planet has machines on their surface, print its name, along with "Yes." If it doesn't, print it's name, along with "Not yet."
3. Pretend your computer has a name. Ask the user for their name. If the name they enter is the same as the user's name, print "Hey! That's my name, too!". If not, print "That's a nice name." The comparison should be case-insensitive.
4. Store the numbers 1 through 9 in a list. Loop through the list, and print the appropriate number as well as the Elven translation of the number. You can find the Elven translations here: https://tolkiengateway.net/wiki/Quenya_numbers
5. Write a basic customer-support system. Ask the user "How can I help you?" If the user's reply contains the word "donate", then respond: "For donations, please contact Aijaz." If the users's reply contains the word "volunteer", then respond: "For volunteering, please contact Ayesha." If they user's reply contains neither "donate" or "volunteer" then respond with "I'm sorry. I don't understand." As always, the checks should be case-insensitive.
6. Ask the user to input a number from 1 to 8. Print the name of the planet that's that number in the solar system. For example, if the user inputs '3', then print "Earth." If the user enters a number greater than eight, then print "That's too high." If the user enters a number less than one, then print "That's too low."

```python
planets_and_moons = [
    ('Mercury', 0),
    ('Venus', 0),
    ('Earth', 1),
    ('Mars', 2),
    ('Jupiter', 80),
    ('Saturn', 83),
    ('Uranus', 27),
    ('Neptune', 14),
]

# 1
for planet, number_of_moons in planets_and_moons:
    if number_of_moons > 20:
        print(f"{planet} has {number_of_moons} moons")

# or

for planet in planets_and_moons:
    planet_name, number_of_moons = planet
    if number_of_moons > 20:
        print(f"{planet} has {number_of_moons} moons")

# or 

print([(planet, number_of_moons) for planet, number_of_moons in planets_and_moons if number_of_moons > 20])

# Another example of list comprehensions

first_10_numbers = range(10)
print([i for i in first_10_numbers if i > 5]) # prints [0, 1, 2, 4, 5]

# 2
for planet_name, number_of_moons in planets_and_moons:
    if planet_name == 'Mercury' or planet_name == "Venus" or planet_name == "Mars":
        print(planet_name + " YES")
    else:
        print(planet_name + " Not Yet")

# 3
computer_name = "Aijaz"
your_name = input("What is your name? ")
if your_name.lower() == computer_name.lower():
    print("Hey! That's my name too!")
else:
    print("That's a nice name")

# 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print("ONE")
    elif number == 2:
        print("TWO")
    elif number == 9:
        print("NINE")

# or

numbers = [(1, "ONE"), (2, "TWO"), (9, "NINE")]
for number, translation in numbers:
    print(f"{number} is translated to {translation} in Elven")

# 5
users_answer = input("How can I help you?")
if users_answer.lower().strip() in ['donate', 'give']:
    print("For donations, contact Aijaz")
elif 'volunteer' in users_answer.lower():
    print('For volunteering, contact Ayesha')
else:
    print("sorry, I don't understand")


# 6
number = int(input("Enter a number from to 8: "))
if number < 1:
    print("Too low")
elif number > 8:
    print("Too High")
else:
    planet_name, num_moons = planets_and_moons[number - 1] # note the - 1 here. Because we satrt from zero
    print(planet_name)


# Examples of boolean expressions
True or False
a == b
a < b
'donate' in users_answer
something in LIST
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
print('january' in months)

# Another example of an if statement
for n in range(1000):
    if n % 2 == 0 and n % 3 == 0 and n % 5 == 0 and n % 78 == 0:
        print(n)

# All this can be reduced to a single list comprehension:
print([item for item in range(1000) if item % 2 == 0 and item % 3 == 0 and item % 5 == 0 and item % 78 == 0])
```

# Review Week

- Lists are iterables
- All iterables share some common functionality
    + You can have them on the right hand side of a for loop
        * `for n in [1, 2, 3, 4, 5]:`
        * `for c in "Aijaz"`:
    + You can call `len()` on them
        * `len([1, 2, 3]) == 3`
        * `len("You") == 3`
    + You can check for containment
        * You can see if something is "in" it
        * `1 in [1, 2, 3, 4, 5]`
        * `"e" in "Saturn"`
    + You can index an iterable
        * `my_list = [10, 20, 30, 40, 50]`
        * `my_list[1]` (20)
        * `my_name = "Inigo Montoya"`
        * `my_name[3] == "g"`
    + You can use slices on an iterable
        * `my_list[:3] == [10, 20, 30]`
        * `my_name[6:] == "Montoya"`
- Conditional statements
    + if
    + Very useful
    + Apples to Apple, Oranges to Oranges
        * You can compare 
            - strings to strings
            - integers to integers
            - indexes to indexes
- You know how to iterate over lists and strings
- You have seen how to create an empty list and add things to it over time:

```python
my_name = "Aijaz"
list_of_characters = []
for c in my_name:
    list_of_characters.append(c)

my_list = [1, 2, 3, 4, 5]
result = []
for n in my_list:
    result.append(n*37)
print(result)
```

# Week 6 Homework

We're gonna start working on code that we'll use in our wordle game. These homework questions are gonna be difficult. Please contact me if you're having difficulty with it. But all I ask is that you spend at least 30 minutes trying it out for yourself before coming to me for help.

You may recall I said in class that everything after `in` in a phrase like `for f in ...` is an iterable. This means that it acts like a list. Strings are also iterables. 

1. Ask the user to enter a word. If the word is not exactly five letters long, print "Invalid length". Hint: The `len` command works for lists. Would it work for other iterables like strings?
2. Also for wordle: Ask the user to input a word. Print a list where each item in the list is the uppercase character from the word. For example, if you enter the word 'ocean', the program should print ['O', 'C', 'E', 'A', 'N']
3. Ask the user to enter a word. Save that word into a variable (like you did in the previous problem). Then ask the user to enter a second word. Save that word into another variable. If both of the words are 5 characters long, then do the following: Create a list named `result`: For each letter in the second word, if the corresponding letter in the first word is the same, then append 'Y' to `result`. If, however, the corresponding letter is not the same, but if the letter in the second word is somewhere in the first word, append '-' to `result`. If the letter is not in the first word at all, append 'N' to `result`. Print `result`. All comparisons should be case-insensitive.

```python

# 1
word = input("Please enter a word: ")
if len(word) != 5:
    print("Invalid length")

# 2 
word = input("Please enter a word: ")
my_list = []
for character in word:
    my_list.append(character.upper())

print(my_list)

# OR (Harraz's method. Better, IMO)
word = input("Please enter a word: ")
my_list = list(word.upper())
print(my_list)

# OR 
# (Don't do this. This is ugly)
print(list(input("Please enter a word: ").upper()))

# OR
word = input("Please enter a word: ")
my_list1 = [character.upper() for character in word]
print(my_list1)

# OR
my_list2 = []
for character in word:
    my_list2.append(character.upper())

print(my_list2)

# 3
word1 = input("Please enter a word: ").upper()
word2 = input("Please enter a second word: ").upper()
if len(word1) == 5 and len(word2) == 5:
    # Create a list named `result`:
    result = []
    # For each letter in the second word,
    for i in range(5):
        if word1[i] == word2[i]:
            result.append('Y')
        elif word2[i] in word1:
            result.append('-')
        else:
            result.append('N')

    print(result)

# OR
# You can use the zip command which you haven't learned yet.
# zip is a function that takes 1 or more iterables 
# and returns an iterable.
# The iterable that zip returns is a tuple where each element
# comes from each iterable that was passed in to zip
for t in zip([1, 2, 3], [10, 20, 30]): 
    print(t)
# prints 
# (1, 10)
# (2, 20)
# (3, 30)

list(zip([1, 2, 3], [10, 20, 30])) 
# returns [(1, 10), (2, 20), (3, 30)]

list(zip([1, 2, 3], [10, 20, 30], ["A", "B", "C"])) 
# returns [(1, 10, 'A'), (2, 20, 'B'), (3, 30, 'C')]

# Coming back to our wordle example, you could do it using zip:
word1 = input("Please enter a word: ").upper()
word2 = input("Please enter a second word: ").upper()
if len(word1) == 5 and len(word2) == 5:
    # Create a list named `result`:
    result = []
    for c1, c2 in zip(word1, word2):
        if c1 == c2:
            result.append('Y')
        elif c2 in word1:
            result.append('-')
        else:
            result.append('N')
    print(result)

```

# Loops

- Use `while` loops to count up or down

    ```python
    current_number = 10
    while current_number >= 0:
        print(current_number)
        current_number -= 1
    print("Liftoff!")
    ```

- Just like `if`, everything after `while` is a Boolean expression. It evaluates to `True` or `False`.
- Use `while True:` to create an infinite loop
- `break` exits a loop

    ```python
    current_number = 1
    while True:
        print(current_number)
        current_number += 1
        if current_number == 7:
            break
            
    print("Done!")
    ```

- One way to print all numbers except 7

    ```python
    # All numbers from 1 to 10 except for 7
    current_number = 1
    while current_number <= 10:
        if current_number != 7:
            print(current_number)
        current_number += 1
    ```

- Another way: Use `continue`, which causes Python to 'jump back' to the most recent loop test, ignoring everything that comes after it.

    ```python
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number == 7:
            continue
        print(current_number)
    ```

- Stepping through the loop

    ```python
    current_number = 0                                # cn
    while current_number < 3:                         #  0   1    2
        current_number += 1                           #  1   2    3
        if current_number == 2:                       #  F   T    F
            continue                                  #  -   Y    -
        print(current_number)                         #  Y        Y
    
    # prints: 1 3
    ```

- Another example with `continue`: Remind yourself to have breakfast everyday except Mondays and Thursdays:

    ```python
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for day in days:
        if day == 'Mon' or day == 'Thu':
            continue
        print(f"Today is {day}. Don't forget to have breakfast.")
    ```

- A better test, in my opinion is to check if `day` is `in` a list:

    ```python
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for day in days:
        if day in ['Mon', 'Thu']:
            continue
        print(f"Today is {day}. Don't forget to have breakfast.")
    ```

- An example of `continue` going up to the most recent loop. (See the video for a description of this):

    ```python
    # a % b is the remainder of a / b
    for n in range(1, 101):
        if n % 15 == 0:
            if n % 2 == 0:
                continue
            print(f"{n} is a multiple of 15")
            for x in range(1, n+1):
                if x % 7 == 0:
                    if x % 2 == 0:
                        continue
                    print(f"   {x} is a multiple of 7")
    ```    

- Sometimes you need to iterate over an iterable with both - the value and the index of the current element. A naïve way is to do this:

    ```python
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for n in range(len(days)):
        print(f"{days[n]} is day {n+1}")
    ```

- A better way is to use `enumerate`, which returns a tuple of the index and the value:

    ```python
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for n, day in enumerate(days):
        print(f"{day} is day {n+1}")
    ```

- You can also use `zip` to pair up elements from two or more lists (as seen above):

    ```python
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    jours = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']
    dias = ['Dom', 'Lun', 'Mar', 'Mie', 'Jeu', 'Vie', 'Sab']
    
    for eng, french, spanish in zip(days, jours, dias):
        print(f"The French word for {eng} is {french}, and the Spanish word is {spanish}")
    ```

# Week 7 Homework

1. Think about how the Wordle game works: We get 6 guesses to guess a random word that the computer has selected. Create a variable named `maximum_guesses` and set its value to 6. 
2. Create another variable name `number_of_guesses` and set its value to 0. (Every time the user guesses a word, `number_of_guesses` should be incremented by one. The value of `maximum_guesses` never changes.) 
3. Create another variable named `random_word`. Set its value to any 5-letter word, like "OCEAN", "STORM" or "AIJAZ" ;) 
4. In class we wrote a `while` loop that looked like this:

    ```python
    current_number = 0
    while True:
        current_number += 1
        print(current_number)
        if current_number == 7:
            break
            
    print("Done!")
    ```

5. Now write a similar `while` loop. Inside the loop you should ask the user to enter a word. 
6. Every time the user enters a word, you should do the following:
    + Increment the `number_of_guesses`
    + Compare the word the user entered to `random_word`. 
    + If the word the user entered is the same as `random_word` then print "That's correct!" and exit the while loop. If not, continue on.
    + If the word the user entered is not the same as `random_word` then print "That's wrong."
    + If the user has run out of guesses, print "Sorry. You ran out of guesses. The word is " and `random_word`. Exit the loop. 
    + If the user has not run out of guesses, then print "Try again."
    
7. We're gonna work on another game (in addition to Wordle). This is the popular game known as Boggle. Create a new file. On the first line of the file type in `import random`. We'll learn about the `import` command later. 
8. Create an empty list named `board`.
9. Create a list named `cubes` containing the following strings:
    + `"AAEEGN"`
    + `"ABBJOO"`
    + `"ACHOPS"`
    + `"AFFKPS"`
    + `"AOOTTW"`
    + `"CIMOTU"`
    + `"DEILRX"`
    + `"DELRVY"`
    + `"DISTTY"`
    + `"EEGHNW"`
    + `"EEINSU"`
    + `"EHRTVW"`
    + `"EIOSST"`
    + `"ELRTTY"`
    + `"HIMNUQ"`
    + `"HLNNRZ"`
10. Each of these strings represents a cube in Boggle. Loop through this list of strings
    + For each string select a random letter from the string and add that letter to the list named `board`. See the following code for instructions on selecting a random letter:
    
        ```python
        # To select a random element from an iterable, 
        # use the function random.choice()
        # For example, to select a random number from a list, 
        # you can do something like the following:
        random_number = random.choice([1, 3, 5, 7, 9, 10, 20, 30, 40, 50])

        # Since strings are iterables as well, you can select
        # a random character from a string the same way:
        random_character = random.choice("OCEAN")

        # This will randomly return O, C, E, A, or N.
        ```

11. Print the list named `board`
12. Like you did with the Wordle homework above, write a while loop that runs forever. Inside the loop ask the user to enter a word.
13. Every time the user enters a word, you should do the following:
    + If the word that the user enters is "Q", then exit the while loop. If not, continue on...
    + Calculate the length of the word. If the word is less than 3 letter long, print "All words need be at least 3 letters long."
    
We'll continue with Boggle over the next few weeks, inshaAllah.

# Dictionaries

- A dictionary is a data structure composed of keys and values. Like a real dictionary, it's easy to find the value for a key in a dictionary.

    ```python
    d = {'card': 'a stiff piece of paper',
         'duck': 'A bird that swims',
         'elephant': 'A large mammal'}
    
    print(d)
    
    print(d['duck'])
    print(d['elephant'])
    print(d['frog'])  # This will throw an error
    ```

- We could use dictionaries to make our "Avatar, The Last Airbender" homework easier:

    ```python
    aang = {"name": "Aang",
            "gender": 'M',
            "nationality": "Southern Air Temple",
            "children": [{'name': 'Bumi', 'gender': 'M'},
                         {'name': 'Kya', 'gender': 'F'},
                         {'name': 'Tenzin', 'gender': 'M'}]
            }

    # You can see above that values can be strings, or arrays, or any other type
    # Keys are strings
    
    # creating an empty dictionary
    katara = {}

    # setting a value
    katara['name'] = 'Katara'

    # setting a value
    katara['gender'] = 'F'

    # setting a value
    katara['nationality'] = "Southern Water Tribe"

    # With lists, both values point to the same list 
    # (like two people holding the same book)
    katara['children'] = aang['children']

    # If we change the name of one of Aang's children...    
    aang["children"][1]['name'] = 'Kiya'
    
    # ... that also changes the name of one Katara's children
    print(katara)

    # deleting a key
    del(katara['gender'])
    print(katara)
    print(aang)
    del(aang['gender'])

    # If you delete a field from every item (dictionary) of the list...
    for child in aang['children']:
        del(child['gender'])

    # ... then that changes everywhere that list is referenced
    print(aang)
    print(katara)

    # Use 'get' to retrieve a value and return a default value 
    # (True in this case) if the key doesn't exist
    # in the dictionary
    print(katara.get('child', True))
    uncle_iroh = {'name': 'Iroh', 'child': False}
    print(uncle_iroh)
    print(uncle_iroh.get('child', True))
    toph = {'name': 'Toph Beifong', 'child': True}
    print(toph.get('child', True))
    print(katara['child'])
    ```    

# Boggle Homework (Part 1)

```python
import random

board = []

cubes = [
    "AAEEGN", "ABBJOO", "ACHOPS", "AFFKPS",
    "AOOTTW", "CIMOTU", "DEILRX", "DELRVY",
    "DISTTY", "EEGHNW", "EEINSU", "EHRTVW",
    "EIOSST", "ELRTTY", "HIMNUQ", "HLNNRZ"
]

for cube in cubes:
    # For each string select a random letter from the string
    # and add that letter to the list named board.
    random_letter = random.choice(cube)
    board.append(random_letter)

print(board)

while True:
    word = input("Please enter a word: ")
    if word.strip().upper() == 'Q':
        # we call .strip() so that something like "  q  " is also accepted
        # strip() strips leading and trailing spaces from a string
        break
    if len(word) < 3:
        print("All words need to be at least three letters long.")
        continue
    print("Here we'll add the rest of the game logic")
```

Keep in mind that if we check for the word length before we check for the `q` then we'll run into an infinite loop.

# Iterating over Dictionaries

- What if we try using a dictionary in a `for` loop.

    ```python
    d = {"name": "Aijaz", "city": "Thornton"}

    for item in d:
        print(item)
    ```

- This prints a list of all the keys. From this we can assume that a dictionary is an iterable.
- Since a dictionary is an iterable, we can use it in list comprehensions: 

    ```python
    print([d[item].upper() for item in d])
    print([item.upper() for item in d])    
    ```

- There are other ways to iterate over dictionaries:

    ```python
    # iterate over the list of values
    for v in d.values():
        print(v)       

    # iterate over the list of keys
    for k in d.keys():
        print(k)       

    # iterate over tuples of keys and values
    for i in d.items():
        k, v = i
        print(f"The value of {k} is {v}")

    # a more pythonic way of doing this is: 
    for k, v in d.items():
        print(f"The value of {k} is {v}")

    ```

# Functions

- A function is a command that tells the computer to do something. We started using functions in week 1 of this class. `print` is a function. 

    ```python
    # print can take a single argument or parameter. 
    # The argument can be any expression: 
    # For example, a string, an integer, a list, or a dictionary
    print("Hello, world")
    print(1)
    print([1, 2, 3, 4])
    print([i * 2 for i in [1, 2, 3, 4]])
    print({"a": 1, "b": 2})

    # print can also take multiple arguments. 
    # If passed multiple arguments, it prints out each argument, 
    # with a space in between them
    print(1, 4)
    print("Hello", "Aijaz")
    my_name = "Aijaz"
    print("My name is", my_name)

    # print can also be used with more than 2 arguments
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    ```

- Some functions have return values. A return value is what the function call evaluates to: 

    ```python
    # The return value of the input function is what the user typed in
    word = input("Please enter a word: ")
    print(word)
    print(word.upper())

    # The return value of len is the length of the 
    # iterable that is the parameter to the function.
    print(len([1, 2, 3, 4, 5]))
    print(len(word))
    print(len({"a": 1, "b": 2, "c": 3}))
    ```

## Making your own functions

- You can make your own functions to do the same thing every time the function is invoked:

    ```python
    def greet():
        print("Hello.")
        print("My name is Inigo Montoya.")
        print("You killed my father.")
        print("Prepare to die.")
    
    greet()
    greet()
    ```

- You can make a function do different things based on the value of the argument(s) passed in:

    ```python
    def welcome(person_name):
        print(f"Hello, {person_name}")
        print("Do you like to drink coffee in the morning?")


    welcome("Aijaz")
    welcome("Wisall")
    welcome("Aqsa")
    ```

- You can make a function return a value that's based on the argument(s) passed in:

    ```python
    def double(value):
        return value * 2


    print(double(3))
    print(double(30))
    print(double("Aijaz"))
    ```

- You can make functions that ensure that you don't have a typo n your calculations:

    ```python
    def pi():
        return 3.14159
    
    
    # This is a lot better than the 2 statements below - where there 
    # is a typo in one of the values of pi
    print(f"The area of a circle with a radius of 2 is {pi() * 2 * 2}")
    print(f"The area of a circle with a radius of 4 is {pi() * 4 * 4}")
    
    # The typo in the second statement causes a miscalculation
    print(f"The area of a circle with a radius of 2 is {3.14 * 2 * 2}")
    print(f"The area of a circle with a radius of 4 is {3.41 * 4 * 4}")
    ```

- You can also create a function that takes in two paramenters and returns a value:

    ```python
    def add(v1, v2):
        return v1 + v2


    print(add(1, 2))
    print(add("Hello", " world"))
    print(add("Hello", add(" ", "world")))
    ```


# Week 9 Homework

In Week 6 you wrote code that prompted the user to enter two words. Then you would print out a list whose contents changed based on the what the user entered. If you remember, we saw two ways to do this: 

```python

word1 = input("Please enter a word: ").upper()
word2 = input("Please enter a second word: ").upper()
if len(word1) == 5 and len(word2) == 5:
    # Create a list named `result`:
    result = []
    # For each letter in the second word,
    for i in range(5):
        if word1[i] == word2[i]:
            result.append('Y')
        elif word2[i] in word1:
            result.append('-')
        else:
            result.append('N')

    print(result)

# OR

word1 = input("Please enter a word: ").upper()
word2 = input("Please enter a second word: ").upper()
if len(word1) == 5 and len(word2) == 5:
    # Create a list named `result`:
    result = []
    for c1, c2 in zip(word1, word2):
        if c1 == c2:
            result.append('Y')
        elif c2 in word1:
            result.append('-')
        else:
            result.append('N')
    print(result)

```

- Create a new file named `wordleText.py`
    + In that file create a function named `process_words` that takes two parameters: `secret_word` and `guess`
    + Modify the code above and put it inside `process_words` so that:
        * You use `secret_word` and `guess` instead of `word1` and `word2`. 
        * Don't prompt the user for `word1` and `word2`. Use `secret_word` instead of `word1` and `guess` instead of `word2`.
        * Don't print the list named `result`. 
        * Instead, have the function return the list named `result`.
    + You can test it this way. Add the following code after your definition of `process_words`:
    
        ```python
        test_data = [('OCEAN', 'COUNT'),
                     ('OCEAN', 'ARISE'),
                     ('TRILL', 'STUMP'),
                     ('MITES', 'MIGHT'),
                     ('STEAM', 'MATES'),
                     ('STEAM', 'STUNG'),
                     ('STEAL', 'STALE'),
                     ('STEAM', 'STEAM'),
                     ('ARISE', 'COUNT')]
        for secret, guess in test_data:
            print(f"{secret}/{guess} => {process_words(secret, guess)}")
        ```

    + If everything is correct, the program should print the following:

        ```
        OCEAN/COUNT => ['-', '-', 'N', '-', 'N']
        OCEAN/ARISE => ['-', 'N', 'N', 'N', '-']
        TRILL/STUMP => ['N', '-', 'N', 'N', 'N']
        MITES/MIGHT => ['Y', 'Y', 'N', 'N', '-']
        STEAM/MATES => ['-', '-', '-', '-', '-']
        STEAM/STUNG => ['Y', 'Y', 'N', 'N', 'N']
        STEAL/STALE => ['Y', 'Y', '-', '-', '-']
        STEAM/STEAM => ['Y', 'Y', 'Y', 'Y', 'Y']
        ARISE/COUNT => ['N', 'N', 'N', 'N', 'N']
        ```

- More functions
    + Create a function named `apologize` that takes in two parameters: `person` and `reason`.
        * It should print an apology to the person for the reason specified.
        * For example, if you call `apologize("brother", "for pouring honey in your hair while you were sleeping")`, it should print `Dear brother. I'm sorry for pouring honey in your hair while you were sleeping`
        * If you call `apologize("Mother", "I scribbled in your favorite book.")` it should print `Dear Mother. I'm sorry I scribbled in your favorite book`
    + Create a function named `triple`. It should take one parameter and return the value of that parameter tripled. 
        * For example, `print(triple(3))` should print `9`.
        * For example, `print(triple("Well,"), "What do we have here?")` should print `Well, Well, Well, What do we have here?`.
    + Create a function named `rot13` that takes one parameter named `string`
        * Create a variable named `alphabet` that has the value `"abcdefghijklmnopqrstuvwxyz"`
        * Create a variable named `answer` that has the value `""` (the empty string)
        * Loop for every character `char` in `string`
            - If the character (lower case) is not in `alphabet`, then set `answer` to `answer` + `char` and continue to the next iteration of the loop
            - Create a variable named `index` that has the value of `alphabet.find(char.lower())`
                + This means that `index` is the integer offset of the first occurrance of `char.lower()` in `alphabet`
                + In other words if `char` is `a` or `A`, `index` is 0
                + If `char` is `e` or `E`, `index` is 4, and so on
            - Create a variable named `new_index` that's `index` + 13 with a wraparound back to 0, if `index` + 13 > 25
                + If `char` is `a`, then new_index should be 13
                + If `char` is `E`, then new_index should be 17
                + If `char` is `m`, then new_index should be 25
                + If `char` is `N`, then new_index should be 0. Why 0? Because we want to replace `n` with `a`, `o` with `b`, and so on.
                    * HINT: This is what modulo (`%`) was invented for. Use this operator.
            - Create a new variable named `rotated_char` that has the value of `alphabet[new_index]`
            - If the character `char` is upper case, then add the upper case version of `rotated_char` to `answer`
                + HINT: An easy way to check if a string is upper case is to call `.isupper()`
                    * `"a".isupper()` is `False`
                    * `"B".isupper()` is `True`
            - Else if `char` is not upper case, then add `char` to `answer`
        * After your loop is over, print the value of `answer`
        * Test out your function with the following python code: Each call should print a simple English sentence: 
        
            ```python
            print(rot13("V yvxr gur Clguba cebtenzzvat ynathntr!"))
            print(rot13("Nvwnm unf n jrveq frafr bs uhzbe, evtug?"))
            print(rot13("Arire tbaan tvir lbh hc, arire tbaan yrg lbh qbja, arire tbaan eha nebhaq naq qrfreg lbh!"))
            ```

- Boggle homework. 
    + Last week I told you to make the variable named `board` a list: 

        ```python
        board = []
        # ...
        for cube in cubes:
            # For each string select a random letter from the string
            # and add that letter to the list named board.
            random_letter = random.choice(cube)
            board.append(random_letter)
        ```    

    + Since the Boggle board is two-dimensional, make `board` be a two-dimensional list – a list of lists. Think of `board` as a list of rows, where each row has 4 random letters. `board` will have 4 such rows, for a total of 16 random letters. You can pre-populate the list like this:

        ```python
        board = [[], [], [], []]
        # ...
        for cube in cubes:
            # For each string select a random letter from the string
            # and add that letter to the list named board.
            random_letter = random.choice(cube)
            # board.append(random_letter)
        ```    

    + Now, you can no longer use the line `board.append(random_letter)`, which I've commented out above. You can't use it, because you don't want to append the random letter to board, but to one of the lists that's an element of `board`. You will need to use a counter:
        *  If `cube` is the first, second, third, or fourth cube, then you need to append `random_letter` to `board[0]`. 
        *  If `cube` is the fifth, sixth, seventh, or eighth cube, then you need to append `random_letter` to `board[1]`. 
        *  And so on.
        *  Modify your code so that you append `random_letter` to the proper row in `board`.
        *  Hints:
            -  Recall that `enumerate`  gives you both an index and an item from a list. This can help here.
            -  There is a python operator named `//` that does integer division
                +  So: `0 // 4`, `1 // 4`, `2 // 4`, and `3 // 4` all have the value of 0
                +  and `4 // 4`, `5 // 4`, `6 // 4`, and `7 // 4` all have the value of 1
                +  and `8 // 4`, `9 // 4`, `10 // 4`, and `11 // 4` all have the value of 2
                +  and `12 // 4`, `13 // 4`, `14 // 4`, and `15 // 4` all have the value of 3
            - How can this fact help? 🤔
    + Print `board` after you populate it correctly.


# Week 10 - More functions


 
"Over the garden wall"
