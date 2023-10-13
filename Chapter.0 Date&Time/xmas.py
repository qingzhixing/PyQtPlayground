from PyQt6.QtCore import QDate, Qt
now = QDate.currentDate()
y = now.year()

print(f"today is {now.toString(Qt.DateFormat.ISODate)}")

xmas1 = QDate(y-1, 12, 25)
xmas2 = QDate(y, 12, 25)

daysPassed = xmas1.daysTo(now)
print(f"{daysPassed} days have passed since last XMas")

nextOfDays = now.daysTo(xmas2)
print(f"There are {nextOfDays} days until next XMas")
