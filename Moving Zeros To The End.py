def move_zeros(lst):
    strlst = [str(i) for i in lst]
    strlst.sort(key='0'.__eq__)
    return [int(i) for i in strlst]