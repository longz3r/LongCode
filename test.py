from win32api import GetSystemMetrics

print("Width =", type(GetSystemMetrics(0)))
print("Height =", GetSystemMetrics(1))