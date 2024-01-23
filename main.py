import json
from datetime import datetime
from RssFeeder import check_rss_update

import requests

WEBHOOK_URL = "xxxxx"

#实现飞书的webhook功能
def webhook(data:dict) -> None:

    params = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh-CN": {
                    "title": "漏洞资料推送！",
                    "content": []
                }
            }
        }
    }

    for items in data:
        element = [
            {
                "tag": "text",
                "text": items
            },
            {
                "tag": "a",
                "text": "点击查看",
                "href": data[items]
            }
        ]
        params["content"]["post"]["zh-CN"]["content"].append(element)
    print(json.dumps(params, indent=4, ensure_ascii=False))

    resp = requests.post(WEBHOOK_URL, json=params)
    resp.raise_for_status()
    result = resp.json()
    if result.get("code") and result.get("code") != 0:
        print(f"发送失败：{result['msg']}")
        return
    print("消息发送成功")

if __name__ == '__main__':
    list=[]
    data=check_rss_update("https://tttang.com/rss.xml")
    webhook(data)


