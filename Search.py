import requests, time, json
def main(departurestation, returnstation,departuredate,returndate,outtargetprice,intargetprice):
    session = requests.session()
    session.headers = {
        'X-apikey': '0aa3d4b7e805493c8e310cfb871c4344',
        'Access-Control-Request-Method': 'GET',
        'Origin': 'https://booking.eurostar.com',
        'Referer': 'https://booking.eurostar.com/',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    url = 'https://api.prod.eurostar.com/bpa/koa/train-search/uk-en/'+departurestation+'/'+returnstation+'?outbound-date='+departuredate+'&inbound-date='+returndate+'&adult=1&booking-type=standard'
    pull = session.get(url)
    data = json.loads(pull.text)
    for i in data["outbound"]["journey"]:
        for x in i["class"]:
            try:
                if int(x["price"]["adult"]) < int(outtargetprice):
                    print("Low outbound fare found: £"+str(x["price"]["adult"]),str(i["departureTime"])+'-'+str(i["arrivalTime"])+" Stock: "+str(x["remaining"]))
                    for i in data ["inbound"]["journey"]:
                        for y in i["class"]:
                            if int(y["price"]["adult"]) < int(intargetprice):
                                print("Low inbound fare found: £"+str(y["price"]["adult"]),str(i["departureTime"])+'-'+str(i["arrivalTime"])+" Stock: "+str(y["remaining"]))
                                return True
            except:
                ()
def search(yearmonth,day,latestday,destination,departure,triplength,inlowprice,outlowprice):
    while day < latestday:
        if day < 10:
            depart = str(yearmonth+'0'+str(day))
            print(depart)
            returndate = day+triplength
            if returndate < 10:
                returndates = str(yearmonth+'0'+str(returndate))
                print(returndates)
                try:
                    success = main(departure,destination,depart,returndates,inlowprice,outlowprice)
                    day = day+1
                    if success == True:
                        input("Low fare found, press enter to continue")
                        success = False
                except:
                    print("Error, possibly no trains on this date - skipping")
                    day = day+1
            else:
                returndates = str(yearmonth+str(returndate))
                print(returndates)
                try:
                    success = main(departure,destination,depart,returndates,inlowprice,outlowprice)
                    day = day+1
                    if success == True:
                        input("Low fare found, press enter to continue")
                        success = False
                except:
                    print("Error, possibly no trains on this date - skipping")
                    day = day+1
        else:
            depart = str(yearmonth+str(day))
            print(depart)
            returndate = day+triplength
            returndates = str(yearmonth+str(returndate))
            print(returndates)
            try:
                success = main(departure,destination,depart,returndates,inlowprice,outlowprice)
                day = day+1
                if success == True:
                    input("Low fare found, press enter to continue")
                    success = False
            except:
                print("Error, possibly no trains on this date - skipping")
                day = day+1
print("Sleak's Eurostar Searcher v1.0\nStation ID Reference List...\nLondon: 1\nParis: 2\nBrussels: 3\nAmsterdam: 4")
yearmonth = input("Enter the departure year-month- i.e. 2020-02-: ")
day = input("Enter the earliest day you want to leave i.e. 1: ")
latestday = input("Enter the latest day you wish to leave i.e. 25: ")
triplength = input("Enter the length of your trip in days i.e. 5: ")
departure = input("Enter the station ID you wish to depart from: ")
destination = input("Enter the station ID you wish to return from: ")
inlowprice = input("Enter the price you want your outbound tickets to be under: ")
outlowprice = input("Enter the price you want your inbound tickets to be under: ")
station = {1:'7015400',2:'8727100',3:'8814001',4:'8400058'}
search(yearmonth,int(day),int(latestday),station[int(destination)],station[int(departure)],int(triplength),int(inlowprice),int(outlowprice))
