# baseline说明
本baseline参考glm4官网:https://github.com/THUDM/GLM-4.git

1、安装环境:pip install -r requirements.txt 具体环境要求请查看https://github.com/THUDM/GLM-4/blob/main/basic_demo/README.md

2、启动服务端：
```shell
python openai_api_server.py
```
3、运行硬件环境：单卡24g 

4、启动预测
```shell
python test_re.py
```

5、推理完成后，允许参考process_transform.py 文件，做一定程度上的转换，转换内容仅限于：由于模型的不稳定输出的不同说法但表达意思相同的答案，如“是的。”允许转换为“是。”
