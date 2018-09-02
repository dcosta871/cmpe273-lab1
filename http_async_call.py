import requests
from threading import Thread

def perform_request():
    r = requests.get('https://webhook.site/d203b4fe-971b-471d-80e7-d388da4f62fc')
    with open("output.txt", "a+") as myfile:
        myfile.write(r.headers['Date'] + '\n')

with open("output.txt", "a+") as myfile:
    myfile.write('async calls\n')
    for x in range(3):
        Thread(target=perform_request).start()
    myfile.write('initiated requests\n')