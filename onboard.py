import urllib.request
import json

CONFIG = {
    "token": "ghp_D2ja9vl3gRK6Zwt3HUAhlsn60zOBG639jVj",
    "owner": "Gpowerluv",
    "repo": "tactical-mobile-game"
}

def onboard_developer(applicant_username):
    url = f"https://api.github.com/repos/{CONFIG["owner"]}/{CONFIG["repo"]}/collaborators/{applicant_username}"
    headers = {
        "Authorization": f"Bearer {CONFIG["token"]}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json"
    }
    data = json.dumps({"permission": "push"}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Success! Status: {response.status}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    onboard_developer("testuser")
