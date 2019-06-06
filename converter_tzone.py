import datetime
import pytz


def gt(dt_str):
    dt1 = str(dt_str[:10])
    dt2 = str(dt_str[11:19])
    new_date = dt1 + ' ' + dt2

    utc = pytz.utc
    fmt = '%Y-%m-%d %H:%M:%S'
    moscow = pytz.timezone('Etc/GMT+3')  # 'Etc/GMT+3'
    new_dt = datetime.datetime.strptime(str(new_date), fmt)

    am_dt = moscow.localize(new_dt)
    return am_dt.astimezone(utc).strftime(fmt)


date = '2019-05-29T17:12:51.704977500Z'
print(gt(date))




