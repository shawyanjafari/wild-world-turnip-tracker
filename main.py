import datetime
import numpy as np
import datetime as dt

today = dt.date.today().weekday()
csv_headers = 'date,morning_price,afternoon_price'
input_accepted = False

# if file exists, record turnip prices for the day
with open('turnip_prices.csv', 'a+') as f:
    if today == 6:  # turnips can't be sold on Sundays
        f.write(f'{datetime.date.today()},{np.nan},{np.nan}\n')
    else:
        while not input_accepted:
            try:
                morning_turnip_prices = int(input('Please enter morning turnip prices: '))
                afternoon_turnip_prices = int(input('Please enter afternoon turnip prices: '))
                input_accepted = True
                f.write(f'{datetime.date.today()},{morning_turnip_prices},{afternoon_turnip_prices}\n')
            except ValueError:
                print("You must enter a number!")
