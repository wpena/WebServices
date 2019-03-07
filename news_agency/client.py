import requests
from requests import Request, Session
import getpass
from getpass import getpass
import stdiomask
import pprint
from django.http import HttpResponse

session = requests.Session()

#--------------------------------------------------------------------------------------------------------#
## LOGIN ##
#--------------------------------------------------------------------------------------------------------#
login_url = "http://127.0.0.1:8000/api/login/"

print("Welcome to Pena's News Agency!")
def login():
    usrname = input("Please enter your username: ")
    passwrd = stdiomask.getpass("Please enter your password: ")
    res = session.post(login_url, data={'username': usrname,
                                'password': passwrd})
    if (res.status_code == 200):
        print("Status Code: " + str(res.status_code))
    print(res.text)
    if (res.status_code == 400):
        print("invalid login")

#--------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------#
    ## LOGOUT ##
#--------------------------------------------------------------------------------------------------------#
logout_url = "http://127.0.0.1:8000/api/logout/"


def logout():
    res = session.post(logout_url)
    if (res.status_code == 200):
        print("Successfully logged out. Au Revoir!")
        print("Status Code: " + str(res.status_code))

#--------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------#
        ## POST STORY ##
#--------------------------------------------------------------------------------------------------------#
post_url = "http://127.0.0.1:8000/api/poststory/"

def post():
    headline = input("Enter Headline: ")
    story_cat = input("Enter Category: ")
    story_region = input("Enter Region: ")
    story_details = input("Enter Details: ")

    res = session.post(post_url, params={'headline': headline, 'story_cat': story_cat, 'story_region': story_region, 'story_details': story_details})
    if(res.status_code == 200):
        print("Status Code: " + str(res.status_code) + " \n")
        print("Story Created \n")

#--------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------#
        ## DELETE STORY ##
#--------------------------------------------------------------------------------------------------------#

delete_url = "http://127.0.0.1:8000/api/deletestory"

# pay_load = {
#     #'id': '1',
# }

def delete():
    #res = session.post(delete_url)
    res = session.post(delete_url, params=id)
    if(res.status_code == 200):
        print("Status Code: " + str(res.status_code) + " \n")
        print("Story Deleted \n")

#--------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------#
        ## DELETE STORY ##
#--------------------------------------------------------------------------------------------------------#
list_url = "http://directory.pythonanywhere.com/api/list/"

def list_news():

    res = requests.request("GET", list_url)
    if(res.status_code == 200):
        print("Status Code: " + str(res.status_code) + " \n")
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(res.text)

#--------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------#
        ## COMMANDS ##
#--------------------------------------------------------------------------------------------------------#
def Service():
    print(""" Hello, below is a list of available service commands...
    Choices are:
    1. Login  - Type 'login' command for this service
    2. Logout - Type 'logout' command for this service
    3. Post   - Type 'post' command for this service
    4. News   - Type 'news' command for this service
    5. List   - Type 'list' command for this service
    6. Delete - Type 'delete <story_key>' command for this service
    7. Exit   - Type 'exit' command to exit
 """)


Service()

while(1):
    user_input = input("Please enter command for service you would like: ")
    print("")
    if (user_input == 'login'):
        login()
        #print("")
    if (user_input == 'logout'):
        logout()
        print("")
    if (user_input == 'post'):
        post()
        print("")
    if (user_input == 'delete' ): 
        delete()
        print("")
    if (user_input == 'list'):
        list_news()
        print("")
    if (user_input == 'exit'):
        exit()
        print("")
