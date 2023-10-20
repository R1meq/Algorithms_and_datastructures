def traverse_zigzag(array):
    def simple_traverse(output):
        count = 0
        for i in range(len(array)):
            for j in range(len(array[i])):
                output[count] = array[i][j]
                count += 1
        return output

    output = [0] * (len(array) * len(array[0]))
    direction = False
    i = 0
    j = 0
    count = 0
    i_upper_bound = 0
    i_lower_bound = 0

    if len(array) - 1 == 0 and len(array[0]) - 1 == 0:
        output[count] = array[i][j]
        return output
    elif (len(array) - 1 == 0 and len(array[0]) != 0) or (len(array) != 0 and len(array[0]) - 1 == 0):
        return simple_traverse(output)
    else:
        output[count] = array[i][j]
        count += 1
        j += 1
        i_upper_bound += 1

    while True:
        if direction:
            if i == i_lower_bound:
                output[count] = array[i][j]
                direction = False
                count += 1
                if j != len(array[0]) - 1:
                    j += 1
                    if i_upper_bound < len(array) - 1:
                        i_upper_bound += 1
                else:
                    i += 1
                    i_lower_bound += 1
            else:
                output[count] = array[i][j]
                count += 1
                i -= 1
                j += 1
        else:
            if j == len(array[0]) - 1:
                i_lower_bound += 1
            if i == i_upper_bound:
                output[count] = array[i][j]
                direction = True
                count += 1
                if i != len(array) - 1:
                    i += 1
                    i_upper_bound += 1
                else:
                    j += 1
            else:
                output[count] = array[i][j]
                count += 1
                i += 1
                j -= 1

        if i == len(array) - 1 and j == len(array[0]) - 1:
            output[count] = array[i][j]
            break

    return output