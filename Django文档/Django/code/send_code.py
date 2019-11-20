"""---author==hxj---"""
import json
import random
import re

import requests
from django.http import JsonResponse


def Send_code(request):
    TEL_PATTERN = re.compile(r'1[3-9]\d{9}')
    tel = request.GET.get('tel', '')
    if TEL_PATTERN.fullmatch(tel):
        code = ''.join(random.choices('0123456789', k=6))
        resp = requests.post(
            url='http://sms-api.luosimao.com/v1/send.json',
            auth=('api', 'key-c6305c397d86ab1093b46ad228e5a3fb'),
            data={
                'mobile': tel,
                'message': f'您的短信验证码是{code}，打死也不能告诉别人哟！【Python小课】'
            },
            timeout=10,
            verify=False
        )
        data = json.loads(resp.text)
        if data['error'] == 0:
            request.session['code'] = code
            result = {'code': 2000, 'message': '短信验证码发送成功'}
        else:
            result = {'code': 2002, 'message': '短信验证码发送失败'}
    else:
        result = {'code': 2001, 'message': '请输入有效的手机号码'}
    return JsonResponse(result)



