# Напиши функцию total_damage(*hits, critical_multiplier=1), 
# которая суммирует все удары, а затем умножает итог на critical_multiplier.
def total_damage(*hits,critical_multiplier = 1):
    hits_sum = 0
    for hit in hits:
        hits_sum += hit
    return hits_sum * critical_multiplier
print(total_damage(10, 25, 40))
print(total_damage(10, 25, 40, critical_multiplier=2))
print(total_damage())