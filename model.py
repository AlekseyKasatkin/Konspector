
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
# import ffmpeg
import os

from utils import utils

#device = "cuda:0" if torch.cuda.is_available() else "cpu"
device = "cuda:0"
#torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
torch_dtype = torch.float16

model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

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

# dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
# sample = dataset[0]["audio"]

file = utils.getfile('./samples')
result = pipe(file, generate_kwargs={'language': "russian", 'task': 'transcribe'})

txt = list(result['text'])
n = 0
for i, el in enumerate(txt):
    if el == ' ':
        n += 1
    if n % 10 == 0:
        txt[i] = el + '\n '
        n = 1
txt = ''.join(txt)

with open('./samples/result.txt', 'w', encoding='utf-8', errors='ignore') as f:
    f.writelines(txt)

os.remove(file)

print('Well Done!')

