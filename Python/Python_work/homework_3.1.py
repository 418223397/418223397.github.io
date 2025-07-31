filepaths = ['news.txt', '']

for fp in filepaths:
    try:
        f = open(fp, "r",encoding='utf-8')
    except:
        print(f'can not open {fp}')
    else:
        content = f.read()
        print(f'file content : {content}')
    finally:
        print('python is easy')






