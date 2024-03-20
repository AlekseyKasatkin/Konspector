import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import ffmpeg
import os
from utils import utils


SAMPLESDIR = './samples'


def transform(file):

    # Set the device to use CUDA if available, otherwise use CPU
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Set the torch data type to float16 if CUDA is available,
    # otherwise use float32
    torch_dtype = torch.float16 if torch.cuda.is_available() \
        else torch.float32

    # Specify the model ID
    model_id = "openai/whisper-large-v3"

    # Load the pre-trained model
    model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id,
                                                      torch_dtype=torch_dtype,
                                                      low_cpu_mem_usage=True,
                                                      use_safetensors=True)
    model.to(device)

    # Load the processor
    processor = AutoProcessor.from_pretrained(model_id)

    # Create a pipeline for automatic speech recognition
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=15,
        batch_size=8,
        return_timestamps=True,
        torch_dtype=torch_dtype,
        device=device,
    )

    # Perform automatic speech recognition on the file
    return pipe(file)


def main():

    # Get the file
    file = utils.getfile(SAMPLESDIR)
    if file is None:
        print("Needed mp3 file!")
        return

    txt = list(transform(file)['text'])

    # Add line breaks every 10 words
    n = 0
    for i, el in enumerate(txt):
        if el == ' ':
            n += 1
        if n == 10:
            txt[i] = el + '\n '
            n = 1

    # Join the transcribed text back into a single string
    txt = ''.join(txt)

    # Write the transcribed text to a file
    with open('./samples/result.txt', 'w', encoding='utf-8', errors='ignore') \
            as f:
        f.writelines(txt)

    # Remove the input file
    os.remove(file)

    # Print a success message
    print('Well Done!')


if __name__ == "__main__":
    main()
