data_list = ['12 guests · 6 bedrooms · 10 beds · 3 baths',
             '10 guests · 5 bedrooms · 7 beds · 4 baths',
                '13 guests · 2 bedrooms · 8 beds · 4 baths']

br_arr = []
old_br_arr = []
for i in data_list:
    for ali in i.split(' · '):
        old_br_arr.append(ali)
        if 'bedrooms' in ali:
            br_arr.append(ali[:2])
br_arr = [int(i) for i in br_arr]
print(br_arr)
print(old_br_arr)
