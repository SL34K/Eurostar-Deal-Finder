# Eurostar Deal Finder
A simple program I created in 2019 to look for cheap Eurostar deals.
This uses the EuroStar API (I located this by sniffing the web requests when getting quotes for trips) to look for a specific deal (example below).

# Example
You and your friends want to go for a 5 day trip from London to Paris sometime in March of 2021 (2021-01-) and want to find tickets under £50 you would enter the following (£30 per ticket is the lowest possible rate between London and Paris currently I believe).
```
Sleak's Eurostar Searcher v1.0
Station ID Reference List...
London: 1
Paris: 2
Brussels: 3
Amsterdam: 4
Enter the departure year-month- i.e. 2020-02-: 2021-03-
Enter the earliest day you want to leave i.e. 1: 1
Enter the latest day you wish to leave i.e. 25: 31
Enter the length of your trip in days i.e. 5: 5
Enter the station ID you wish to depart from: 1
Enter the station ID you wish to return from: 2
Enter the price you want your outbound tickets to be under: 50
Enter the price you want your inbound tickets to be under: 50
2021-03-01
2021-03-06
Low outbound fare found: £44.5 05:40-09:17 Stock: 87
Low inbound fare found: £44.5 07:03-08:32 Stock: 203
Low fare found, press enter to continue
```
If you press enter to continue it will continue searching
```
2021-03-02
2021-03-07
Low outbound fare found: £44.5 05:40-09:17 Stock: 116
Low inbound fare found: £44.5 08:03-09:30 Stock: 101
Low fare found, press enter to continue
```
Hopefully this all makes sense, I haven't edited this code since I put it together to use in early 2019 but I have tested it today and it still works

# Dependencies
Requests
