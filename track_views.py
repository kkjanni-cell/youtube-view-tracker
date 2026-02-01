import requests
import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

API_KEY = os.environ["YOUTUBE_API_KEY"]
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
time_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S")

file_exists = os.path.isfile("views.csv")

with open("views.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["time_utc", "views"])
    writer.writerow([time_now, views])

print(time_now, views)
