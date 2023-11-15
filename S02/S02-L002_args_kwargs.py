

def calculate_paint(efficiency_ltr_per_m2, *areas):
    paint_needed = 0
    for area in areas:
        paint_needed += efficiency_ltr_per_m2 * area

    return paint_needed
def log_it(*args):
    with open('log.txt','a') as file:
        for arg in args:
            file.write(arg +" ")
        file.write("\n")



print(calculate_paint(0.1, 10,20,30))
rooms_area = [10.2,23.4,5.4]
print(calculate_paint(0.1,*rooms_area))

log_it('asd  asd sadsa da s')
log_it('asd', 'dat', 'asd', '221310')