import glob

def getfile(path):
    files = glob.glob(f'{path}/*.mp3')
    if len(files) > 0:   # Проверяем, что список files не пустой
        return files[0]  # Возвращаем первый элемент списка
    else:
        return None      # Возвращаем None, если список пустой
