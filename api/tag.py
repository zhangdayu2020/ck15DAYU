import requests

import json
class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpsecret = "4Y8E2yFo3qNuWKNHmq16eiF28nqhrEkmFNxn9oTyQmg"
        corpid = 'ww3ba71edc4fc65297'
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={"corpid": corpid, "corpsecret": corpsecret}
                         )
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # print(json.dumps(r.json(), indent=2))
        token = r.json()['access_token']
        return token


    # "errcode": 40071,
    # "errmsg": "UserTag Name Already Exist, hint: [1611461360_130_be4fe58a65154a268d176f62f0d5d51b], from ip: 116.76.73.52, more info at https://open.work.weixin.qq.com/devtool/query?e=40071"
    def add(self,groupname,tagname,**kwargs):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token":self.token},
            json={
                "group_name":groupname,
                "tag": tagname,
                **kwargs
                        }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def find_group_id_by_name(self,group_name):
        for group in self.list().json()["tag_group"]:
            if group_name in group["group_name"]:
                return group["group_id"]
        print("group name not in group")
        return ""



    def add_and_detect(self,groupname,tagname,**kwargs):
        r=self.add(groupname,tagname,**kwargs)
        if r.json()['errcode']==40071:
            group_id=self.find_group_id_by_name(groupname)
            self.delete_group(group_id)
            r = self.add(groupname, tagname, **kwargs)
        print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={'tag_id': []}

        )
        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, tag_name):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            params={'access_token': self.token},
            json={"id": ("%s" % id),
                  "name": tag_name
                  }
        )

        print(json.dumps(r.json(), indent=2))
        return r

    # "errcode": 40068,
    # "errmsg": "invalid tagid,
    def delete_group(self,groupid):
        r=requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token":self.token},
            json={"group_id":groupid}

        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete_tag(self,tagid):
        r=requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token":self.token},
            json={
                "tag_id": tagid

            }

        )
        print(json.dumps(r.json(), indent=2))
        return r