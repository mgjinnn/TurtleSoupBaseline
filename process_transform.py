import pandas as pd

# data = pd.read_csv('test_b_baseline_qwen1.5_7b.csv',encoding='utf8')
# data = pd.read_csv('predict_result_glm4.csv',encoding='gbk')
# data = pd.read_csv('predict_result_14b.csv',encoding='gbk')
# data = pd.read_csv('test_a_baseline_qwen1.5_7b.csv',encoding='gbk')
# data = pd.read_csv('test_b_glm4-9b-result.csv',encoding='gbk')
# data = pd.read_csv('test_b_baseline_qwen1.5_7b.csv',encoding='gbk')
# data = pd.read_csv('final_testa_glm4_predict_result.csv',encoding='gbk')
# data = pd.read_csv('test_a_predict_result_glm4.csv',encoding='gbk')
# data = pd.read_csv('dev_predict_result_glm4.csv',encoding='utf8')
data = pd.read_csv('dev_glm4_9b_predict_result.csv',encoding='gbk')
print(len(data))
# data=data[data['label']!='不重要。']
print(len(data))
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
        if "不是。" in ans:
            res = "不是。"
    return res
data['answer'] = data['answer'].apply(lambda x: trans(x))

print(f"old label acc is :{len(data[data['label']==data['answer']])/len(data)}")

# print(f"new label acc is :{len(data[data['new_label']==data['answer']])/len(data)}")
#
print(f"glm4 label acc is :{len(data[data['label']==data['glm4']])/len(data)}")
# data.to_csv('./final_predict_result.csv')