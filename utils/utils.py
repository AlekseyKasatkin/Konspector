import glob


def getfile(path):
    """Uploading audio file"""
    files = glob.glob(f'{path}/*.mp3')
    return files[0]
