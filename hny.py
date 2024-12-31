import time
from datetime import datetime, timedelta

now = datetime.now()
midnight = now.replace(hour=0, minute=0, second=0) + timedelta(days=1) 
time_to_midnight = midnight - now

time.sleep(time_to_midnight.total_seconds())
print("Happy New Year!")