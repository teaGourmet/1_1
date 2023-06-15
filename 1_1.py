#N**2
def strcounter(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

strcounter('aaaabbbbbcccd')

#M*N
def strcounter(s):
    for sym in set(s):
        counter = 0 
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
strcounter('aaabbbbccccc')

#N
def strcounter(s):
    sym_counter = {}
    for sym in s:
        sym_counter[sym] = sym_counter.get(sym, 0) + 1
    for sym, count in sym_counter.items():
        print(sym, count)
strcounter('aaaabbbccccccc')