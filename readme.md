# baseline说明

1、base模型采用qwen1.5-7b-chat模型，未做微调。 模型下载地址：https://www.modelscope.cn/models/qwen/Qwen1.5-7B-Chat/summary

2、运行环境：单卡24g ，使用半精度形式即可加载推理

3、推理代码可参考 qwen7b_pre.py 文件，包含prompt示例，与模型加载推理代码示例

4、推理完成后，允许参考process_transform.py 文件，做一定程度上的转换，转换内容仅限于：由于模型的不稳定输出的不同说法但表达意思相同的答案，如“是的。”允许转换为“是。”

5、baseline在测试集A的准确率约为36.5%