import json
import datetime

import jsonpath
import pytest
import requests

from api.tag import Tag
class Testtag:
    def setup_class(self):
        self.tag= Tag()

    @pytest.mark.parametrize("tag_id,tag_name",[
                             ['etL_AEDgAAmLkcZSXNBosVXWhnExVQaA','hogwarts01_aaaa'],
                             ['etL_AEDgAAmLkcZSXNBosVXWhnExVQaA','hogwarts01_bbbb'],
                             ['etL_AEDgAAmLkcZSXNBosVXWhnExVQaA','hogwarts01_ddddd']
                            ])
    def test_tag_list(self,tag_id,tag_name):
        group_name="hogwarts01"
        tag_id=tag_id
        tag_name = tag_name + str(datetime.datetime.now().strftime("%s"))

        r=self.tag.list()
        r=self.tag.update(id=tag_id,
                     tag_name = tag_name
                     )
        r=self.tag.list()
        tags=[]
        for group in r.json()['tag_group']:
            if group['group_name'] == group_name:
                for tag in group['tag']:
                    if tag['name'] == tag_name:
                        tags.append(tag)
        print(tags)
        # jsonpath(f"$..[?(@.name='{tag_name}')]")

        assert tags!=""

    def test_add_tag(self):

        add_group="GROUP_123"
        add_tag=[
                {"name": "TAG_NAME_1"},
                {"name": "TAG_NAME_2"},
                {"name": "TAG_NAME_3"},
                ]
        self.tag.add(groupname=add_group,tagname=add_tag)

    def test_list(self):
        self.tag.list()

    def test_delete(self):
        oldtag=["etL_AEDgAAv9KhmVVswhhbK9EdoI2aYw"]
        self.tag.delete_tag(oldtag)


    def test_add_and_detect_tag(self):

        add_group="GROUP_123"
        add_tag=[
                {"name": "TAG_NAME_1"},
                {"name": "TAG_NAME_2"},
                {"name": "TAG_NAME_3"},
                ]
        self.tag.add_and_detect(groupname=add_group,tagname=add_tag)