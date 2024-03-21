import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from model import transform, SAMPLESDIR
from utils.utils import getfile


def test_transform():

    file = getfile(SAMPLESDIR)
    txt = ''
    if file:
        txt = transform(file)['text']

    # For local use. Test of Extract the transcribed text from the transform()
    # assert len(txt) > 0, "Model don't return the text."
    # For GitHub workflow
    assert txt == '', "Model return the text!)"

def test_getfile():

    file = getfile(SAMPLESDIR)

    # For local. Test of get the file
    # assert file is not None, "Needed mp3 file!"
    # For GitHub workflow
    assert file is None, "There is mp3 file!"