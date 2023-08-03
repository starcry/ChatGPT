import calendar
import sys
import requests
import json
import os

class WeekendDates:
    def __init__(self, month_name):
        self.month_name = month_name.lower()
        self.month = self.month_to_number()
        self.now = calendar.datetime.datetime.now()
        self.year = self.get_year()

    def month_to_number(self):
        months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        return months.index(self.month_name) + 1

    def get_year(self):
        current_year = self.now.year
        current_month = self.now.month
        if self.month <= current_month:
            current_year += 1
        return current_year

    def get_weekend_dates(self):
        cal = calendar.monthcalendar(self.year, self.month)
        dates = []
        for week in cal:
            friday = week[4]
            sunday = week[6]
            if friday == 0:
                if self.month == 1:
                    self.year -= 1
                    self.month = 12
                else:
                    self.month -= 1
                friday = calendar.monthrange(self.year, self.month)[1]
            if sunday == 0:
                if self.month == 12:
                    self.year += 1
                    self.month = 1
                else:
                    self.month += 1
                sunday = 1
            friday_date = f"{self.year}-{self.month:02d}-{friday:02d}"
            sunday_date = f"{self.year}-{self.month:02d}-{sunday:02d}"
            dates.append([friday_date, sunday_date])
        return dates

    def get_flights(self, dates):
        base_url = "http://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/"
        api_key = os.getenv('SKYAPI')
        for date_pair in dates:
            params = {
                "country": "UK",
                "currency": "GBP",
                "locale": "en-GB",
                "originPlace": "LON",
                "destinationPlace": "anywhere",
                "outboundPartialDate": date_pair[0],
                "inboundPartialDate": date_pair[1],
                "apiKey": api_key
            }
            response = requests.get(base_url, params=params)
            data = json.loads(response.text)
            print(json.dumps(data, indent=4))

if len(sys.argv) < 2:
    print("Please provide a month as a command line argument.")
    sys.exit(1)

weekend_dates = WeekendDates(sys.argv[1])
dates = weekend_dates.get_weekend_dates()
weekend_dates.get_flights(dates)

