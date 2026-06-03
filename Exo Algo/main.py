
# reverse string

def reverse_string(string):
    return string[::-1]

print(reverse_string("hello"))
print('#####################')

# count vowels
def count_vowels(string):
    vowel = "aeiouy"
    count = 0
    for i in string:
        if i in vowel: 
            count += 1
    return count

print(count_vowels("bonjour"))
print('#####################')

#  palindrome
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("radar"))
print(is_palindrome("python"))
print('#####################')


#  Find Max
def find_max(list_number):
    maximum = 0
    for i in list_number:
        if i > maximum:
            maximum = i

    return maximum

print(find_max([3, 8, 2, 15, 4]))
print('#####################')


# count occurences
def count_occurrences(list_number, value):
    count_value = 0
    for i in list_number:
        if i == value:
            count_value += 1

    return count_value

print(count_occurrences([1, 2, 3, 2, 2, 4], 2))
print('#####################')


# FizzBuzz
# def fizz_buzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
    
# fizz_buzz()
# print('#####################')


def valid_parentheses(string):
    pile = ['0']
    for i in string:
        if i == ')' and pile[-1] == '(':
            pile = pile[:-1]
        elif i == ']' and pile[-1] == '[':
            pile = pile[:-1]
        elif i == '}' and pile[-1] == '{':
            pile = pile[:-1]
        else:
            pile.append(i)
    
    if pile == ['0']:
        return True
    else:
        return False

print(valid_parentheses("()[]{}"))
print(valid_parentheses("([)]"))
print(valid_parentheses("{[]}"))
print('#####################')

# Find Duplicates
def find_duplicates(list_numbers):
    list_duplicate = []
    while len(list_numbers) > 0: 
        num = list_numbers.pop()
        if num in list_numbers:
            list_duplicate.append(num)

    return list_duplicate


print(find_duplicates([1, 2, 3, 2, 5, 1]))
print('#####################')


def longest_word(string):
    list_words = string.split(' ')
    longest_word = ''
    for word in list_words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

print(longest_word("bonjour je suis davit"))
print('#####################')



def two_sum(numbers, target):
    indexes = []
    for index, i in enumerate(numbers):
        if target-i in numbers:
            indexes.append(index)
            index_2 = numbers.index(target-i)
            indexes.append(index_2)
            break

    return indexes[0], indexes[1]


def two_sum(numbers, target):
    indexes = {}
    for index, i in enumerate(numbers):
        if target-i in indexes:
            return (indexes[target-i], i)
        indexes[target-i] = i


print(two_sum([2, 7, 11, 15], 9))



