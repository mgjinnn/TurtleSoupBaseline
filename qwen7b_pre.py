from transformers import AutoModelForCausalLM, AutoTokenizer

import os 

os.environ['cuda_visible_devices'] = '1'

os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
import pandas as pd


test_a = pd.read_csv('test_a.csv',encoding='gbk')

device = "cuda" # the device to load the model onto


model = AutoModelForCausalLM.from_pretrained(
    "/home/wenhy/Qwen1.5-7b-chat/qwen/Qwen1___5-7B-Chat"
).to(device)

tokenizer = AutoTokenizer.from_pretrained("/home/wenhy/Qwen1.5-7b-chat/qwen/Qwen1___5-7B-Chat")

def prompt1(x,y,z):
    #prompt = "Give me a short introduction to large language model."
    messages = [
        {"role": "system", "content": f'''你是海龟汤出题人，我们来玩一个叫做海龟汤的游戏。海龟汤是一种情景猜谜的推理游戏。其玩法是:出题者提出一个简单又难以理解的事件，
    玩家可以提出任何封闭式问题以试图缩小范围并找出事件背后真正的原因，封闭式问题指的是问题答案只能为："是。"或者"不是。"。如果玩家的问题不是一个封闭式问题，请回答："问法错误。"。
    海龟汤由汤面和汤底组成，汤面指的是海龟汤的题目，汤底指的是题目背后的真相。如果用户的问题和汤面和汤底不相关，请回答："不重要。",如果用户的答案命中了汤底的核心真相，且大部分内容都得到了还原，请回答："回答正确。"。游戏过程中，你需要根据汤底、汤面、玩家的问题，以及上述规则，判断并选择以下五个选项中的一个来回答玩家提出的问题，不能给出更多的提示。你的回答选项： [是。|不是。|不重要。|问法错误。|回答正确。]。最后玩家通过这些问题和回答来逐渐找到事件的真相，以下是一份海龟汤的汤面和汤底，
    汤面：[{x}]。汤底：[{y}]。请你扮演出题者的角色，我来扮演玩家的角色。由我先提问：'''},
        {"role": "user", "content": z}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(device)

    generated_ids = model.generate(
        model_inputs.input_ids,
        max_new_tokens=512
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response


test_a['answer'] = test_a.apply(lambda x:prompt1(x.puzzle,x.truth,x.text),axis=1)

test_a_baseline_pre = test_a
test_a_baseline_pre.to_csv('test_a_baseline_qwen1.5_p0.csv',index=False)