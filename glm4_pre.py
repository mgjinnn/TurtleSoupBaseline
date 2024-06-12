#coding:utf-8

import pandas as pd
from zhipu_sdk import zhipu_sdk
from tqdm import tqdm,trange
test_a = pd.read_csv('dev.csv',encoding='utf8')
test_a = test_a
def prompt1(x,y,z):
    #prompt = "Give me a short introduction to large language model."
    messages = [
        {"role": "system", "content": f'''你是海龟汤出题人，我们来玩一个叫做海龟汤的游戏。海龟汤是一种情景猜谜的推理游戏。其玩法是:出题者提出一个简单又难以理解的事件，
    玩家可以提出任何封闭式问题以试图缩小范围并找出事件背后真正的原因，封闭式问题指的是问题答案只能为："是。"或者"不是。"。如果玩家的问题不是一个封闭式问题，请回答："问法错误。"。
    海龟汤由汤面和汤底组成，汤面指的是海龟汤的题目，汤底指的是题目背后的真相。如果用户的问题和汤面和汤底不相关，请回答："不重要。",如果用户的答案命中了汤底的核心真相，且大部分内容都得到了还原，请回答："回答正确。"。游戏过程中，你需要根据汤底、汤面、玩家的问题，以及上述规则，判断并选择以下五个选项中的一个来回答玩家提出的问题，不能给出更多的提示。你的回答选项： [是。|不是。|不重要。|问法错误。|回答正确。]。最后玩家通过这些问题和回答来逐渐找到事件的真相，以下是一份海龟汤的汤面和汤底，
    汤面：[{x}]。汤底：[{y}]。请你扮演出题者的角色，我来扮演玩家的角色。由我先提问：'''},
        {"role": "user", "content": z}
    ]
    prompt = f'''你是海龟汤出题人，我们来玩一个叫做海龟汤的游戏。海龟汤是一种情景猜谜的推理游戏。其玩法是:出题者提出一个简单又难以理解的事件，
    玩家可以提出任何封闭式问题以试图缩小范围并找出事件背后真正的原因，封闭式问题指的是问题答案只能为："是。"或者"不是。"。如果玩家的问题不是一个封闭式问题，请回答："问法错误。"。
    海龟汤由汤面和汤底组成，汤面指的是海龟汤的题目，汤底指的是题目背后的真相。如果用户的问题和汤面和汤底不相关，请回答："不重要。",如果用户的答案命中了汤底的核心真相，且大部分内容都得到了还原，请回答："回答正确。"。游戏过程中，你需要根据汤底、汤面、玩家的问题，以及上述规则，判断并选择以下五个选项中的一个来回答玩家提出的问题，不能给出更多的提示。你的回答选项： [是。|不是。|不重要。|问法错误。|回答正确。]。最后玩家通过这些问题和回答来逐渐找到事件的真相，以下是一份海龟汤的汤面和汤底，
    汤面：[{x}]。汤底：[{y}]。请你扮演出题者的角色，我来扮演玩家的角色。由我先提问：{z}'''

    send_input = prompt.format(x=x,y=y,z=z)
    response = zhipu_sdk(send_input)
    return response

answers=[]

for i in trange(len(test_a)):
    puzzle=test_a['puzzle'][i]
    truth = test_a['truth'][i]
    text = test_a['text'][i]
    answer = prompt1(puzzle,truth,text)
    answers.append(answer)
test_a['answer']=answers
test_a.to_csv('dev_predict_result_glm4.csv',index=False)
#
# test_a_baseline_pre = test_a
# test_a_baseline_pre.to_csv('your_predict_result.csv',index=False)
