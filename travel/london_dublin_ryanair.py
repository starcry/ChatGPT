import sys
import calendar
from datetime import datetime

# Get the month from the command line arguments
month_name = sys.argv[1].capitalize()
month = list(calendar.month_name).index(month_name)
year = datetime.now().year

# Define the URL parts
urlStart = "https://www.ryanair.com/gb/en/trip/flights/select?adults=1&teens=0&children=0&infants=0&dateOut="
urlMid = "&dateIn=&isConnectedFlight=false&isReturn=false&discount=0&promoCode=&originMac=LON&destinationIata=DUB&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&tpStartDate="
urlEnd = "&tpEndDate=&tpDiscount=0&tpPromoCode=&tpOriginMac=LON&tpDestinationIata=DUB"

# Get the first and last day of the month
_, last_day = calendar.monthrange(year, month)

# Loop over all days in the month
for day in range(1, last_day + 1):
    date = datetime(year, month, day)
    # Check if the day is a Friday or Sunday
    if date.weekday() in [4, 6]:  # 4 is Friday, 6 is Sunday
        # Format the date as a string
        date_str = date.strftime('%Y-%m-%d')
        # Generate the URL
        url = urlStart + date_str + urlMid+ date_str + urlEnd
        # Print the day of the week and the URL
        print(f'{calendar.day_name[date.weekday()]}: {url}')

