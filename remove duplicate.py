def remove_duplicate(l1,l2):
    
    pos = 0
    check = 0
    while check < len(l1):
        reset = False
        while pos < len(l2):
            if l1[check] == l2[pos]:
                p1 = l1.pop(check)
                p2 = l2.pop(pos)
                reset = True
                pos = len(l2)
            else:
                pos+=1
                
        if reset:
            check = 0
        else:
            check+=1
        pos = 0
    return l1,l2