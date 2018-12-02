from flask import Flask
import time

app = Flask('isItElevenEleven')

@app.route("/")
def is_it_eleven_eleven():
	utc_time = time.gmtime()

	minutes_into_current_hour = utc_time.tm_min
	hours_into_current_day = utc_time.tm_hour

	minutes_is_eleven = True if minutes_into_current_hour == 11 else False
	hours_is_eleven = True if hours_into_current_day == 11 or hours_into_current_day == 23 else False
	is_it_eleven_eleven = True if minutes_is_eleven and hours_is_eleven else False
	is_it_eleven_eleven_display_text = "Yes" if is_it_eleven_eleven == True else "No"

	html = "<div>The current UTC time is {hour}:{minute}</div>" \
	"<div>Is it 11:11? {yes_or_no}.</div>" \
	.format(hour=hours_into_current_day, minute=minutes_into_current_hour, yes_or_no=is_it_eleven_eleven_display_text)

	return html

app.run(host='0.0.0.0', port=80)
