import sys
import calendar
import webbrowser
from datetime import datetime

# Get the month from the command line arguments
month_name = sys.argv[1].capitalize()
month = list(calendar.month_name).index(month_name)
year = datetime.now().year

# Define the URL parts
Friday = ["https://www.ryanair.com/gb/en/trip/flights/select?adults=1&teens=0&children=0&infants=0&dateOut=", "&dateIn=&isConnectedFlight=false&isReturn=false&discount=0&promoCode=&originMac=LON&destinationIata=DUB&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&tpStartDate=", "&tpEndDate=&tpDiscount=0&tpPromoCode=&tpOriginMac=LON&tpDestinationIata=DUB"]
Sunday = ["https://www.ryanair.com/gb/en/trip/flights/select?adults=1&teens=0&children=0&infants=0&dateOut=", "&dateIn=&isConnectedFlight=false&discount=0&isReturn=false&promoCode=&originIata=DUB&destinationMac=LON&tpAdults=1&tpTeens=0&tpChildren=0&tpInfants=0&tpStartDate=", "&tpEndDate=&tpDiscount=0&tpPromoCode=&tpOriginIata=DUB&tpDestinationMac=LON"]

# Get the first and last day of the month
_, last_day = calendar.monthrange(year, month)

# Loop over all days in the month
for day in range(1, last_day + 1):
    date = datetime(year, month, day)
    # Format the date as a string
    date_str = date.strftime('%Y-%m-%d')
    
    # Check if the day is a Friday or Sunday
    if date.weekday() == 4:  # 4 is Friday
        # Generate the URL
        url = Friday[0] + date_str + Friday[1] + date_str + Friday[2]
        # Print the day of the week and the URL
        print(f'Friday: {url}')
        # Open the URL in a new tab
        webbrowser.get('firefox').open_new_tab(url)
    elif date.weekday() == 6:  # 6 is Sunday
        # Generate the URL
        url = Sunday[0] + date_str + Sunday[1] + date_str + Sunday[2]
        # Print the day of the week and the URL
        print(f'Sunday: {url}')
        # Open the URL in a new tab
        webbrowser.get('firefox').open_new_tab(url)

