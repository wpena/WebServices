import requests
from requests import Request, Session
import getpass
from getpass import getpass
import stdiomask

sesh = requests.Session()

#--------------------------------------------------------------------------------------------------------#
                                            ## LOGIN ##
#--------------------------------------------------------------------------------------------------------#
login_url = "http://127.0.0.1:8000/api/login/"

headers = {
    'authorization': "Basic Og==",
    'content-type': "application/x-www-form-urlencoded",
}

def login():
    usrname = input("Please enter your username: ")
    passwrd = stdiomask.getpass("Please enter your password: ")
    res = sesh.post(login_url, {'username': usrname,
                                'password': passwrd}, headers=headers,)
    if (res.status_code == 200):
        print("Status Code: " + str(res.status_code))
        print("Welcome to Pena's News Agency!")
    print(res.text)
    
#--------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------#
                                            ## LOGOUT ##             
#--------------------------------------------------------------------------------------------------------#
logout_url = "http://127.0.0.1:8000/api/logout/"

def logout():
    res = sesh.post(logout_url)
    if (res.status_code == 200):
        print("You have successfully logged out!")
        print("Status Code: " + str(res.status_code))


#--------------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------------#
                                            ## POST STORY ##
#--------------------------------------------------------------------------------------------------------#
post_url = "http://127.0.0.1:8000/api/poststory/"

payload = {
    'headline': 'Drake Baby Momma',
    'author': 'TestUser2',
    'story_cat': 'art',
    'story_region': 'us',
    'story_details': 'Some Unknown youT came out of nowhere.'
}

headers = {
    'authorization': "Basic Og==",
    'content-type': "application/x-www-form-urlencoded",
}

def post():
    res = sesh.post(post_url, data=payload, headers=headers)
    if(res.status_code == 200):
        print("Status Code: " + str(res.status_code) + " \n")
        print("Story Created \n")

#--------------------------------------------------------------------------------------------------------#


#--------------------------------------------------------------------------------------------------------#
                                            ## DELETE STORY ##
#--------------------------------------------------------------------------------------------------------#

# delete_url = "http://127.0.0.1:8000/api//deletestory/"

# payload = {
#     'story_key': '15'
# }

# headers = {
#     'authorization': "Basic Og==",
#     'content-type': "application/x-www-form-urlencoded",
# }

# def delete():
#     res = sesh.post(delete_url, data=payload, headers=headers)
#     if(res.status_code == 200):
#         print("Status Code: " + str(res.status_code) + " \n")
        #print("Story Deleted \n")

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
    if (user_input == 'exit'):
        exit()
        print("")

