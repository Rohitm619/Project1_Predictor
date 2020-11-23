from django.shortcuts import render, HttpResponse
#Importing request module for requesting web server
import urllib
import requests
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def dynamic(request):
    
    if request.method == "POST":
        
        

        p1 = request.POST['player1']
        p2 = request.POST['player2']
        p3 = request.POST['player3']
        p4 = request.POST['player4']
        p5 = request.POST['player5']
        p6 = request.POST['player6']
        p7 = request.POST['player7']
        p8 = request.POST['player8']
        p9 = request.POST['player9']
        p10 = request.POST['player10']
        p11 = request.POST['player11']

        p12 = request.POST['player12']
        p13 = request.POST['player13']
        p14 = request.POST['player14']
        p15 = request.POST['player15']
        p16 = request.POST['player16']
        p17 = request.POST['player17']
        p18 = request.POST['player18']
        p19 = request.POST['player19']
        p20 = request.POST['player20']
        p21 = request.POST['player21']
        p22 = request.POST['player22']


        country1 = {
        'p1' : p1,
        'p2' : p2,
        'p3' : p3,
        'p4' : p4,
        'p5' : p5,
        'p6' : p6,
        'p7' : p7,
        'p8' : p8,
        'p9' : p9,
        'p10' : p10,
        'p11' : p11,
        }

        country2 = {
        'p12' : p12,
        'p13' : p13,
        'p14' : p14,
        'p15' : p15,
        'p16' : p16,
        'p17' : p17,
        'p18' : p18,
        'p19' : p19,
        'p20' : p20,
        'p21' : p21,
        'p22' : p22,
        }
    
        countc1 = 0
        countc2 = 0

        for every_val_in_c1 in country1.values():
            
            urlc1= f'http://howstat.com/cricket/Statistics/Players/PlayerInnings_ODI.asp?PlayerID={every_val_in_c1}#bat'

            datac1 = requests.get(urlc1)
            html_code_c1 = datac1.content
            soupc1 = BeautifulSoup(html_code_c1, 'html.parser')

            Scraping_Valuesc1 = soupc1.findAll(class_=['TextBlackBold8','AsteriskSpaceBold'])
            Scraping_Country = soupc1.findAll(class_='Banner2')
            
            Valuesc1 = []
            Country = []

            for every_value in Scraping_Country:
                Country.append(every_value.getText(strip=True))
            
            s= str(Country[0])
            start = s.find("(")
            end = s.find(")")
            substring = s[start+1:end]

            for every_value in Scraping_Valuesc1:
                Valuesc1.append(every_value.getText(strip=True))
            countc1 = countc1 + float(Valuesc1[8])






        for every_val_in_c2 in country2.values():
            urlc2= f'http://howstat.com/cricket/Statistics/Players/PlayerInnings_ODI.asp?PlayerID={every_val_in_c2}#bat'

            datac2 = requests.get(urlc2)
            html_code_c2 = datac2.content
            soupc2 = BeautifulSoup(html_code_c2, 'html.parser')

            Scraping_Valuesc2 = soupc2.findAll(class_=['TextBlackBold8','AsteriskSpaceBold'])
            Scraping_Country_for_c2 = soupc2.findAll(class_='Banner2')

            Country_for_c2 = []
            Valuesc2 = []


            for every_value in Scraping_Country_for_c2:
                Country_for_c2.append(every_value.getText(strip=True))

            s_for_c2= str(Country_for_c2[0])
            start_for_c2 = s_for_c2.find("(")
            end_for_c2 = s_for_c2.find(")")

            substring_for_c2 = s_for_c2[start_for_c2+1:end_for_c2]

            for every_value in Scraping_Valuesc2:
                Valuesc2.append(every_value.getText(strip=True))
            countc2 = countc2 + float(Valuesc2[8])

        
        # print(substring_for_c2)


        # print(countc1)
        # print(countc2)

        grandTotalAvg = countc1 + countc2

        percentC1 = ((countc1/grandTotalAvg)*100)
        percentC2 = ((countc2/grandTotalAvg)*100)

        winning_percentage_of_countries = {
                'c1_per' : percentC1,
                'c2_per' : percentC2,
                'country1' : str(substring),
                'country2' : str(substring_for_c2),
        }

    return render(request, "dynamic.html", context=winning_percentage_of_countries)