start_count = int(input())
population = int(input())
quatity_days = int(input())
for size_population in range(quatity_days):
    percent = start_count*(population/100)
    print(size_population+1,start_count)
    start_count += percent