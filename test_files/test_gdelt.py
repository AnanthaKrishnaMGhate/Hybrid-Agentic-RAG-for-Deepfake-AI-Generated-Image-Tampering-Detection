import requests

query = "Artificial Intelligence"

url = (
    "https://api.gdeltproject.org/api/v2/doc/doc"
    f"?query={query}"
    "&mode=ArtList"
    "&maxrecords=5"
    "&format=json"
)

response = requests.get(url)

print("Status:", response.status_code)
print(response.text[:1000])