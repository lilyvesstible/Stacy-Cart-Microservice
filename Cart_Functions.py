#Data comes as a tuple, (Serial ID, Quantity)
def AddItem(data, itemList):
    for i in range(data[1]):
        itemList.append(data[0])
    return itemList

def DeleteItem(data, itemList):
    print("STARTINGGG")
    for i in range(int(data[1])):
        if data[0] in itemList:
            print("One of oweghweiofhwf")
            itemList.remove(data[0])
        else:
            break
    return itemList

def PrintList(itemList):
    textSent = ""
    first = True
    for i in itemList:
        if  first == False:
            textSent += (", " + str(i))
        else:
            textSent += str(i)
            first = False
    return textSent

#Input: operation type (int), data (tuple (Serial ID, Quantity)), Item List (list)
#Output: Tuple (New List, string to be sent)
def OpChoose(data, op, itemList):
    #Add Item
    if op == 0:
        return (AddItem(data, itemList), "[ITEM ADDED]")
    #Remove Item
    elif op == 1: 
        return (DeleteItem(data, itemList), "[ITEM DELETED]")
    #Clear List
    elif op == 2:
        return ([], "[LIST CLEARED]")
    #Concatenates list into string
    elif op == 3:
        return (itemList, PrintList(itemList))
    #Quit Server
    elif op == 4:
        return (itemList, "[QUIT]")
    #Error Handling
    else:
        return (itemList, "[UNKNOWN OPERATION]")
    
#Decodes message from a string
def DecodeMessage(message, itemList):
    decode = message.split(", ")
    #Checks if message is correct
    if len(decode) == 3:
        data = (int(decode[0]), int(decode[1]))
        op = int(decode[2])
        return OpChoose(data, op, itemList)
    else: 
        return (itemList, "[INVALID MESSAGE]")