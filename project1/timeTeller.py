from datetime import datetime
import pytz


formatTime = "%H:%M:%S"

laTime = pytz.timezone('America/Los_Angeles')
laTimeOutput = datetime.now(laTime)
print("LA time(western): ", laTimeOutput.strftime(formatTime))



londonTime = pytz.timezone('Europe/London')
londonTimeOutput = datetime.now(londonTime)
print("London time: ", londonTimeOutput.strftime(formatTime))


tokyoTime = pytz.timezone('Asia/Tokyo')
tokyoTimeOutput = datetime.now(tokyoTime)
print("Tokyo Time: ", tokyoTimeOutput.strftime(formatTime))

currentTime = datetime.now()
print("It is currently(12 hour clock): ", currentTime.strftime('%I:%M:%S'))
print("It is currently(24 hour clock): ", currentTime.strftime('%H:%M:%S'))