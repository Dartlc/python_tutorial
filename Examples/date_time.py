import datetime

from dateutil.relativedelta import relativedelta

current_date = datetime.datetime.now()
print(current_date)

past_date = current_date - relativedelta(days=10)
print(past_date)

future_date = datetime.datetime.now() + relativedelta(days=10)
print(future_date)
