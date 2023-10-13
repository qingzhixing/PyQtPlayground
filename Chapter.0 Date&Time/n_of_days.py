from PyQt6.QtCore import QDate

day = QDate(1945, 5, 7)

print(f"Days in month: {day.daysInMonth()}")
print(f"Days in year: {day.daysInYear()}")
