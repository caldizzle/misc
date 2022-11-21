
import datetime
import time
import sys

url = "https://docs.google.com/forms/d/e/1FAIpQLScuhu3XFlmJ4mZKb0Un1HGCpokn7N-u9yDtvAxcgCYov4dacQ/formResponse"

values = {
    "entry.661356196": "uncle fatty"
}

for d in values:

    try:
        requests.post(url, data=d)
        print("Form Submitted.")
        time.sleep(5)
    except:
        print("Error Occured!")
