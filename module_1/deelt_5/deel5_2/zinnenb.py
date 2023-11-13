def x (total_minutes: int) -> str:
    hours = total_minutes // 60
    minutes = round(total_minutes % 60)
    return f'{hours:02d}:{minutes:02d}'

resulaat = x(70)
nr = float(int(10.9))
print (nr )