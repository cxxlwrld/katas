def spin_words(sentence):
    out = []
    for i in sentence.split(' '):
        if len(i) >= 5:
            out.append(i[::-1])
        else:
            out.append(i)
    return ' '.join(out)