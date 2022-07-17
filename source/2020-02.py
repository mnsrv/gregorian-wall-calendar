# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import calendar
import math

# [W]IDTH, [H]EIGHT, [M]ARGIN, [F]FONT-SIZE
# Note: 1 inch = 72 units
# A4: 210 x 297
# Inches: 8.268 x 11.693
# Units: 595,296 x 841,896
W,H,M,F = 594,789,24,78
fix_header = 24
fix_grid = 4

cal= calendar.Calendar()
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = 12
year = 2022

# GRID
def grid():
    lineJoin("round")
    stroke(0.8)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = 78, 78
    for x in range(8):
        polygon(((M)+stpX, M),
                ((M)+stpX, (H-(F*2))-(M+((F/4)*2))))
        stpX += incX
    for y in range(8):
        polygon((M, (M)+stpY),
                (W-(M), (M)+stpY))
        stpY += incY

# MAIN
size("A4")
grid() # Toggle for grid view
stroke(None)

fontSize(F)
font("Inter-ExtraBold")
text(months[month - 1], (M-4, fix_header+M+(F*8)))
tracking(-4)
text(str(year), (M-4, fix_header+M+(F*7)))

fontSize(F/4)
font("Inter-Regular")
tracking(None)
text("Mon", ((M+2)+(F*0), (M+(F*7))-18))
text("Tue", ((M+2)+(F*1), (M+(F*7))-18))
text("Wed", ((M+2)+(F*2), (M+(F*7))-18))
text("Thr", ((M+2)+(F*3), (M+(F*7))-18))
text("Fri", ((M+2)+(F*4), (M+(F*7))-18))
text("Sat", ((M+2)+(F*5), (M+(F*7))-18))
text("Sun", ((M+2)+(F*6), (M+(F*7))-18))

row = 6
for x in cal.itermonthdays2(year, month):
    day = x[0]
    weekday = x[1]
    if day == 0:
        continue
    text(str(day), ((M+2)+(F*weekday), (M+(F*row))-18))
    if weekday == 6:
        row = row - 1

saveImage('../pdfs/{}-{}.pdf'.format(year, month))
