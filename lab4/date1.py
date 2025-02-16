from datetime import datetime, timedelta
c_date = datetime.today()

new_date = c_date - timedelta(days=5)

print("Date:", c_date.strftime("%Y-%m-%d"))
print("After subtracting 5 days:", new_date.strftime("%Y-%m-%d"))
