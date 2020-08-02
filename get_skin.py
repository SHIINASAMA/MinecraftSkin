# 获取UUID
# https://api.mojang.com/users/profiles/minecraft/ID
# 获取皮肤地址
# https://sessionserver.mojang.com/session/minecraft/profile/UUID

import requests
import json
import base64

user_name = input('请输入你的Minecraft Java版ID:')
uuid_url = 'https://api.mojang.com/users/profiles/minecraft/' + user_name

print('正在获取UUID')
response = requests.get(uuid_url)
print('返回内容：')
print(response.text)

user_profile = json.loads(response.text)
uuid = user_profile['id']

skin_url = 'https://sessionserver.mojang.com/session/minecraft/profile/'
print('正在获取皮肤地址')
response = requests.get(skin_url + uuid)
print('返回内容：')
print(response.text)

print('正在解码base64数据')
user_profile = json.loads(response.text)
properties = user_profile.get('properties')
data_base64 = properties[0]['value']
user_profile_str = base64.b64decode(data_base64).decode("utf-8")
user_profile = json.loads(user_profile_str)
download_url = user_profile['textures']['SKIN']['url']
print('皮肤下载地址为：' + download_url)

print('开始下载')
response = requests.get(download_url)
with open(user_name+'.png','wb')as code:
    code.write(response.content)
print('下载完成')