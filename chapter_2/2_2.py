#Chapter 2
# EX 2.2
#1) What is the volume of a sphere with radius 5?
import math
radius = 5
volume = 4/3 * math.pi * radius**3
print('volume sfera: ', volume)
#2)
book_cover_pr = 24.95
discount_book = 40
ship_cost_first = 3
ship_cost_others = 0.75
tot_cost_60 = 60 * (24.95 - (24.95*0.4)) + 3 + 59*0.75
print('costo tot 60 copie: ', tot_cost_60)
#3)
start_miles = 1
start_min = start_miles *(8 + 15 / 60)
mid_miles = 3
mid_min = mid_miles * (7 + 12 / 60)
end_miles = 1
end_min = start_min
tot_min = start_min + mid_min + end_min
print('minuti trascorsi: ', tot_min)
print('ora di rientro: ', 7, (tot_min - 8))
