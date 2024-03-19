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


Grade = [5,4,4] #grades where A is 5 b is 4 and c is 3
Unit_point = [4,5,6] #unit of the course 
zipped = list(zip(Grade, Unit_point))  #list of tuples with the A and B lists elements
print('zipped = ',zipped)
print('Type of zipped elements is ',type(zipped[1]))
sum_of_cumm=0
for a,b in zipped: #llop over the both grades and unit point and multiply them  together
    sum_of_cumm+=(a*b)

print(sum_of_cumm)