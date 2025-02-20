from datetime import datetime

print(datetime.now().second)
print(datetime.now().second + 2)

wait_until = datetime.now().second + 2
while datetime.now().second < wait_until:
    pass #print("wainting...")
print("done")

while True:
    if datetime.now().second >= wait_until:
        print("wait 2 seconds")
        break
print("done")

while True:
    if datetime.now().second < wait_until:
        continue
    break
        