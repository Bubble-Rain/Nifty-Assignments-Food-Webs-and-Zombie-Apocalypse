
def formatNames(dataList, recursive = False):

    numNames = len(dataList)

    if(numNames > 1 ):

        head = dataList[0]
        tail = dataList[1:]

        if len(tail) > 1:
            return head + ', ' + formatNames(tail, recursive = True)
        else:
            return head + formatNames(tail, recursive = True)
        
    elif(recursive):
        return ' and ' + dataList[0] 
    else:
        return dataList[0]


def oneType(type, dataList):

    start = type + ': '
    
    namesString = formatNames(dataList)
    

    return start + namesString