#  love calculator: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

#  2. Then check for the number of times the letters in the word LOVE occurs.   

#  3. Then combine these numbers to make a 2 digit number and print it out. 

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    user1 = input("please type in your love test sentence, user1.")
    user2 = input("please type in your love test sentence, user2.")
    print("we will now calculate how many times have you two used the golden words (L, O, V, E\n then we will write them down for you two.")
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    second_digit = l + o + v + e
    score = str(second_digit)
    print(f"your combined scores is: {score}")
calculate_love_score("carlos", "valentino")

# my love for her is inevitable, she is the one, the one from my dreams, i freaking love her soo much.
# he is the kindest, richest, most beautiful person in the world to me, I love him from the bottom of my heart.