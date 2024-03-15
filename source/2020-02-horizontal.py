# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import calendar
import math

# [W]IDTH, [H]EIGHT, [M]ARGIN, [F]FONT-SIZE
# Note: 1 inch = 72 units
# A4: 210 x 297
# Inches: 8.268 x 11.693
# Units: 595,296 x 841,896
W,H,M,F = 789,594,24,78
fix_header = 24
fix_grid = 4
cellX = (W - M * 2) / 7

cal= calendar.Calendar()
monthsInPolish = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
month = 1
year = 2023

# GRID
def grid():
    lineJoin("round")
    stroke(0.8)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = cellX, 78
    for x in range(8):
        polygon(((M)+stpX, M),
                ((M)+stpX, (H-M-F)))
        stpX += incX
    for y in range(7):
        polygon((M, (M)+stpY),
                (W-(M), (M)+stpY))
        stpY += incY

# MAIN
size("A4Landscape")
grid() # Toggle for grid view
stroke(None)

fontSize(F)
openTypeFeatures(ss01=True, ss02=True)
font("Inter-ExtraBold")
text(monthsInPolish[month - 1], (M-4, fix_header+M+(F*6)))


fontSize(F/4)
font("Inter-Regular")
tracking(None)

row = 6
for x in cal.itermonthdays2(year, month):
    day = x[0]
    weekday = x[1]
    if day == 0:
        continue
    text(str(day), ((M+2)+(cellX*weekday), (M+(F*row))-18))
    if weekday == 6:
        row = row - 1

saveImage('../pdfs/{}-{}-horizontal.pdf'.format(year, month))
