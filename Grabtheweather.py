#Grab the current Date, Temperature, Condition and Wind speed and direction
#From enivroment canada website

from bs4 import BeautifulSoup
import requests


while True:
    print("Please select the city of interest\n")
    print("1-Toronto, ON")
    print("2-Vaughan, ON")
    print("3-Montreal, QC")
    print("4-Calgary, AB")
    print("5-Vancouver, BC")
    print("6-Exit Program")

    while True:
        try:
            option = int(input("Please choose a number from 1-5\n"))
        except ValueError:
            print("Sorry I did not understand that")
            continue
        if option > 6:
            print("Sorry your Value must be less than 6")
            continue
        else:
            break

    url = ['https://weather.gc.ca/city/pages/on-143_metric_e.html','https://weather.gc.ca/city/pages/on-64_metric_e.html','https://weather.gc.ca/city/pages/qc-147_metric_e.html','https://weather.gc.ca/city/pages/ab-52_metric_e.html','https://weather.gc.ca/city/pages/bc-74_metric_e.html']

    if option == 1:
        source = requests.get(url[0]).text
    elif option == 2:
        source = requests.get(url[1]).text
    elif option == 3:
        source = requests.get(url[2]).text
    elif option == 4:
        source = requests.get(url[3]).text
    elif option == 5:
        source = requests.get(url[4]).text
    elif option == 6:
        exit()


    soup = BeautifulSoup(source, 'lxml')
    article = soup.find('main').find('section').find('details').find('div')
    stats = list()
    for information in article.find_all('dd',class_='mrgn-bttm-0'):
        temp = information.text
        stats.append(temp)

    print("Location:",stats[0])
    print('Time and Date:',stats[1])
    print("Conditions:",stats[2])
    print("Temperature:",stats[6].rstrip())
    print("Humidity:",stats[10])
    print("Wind:",stats[11].strip(),'\n')
