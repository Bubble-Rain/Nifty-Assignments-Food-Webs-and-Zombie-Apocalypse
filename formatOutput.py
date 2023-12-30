
def formatNames(dataList, recursive = False):

    head, *tail = dataList

    if(not tail):
        return head + ', ' + formatNames(tail, recursive = True)
    elif(recursive):
        return ' and ' + head 
    else:
        return head


def oneType(type, dataList):

    start = type + ': '
    
    namesString = formatNames(dataList)
    

    return start + namesString