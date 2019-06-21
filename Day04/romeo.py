with open('romeo.txt', mode='rt') as file:
    list_of_lines= file.readlines()
    word_dict={}
    
    for line in list_of_lines:
        words_list=line.split()
        for word in words_list:
            if word not in list(word_dict.keys()):
                word_dict[word]=1
            else:
                 word_dict[word]+=1
                 
for key, value in word_dict.items():
    print(key, value)