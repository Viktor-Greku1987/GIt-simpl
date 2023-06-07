import pymorphy2
global name_radio
def chek_radiost(text):
    print("text",text)
    list_radio = []
    morph = pymorphy2.MorphAnalyzer()
    elem_lst = []
    text = text.split()
    word_list = []
    result_list = []
    for i in text:
        word_list.append(i)
    for ii in word_list:
        p = morph.parse(ii)[0]
        res = p.normal_form
        result_list.append(res)
    for elem in result_list:
        elem_lst.append(elem)
    with open('radio.txt', 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            if line[-1] == '\n':
                line = line[0:len(line) - 1]
            key_radio, URL_radio = line.split('; ')

            key_radio_1 = key_radio.split()
            #print("key_radio: ",key_radio)
            #print(elem_lst)
            chek_rad = list(set(key_radio_1) & set(elem_lst))
            if chek_rad !=[]:
                #print("chek_rad", key_radio )
                name_radio = key_radio

                return name_radio
            else:
                print('радио не найдино')
                return ''



#chek_radiost('Викторию, включи радио европы плюсы')