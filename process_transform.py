import pandas as pd

data = pd.read_csv('your_predict_result.csv')

# 做一定程度上的转换，转换不同说法但表达意思相同的答案。需写清说明。
def trans(ans):

    res = ans
    if len(ans)<25:
        if "是的。" in ans:
            res = "是。"
        if "问法错误。" in ans:
            res = "问法错误。"
        if "回答正确" in ans:
            res = "回答正确。"
        if "不重要。" in ans:
            res = "不重要。"
    return res
data['answer_trans'] = data['answer'].apply(lambda x: trans(x))

print(f"acc is :{len(data[data['label']==data['answer_trans']])/len(data)}")

data.to_csv('./final_predict_result.csv')