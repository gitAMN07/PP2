from datetime import datetime

current_datetime = datetime.now()
without_microseconds = current_datetime.replace(microsecond=0)

print("Original Datetime:", current_datetime)
print("Without Microseconds:", without_microseconds)