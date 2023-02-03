# import random
# import requests
# from bs4 import BeautifulSoup
# import tkinter 
# from tkinter import messagebox

# # represented as arrays and strings to allow for arithmetic operations and string concat.
# uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# special_chars = ['!', '@' , '#', '$', '%', '^', '&', '*', '(', ')', '|', '+', '=', '-', '_', '~', '`', '>', '<', ':', ';', '.', ',', '?', '\'', '"', '{', '}', '[', ']', '\'']
# digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# max_length = 12

# # # hide tkinter window
# # root = tkinter.Tk()
# # root.withdraw()

# #select checkboxes
# # messagebox.showinfo("Title", "Message")
# # getpage = requests.get('http://127.0.0.1:5500/index.html?')
# # getpage_soup = BeautifulSoup(getpage.text, 'html.parser')
# # checkboxes = getpage_soup.find_all('input', {'checkbox1'})
# # print(checkboxes)
  
# # combine all characters into one array
# combined_arr = uppercase + lowercase + special_chars + digits 

# # randomly select one digit from every character type

# random_upper = random.choice(uppercase)
# random_lower = random.choice(lowercase)
# random_specialChar = random.choice(special_chars)
# randomNum = random.choice(digits)

# #password only contains 4 chars so far
# temp_pass = random_upper + random_lower + random_specialChar + randomNum


# for x in range(max_length - 4): # 0-7?
#     temp_pass = temp_pass + random.choice(combined_arr)
    
# def init():
#     password = []

# init()
        
        

