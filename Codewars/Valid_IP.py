def is_valid_IP(string):
    """
    req1) len after split('.') == 4
    req2) has to be convertable to int
    req3) len of each 1 to 3
    req4) can't start from 0
    """
    for i in range(len(string)):
        if string[i] == ' ':
            print('spaces!')
            return False
    string = string.split('.')
    # req 1
    if len(string) != 4:
        print("wrong amount")
        return False
    print(string)
    for i in range(4):
        try:
            if string[i] == '' or (string[i][0] == '0' and len(string[i]) > 1) or len(string[i]) > 3:
                print('empty; 0; length')
                return False
            string[i] = int(string[i])
            if string[i] not in range(0, 256):
                print('range')
                return False
        except ValueError:
            print(f'{i+1}:error')
            return False
    # for i in range(4):
    # print(string)
    return True


string = '1.2 55.0.1'
print(is_valid_IP(string))
