# coding:utf-8
import json
import jwt
import requests
import time


# model_type = 'glm-3-turbo'
model_type = 'glm-4'

def generate_token(apikey: str, exp_seconds: int):
    try:
        id, secret = apikey.split(".")
    except Exception as e:
        raise Exception("invalid apikey", e)

    payload = {
        "api_key": id,
        "exp": int(round(time.time() * 1000)) + exp_seconds * 1000,
        "timestamp": int(round(time.time() * 1000)),
    }

    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )

def zhipu_sdk(text,history=[],temperature=0.1):
    messages = [
        {
            "role": "user",
            "content": text
        }
    ]
    messages = history +messages
    zhipu_api = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
    apikey = '32a3174f1d2e25a60c59e481f2d4fb8d.X9IShFEX6OK8Md64'
    data = json.dumps({
        "model":model_type,
        "messages":messages,
        "temperature": temperature
    })
    token = generate_token(apikey, 60)
    # print(token)
    # Authorization
  #   headers = {"Authorization":token,'Content-Type': 'application/json',
  # 'Cookie': 'acw_tc=784e2c8f17084990990047570e6a6ad690e149974607208376739d02200629'}
    headers = {"Authorization": token, 'Content-Type': 'application/json'}
    res = requests.post(url=zhipu_api, data=data, headers=headers)
    # print(res)
    if res.status_code == 200:
        #print(res.json()['choices'][0])
        result = res.json()['choices'][0]['message']['content']
    else:
        result = ''
    return result
        
   

if __name__ == '__main__':
    # print(zhipu_chat(
    #     '你是谁'))
    # start=time.time()
    # print(zhipu_draw(
    #     '帮我画一只小猫的图片'))
    prompt_norm_5 = '你是一个商品标题总结器，请从下面商品标题直接提炼出一个5字以内的商品标题：'
    # prompt_norm_5 = '你是一个商品简称提取器，请从下面商品标题直接提炼出一个5字以内的商品简称：'
    prompt_norm_10 = '你是一个商品标题总结器，请从下面商品标题直接提炼出一个10字以内的商品标题：'
    prompt="%s。优化成%s个字短标题"
    texts=['GLACIERBOY ROCK CANDY NECKLACE 混合镶嵌圆形冰糖项链 银色','goco够酷潮玩 Nicole甜蜜世界系列盲盒一套全套大礼包 拆盲盒 周末及节假日不发货','notime 美容仪器家用童颜机面膜脸部红蓝光导入光谱面罩光子嫩肤仪 SKB-1818P','youppiestaywithme2021新款黑桃公主飘带连衣裙 设计感可爱泡泡袖连衣裙','【杨超越同款】ABYBCHARMING星晴 颈链珍珠个性项链女ins冷淡风潮流锁骨链网红','EGOGO 太空船投影灯 星空灯投影仪满天星房间卧室创意浪漫梦幻星星灯小夜灯创意礼品礼物','MadeByDizon渐变多层笑脸项链 轻机能工业锁链式短链 不褪色asap rocky','纵贯线 野餐垫加厚便携户外垫子露营帐篷沙滩垫防水防沙防潮垫125*145cm CD-05','SIUU西佑 灭蚊灯家用室内卧室宿舍杀蚊孕妇婴幼儿儿童驱蚊神器紫外光触媒物理静音可爱自动','【现货】包邮『蛋包饭&冰淇淋』20/40cm套装无属性棉花娃衣可爱连体爬爬服玩偶公仔衣服']
    for text in texts:
        send_input=prompt_norm_5+text
        print(zhipu_sdk(send_input,[]))
    # print(time.time()-start)
