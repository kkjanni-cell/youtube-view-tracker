import requests
import csv
import os
from datetime import datetime

API_KEY = os.environ["AIzaSyCTaF_DFd6q1x99yllqXC4twYd6KB13XfU"]
VIDEO_ID = "PltUK8r4sjw"

URL = "https://www.googleapis.com/youtube/v3/videos"

params = {
    "part": "statistics",
    "id": VIDEO_ID,
    "key": API_KEY
}

response = requests.get(URL, params=params)
data = response.json()

views = data["items"][0]["statistics"]["viewCount"]
time_now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

file_exists = os.path.isfile("views.csv")

with open("views.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["time_utc", "views"])
    writer.writerow([time_now, views])

print(time_now, views)
