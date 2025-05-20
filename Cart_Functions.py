#Data comes as a tuple, (Serial ID, Quantity)
def AddItem(data, list):
    for i in range(data[1]):
        list.append(data[0])
    return list