import json
import datetime

import jsonpath
import requests

def test_tag_list():
    corpsecret = "4Y8E2yFo3qNuWKNHmq16eiF28nqhrEkmFNxn9oTyQmg"
    corpid = 'ww3ba71edc4fc65297'
    r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                   params={"corpid": corpid, "corpsecret": corpsecret}
                   )
    assert r.status_code==200
    assert r.json()['errcode'] == 0
    print(json.dumps(r.json(), indent=2))
    token=r.json()['access_token']
    r=requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={'access_token':token},
        json={'tag_id':[]}

    )
    print("======")
    print(json.dumps(r.json(),indent=2))
    print("======")
    assert r.status_code==200
    assert r.json()['errcode'] == 0
    tag_name="hogwarts01_1_update"+str(datetime.datetime.now().strftime("%s"))
    print(tag_name)
    r=requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
        params={'access_token': token},
        json={"id":"etL_AEDgAAmLkcZSXNBosVXWhnExVQaA",
              "name":tag_name
              }
    )
    print("======")
    print(json.dumps(r.json(),indent=2))
    print("======")
    assert r.status_code==200
    assert r.json()['errcode'] == 0

    # tags = []
    print(r.raw)
    r=requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={'access_token':token},
        json={'tag_id':["etL_AEDgAAmLkcZSXNBosVXWhnExVQaA"]}

    )
    tags=[]
    for group in r.json()['tag_group']:
        if group['group_name'] == 'hogwarts01':
            for tag in group['tag']:
                if tag['name'] == tag_name:
                    tags.append(tag)
    print(tags)
    jsonpath(f"$..[?(@.name='{tag_name}')]")

    assert tags!=""