def strcounter(s): #привет
    syms_counter={} #список
    for sym in s:
        syms_counter[sym]=syms_counter.get(sym, 0)+1

    for sym, count in syms_counter.items():
        print(sym, count)
strcounter('anamkcd')
