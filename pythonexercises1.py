#Python Exercises

# 1.	Write a Python program to get the Python version you are using
# python --version #this would be executed in the terminal

# 2.	Write a Python program to display the current date and time.
import datetime #imports datetime module
now = datetime.datetime.now() #creates variable 'now' with the value of current date + time
print ("Current date and time: ") #prints description
print (now.strftime("%Y-%m-%d %H:%M:%S")) #prints date in the format of year, month, day / hour, minute, second

#3.	Write a Python program to calculate the length of a string
print("Hello, the following program will calculate the length of your word.")
string = input("What word would you like to calculate the length of? (Type in your word and press 'enter') ") #asks user for input
print("The length of '" + string + "' is " + str(len(string)) + " characters") #prints statement along with chosen word and its length

#4.	Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"] #list of items
first_and_last = [color_list[0], color_list[-1]] #0 is first item of list -1 is last item
print(first_and_last)

#5.	Write a Python program to get the volume of a sphere with radius 6.
pi = 3.1415926535897931 #the value of pi
r = 6.0 #the radius of the sphere
v = 4.0/3.0 * pi * r**3 #the formula used to calculate volume
print('The volume of the sphere with the radius of {} is:'.format(r), v)

#6.	Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {
    1:10,
    2:20
}
dic2 = {
    3:30,
    4:40
}
dic3 = {
    5:50,
    6:60
}

new_dic = {**dic1, **dic2, **dic3} #we can use **(kwargs) to pass the values of each dictionary
print(new_dic)


#7.	Write a Python function that takes a list of words and returns the longest word and the length of the longest one.
def word_function():
    print("WELCOME TO WORD MAGIK")
    print("You can use this program to list your words and find out what your longest word is, as well as the length of your longest word.")
    print("You can hit 'enter' to add further words. Hit 'q' followed by 'enter' to quit.")
    print("\nEnter some words here: ")

    words = []

    while True:
        data = input() #creates empty list where user's input will be stored and examined
        if str.lower(data) == "q": #allows the user to use both uppercase and lowercase q
            break #only breaks out of the loop if user enters Q or q
        words.append(data)

    print("\nYou wrote: ") #adds user input to the end of the list 'words'

    for i in words: #lists the words entered by user
        if i == words[-1]: #targets the users last inputted word
            print(i, end=" ") #prints the list on one line with nothing at the end of the word, the last word of the list here
        else:
            print(i, end=", ") #prints the list on one line with a comma at the end of each word apart from the last word

    longest_word = max(words, key=len) #creates a variable for the largest word in the 'words' list, this is based on the word's length

    print("\n")
    print("Your longest word is:", longest_word)
    print("The length of '" + longest_word + "' is " + str(len(longest_word)) + " characters")

word_function()
