print()


def say_hi(name):
    print()
    print("Hi " + name + ", I'm Pxxx Cxxxxxx")
    print()


say_hi(input("What's your name? "))

address = "Hxxxxxxxxx, XXX"
email = "cxxxxxxxxxxxxxx@protonmail.com"
mobile = "04xxxxxxxx"

know = ""
who_am_i = "Creative, Customer Focused, Solution Orientated and Passionate about Learning."
important_to_me = "Fun, Family and Work/Life Balance."
experience = "Banking, Solar Power, Businesses, Hospitality and Government."
learning = "Python Coding Language & Blockchain Technology now and NET+, SEC+ and CEH in the near future."
interested_in = "Blockchain, Help Desk, Ethical Hacking, NFT's, Software Development and Crypto Trading."
finished = ("Thank you for considering me! " + "Pxxx Cxxxxxxx - " + email + " - " + mobile)


print("Please select a number to know more... ")
print("1. Who am I?")
print("2. What's important to me?")
print("3. What experience do I have?")
print("4. What am I learning?")
print("5. What else am I interested in?")
print("0. That's all I need to know Phil.")


while know != 0:
    if know == 1:
        print(who_am_i)
    if know == 2:
        print(important_to_me)
    if know == 3:
        print(experience)
    if know == 4:
        print(learning)
    if know == 5:
        print(interested_in)
    know = input("Number... ")
print("Please only use digits 0 to 5, thanks.")




