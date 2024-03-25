# from bs4 import BeautifulSoup
# from requests import get


# # For Scrapping the Neccesary Jobs online

# url =get("https://weworkremotely.com/")


# soup = BeautifulSoup(url.text, 'lxml')

# # Got all the jobs in the we work remote home page
# jobs = soup.find_all('li', class_='feature')

# # looped through it to find the neccessary things we need 
# for i in jobs:
#     logo_div = soup.find('div', class_='flag-logo')

#     # Extract the value of the "style" attribute
#     style_attribute = logo_div.get('style')

#     # Parse the style attribute to get the background image URL
#     # Note: This is a simple example and assumes a specific structure of the style attribute
#     logo_url = style_attribute.split("url(")[1].split(")")[0]
#     company=i.find( "span",class_="company")
#     job_title=i.find( "span",class_="title")
#     try:
#         date=i.find( "span",class_="date")
#     except:
#         date="No Date Giving"
#     region=i.find( "span",class_="region")  



"""
The Function is invert_dict and it takes a dictionary as an argument. a dictionary with name of student as the key and a list of the 
subjects he is offering as the value. The aim of the function is to get this dictionary and invert it such that the course becomes the key 
and a list of names of students offering it becomes the value.
"""


"""
Catching can really help in file error, for example, when you try to read a file that is not in the system or the directory you 
specified we will end up getting an error which will end up crashing our programme. But with the try and except blocks we will be able to try 
that piece of code, if the file we are looking for dosnt exist it will now move to the except block which will now tell the user that the file 
is not in the system instead of crashing our entire software.
"""

#The try Block
try:
    #Specifying the files directory
    file_path = "non_existent_file.txt"
    #Trying to open the file in the file path and read it 
    with open(file_path, 'r') as file:
        content = file.read()

    #Printing out the content if the file exist
    print("File content:", content)
#Throwing out the file not found error if the file is not found 
except FileNotFoundError:
    print("Error: The specified file does not exist.")
#this is the general exception that catches all other errors.
except Exception as e:
    print("An unexpected error occurred:", str(e))
