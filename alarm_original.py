import datetime
import time
import winsound

# Get current date and user alarm input
current_date = datetime.datetime.now().date()
user_time = input('Input Alarm time in "HH:MM:SS" format: ')

# Handle user input
try:
    user_time = datetime.datetime.strptime(user_time, '%H:%M:%S').time()
    user_time = datetime.datetime.combine(current_date, user_time)
except ValueError:
    print('Invalid format, use "HH:MM:SS" format')
    exit()

while True:
    # Get the current times and display in terminal
    current_time = datetime.datetime.now()
    date_str = current_time.strftime('%d-%m-%y')
    time_str = current_time.strftime('%H:%M:%S')
    
    print(f'Current date: {date_str}\nCurrent time: {time_str}')    

    # Logic that makes sure the alarm goes off in time
    if current_time >= user_time:
        if current_time > user_time:
            print(f'Current time: {current_time}\nAlarm time: {user_time}')
            print(f'Alarm is set for the past, you are "{current_time - user_time}" hours, minutes, seconds LATE')
        else:
            print('Wake Up!')
        
        # Play sound and break loop
        winsound.Beep(1000, 500)
        break
    
    time.sleep(1)