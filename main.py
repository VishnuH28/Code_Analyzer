import requests
import openai

github_token = 'YOUR_GITHUB_TOKEN'
github_api_url = 'GITHUB_API_URL'
openai.api_key = 'YOUR_OPENAI_SECRETKEY'

def make_sample_request():
    url = f'{github_api_url}/user'
    headers = {'Authorization': f'token {github_token}'}

    response = requests.get(url, headers=headers) 

    if response.status_code == 200:
        user_data = response.json()
        print(f"Authenticated as {user_data['login']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

def get_repository_info(owner, repo):
    url = f'{github_api_url}/repos/{owner}/{repo}'
    headers = {'Authorization': f'token {github_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repo_info = response.json()
        print(f"Repository Name: {repo_info['name']}")
        print(f"Description: {repo_info['description']}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

def analyze_code_with_chatgpt(code_snippet):
    prompt = f"Analyzing the following code:\n\n{code_snippet}\n\nSuggestions:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    suggestions = response['choices'][0]['message']['content'].strip()

    with open("code_analysis_results.txt", "w") as file:
        file.write(f"Suggestions for Code Improvement:\n{suggestions}")

    print(f"Suggestions for Code Improvement:\n{suggestions}")

if __name__ == "__main__":
    make_sample_request()  
    get_repository_info('VishnuH28', 'collegeManagement')
    code_snippet = """
def calculate_square(n):
    return n * n
result = calculate_square(5)
print(result)
"""
    analyze_code_with_chatgpt(code_snippet)