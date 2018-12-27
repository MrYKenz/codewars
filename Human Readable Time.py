def time(n):
    if n > 0 and n < 360000:
        hours = n // 3600
        mins = (n % 3600) // 60
        secs = (n % 3600) % 60
        # return 'hr:' + str(hours) + ' m:' + str(mins) + ' s:' + str(secs)
        return '{:02d}:{:02d}:{:02d}'.format(hours,mins,secs)
    else:
        return '00:00:00'



print(time(7350))
