from datetime import datetime

weekDays = ("月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日")

def solution_station_2(date):
    date_format = '%Y-%m-%d'
    date_obj = datetime.strptime(date, date_format)
    day = date_obj.weekday()
    dayOfWeek = weekDays[day]
    return dayOfWeek
