import requests


# GitHub Access Token and file with repo list
GITHUB_TOKEN = 'add_your_github_token_here'
#In repos_to_delete.txt file, set a list of your repos you want to delete
# Format -> userName/repoName
REPOS_FILE = 'repos_to_delete.txt'
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def delete_repo(repo):
    """Deletes a given repository on GitHub."""
    url = f"https://api.github.com/repos/{repo}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Successfully deleted {repo}")
    else:
        print(f"Failed to delete {repo}: {response.json()}")

def main():
    with open(REPOS_FILE, 'r') as file:
        repos = file.read().splitlines()
        for repo in repos:
            delete_repo(repo)

if __name__ == "__main__":
    main()
