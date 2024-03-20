import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
import ffmpeg
from model import transform, SAMPLESDIR
from utils.utils import getfile


def test_transform():

    file = getfile(SAMPLESDIR)
    txt = ''
    if file:
        txt = transform(file)['text']

    # Test of Extract the transcribed text from the transform()
    assert len(txt) > 0, "Model don't return the text."


def test_getfile():

    file = getfile(SAMPLESDIR)

    # Test of get the file
    assert file is not None, "Needed mp3 file!"



