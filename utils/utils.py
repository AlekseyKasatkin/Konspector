import glob

def getfile(path):
    files = glob.glob(f'{path}/*.mp3')
    return files[0]


