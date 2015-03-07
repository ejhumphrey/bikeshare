import csv
import numpy
import time

TIME_FMT = "%Y-%m-%d %H:%M:%S"


def load_data(csv_file):
    pass


def parse_timestamp(timestamp):
    tstruct = time.strptime(timestamp, TIME_FMT)
    clock = tstruct.tm_sec + tstruct.tm_min * 60 + tstruct.tm_hour * 3600
    return dict(weekday=tstruct.tm_wday,
                month=tstruct.tm_mon,
                day=tstruct.tm_mday,
                year=tstruct.tm_year,
                clock=clock)
