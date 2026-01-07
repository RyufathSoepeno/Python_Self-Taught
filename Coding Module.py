#Import Calendar

import datetime
import calendar

#In here, we are creating; Motnhly progress, Weekly progress


balance = 5000
interest_rate = 0.13
monthly_payment = 500

today = datetime.date.today()

#To set up the first day, you need to set the days in each month
#datetime.date.today() is one of the examples of a module code
#Today follows month, since this is written in December, it is 31
#Do mind that not all imports have two programs 
#Import_Name.Program_Type.Program
#Or Import_Name.Porgram

days_in_current_month = calendar.monthrange(today.year, today.month)
print(days_in_current_month)

days_in_current_month = calendar.monthrange(today.year, today.month)[1]
print(days_in_current_month)

days_till_end_month = days_in_current_month - today.day
#Shows how many days are due
print(days_till_end_month)

start_date = today + datetime.timedelta(days = days_till_end_month + 1)
#We give +1 to make sure the code works based on maths
#timedelta(days=output)
#Before the output it was 2021-01-01; because it is nearest start date from december
print(start_date)

end_date = start_date

while balance > 0:
    interest_charge = (interest_rate/ 12) * balance
    balance += interest_charge
    balance -= monthly_payment
    balance = round(balance, 2)#round(variable, d.p.)
    if balance < 0 :
        balance = 0 #Tell that the money is all out
        #Or you could try
    print(end_date, balance)



import datetime

current_weight = 80 #In KG
goal_weight = 65
avg_lost_week = 0.8

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight :
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lost_week

b = end_date - start_date
print("reached goal in", b.days // 7, "weeks")
#// = Floor Division (Divivding without rounding and including remainder)
