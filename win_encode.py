# -*-coding:utf-8-*-
def win_encode(input_str):
    output_list = []
    for char in input_str:
        bin_char = bin(ord(char))
        bin_char = bin_char[bin_char.index("b") + 1:]
        for bit in bin_char:
            if bit == "1":
                output_list.append("赢")
            else:
                output_list.append("麻")
        output_list.append("了")
    return "".join(output_list)


def win_decode(input_str):
    if input_str.strip("赢麻了") != "":
        return "error input"
    input_slist = input_str.split("了")
    utf_list = []
    for sub_list in input_slist:
        utf_char = "0b"
        if sub_list == "":
            continue
        for bit in sub_list:
            if bit == "赢":
                utf_char += "1"
            else:
                utf_char += "0"
        utf_list.append(chr(int(utf_char, 2)))
    return "".join(utf_list)

