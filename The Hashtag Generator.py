def generate_hashtag(s):
    lst = []
    for i in s.split(" "):
        lst.append(i.capitalize())
        hashtag = '#'+''.join(lst)
    if len(s)==0:
        return False
    elif len(hashtag) > 140:
        return False
    else:
        return hashtag