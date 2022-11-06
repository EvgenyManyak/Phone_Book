def input_write(data: str):
    open('file.txt','a', encoding = 'utf8').write(data + '\n')