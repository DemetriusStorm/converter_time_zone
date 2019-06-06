import datetime


def from_utc(utctime, fmt="%Y-%m-%dT%H:%M:%S.%fZ"):
    """
    Convert UTC time string to time.struct_time
    """
    # change datetime.datetime to time, return time.struct_time type
    return datetime.datetime.strptime(utctime, fmt)


date = '2019-05-29 10:41:54.977500'
print(from_utc(date))

