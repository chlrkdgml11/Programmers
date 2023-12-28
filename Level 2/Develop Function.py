import queue

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = 	[1, 1, 1, 1, 1, 1]


# progresses = [93, 30, 55]
# speeds = 	[1, 30, 5]

progresses = [1, 99]
speeds = [99, 1] 

days = []

for i in range(len(progresses)):

    p = progresses[i]
    s = speeds[i]

    day_q = (100 - p) // s
    day_r = (100 - p) % s    

    if day_r:
        days.append(day_q + 1)
    else:
        days.append(day_q)
    
print(days)


result = []
cnt = 0
temp = days[0]

for i in range(len(days)):

    try:

        if temp >= days[i+1]:
            cnt += 1
        
        else:
            cnt += 1
            result.append(cnt)
            cnt = 0
            temp = days[i+1]

    
    except:
        cnt += 1
        result.append(cnt)

print(result)


    
    


