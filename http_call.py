import requests

with open("output.txt", "a+") as myfile:
    myfile.write('sync calls\n')
    for x in range(3):
        r = requests.get('https://webhook.site/d203b4fe-971b-471d-80e7-d388da4f62fc')
        myfile.write(r.headers['Date'] + '\n')
    myfile.write('\n')
