from pycbrf import ExchangeRates
from datetime import datetime
from time import sleep


t1 = datetime.now()
for i in range(50):
    print(ExchangeRates(datetime.now())["USD"].value)  # value in a moment
    # sleep(10)  # delay

print(datetime.now() - t1)
