price = 123
bonus = 23
bonus_granted = True

price -= bonus if bonus_granted else price
print(price)

rating = 5
print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')

import datetime as dt

today_weekday = dt.date.today().strftime("%A")

print("I'm helping my mum" if today_weekday == 'Monday' else
      "You are doing laundry" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "I'm on duty" if today_weekday == 'Thursday' else
      "I have two meetings" if today_weekday == 'Friday' else
      "You have lessons" if today_weekday == 'Saturday' else
      "SUNDAY WILL BE FOR US")
