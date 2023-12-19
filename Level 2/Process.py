import queue

process_q = queue.Queue()
chr_q = queue.Queue()

priority = [5, 4, 3, 2, 1]
location = 0
l = len(priority)
priority_chr = []
result = []
for i in range(len(priority)):
    priority_chr.append(chr(i + 65))

while(len(priority) > 0):
    print('priority = ', priority)
    print('priority_chr = ', priority_chr)
    
    if priority[0] != max(priority):
        print('result X')

        process_q.put(priority[0])
        chr_q.put(priority_chr[0])

        del priority[0]
        del priority_chr[0]

    
    else:
        print('result O')
        result.append(priority_chr[0])

        del priority[0]
        del priority_chr[0]
    

    print('result = ', result)
    print('')

while(len(result) != l):
    result.append(chr_q.get())

print(result)
print(result.index(chr(65 + location)) + 1)


