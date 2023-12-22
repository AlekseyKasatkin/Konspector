from ctransformers import AutoModelForCausalLM, AutoConfig, Config
from transformers import AutoTokenizer

model_name = "TheBloke/Mistral-7B-OpenOrca-GGUF"
model_file = "gpt4all-falcon-q4_0.gguf"
model_type = "mistral"
gpu_layers = 50

model = AutoModelForCausalLM.from_pretrained(model_name, model_file=model_file, model_type=model_type, gpu_layers=gpu_layers)


prompt = 'Расскажи про гелий на русском языке.'
prompt = 'what is it 2+2 ?'
output = model(max_new_tokens=313, temperature=1, seed=42, prompt=prompt)

print(output)


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, model_file=model_file, model_type=model_type, gpu_layers=gpu_layers)



prompt = 'Расскажи про нашу планету.'
output = llm(prompt=prompt, max_new_tokens=100, seed=42, temperature=0.5)
print(output)

i_temperature = 0.30
i_max_new_tokens=1100
repo = 'TheBloke/TinyLlama-1.1B-1T-OpenOrca-GGUF'
model_file = "tinyllama-1.1b-1t-openorca.Q4_K_M.gguf"
i_repetitionpenalty = 1.2
i_contextlength=12048
logfile = 'TinyLlamaOpenOrca1.1B-stream.txt'
print("loading model...")

conf = AutoConfig(Config(temperature=i_temperature, repetition_penalty=i_repetitionpenalty, batch_size=64,
                max_new_tokens=i_max_new_tokens, context_length=i_contextlength))
llm = AutoModelForCausalLM.from_pretrained(repo, model_file=model_file,
                                        model_type="llama",config = conf)



import openai

openai.api_base = "http://localhost:4891/v1"



from gpt4all import GPT4All
model = GPT4All("mistral-7b-openorca.Q4_0.gguf", device='gpu')
output = model.generate(" Столица России?")
print(output)

from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", device='gpu') # device='amd', device='intel'
output = model.generate("The capital of France is ", max_tokens=3)
print(output)

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", device='gpu')
system_template = 'ты помошник в библиотеке Имени Ленина. ты общаешься только на русском языке. Твоя задача помогать людям искать ошибки в тексте. Делать краткое резюме источников. Помогать излагать ифнормацию более простым языком.'
prompt_template = 'USER: {0}\nASSISTANT: '
prompts = ['10 самых близких звезд?']
print(model.generate(prompts[0]))

first_input = system_template + prompt_template.format(prompts[0])
response = model.generate(first_input, temp=0)
print(response)
for prompt in prompts[1:]:
    response = model.generate(prompt_template.format(prompt), temp=0)
    print(response)



okenizer = AutoTokenizer.from_pretrained(model_name, model_max_length = chatf.context_length)

model = llm

system_template = 'dsfsdfdsf'
model.prepare_inputs_for_generation(system_template)
system_template = 'A chat between a curious user and an artificial intelligence assistant.'
# many models use triple hash '###' for keywords, Vicunas are simpler:
prompt_template = 'USER: {0}\nASSISTANT: '
with model.chat_session(system_template, prompt_template):
    response1 = model.generate('why is the grass green?')
    print(response1)
    print()
    response2 = model.generate('why is the sky blue?')
    print(response2)

model.tokenize(system_template)

system_template = 'A chat between a curious user and an artificial intelligence assistant.'
tokens = model.tokenize(system_template)
mgen = model.generate(tokens, seed=42)

txt = '''' Music ДИНАМИЧНАЯ МУЗЫКА До порванных от напряжения жил Я 
 сохранял свои воспоминания Которыми все эти годы жил Я 
 их хранил на сумрачнай вершыне Ва тьме бездонны пропасті 
 хранію На замам не хрустальнаго кувшына Ка каплю высохших 
 чернил Утаскивают судьбой Сжимают с горла ворот и мне 
 Клубочные мои Превращаются в змей Кровью памяти моей я 
 брызгал в город Кровью памяти моей Кровью памяти моей 
 Кровью памяти моей ДИНАМИЧНАЯ МУЗЫКА Весна И сделать всё, 
 чтоб самому забыть. Но память, как и смерть, неистребима, 
 Как дождь ночной по черноте стекла, Кровавыми осколками рутина 
 Она на дно хрустальное текла Удавшую дворик сжимает в 
 сторону ворот мне Пусти мои Сторм обороты мне Мысли 
 мои превращаются в злей Кровью в памяти моей опрыскан 
 город Кровью в памяти моей Кровью памяти моей Эй-эй! 
 Кровью памяти моей ПЕСНЯ Кровью повесимой Кровью повесимой Кровью 
 Суинни Тодд Флит-стрит его дом принадлежит соседу-мяснику. В нем 
 торгует пирожками из тухлого мяса племянница мясника Лавет.'''