import datetime

"""
    utc time
"""

current_date_time = datetime.datetime.utcnow()
print(current_date_time)

"""
    asian time
"""
current_date_time = datetime.datetime.now()
print(current_date_time)

from dateutil.relativedelta import relativedelta

"""
    relativedelta
"""
current_date_time += relativedelta(days=30)
print(current_date_time)

current_date_time -= relativedelta(years=1)
print(current_date_time)

""" 
    timedelta
"""

from datetime import timedelta

current_date_time -= timedelta(days=20)
print(current_date_time)
