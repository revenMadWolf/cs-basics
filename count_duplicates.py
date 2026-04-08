unclean_list = [4,2,4,3,2,1]

clean_list = list(set(unclean_list))

info_list = []

for x in clean_list:
    count = 0
    for y in unclean_list:
        if x == y:
            count += 1
    info_list.append((x,count))

print(info_list)