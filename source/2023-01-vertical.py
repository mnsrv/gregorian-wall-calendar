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
cellY = (H - M * 2 - F) / 6

cal= calendar.Calendar()
monthsInPolish = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
monthsInSakha = ["Тохсунньу", "Олунньу", "Кулун тутар", "Муус устар", "Ыам ыйа", "Бэс ыйа", "От ыйа", "Атырдьах ыйа", "Балаҕан ыйа", "Алтынньы", "Сэтинньи", "Ахсынньы"]
month = 12
year = 2023

# GRID
def grid():
    lineJoin("round")
    stroke(0.9)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = F, cellY
    for x in range(8):
        polygon(((M)+stpX, M),
                ((M)+stpX, (H-F-M)))
        stpX += incX
    for y in range(7):
        polygon((M, (M)+stpY),
                (W-(M), (M)+stpY))
        stpY += incY

# MAIN
size("A4")
grid() # Toggle for grid view
stroke(None)

fontSize(60)
openTypeFeatures(ss01=True, ss02=True)
font("Inter-Bold")
text(monthsInPolish[month - 1], (M-4, H - M))
font("Inter-Italic")
text(monthsInSakha[month - 1], (M-4, H - M - 60))
font("Inter-Italic")
fontSize(F/2)
text(str(year), (W-M - 100, H - M - 60))


fontSize(24)
font("Inter-Regular")
tracking(None)

row = 6
for x in cal.itermonthdays2(year, month):
    day = x[0]
    weekday = x[1]
    if day == 0:
        continue
    text(str(day), ((M+4)+(F*weekday), (M+(cellY*row))-24))
    if weekday == 6:
        row = row - 1

saveImage('../pdfs/{}-{}-vertical.pdf'.format(year, month))
