# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "AKAYoo/akayoo.github.io@master"
}

# 站点设置
site_name = "大王Wiki"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "AKAYoo"
email = "ayooo@189.cn"
author_homepage = "https://wiki.comzg.com"
description = "只坚持一种正义。我的正义。"
key_words = ['Maverick', 'AKAYoo', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "灯泡博客",
        "url": "https://blog.dpuuu.com",
        "brief": "灯泡博客的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/AKAYoo",
        "icon": "gi gi-github"
    },
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
