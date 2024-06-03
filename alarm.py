import datetime
import time
import winsound
from tkinter import *
import threading

alarm_thread = None

# Function that checks the current time against the alarm time
def alarm_clock(timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        time_now = current_time.strftime('%H:%M:%S')
        date_now = current_time.strftime('%d/%m/%y')
        print('Current Date:', date_now, time_now)
        
        if time_now >= timer:
            print('Wake Up!')
            winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
            break

# Function uses threads to not block the tkinter functionalities 
# Also gives alarm_clock function the user alarm input
def set_alarm():
    global alarm_thread
    
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    print(f'Set alarm for: {set_alarm_timer}')

    if alarm_thread is not None and alarm_thread.is_alive():
        print('An alarm is already set')
        return
    
    alarm_thread = threading.Thread(target=alarm_clock, args=(set_alarm_timer,))
    alarm_thread.start()
    get_user_input.config(state=DISABLED)

# Updates with current time on the GUI
def update_time():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    current_time_label.config(text=f'Current Time: {current_time}')
    clock_ui.after(1000, update_time)
    
    
clock_ui = Tk()

clock_ui.title('Alarm Clock')
clock_ui.geometry('400x200')

user_info = Label(clock_ui, text='Enter time in displayed format', fg='red', bg='black', font='Arial')
user_info.place(x=100, y=100)
add_time = Label(clock_ui, text='Hour / Minute / Second', font=60)
add_time.place(x=125)
user_alarm = Label(clock_ui, text='When should the alarm\n go off?', fg='blue', relief='solid', font=('Ariel', 7, 'bold'))
user_alarm.place(x=0, y=30)


hour = StringVar()
min = StringVar()
sec = StringVar()

hour_time = Entry(clock_ui, textvariable=hour, bg='orange', width=15)
hour_time.place(x=120, y=30)
minute_time = Entry(clock_ui, textvariable=min, bg='orange', width=15)
minute_time.place(x=170, y=30)
second_time = Entry(clock_ui, textvariable=sec, bg='orange', width=15)
second_time.place(x=220, y=30)

current_time_label = Label(clock_ui, text='', fg='black', font=('Ariel', 10, 'bold'))
current_time_label.place(x=10, y=180)

get_user_input = Button(clock_ui, text='Set Alarm', fg='red', width=10, command=set_alarm)
get_user_input.place(x=110, y=70)

update_time()

clock_ui.mainloop()