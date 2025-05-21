#Data comes as a tuple, (Serial ID, Quantity)
def AddItem(data, itemList):
    for i in range(data[1]):
        itemList.append(data[0])
    return itemList

def DeleteItem(data, itemList):
    for i in range(int(data[1])):
        if data[1] in itemList:
            itemList.remove(data[1])
        else:
            break
    return itemList

#Returns a tuple, (New List, string to be sent)
def OpChoose(op, data, itemList):
    #Add Item
    if op == 0:
        return (AddItem(data, itemList), "[ITEM ADDED]")
    #Remove Item
    elif op == 1: 
        return (DeleteItem(data, itemList), "[ITEM DELETED]")
    #Clear List
    elif op == 2:
        return ([], "[LIST CLEARED]")