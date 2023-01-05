#-*- encoding: utf-8 -*-# -- coding: utf-8 --

# 目录

# 1. jwt认证流程
# 2. jwt创建token
# 2.1 原理
# 2.2 代码实现
# 3. jwt校验token

# 备注：参考 https://www.cnblogs.com/wupeiqi/p/11854573.html


# 1. jwt认证流程
# a. 流程：用户登录成功后，服务器返回给浏览器token,以后浏览器访问服务器都要带着token,服务器进行校验，校验成功才返回数据给浏览器
# b. jwt的token和传统token的区别：
# # 传统的token-用户登陆成功后，服务器给用户返回一个token，并且在服务端存一份，以后用户再来访问时，需要携带token，服务端收到token后去数据库或者缓存中去校验token是否超时，是否合法。
# # jwt的token-用户登陆成功后，服务器通过jwt生成一个随机token给用户（服务端无需保留token），以后用户每次来访问，需携带token,服务端收到后通过jwt进行解密校验，是否合法，校验成功返回数据。

# 2. jwt创建token
# 2.1 原理
## 由 . 连接的三段字符串构成。生成规则：
## 第一段：HEADER部分，包含算法类型和token类型，对此json进行base64url加密，这就是token的第一段。
# {
#   "alg": "HS256",
#   "typ": "JWT"
# }
## 第二段：PAYLOAD部分，包含一些数据，对此json进行base64url加密，这就是token的第二段
# {
#   "sub": "1234567890",
#   "name": "John Doe",
#   "iat": 1516239022
# }
## 第三段：SIGNATURE部分，把前两段的base密文通过.拼接起来，然后对其进行HS256加密，再然后对hs256密文进行base64url加密，最终得到token的第三段。
# base64url(
#     HMACSHA256(
#       base64UrlEncode(header) + "." + base64UrlEncode(payload),
#       your-256-bit-secret (秘钥加盐)
#     )
# )
# 2.2 代码实现

# import jwt
# import datetime
# from jwt import exceptions
#
# SALT = 'iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv='
#
#
# def create_token():
#     # 构造header
#     headers = {
#         'typ': 'jwt',
#         'alg': 'HS256'
#     }
#     # 构造payload
#     payload = {
#         'user_id': 1,  # 自定义用户ID
#         'username': 'wupeiqi',  # 自定义用户名
#         'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)  # 超时时间
#     }
#
#     # result = jwt.encode(payload=payload, key=SALT, algorithm="HS256", headers=headers).decode('utf-8')
#     result = jwt.encode(payload=payload, key=SALT, algorithm="HS256", headers=headers)
#     return result
#
# if __name__ == '__main__':
#     token = create_token()
#     print(token)
    # eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ind1cGVpcWkiLCJleHAiOjE2NTQ2NzE0ODl9.VF12AoHcGNZdpjRlXSy5MITy2kfIQU_6l7EGn3f_ES8

# 3. jwt校验token

import jwt
import datetime
from jwt import exceptions

SALT = 'iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv='
def get_payload(token):
    """
    根据token获取payload
    :param token:
    :return:
    """
    try:
        # 从token中获取payload【不校验合法性】
        # unverified_payload = jwt.decode(token, None, False)
        # print(unverified_payload)

        # 从token中获取payload【校验合法性】
        verified_payload = jwt.decode(token, SALT, True)
        return verified_payload
    except exceptions.ExpiredSignatureError:
        print('token已失效')
    except jwt.DecodeError:
        print('token认证失败')
    except jwt.InvalidTokenError:
        print('非法的token')


if __name__ == '__main__':
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzM1NTU1NzksInVzZXJuYW1lIjoid3VwZWlxaSIsInVzZXJfaWQiOjF9.xj-7qSts6Yg5Ui55-aUOHJS4KSaeLq5weXMui2IIEJU"
    payload = get_payload(token)