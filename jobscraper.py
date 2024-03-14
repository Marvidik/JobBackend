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



def reverse_sentence(sentence):

    # Split the sentence into a word list
    word_list = sentence.split()

    print(word_list)

    # Reverse the word list
    reversed_word_list = list(reversed(word_list))

    print(reversed_word_list)




reverse_sentence("This is for a project in python")