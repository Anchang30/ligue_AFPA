import requests

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

querystring = {"country":"France"}

headers = {
	"X-RapidAPI-Key": "75a37ef9a9msh7007ea31089e9a2p1b8d8bjsn6f08f8c5b5ed",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())