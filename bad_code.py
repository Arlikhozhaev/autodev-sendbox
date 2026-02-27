def process_data(data):
    result = []
    for i in range(len(data)):
        if isinstance(data[i], int):
            if data[i] % 2 == 0:
                result.append(data[i] * 2)
            else:
                result.append(data[i] * 3)
        else:
            if isinstance(data[i], str):
                if len(data[i]) > 3:
                    result.append(data[i].upper())
                else:
                    result.append(data[i].lower())
            else:
                result.append(None)
    return result