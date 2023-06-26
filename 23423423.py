#=https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb   依赖这套代码开发一个openai自定义模型加强回复效果.
#===经过测试: openai对于prompt很敏感,相同的东西尽量用规范的书写模式来提问答案准确度会更高. 不规范的话他可能会回答成英文.
#========经过测试. openai对于信息输入过多也会效果不好.所以加入similarity 的权重.
print(1)
import numpy as np
import openai
import pandas as pd
import pickle
import tiktoken

#=两个初始model的名字.
COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDING_MODEL = "text-embedding-ada-002"

openai.api_key = "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"
prompt = "Who won the 2020 Summer Olympics men's high jump?"
# a1=openai.Completion.create(
#     prompt=prompt,
#     temperature=0,
#     max_tokens=300,
#     model=COMPLETIONS_MODEL
# )
if 0:
    print(2)
    a=openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        model=COMPLETIONS_MODEL
    )["choices"][0]["text"].strip(" \n")
    print(a) #=======这个回答是错的.
    print(3)







    prompt = """Answer the question as truthfully as possible, and if you're unsure of the answer, say "Sorry, I don't know".

    Q: Who won the 2020 Summer Olympics men's high jump?
    A:"""

    print(openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        model=COMPLETIONS_MODEL
    )["choices"][0]["text"].strip(" \n"))







    #===============加入context
    prompt = """Answer the question as truthfully as possible using the provided text, and if the answer is not contained within the text below, say "I don't know"

    Context:
    The men's high jump event at the 2020 Summer Olympics took place between 30 July and 1 August 2021 at the Olympic Stadium.
    33 athletes from 24 nations competed; the total possible number depended on how many nations would use universality places 
    to enter athletes in addition to the 32 qualifying through mark or ranking (no universality places were used in 2021).
    Italian athlete Gianmarco Tamberi along with Qatari athlete Mutaz Essa Barshim emerged as joint winners of the event following
    a tie between both of them as they cleared 2.37m. Both Tamberi and Barshim agreed to share the gold medal in a rare instance
    where the athletes of different nations had agreed to share the same medal in the history of Olympics. 
    Barshim in particular was heard to ask a competition official "Can we have two golds?" in response to being offered a 
    'jump off'. Maksim Nedasekau of Belarus took bronze. The medals were the first ever in the men's high jump for Italy and 
    Belarus, the first gold in the men's high jump for Italy and Qatar, and the third consecutive medal in the men's high jump
    for Qatar (all by Barshim). Barshim became only the second man to earn three medals in high jump, joining Patrik Sjöberg
    of Sweden (1984 to 1992).

    Q: Who won the 2020 Summer Olympics men's high jump?
    A:"""

    print(openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model=COMPLETIONS_MODEL
    )["choices"][0]["text"].strip(" \n"))