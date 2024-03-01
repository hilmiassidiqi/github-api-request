import requests

response = requests.get("https://api.github.com/repos/hilmiassidiqi/github-api-request")
result = response.json()
 
print(f"Repository id: {result['id']}\nOwner id: {result['owner']['id']}\nGit URL: {result['git_url']}")