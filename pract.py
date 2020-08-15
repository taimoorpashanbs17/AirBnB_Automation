data_list = ['Wifi\nContinuous access in the listing', 'Washer\nIn the building, free or for a fee', 'Iron', 'Laptop-friendly workspace\nA table or desk with space for a laptop and a chair that’s comfortable to work in', 'Heating\nCentral heating or a heater in the listing', 'Essentials\nTowels, bed sheets, soap, and toilet paper', 'TV', 'Hot water', 'High chair', 'Crib', 'Elevator\nThe home or building has an elevator that’s at least 52 inches deep and a doorway at least 32 inches wide.', 'Single level home\nNo stairs in home', 'Free street parking', 'Kitchen\nSpace where guests can cook their own meals', 'Microwave', 'Refrigerator', 'Cooking basics\nPots and pans, oil, salt and pepper', 'Dishes and silverware', 'Stove', 'Coffee maker', 'Dishwasher', 'Oven', 'Host greets you', 'Long term stays allowed\nAllow stay for 28 days or more', "Luggage dropoff allowed\nFor guests' convenience when they have early arrival or late departure", 'Hangers', 'Hair dryer', 'Bed linens', 'Extra pillows and blankets', 'Garden or backyard', 'Patio or balcony', 'Fire extinguisher', 'First aid kit', 'Unavailable: Shampoo\nShampoo', 'Unavailable: Air conditioning\nAir conditioning', 'Unavailable: Private entrance\nPrivate entrance', 'Unavailable: Smoke alarm\nSmoke alarm', 'Unavailable: Carbon monoxide alarm\nCarbon monoxide alarm']


br_arr = []
for i in data_list:
    for ali in i.split('\n'):
        br_arr.append(ali)
        # if 'Wifi' in ali:
        #     br_arr.append(ali)
print(br_arr)
