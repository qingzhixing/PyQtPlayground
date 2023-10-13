from PyQt6.QtCore import QDateTime, Qt

dateTime = QDateTime.currentDateTime()

print("Local Date Time: ", dateTime.toString(Qt.DateFormat.ISODate))
print("Universal Date Time: ", dateTime.toUTC().toString(Qt.DateFormat.ISODate))

# 本地时间和标准时间的秒数偏移
print(f"The offset from UTC is: {dateTime.offsetFromUtc()} seconds")

print("Local Date Time: ", dateTime.toString(Qt.DateFormat.ISODate))
