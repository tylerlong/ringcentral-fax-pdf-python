from ringcentral_client import RestClient
import json

rc = RestClient("clientId", "clientSecret", 'https://platform.ringcentral.com')
rc.authorize('usernae', 'extension', 'password')

with open('/Users/tyler.liu/Desktop/google.pdf', 'rb') as pdf_file:
    files = [
      ('json', ('request.json', json.dumps({ 'to': [{ 'phoneNumber': '16506417402' }] }), 'application/json')),
      ('attachment', ('test.pdf', pdf_file, 'application/pdf')),
    ]
    r = rc.post('/restapi/v1.0/account/~/extension/~/fax', files = files)
    print(r.status_code)
