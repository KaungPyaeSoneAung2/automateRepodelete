import requests

#The Token should have Repo & delete_repo permission
GITHUB_TOKEN = 'add_your_github_token_here'
#In repos_to_upadte.txt file, set a list of your repos you want to change to private
# Format -> userName/repoName
REPOS_FILE = 'repos_to_update.txt' 
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def make_repo_private(repo):
    """Changes the given repository to private."""
    url = f"https://api.github.com/repos/{repo}"
    data = {"private": True}
    response = requests.patch(url, headers=HEADERS, json=data)
    
    if response.status_code == 200:
        print(f"Successfully made {repo} private.")
    elif response.status_code == 404:
        print(f"Repository {repo} not found.")
    else:
        print(f"Failed to make {repo} private: {response.json()}")

def main():
    with open(REPOS_FILE, 'r') as file:
        repos = file.read().splitlines()
        for repo in repos:
            make_repo_private(repo)

if __name__ == "__main__":
    main()
