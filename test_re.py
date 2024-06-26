from openai import OpenAI
base_url = "http://localhost:8000/v1/"
client = OpenAI(api_key="EMPTY", base_url=base_url)
import time
import pandas as pd


test_a = pd.read_csv('test_a.csv',encoding='gbk')


def simple_chat(sys_content,usr_content,use_stream=False):
    messages = [
        {
            "role": "system",
            "content": sys_content,
        },
        {
            "role": "user",
            "content": usr_content
        }
    ]
    response = client.chat.completions.create(
        model="glm-4",
        messages=messages,
        stream=use_stream,
        max_tokens=1024,
        temperature=0.1,
        presence_penalty=1.1,
        top_p=0.8)
    if response:
        if use_stream:
            stream_list=[]
            for chunk in response:
                stream_list.append(chunk.choices[0].delta.content)
            return stream_list
        else:
            content = response.choices[0].message.content
            return content
    else:
        return (f"Error:, {response.status_code}")

def prompt1(x,y,z):
    sys_prom=f'''你是海龟汤出题人，我们来玩一个叫做海龟汤的游戏。海龟汤是一种情景猜谜的推理游戏。其玩法是:出题者提出一个简单又难以理解的事件，
    玩家可以提出任何封闭式问题以试图缩小范围并找出事件背后真正的原因，封闭式问题指的是问题答案只能为："是。"或者"不是。"。如果玩家的问题不是一个封闭式问题，请回答："问法错误。"。
    海龟汤由汤面和汤底组成，汤面指的是海龟汤的题目，汤底指的是题目背后的真相。如果用户的问题和汤面和汤底不相关，请回答："不重要。",如果用户的答案命中了汤底的核心真相，且大部分内容都得到了还原，请回答："回答正确。"。游戏过程中，你需要根据汤底、汤面、玩家的问题，以及上述规则，判断并选择以下五个选项中的一个来回答玩家提出的问题，不能给出更多的提示。你的回答选项： [是。|不是。|不重要。|问法错误。|回答正确。]。最后玩家通过这些问题和回答来逐渐找到事件的真相，以下是一份海龟汤的汤面和汤底，
    汤面：[{x}]。汤底：[{y}]。请你扮演出题者的角色，我来扮演玩家的角色。由我先提问：'''
    usr_prom = z
    res = simple_chat(sys_content=sys_prom,usr_content=usr_prom)

    return res

t1 = time.time()
print(f"now: {t1}")
test_a['answer'] = test_a.apply(lambda x:prompt1(x.puzzle,x.truth,x.text),axis=1)
print(f"cost:{time.time()-t1}")
test_a_baseline_pre = test_a
test_a_baseline_pre.to_csv('your_predict_result.csv',index=False)