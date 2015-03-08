"""

Data Fields
-----------
datetime - hourly date + timestamp
season -  1 = spring, 2 = summer, 3 = fall, 4 = winter
holiday - whether the day is considered a holiday
workingday - whether the day is neither a weekend nor holiday
weather - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
          2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
          3: Light Snow, Light Rain + Thunderstorm + Scattered clouds,
             Light Rain + Scattered clouds
          4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
temp - temperature in Celsius
atemp - "feels like" temperature in Celsius
humidity - relative humidity
windspeed - wind speed
casual - number of non-registered user rentals initiated
registered - number of registered user rentals initiated
count

"""

import csv
import numpy as np
import time

TIME_FMT = "%Y-%m-%d %H:%M:%S"
FIELDS = ['datetime', 'season', 'holiday', 'workingday', 'weather', 'temp',
          'atemp', 'humidity', 'windspeed', 'casual', 'registered', 'count']
DATEFIELDS = ["year", "month", "day", "hour"]


def load_train_data(filename):
    reader = csv.reader(open(filename))
    data, rentals = [], []
    next(reader)
    for row in reader:
        timedata = parse_timestamp(row[0])
        data.append([timedata[key] for key in DATEFIELDS] + list(row[1:-3]))
        rentals.append(row[-3:-1])

    return np.asarray(data, dtype=float), np.asarray(rentals, dtype=float)


def load_test_data(filename):
    reader = csv.reader(open(filename))
    data = []
    next(reader)
    for row in reader:
        timedata = parse_timestamp(row[0])
        data.append([timedata[key] for key in DATEFIELDS] + list(row[1:]))

    return np.asarray(data, dtype=float)


def parse_timestamp(timestamp):
    tstruct = time.strptime(timestamp, TIME_FMT)
    return dict(month=tstruct.tm_mon,
                day=tstruct.tm_mday,
                year=tstruct.tm_year,
                # weekday=tstruct.tm_wday,
                hour=tstruct.tm_hour)
