#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:10:37 2019

@author: luyali
"""

import requests
import json

class get_api():
    repo_dict={}
    def get_info_api(name):
        url = 'https://api.github.com/users/'+name+'/repos'
        r=requests.get(url)
        print(r.status_code)


        print("The user has "+str(len(r.json())) + " repos, names and commits as follows: ")
        for item in r.json():
            url_comm = 'https://api.github.com/repos/'+name+'/'+item['name']+'/commits'
            s=requests.get(url_comm)
            commits_list=s.json()
            commits_dict=commits_list[0]
            print("Name: " +item['name']+"; Commits: "+str(len(commits_dict)))

        return "Right"
