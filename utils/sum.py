
import re
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration

clean_expr = re.compile(r"[\xa0\x1a\x16\x1b\x17\x15\u2004]")
spaces_expr = re.compile(r"\s{2,}")


def process_text(text: str) -> str:
    """Осуществляет пред- и постобработку текста."""
    text = clean_expr.sub(" ", text)
    text = spaces_expr.sub(" ", text)

    if "." in text:
        index = text.rindex(".")
        text = text[:index + 1]

    return text

summarizer = pipeline("summarization",
                      # model="basic-go/FRED-T5-large-habr-summarizer",
                      model = 'd0rj/rut5-base-summ',
                      device=0)
tokenizer = T5Tokenizer.from_pretrained('d0rj/rut5-base-summ')
outputs = summarizer.generate(tokenizer)
summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

#
# with open('samples/result.txt') as f:
#     ARTICLE = f.read()
# input_ids = tokenizer(ARTICLE, return_tensors='pt').input_ids
# if len(ARTICLE) > 30000:
#     txt = 'Саммаризация произведена на основе части текста. Чтобы узнать подробности, скачайте файл целиком'
# else:
#     txt = 'Саммаризация произведена на основе всего текста. '
#
# ARTICLE = process_text(ARTICLE)[0:20000]
#
# response = summarizer(ARTICLE,
#                       max_new_tokens=360,
#                       num_beams=2,
#                       do_sample=True,
#                       top_k=100,
#                       repetition_penalty=2.5,
#                       length_penalty=1.0)
# summary = process_text(response[0]["summary_text"])
# with open('samples/result_sum.txt', "w+", encoding='utf-8', errors='ignore') as fsum:
#     print(summary)
#     fsum.write(summary)
