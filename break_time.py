import time
import webbrowser
total_breaks = 3
break_count = 0
print ("this start on "+time.ctime())
while (break_count < total_breaks):
    time.sleep (60)
    webbrowser.open("https://www.python.org/downloads/")
    break_count = break_count + 1
