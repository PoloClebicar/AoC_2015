def main():
    file = open("/mnt/c/Users/thepo/Documents/GitHub/AoC_2015/list.txt", "r")

    wires = {"name": "TEST_name", "value": "TEST_value"}
    wireList = []
    
    wireList.append(wires.copy())

    print(dic_uptade(wireList, "TEST_namoooe", wires))
    print(wireList)

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
                    and_operation(wire_1, wire_2, second_half)
                case "OR":
                    or_operation(wire_1, wire_2, second_half)
                case "RSHIFT":
                    rshift_operation(wire_1, wire_2, second_half)
                case "LSHIFT":
                    lshift_operation(wire_1, wire_2, second_half)

        # operation 'wire'
        elif first_half[0].isupper():
            #NOT operation
            wire_1 = first_half.split(" ")[1]
            wire_1 = wire_1.strip()
            not_operation(wire_1, second_half)
            ...
        #value
        else:
            #assing value
            print("VALUE ASSINGNED")
            ...
            #and, or, RSHIFT, LSHIFT, NOT

def not_operation(wire_1, final_wire):
    print("NOT OPERATION")
    ...

def and_operation(wire_1, wire_2, final_wire):
    print("AND OPERATION")
    ...

def or_operation(wire_1, wire_2, final_wire):
    print("OR OPERATION")
    ...

def rshift_operation(wire_1, wire_2, final_wire):
    print("RSHIFT OPERATION")
    ...

def lshift_operation(wire_1, wire_2, final_wire):
    print("LSHIFT OPERATION")
    ...

def dic_uptade(wireList, wire, wires):
    #Check id the current wire is on the dictionary
    #if yes, assing due value
    #if no, create and assing value 0
    for dics in wireList:
        if wire in dics.values():
            return dics.get("value")
        else:
            wires.update({"name": wire, "value": 0})
            wireList.append(wires.copy())
            return 0
    ...



main()