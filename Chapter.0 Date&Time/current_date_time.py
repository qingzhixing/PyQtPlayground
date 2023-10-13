from PyQt6.QtCore import QDate, QTime, QDateTime, Qt

nowDate = QDate.currentDate()

print("ISODate: ", nowDate.toString(Qt.DateFormat.ISODate))
print("RFC2822Date: ", nowDate.toString(Qt.DateFormat.RFC2822Date))

dateTime = QDateTime.currentDateTime()

print("Date Time: ", dateTime.toString())

time = QTime.currentTime()

print("Time: ", time.toString(Qt.DateFormat.ISODate))
