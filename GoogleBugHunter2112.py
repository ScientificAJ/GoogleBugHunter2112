#!/usr/bin/env python3

from operator import index
from termcolor import colored

import requests
from bs4 import BeautifulSoup

import time

print(colored("""

Hi, This is a Tool for Google Dork Made By AJ.

Happy Bug Hunting!


""", 'green', attrs=['bold']))

print(colored("Please Check If The Website Has Bug Hunting Program!", attrs=['bold']))

parameter = str(input("Please Enter the Google Dork: "))

numberofpages = input("Please Enter The Number Of Pages To Scan: ")

parameter = list(parameter.split(" "))

speciouspresent = time.time()

url = "https://google.com/search?q="

start = 0

for numbers in range(int(numberofpages)):

    for i in parameter:

        url = url + i + " "

    url.replace(" ", "+")

    start = start + 5

    url = url + "?start=" + " " + str(start)

    results = requests.get(url=url)

    results = results.text

    soup = BeautifulSoup(results, "html.parser")

    links = soup.find_all("a")


    resultlinks = []


    for link in links:

        result = link.get("href")
        resultlinks.append(result)

        resultlinks[0] = ""

    linkslength = []

    for i in resultlinks:
        if "google" in i:
            i = ""
            

        i = i.replace("/url?q=", "")

        if "/search" in i:

            i = ""        
            
        i = i.split("&sa")[0]

        print(i)

        linkslength.append(i)

        with open("links.txt", "a") as file:

            file.write(i + ", ")
            file.write("\n")
    
print("Found " + str(len(linkslength)) + " " + "Links!")

calculatedtime = time.time() - speciouspresent

print("[*] Found In: " + str(calculatedtime))


    




