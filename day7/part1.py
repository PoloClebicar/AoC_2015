def main():
    file = open("/mnt/c/Users/thepo/Documents/GitHub/AoC_2015/list.txt", "r")

    wires = {}
    wireList = []

    for lines in file:
        first_half, second_half = lines.split("->")
        first_half = first_half.strip()
        second_half = second_half.strip()

        #Check the kinda of operation is being done

        # 'wire' operation 'wire'
        if first_half[0].islower():
            #detect operation
            wire_1, operation, wire_2 = first_half.split(" ")
            wire_1 = wire_1.strip()
            wire_2 = wire_2.strip()
            operation = operation.strip()

            match operation:
                case "AND":
                    and_operation(wireList ,wire_1, wire_2, second_half, wires)
                case "OR":
                    or_operation(wireList ,wire_1, wire_2, second_half, wires)
                case "RSHIFT":
                    rshift_operation(wireList ,wire_1, wire_2, second_half, wires)
                case "LSHIFT":
                    lshift_operation(wireList ,wire_1, wire_2, second_half, wires)

        # operation 'wire'
        elif first_half[0].isupper():
            #NOT operation
            wire_1 = first_half.split(" ")[1]
            wire_1 = wire_1.strip()
            not_operation(wireList, wire_1, second_half, wires)
            ...
        #value
        else:
            #assing value
            first_half = first_half.strip()
            #print(first_half, second_half)
            define_dic_value(wireList, second_half, wires, first_half)
            ...
            #and, or, RSHIFT, LSHIFT, NOT

    print(wireList)

def not_operation(wireList, wire_1, final_wire, wires):
   value = get_dic_value(wireList, wire_1, wires)
   #print(value)
   value  = 0b1111111111111111 - value
   #print(value)
   define_dic_value(wireList, final_wire, wires, value)
   ... 

def and_operation(wireList, wire_1, wire_2, final_wire, wires):
    value_1 = get_dic_value(wireList, wire_1, wires)
    value_2 = get_dic_value(wireList, wire_2, wires)

    print(value_1, value_2)

    final_value = value_1 & value_2

    define_dic_value(wireList, final_wire, wires, final_value)
    ...

def or_operation(wireList, wire_1, wire_2, final_wire, wires):
    value_1 = get_dic_value(wireList, wire_1, wires)
    value_2 = get_dic_value(wireList, wire_2, wires)

    final_value = int(value_1) | int(value_2)

    define_dic_value(wireList, final_wire, wires, final_value)
    ...

def rshift_operation(wireList, wire_1, wire_2, final_wire, wires):
    value = get_dic_value(wireList, wire_1, wires)
    value >>= int(wire_2)
    define_dic_value(wireList, final_wire, wires, value)
    ...

def lshift_operation(wireList, wire_1, wire_2, final_wire, wires):
    value = get_dic_value(wireList, wire_1, wires)
    value <<= int(wire_2)
    define_dic_value(wireList, final_wire, wires, value)
    ...



##############################################
################ TODO ########################
###### FIX THE GET AND DEFINE FUNCTIONS ######
##############################################

def get_dic_value(wireList, wire, wires):
    #If there is a value in the dic
    #return that value
    #if not initialize that value as 0
    if len(wireList) >= 1:
        for dics in wireList:
            if wire in dics.keys():
                return dics.get("value")
            else:
                #print("HEY")
                wires.update({"name": wire, "value": 0})
                wireList.append(wires.copy())
                return 0
    else:
        wires.update({"name": wire, "value": 0})
        wireList.append(wires.copy())
        return 0


def define_dic_value(wireList, wire, wires, value):
    if len(wireList) >= 1:
        for dics in wireList:
            if wire in dics.keys():
                wires.update({"name": wire, "value": value})
                return
            else:
                wires.update({"name": wire, "value" : value})
                wireList.append(wires.copy())
                return
    else:
        wires.update({"name": wire, "value": value})
        wireList.append(wires.copy())
        return 
    

main()