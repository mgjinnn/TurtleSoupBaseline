'''

A baseline(chatglm3-6b) prediction on the test_a dataset

'''

import pandas as pd

from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("/home/wenhy/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("/home/wenhy/chatglm3-6b", trust_remote_code=True, device='cuda:1')
model = model.eval()


test_a = pd.read_csv('test_a.csv',encoding='gbk')
# puzzle = test_a['puzzle'][0]
# truth = test_a['truth'][0]
# text = test_a['text'][0]

# prompt= f'''你是海龟汤出题人，我们来玩一个叫做海龟汤的游戏。海龟汤是一种情景猜谜的推理游戏。其玩法是:出题者提出一个简单又难以理解的事件，
# 玩家可以提出任何封闭式问题以试图缩小范围并找出事件背后真正的原因，封闭式问题指的是问题答案只能为：是或者不是。如果玩家的问题不是一个封闭式问题，请回答：问法错误。游戏过程中，你只能用 ['是。'，'不是。'，'不重要。'，'问法错误。']来回答玩家提出的问题，最后玩家通过这些问题和回答来逐渐找到事件的真相，
# 海龟汤由汤面和汤底组成，汤面指的是海龟汤的题目，汤底指的是题目背后的真相。如果用户的问题和汤面和汤底不相关，请回答：不重要。如果用户的答案命中了汤底的核心真相，且大部分内容都得到了还原，请回答：回答正确。以下是一份海龟汤的汤面和汤底，
# 汤面：{puzzle}。汤底：{truth}。请你扮演出题者的角色，我来扮演玩家的角色。由我先提问：{text}'''

def func(x,y,z):
    response, history = model.chat(tokenizer, f'''你是海龟汤出题人，我们来玩一个叫做海龟汤的游戏。海龟汤是一种情景猜谜的推理游戏。其玩法是:出题者提出一个简单又难以理解的事件，
玩家可以提出任何封闭式问题以试图缩小范围并找出事件背后真正的原因，封闭式问题指的是问题答案只能为：是或者不是。如果玩家的问题不是一个封闭式问题，请回答：问法错误。游戏过程中，你只能用 ['是。'，'不是。'，'不重要。'，'问法错误。']来回答玩家提出的问题，最后玩家通过这些问题和回答来逐渐找到事件的真相，
海龟汤由汤面和汤底组成，汤面指的是海龟汤的题目，汤底指的是题目背后的真相。如果用户的问题和汤面和汤底不相关，请回答：不重要。如果用户的答案命中了汤底的核心真相，且大部分内容都得到了还原，请回答：回答正确。以下是一份海龟汤的汤面和汤底，
汤面：{x}。汤底：{y}。请你扮演出题者的角色，我来扮演玩家的角色。由我先提问：{z}''', history=[])
    return response

test_a['answer'] = test_a.apply(lambda x:func(x.puzzle,x.truth,x.text),axis=1)

test_a_baseline_pre = test_a
test_a_baseline_pre.to_csv('test_a_baseline_pre.csv',index=False)
