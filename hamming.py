def distance(str1, str2):
    str1_striped = str1.strip()
    str2_striped = str2.strip()

    str1_length = len(str1_striped)  
    str2_length = len(str2_striped)
    
    if str1_length != str2_length:
        raise Exception(f'str1 length {str1_length} != str2 length {str2_length}')

    dist = 0

    for el1, el2 in zip(str1_striped, str2_striped):
        if el1 != el2:
            dist += 1


    # for i in range(str1_length):
    #     if str1_striped[i] != str2_striped[i]:
            # dist += 1
    
    return dist