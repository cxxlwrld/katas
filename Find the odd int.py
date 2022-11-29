def find_it(seq):
    return set([i for i in seq if seq.count(i) % 2]).pop()