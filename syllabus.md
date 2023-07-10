# Syllabus & Lesson Plan

We will be using [Python Crash Course, 2nd Edition](https://nostarch.com/pythoncrashcourse2e/) as the course textbook. The syllabus (mostly) follows the order of topics as introduced in the book. I will be using different examples during class so you can use the book to study the topics in greater detail, and get a better understanding of them.

## Setup
- Reboot computer
- Make sure new battery is in camera
- Launch Pycharm
- Close all Pycharm windows
- Quit Pycharm
- Delete wk01
- Launch screenflow start recording
    + Make sure screenflow is recording audio and video
- Launch zoom
    + Make sure zoom is recording
- Do clapper
- Stop Screenflow confirm video is good
- Restart screenflow
- Set focus on Fuji webcam

## Week 1
* Welcome
    - About me
    - About MYPI
        + Two sisters
        + Originally for girls
        + I do outdoor stuff
    - What you'll learn in this class
        + Programming with Python
        + Good enough to interview
* House Rules
    - Feel free to interrupt
        + Just unmute yourself
        + Or raise your hand
    - I'll feel free to tell you to hold on
    - It's ok to say I don't understand 
        + That's on me, not on you
        + Different ways to explain work with different people
    - It's up to you if you want to turn your video on or not
        + It's easier for me to judge if you're confused about something if your video is on. 
        + But at the end it's up to you, and I won't be offended one way or the other
    - Office hours
* Computers are stupid
    * Order
    * Explicit instructions 
    * Only understand very simple languages
* Launching and using the REPL
    * Your first Python Program in the repl
    * Print("hello world")
    * Now you're a programmer
* Pycharm
    * Launch
    * Creating a new project.
    * Type in hello_world.py 
    * How to run the current file
    * Add a second print statement 
* What happens when you run a program
* Syntax highlighting

--- 

* Variables
    * Use a sheet of paper, folded up
    * Two sheets. Give a sheet to each student
    * Ask student to unfold and read the value
    * Use wrong name: Computers are stupid
    * Update variable repeat
    * Message = "hw" print message 
    * Try invalid variable names
        * starting with number
        * With space
        * Typos
    * Assignment 
    * Lookup
    * Give a student a blank sheet. None.
    * Multiple assignment
* Strings
* Operators 
    * print "hello " + "world" string
    * Introduce Integers
    * Int operators
* Functions - title(), upper(), and lower()
* Use pycharm
* "Hello world".title()
* Using variables in strings: f strings
* New lines in strings
* Quotes in strings
* Double and triple quoted strings 
* Comments 
    * why use comments?
* Reading User Input 
* Putting it all together


* **Homework**
    * Babyshark.py
    * Write a program that asks you to input a string. Once you input a string it should print out that string, followed by "shark! Do do do, do do do!" 3 times followed by the string, and then "shark"

    ```
        What is your name? 
        Baby
        Baby shark! Do do do do do do!
        Baby shark! Do do do do do do!
        Baby shark! Do do do do do do!
        BABY SHARK!
    ```
    
## Week 2: Introduction to Lists and Tuples

    ```python
    import pyttsx3
    what = input("What should I say? ")
    engine = pyttsx3.init()
    engine.say(what)
    engine.runAndWait()
    ```

- Homework review

    ```python
    name = input("What is your name? ")
    print(name + " shark! Do do do do do do!")
    print(name + " shark! Do do do do do do!")
    print(name + " shark! Do do do do do do!")
    print(name.upper() + " SHARK!")    
    ```

- Anything we missed last week

* What is a list
* Accessing elements with indexes
    * index 0 refers to the first item in the list
    * It's this way in most computer languages
    * Think of an index as the _distance from the first item_
    * The index of the last item is the length of the list - 1

        ```python
        my_list = [10, 20, 30]
        l = len(my_list)
        my_list[0]
        my_list[1]
        my_list[2]
        my_list[3] # this should throw an error. Talk about this
        ```

    * You can also use negative indexes. `-1` for the last item, and so on
    * `li = things[-1]`
    * Why `-1`?  Because `-0` doesn't make sense.
* Changing, adding, and removing elements
    * modifying elements 
    * Adding elements `append`
    * `insert(0, "abc")`
    * `l = things.pop()`
    * `a = things.pop(3)`
    * `things.del(3)`
    * `things.remove('a thing')`
    * `l1.extend(l2)` 
* Organizing a list
    * Sort permanently with `cars.sort()`
    * Get a sorted copy with `sorted(cars)`
    * Reversing a list with `cars.reverse()`
* `n = len(things)` 
* Tuples
    * Parens 
    * Safety check
    * Usually heterogenous
* Lists containing lists
    * `l1.append(l2)`
    * List data structures
        * [x,y]
        * If you never need to add or delete, use tuples instead 
* List copy references 
    * References
    * Make a "book" of folded sheets of paper
    * Have one student "hold" it with a string
    * Have another student hold onto it as well
    * Update the value in one of the folded sheets 
    * Ask each student to read out their value written on the paper
    * Explain that the strings are references and that the students are variables
    * Making a copy with `l2 = list(l1)`
    * Get a second blank book and copy the values from one book to another
    * Repeat the exercise with lists of lists (books containing books)
* *Homework* 
    1. Make a list of your favorite sports in order of preference (most favorite first)
    2. Print the list
    3. You learn about a new game called "7 tiles" and suddenly it's your favorite game. Modify the list so that this is new game is now in the first spot, with everything else moving down a spot. Print the list.
    4. After a week, "7 tiles" moves to the second spot but the third most favorite game moves to the top spot. Modify the list accordingly, and print the list.
    5. After another week, you get bored of "7 tiles" and remove it from your list altogether. Everything else stays the same. Modify the list accordingly, and print the list.
    6. Print the list in reverse order
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

## Week 3. Working with Lists and Tuples

* Homework review
* Did you use a list or a tuple for children or bending? Why?
* Looping through an entire list

    ```python
    things = ['Raindrops', 'Whiskers', 'Kettles', 'Mittens', 'Packages']
    for thing in things:
        print(thing)
    ```

* Step through loop
* Multiple statements in a block
    - 2 print statements

* Statements after a for loop

    ```python
    for person in ("Aijaz", "Adel", "Ayesha"):
        print(f"Hello, {person}")
        
    print("It's good to meet all of you.")
        
    the_sum = 0
    for n in (1, 2, 3, 4):
        the_sum = the_sum + n
        
    print(f"The sum of the first 4 integers is {the_sum}")
    ```

* Blank line optional
* Avoiding Indentation Errors
* Making Numerical Lists
    - Many reasons exist: games, measurements, etc.
    - Range
        + Two parameters: start_at and stop_before
        + Never includes the second parameter

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

        + `range` with 1 parameter

            ```python
            for n in range(5):
                print(n)
            ```

        + `range` with 1 parameter - starts at 0, stops at parameter - Works well with list indexes

            ```python
            odds = [1, 3, 5, 7, 9]
            for f in range(len(odds)):
                print(odds[f] + 1)
            ``` 

        + `range` with 3 parameter: increment by parameter 3 instead of 1

            ```python
            for v in range(1, 10, 3):
                print(v)
            ```

        + Using `range` to create lists

            ```python
            l = list(range(1, 10, 3))
            ```

* Functions on lists
    - `min()`
    - `max()`
    - `sum()`
    - `len()`

* List comprehensions
    - Elegant shorthand for the creation of a new list and a `for` loop.

        ```python
        numbers = [1, 2, 3, 4, 5]
        doubles = [x * 2 for x in numbers]
        triples = [item * 3 for item in numbers]
        halves = [item/2 for item in numbers]
        ``` 

    - You can also use ranges with list comprehensions

        ```python
        squares = [x**2 for x in range(1, 10)]
        ```

* List slices
    - A slice is like a range for lists
    - A slice returns a new list

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        first_3 = months[0:3] # ['Jan', 'Feb', 'Mar']
        q2 = months[3:6] # ['Apr', 'May', 'Jun']
        ```

    - Omitting the first parameter implies it's 0

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        first_third = months[:4] # ['Jan', 'Feb', 'Mar', 'Apr']
        ```

    - Omitting the second parameter implies it's the last index + 1

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        last_third = months[8:4] # ['Sep', 'Oct', 'Nov', 'Dec']
        ```

    - Omitting both parameter implies indexes 0 and the last index + 1

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        year = months[:]
        ```

    - An index of -1 is the index of the last item
    - An index of -2 is the second-last item, and so on

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        p4 = months[-4:-1] # ['Sep', 'Oct', 'Nov']
        ```

* **Homework**

    1. Create a data structure to represent a planet and it's confirmed number of moons. Create a list of these data structures. You can find the data on [Wikipedia](https://en.wikipedia.org/wiki/Planet#Planetary_attributes)
    2. Print the name of each planet along with its number of confirmed moons. 
    3. Print the total number of confirmed moons in the solar system. 
    4. For each of the the first 4 planets in the solar system, print the planet's name, and it's number of moons. Print the total number of moons for those 4 planets.
    5. For each of the the last 3 planets in the solar system, print the planet's name, and it's number of moons. Print the total number of moons for those 3 planets.
    6. Use a single Python statement no more than 80 characters long to generate a list of of the reciprocals of the first 1000 positive integers. (Remember: a positive integer is any whole number greater than 0, and the reciprocal of n is 1/n).


## Week 4. Conditionals

* Programs so far have been boring
* Programs get interesting when they examine conditions and make decisions based on the value of those conditions.
* If statements

    ```python
    team = input("What is your favorite NBA team?")
    if team == "Bulls":
        print("They're my favorite team, too!")
    else:
        print("They're not as good as the Bulls, NGL")
    ```

* Assignment vs Test for equality 

    ```python
    team = 'Bulls'
    team == 'Bulls'
    team == 'Nuggets'
    ```

* Syntactic VS Semantic equality

    ```python
    team = 'Lakers'
    team == 'Lakers'
    team == 'lakers'
    lower(team) 
    lower(team) == 'lakers'
    team = 'LAKERS'
    lower(team) == 'lakers'
    team = 'lAkERs'
    lower(team) == 'lakers'
    team == 'lAkERs'
    ```

* Using "bulls" in team.lower()

* Testing for inequality

    ```python
    team = input("What is your favorite NBA team?")
    if team != "Bulls":
        print("They're not as good as the Bulls, NGL")
    else:
        print("They're my favorite team, too!")
    ```

* Why, then do we have == and != if computers are so stupid
    - Because computers are good at numbers
    

* Testing numbers

    ```python
    age = input('How old are you?')
    age = int(age)
    if age > 17:
        print('You are an adult')
    else: 
        print("You're still a child.")
    ```

* Debugging - Using `int()` to accept numerical input

* Testing multiple conditions

    ```python
    age = int(input('How old are you?'))
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
        print("You can drive!")
    elif age == 18:
        print("You can vote!")
    ```

* Checking multiple conditions
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
* Everything between the `if` and the `:` is called a Boolean expression
* A boolean expression can be composed of other Boolean expressions (like we just saw with `or` and `and`)
* Other boolean tests
    - `"Feb" in ["Jan", "Feb", "Mar"]`
    - `"Jun" in ["Jan", "Feb", "Mar"]`
    - `"feb" not in ["Jan", "Feb", "Mar"]`
    - `"ear" in "hearing"`
    - `5 >= 4`
* Describe the modulo operator (`%`)
    - `5 % 3` has the value of the _remainder_ when you divide 5 by 3 (in this case: 2)
    - if `x % y == 0` it means that `x` is a multiple of `y`
    - this is often used to test if a number is odd or even. If that number % 2 is 0, then it is a multiple if 2. Which makes it even. Otherwise that number % 2 is 1, and that makes it odd.
    - The value of `x % y` is always a number >= 0 and less than `y`
* Knowing this, now you can also limit which items make it into a comprehension using a comprehension condition:

    ```python
    squares_of_evens = [x**2 for x in range(1,10) if x%2 == 0]
    ```

### Homework

* Continuing with last week's homework on the number of moons each planet has, print the names of the planets that more than 20 moons, as well as the number of moons they have. 
* According to this page (https://en.wikipedia.org/wiki/List_of_landings_on_extraterrestrial_bodies) three other planets in our solar system (Mercury, Venus, and Mars) have human-made machines on their surface. Loop through the list of planets. If a planet has machines on their surface, print its name, along with "Yes." If it doesn't, print it's name, along with "Not yet."
* Pretend your computer has a name. Ask the user for their name. If the name they enter is the same as the user's name, print "Hey! That's my name, too!". If not, print "That's a nice name." The comparison should be case-insensitive.
* Store the numbers 1 through 9 in a list. Loop through the list, and print the appropriate number as well as the Elven translation of the number. You can find the Elven translations here: https://tolkiengateway.net/wiki/Quenya_numbers
* Write a basic customer-support system. Ask the user "How can I help you?" If the user's reply contains the word "donate", then respond: "For donations, please contact Aijaz." If the users's reply contains the word "volunteer", then respond: "For volunteering, please contact Ayesha." If they user's reply contains neither "donate" or "volunteer" then respond with "I'm sorry. I don't understand." As always, the checks should be case-insensitive.
* Ask the user to input a number from 1 to 8. Print the name of the planet that's that number in the solar system. For example, if the user inputs '3', then print "Earth." If the user enters a number greater than eight, then print "That's too high." If the user enters a number less than one, then print "That's too low."

We're gonna start working on code that we'll use in our wordle game. These homework questions are gonna be difficult. Please contact me if you're having difficulty with it. But all I ask is that you spend at least 30 minutes trying it out for yourself before coming to me for help.

You may recall I said in class that everything after `in` in a phrase like `for f in ...` is an iterable. This means that it acts like a list. Strings are also iterables. 

* Ask the user to enter a word. If the word is not exactly five letters long, print "Invalid length". Hint: The `len` command works for lists. Would it work for other iterables like strings?

* Also for wordle: Ask the user to input a word. Print a list where each item in the list is the uppercase character from the word. For example, if you enter the word 'ocean', the program should print ['O', 'C', 'E', 'A', 'N']

* Ask the user to enter a word. Save that word into a variable (like you did in the previous problem). Then ask the user to enter a second word. Save that word into another variable. If both of the words are 5 characters long, then do the following: Create a list named `result`: For each letter in the second word, if the corresponding letter in the first word is the same, then append 'Y' to `result`. If, however, the corresponding letter is not the same, but if the letter in the second word is somewhere in the first word, append '-' to `result`. If the letter is not in the first word at all, append 'N' to `result`. Print `result`. All comparisons should be case-insensitive.

For example, if the 1st word is 'ARENA' and the second word is 'RAINS', `result` should be: `['-', '-', 'N', 'Y', 'N']`.

01234
ARENA
RAINS



Examples of modulo:

```python
hours = int(seconds_input / 3600)
minutes = int((seconds_input % 3600) / 60)
min2 = int(seconds_input/60) % 60
seconds = seconds_input % 60
return f"{hours}:{minutes}({min2}):{seconds}"
```

And also for figuring out where something should go in a circular list


## Review week

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




## Week 7 Homework

- Think about how the Wordle game works: We get 6 guesses to guess a random word that the computer has selected. Create a variable named `maximum_guesses` and set its value to 6. 
- Create another variable name `number_of_guesses` and set its value to 0. (Every time the user guesses a word, `number_of_guesses` should be incremented by one. The value of `maximum_guesses` never changes.) 
- Create another variable named `random_word`. Set its value to any 5-letter word, like "OCEAN", "STORM" or "AIJAZ" ;) 
- In class we wrote a `while` loop that looked like this:

    ```python
    current_number = 0
    while True:
        current_number += 1
        print(current_number)
        if current_number == 7:
            break
            
    print("Done!")
    ```

- Now write a similar `while` loop. Inside the loop you should ask the user to enter a word. 
- Every time the user enters a word, you should do the following:
    + Increment the `number_of_guesses`
    + Compare the word the user entered to `random_word`. 
    + If the word the user entered is the same as `random_word` then print "That's correct!" and exit the while loop. If not, continue on.
    + If the word the user entered is not the same as `random_word` then print "That's wrong."
    + If the user has run out of guesses, print "Sorry. You ran out of guesses. The word is " and `random_word`. Exit the loop. 
    + If the user has not run out of guesses, then print "Try again."
    
- We're gonna work on another game (in addition to Wordle). This is the popular game known as Boggle. Create a new file. On the first line of the file type in `import random`. We'll learn about the `import` command later. 
- Create an empty list named `board`.
- Create a list named `cubes` containing the following strings:
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
- Each of these strings represents a cube in Boggle. Loop through this list of strings
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

- Print the list named `board`
- Like you did with the Wordle homework above, write a while loop that runs forever. Inside the loop ask the user to enter a word.
- Every time the user enters a word, you should do the following:
    + If the word that the user enters is "Q", then exit the while loop. If not, continue on...
    + Calculate the length of the word. If the word is less than 3 letter long, print "All words need be at least 3 letters long."
    
We'll continue with Boggle over the next few weeks, inshaAllah.


## While loops

* Backbone of most software
* Example: Loop variable

    ```python
    current_number = 10
    while current_number >= 0:
        print(current_number)
        current_number -= 1
    print("Liftoff!")
    ```

* Example: Break

    ```python
    current_number = 1
    while True:
        print(current_number)
        current_number += 1
        if current_number == 7:
            break
            
    print("Done!")
    ```

    - If you forget the break statement you'll wind up with an infinite loop. You'll have to hit ctrl-C to stop the program
    
    - Looping over a list

        ``` python
        people = ["Alice", "Bob", "Charlie"]
        for person in people:
            print(person)
        ```
        
        + Sometimes we want the index of the item along with the item:

            ``` python
            people = ["Alice", "Bob", "Charlie"]
            i = 0
            for person in people:
                print(f"The person at index {i} is {person}")
                i += 1
            ```
        
        + Since this a common thing to want to do, there's a shortcut to do this in python:

            ``` python
            people = ["Alice", "Bob", "Charlie"]
            for thing in enumerate(people):
                print(thing)
            ```

            ``` python
            people = ["Alice", "Bob", "Charlie"]
            for i, person in enumerate(people):
                print(f"The person at index {i} is {person}")
            ```
            
### Homework

## Week 5. Dictionaries
- Creating dictionaries
    
    ```python

    ```

- Why dictionaries are helpful
    + Speed
    + Programmer ease of use
    + Example: _Avatar_ homework
- Working with dictionaries
    + Accessing values
    + Adding new key-value pairs
    + Creating empty dictionaries
    + Modifying values
    + Removing key-value pairs with `del`
    + Using get instead of keyed access
- Looping through dictionaries
    + `items()`
    + `keys()`
    + Looping through keys in a particular order with `sorted()`
    + `values()`
- Nesting
    + Going deeper with the _Avatar_ homework
    + Could nest dictionaries or arrays, or anything else
    + Example of dictionary inside a dictionary

## Week 6. Loops
- While Loops
- Loops with lists and dictionaries

## Week 7. Making your own Functions
- Defining a function
- Passing arguments
- Return values
- Positional Arguments

    ```python
    def family_info(relationship, name):
        print(f"I have a {relationship} named {name}")

    family_info("brother", "Adel")
    family_info("sister", "Hamida")

    # but position is important
    family_info("Maazin", "son")

    ```

- Keyword Arguments

    ```python
    family_info(relationship="brother", name="Adel")
    family_info(name="Hamida", relationship="sister")

    # Note that the function itself hasn't changed - just how we call it
    ```

- Default Values
    
    ```python
    def vehicle_info(color, vehicle):
        print(f"I have a {color} {vehicle}")

    vehicle_info('red', 'car')
    vehicle_info('blue', 'bicycle')


    # Let's assume most vehicles are cars

    def vehicle_info(color, vehicle):
        print(f"I have a {color} {vehicle}")


    ```
- Passing a list
- Passing an arbitrary number of Arguments
- Storing your functions in modules
- Doc strings

## Week 8. Classes
- Creating and using a class
- Working with classes and instances
- Inheritance
- Importing classes
- The Python Standard Library

## Week 9. Files and Exceptions
- Reading from a file
- Writing to a file
- Exceptions
- Storing Data

## Week 10. Introducing PyGame

## Week 11. Project Work

## Week 12. Project Work

## Week 13. Project Work

## Week 14. Project Work

## Week 15. Project Work

## Week 16. Project Work

