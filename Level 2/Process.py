import queue
import random

process_q = queue.Queue()
chr_q = queue.Queue()

priority = [1,1,9,1,1,1]
location = 0

priority_chr = []
for i in range(len(priority)):
    priority_chr.append(chr(i + 65))

for p in priority:
    process_q.put(p)

for pc in priority_chr:
    chr_q.put(pc)

result = []
l = len(priority)

while(len(result) != l):
    M = max(priority)

    process_temp = process_q.get()
    chr_temp = chr_q.get()

    if process_temp == M:
        result.append(chr_temp)
        priority.remove(process_temp)
    
    else:
        process_q.put(process_temp)
        chr_q.put(chr_temp)

print(result)
print(result.index(chr(65 + location)) + 1)






