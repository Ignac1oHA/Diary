import datetime
now = datetime.datetime.now()
today = now.strftime("%d/%m/%y %H:%M")
print(today)

fp = open("my_diary.txt", "a")
while True:
    entry = input("What are you doing now(Type quit to exit)")
    if entry == "quit":
        break
        #\n means a new line

        fp.write(f"{today} {entry}\n")
    fp.write(entry)
fp.close()