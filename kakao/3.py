def timeMeasure(size, cities):
    time = 0
    cache = []

    try:
        for i in range(len(cities)):
            if cities[i].lower() in cache:
                cacheHit = cache.pop()
                cache.insert(0,cacheHit)
                time += 1 
            else: 
                if len(cache) < size :
                    cache.insert(0,cities[i].lower())
                    time += 5
                elif len(cache) == size:
                    cache.pop()
                    cache.insert(0,cities[i].lower())
                    time += 5

    except:
        for i in range(len(cities)):
            time += 5
        
    return time


print(timeMeasure(3,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(timeMeasure(3,['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
print(timeMeasure(2,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(timeMeasure(5,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(timeMeasure(2,['Jeju', 'Pangyo', 'NewYork', 'newyork']))
print(timeMeasure(0,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))