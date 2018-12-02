from flask import Flask
import time

app = Flask('isItElevenEleven')

@app.route("/")
def display_the_time():
	utc_time = time.gmtime()

	seconds_into_current_minute = utc_time.tm_sec
	minutes_into_current_hour = utc_time.tm_min
	hours_into_current_day = utc_time.tm_hour

	html = "<div>The current UTC time is {hour}:{minute}:{second}</div>" \
	.format(hour=hours_into_current_day, minute=minutes_into_current_hour, second=seconds_into_current_minute)

	return html

app.run(host='0.0.0.0', port=80)
