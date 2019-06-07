import datetime
import pytz
import configparser


def converter_tz(dt_str):
    config = configparser.ConfigParser()
    config.read('xmlparser.cfg')
    local_time_zone = config['TimeZone']['LocalTimeZone']

    dt1 = str(dt_str[:10])
    dt2 = str(dt_str[11:19])
    new_date = dt1 + ' ' + dt2

    utc = pytz.utc
    fmt = '%Y-%m-%d %H:%M:%S'
    moscow = pytz.timezone(str(local_time_zone))  # 'Etc/GMT+3'
    new_dt = datetime.datetime.strptime(str(new_date), fmt)

    am_dt = moscow.localize(new_dt)
    with open('XMLParserWS.log', 'a') as f:
        f.write(am_dt.astimezone(utc).strftime(fmt)+'\n')
    return am_dt.astimezone(utc).strftime(fmt)


date = '2019-05-29T17:12:51.704977500Z'
print(converter_tz(date))





