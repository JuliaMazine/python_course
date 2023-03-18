import time
def something():
   time.sleep(3)

t0 = time.time()
something()
x = time.time() - t0
file = time.strftime('%H.%M.%S %d.%m.%Y') + '.txt'
with open(file, 'w', encoding='utf-8') as j:
    j.write(str(x))

