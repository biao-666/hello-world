print("hello word")
import time
import requests

now_time = time.time()
print("部署jenkins测试！！！")
print(now_time)
print('cqbteset')

# 这是个测试
url = 'http://www.weather.com.cn/data/sk/101010100.html'
r = requests.get(url)
print(f"返回数据编码{r.encoding}")
r.encoding = 'utf-8'
print(r.text)
print(r.json())
