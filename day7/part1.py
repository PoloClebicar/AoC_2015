####################################################################
####################################################################
### TODO: Rewrite from the start to correctly account for all the ##
### types that are messing everything up, I belive most of the #####
### functions are okay, the main ones at least, not super sure #####
### about the and_value and transfer. so probably redo those########
####################################################################
####################################################################


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
            try:
                wire_1, operation, wire_2 = first_half.split(" ")
                wire_1 = wire_1.strip()
                wire_2 = wire_2.strip()
                operation = operation.strip()
            except ValueError:
                print(second_half)
                wire_1 = first_half.strip()
                wire_2 = None
                operation = "transfer"

            match operation:
                case "AND":
                    and_operation(wireList ,wire_1, wire_2, second_half, wires)
                case "OR":
                    or_operation(wireList ,wire_1, wire_2, second_half, wires)
                case "RSHIFT":
                    rshift_operation(wireList ,wire_1, wire_2, second_half, wires)
                case "LSHIFT":
                    lshift_operation(wireList ,wire_1, wire_2, second_half, wires)
                case "transfer":
                    transfer_op(wireList, wire_1, second_half, wires)

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
            try:
                value_AND, operation, wire_2 = first_half.split(" ")
                value_AND = value_AND.strip()
                value_AND = int(value_AND)
                wire_2 = wire_2.strip()
                
                and_operation_number(wireList, wire_1, value_AND, second_half, wires)
                ...
            except ValueError:
                define_dic_value(wireList, second_half, wires, first_half)
                ...

    for j in range(len(wireList)):
        if wireList[j]["name"] == "a":
            print(wireList[j]["value"])

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

    final_value = value_1 & value_2

    define_dic_value(wireList, final_wire, wires, final_value)
    ...

def and_operation_number(wireList, wire_1, value, final_wire, wires):
    value_1 = get_dic_value(wireList, wire_1,wires)

    final_value = value_1 | value

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

def get_dic_value(wireList, wire, wires):
    for i in range(len(wireList)):
        if wireList[i]["name"] == wire:
            return wireList[i]["value"]
    
    define_dic_value(wireList, wire, wires, 0)
    return 0 
        
def define_dic_value(wireList, wire, wires, value):
    if len(wireList) < 1:
        wires = {"name" : wire, "value" : int(value)}
        wireList.append(wires.copy())
        return 
    
    for i in range(len(wireList)):
        if wire == wireList[i]["name"]:
            wireList[i] = {"name" : wire, "value" : int(value)}
            return
        else:
            wires = {"name" : wire, "value" : int(value)}
            wireList.append(wires.copy())
            return

def transfer_op(wireList, wire_1, final_wire, wires):
    value = get_dic_value(wireList, wire_1, wires)
    define_dic_value(wireList, final_wire, wires, value)


main()