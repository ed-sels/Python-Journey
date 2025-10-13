import requests

# Simple GET Request
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())

#Simple POST Request
new_post = {
    "title": "Learning APIs with Python",
    "body": "APIs let your Python code talk to the internet!",
    "userId": 1
}

response_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print("\nNew Post Response:")
print(response_post.json())
