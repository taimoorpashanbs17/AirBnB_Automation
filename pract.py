# data_list = ['Season Hotel', 'Roma']
# data = "Entire apartment in Roma"


def hotel_name_verification(data_list, data):
    data_missing = []
    for i in data_list:
        if str(i) not in data:
            data_missing.append(i)
    length = bool(len(data_missing) == 0)
    return length


print(hotel_name_verification(['apartment', 'Roma'], "Entire apartment in Roma"))


