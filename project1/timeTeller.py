from datetime import datetime
#import for timezones
import pytz

# this is to save repeated code - formats the time in 24hrs
formatTime = "%H:%M:%S"

# the time in LA
laTime = pytz.timezone('America/Los_Angeles')
laTimeOutput = datetime.now(laTime)
print("LA time(western): ", laTimeOutput.strftime(formatTime))


# the time in london
londonTime = pytz.timezone('Europe/London')
londonTimeOutput = datetime.now(londonTime)
print("London time: ", londonTimeOutput.strftime(formatTime))

# the time in tokyo
tokyoTime = pytz.timezone('Asia/Tokyo')
tokyoTimeOutput = datetime.now(tokyoTime)
print("Tokyo Time: ", tokyoTimeOutput.strftime(formatTime))

#The current time
currentTime = datetime.now()
print("It is currently(12 hour clock): ", currentTime.strftime('%I:%M:%S'))
print("It is currently(24 hour clock): ", currentTime.strftime(formatTime))