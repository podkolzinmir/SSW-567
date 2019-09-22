import requests
import json

def GithubApi(username):
    response = requests.get("https://api.github.com/users/"+username+"/repos")
    
    if response.status_code != 403:
        print("No Account with that Username")
        return False

    response = json.loads(response.content)

    if len(response) <= 0:
        print("No Repositories")
        return False
  
    for repo in response:
        repoResponse = requests.get(repo['commits_url'].split("{")[0])
        repoResponse = json.loads(repoResponse.content)
        print("Repository Name: "+ repo['name'] + " \t\t\t\tNumber Of Commits: " + str(len(repoResponse)))
   
    return True

if __name__ == "__main__":
    userInput = input("Enter Github Username: ")
    GithubApi(userInput)