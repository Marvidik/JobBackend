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

#Creating the functon that takes the original dictionary as an argument 
def invert_dict(original_dict):

    # Created an empty inverted_dict which will store the values of the new dictionary when we are done inveerting it 
    inverted_dict = {}

    # Looped though the keys and values pairs of the dictionary
    #The .items() function keeps the corresponding key and value pair in a tuple
    for student, courses in original_dict.items():
        #Looping through just the courses because it a list of courses 
        for course in courses:
            # Checking if the course has been added as a key to our inverted_dict if not it gets added with an empty list as its value 
            if course not in inverted_dict:
                inverted_dict[course] = []
            # We then add the student o the list of the course he/she is offering.
            inverted_dict[course].append(student)
    #Returns the inverted_dict
    return inverted_dict

# Sample input dictionary
original_dict = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102'],
    
}

# Print original dictionary
print("Original Dictionary:")
print(original_dict)

# Inverting the original dictionary
inverted_dict = invert_dict(original_dict)

# Print inverted dictionary
print("\nInverted Output:")
print(inverted_dict)
