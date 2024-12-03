import sqlite3

conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()


cur.execute("DELETE FROM gold_admin")
conn.commit()
conn.close()
# import requests
# import base64
# def createApiUser():
      
#       headers = {'Accept': '*/*',
#                   'Content-Type': 'application/json',
#                   'X-Reference-Id': '9e84a13a-b931-42b9-ad7b-64340411c500',
#                   'Ocp-Apim-Subscription-Key': '3edd8df4a822438297e3ef23e70c3aca',}
#       data={
#             "providerCallbackHost": "https://webhook.site/fc2a2731-9a9b-476e-a40c-5aabf5592dd3"
#             }
#       r = requests.post('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser',json=data, headers = headers)
#       print(r.json)
# # createApiUser()

# def GetApiUserInfo():
#       headers = {'Accept': '*/*',
#                  'Content-Type': 'application/json',
#                  'Ocp-Apim-Subscription-Key': '3edd8df4a822438297e3ef23e70c3aca',
#       }
      
#       params={
#             'X-Reference-Id': '9e84a13a-b931-42b9-ad7b-64340411c500'
#       }
      
#       r = requests.get('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/ae8231b8-d56a-4fa7-9e57-96fe55ee15cb',params=params,headers = headers)
#       print(r)
# # GetApiUserInfo()


# def CreateApiKey():
      
#       headers = {'Accept': '*/*',
#                  'Content-Type': 'application/json',
#                  'Ocp-Apim-Subscription-Key': '3edd8df4a822438297e3ef23e70c3aca',
#       }
      
#       params={
#             'X-Reference-Id': '9e84a13a-b931-42b9-ad7b-64340411c500'
#       }
      
#       r = requests.post('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/9e84a13a-b931-42b9-ad7b-64340411c500/apikey',params=params,headers = headers)
#       print(r.text)
      
#       {"apiKey":"b03c903926034ffcb76408582064da3d"}
# # CreateApiKey()  


# def generate_authorization(user, key):
#     # Concatenate user and key with a colon
#     auth_string = f"{user}:{key}"
    
#     # Encode the string in Base64
#     auth_bytes = auth_string.encode('utf-8')  # Convert to bytes
#     auth_b64 = base64.b64encode(auth_bytes).decode()  # Encode and decode back to string
    
#     return f"Basic {auth_b64}"

# # Example usage:
# user = "9e84a13a-b931-42b9-ad7b-64340411c500"
# key = "b03c903926034ffcb76408582064da3d"
# # authorization_value = generate_authorization(user, key)
# # print("Authorization Header Value:", authorization_value)    

# def CreateAccessToken():
#       # user = "9e84a13a-b931-42b9-ad7b-64340411c500"
#       # key = "b03c903926034ffcb76408582064da3d"
#       # auth_string = f"{user}:{key}"
#       # auth_b64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
#       # athkey = f"Basic {auth_b64}"
#       # print(athkey)
#       headers = {'Accept': '*/*',
#                  'Content-Type': 'application/json',
#                  'Ocp-Apim-Subscription-Key': '55d237aeb9b04db59cbeb8751f6e8df4',
#                  'Authorization': "Basic OWU4NGExM2EtYjkzMS00MmI5LWFkN2ItNjQzNDA0MTFjNTAwOmIwM2M5MDM5MjYwMzRmZmNiNzY0MDg1ODIwNjRkYTNk",
#             #      "apiKey":"30dae6e8bb7743d7b7b186c413ad8569"
#       }      
#       r = requests.post('https://sandbox.momodeveloper.mtn.com/collection/token/', headers = headers)
#       print(r.json())
      
#       {'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjllODRhMTNhLWI5MzEtNDJiOS1hZDdiLTY0MzQwNDExYzUwMCIsImV4cGlyZXMiOiIyMDI0LTExLTEyVDA2OjMwOjIyLjM4MyIsInNlc3Npb25JZCI6ImJkOGU2NjJiLTU1OTItNGZhMC05MzRiLWZlYTI1Nzg3OTY1MCJ9.J1D6wyAePJyOk6r20NHG7XDLvyt1mBA78aFxOKcKIY9sjH0RllMV2fc2mzXRJ4-om6v9EO1dwtcLiKyasqNIddbDxJae0zp-J5DSaFVH2DuOjXAt5VVHTr5bmkrw8qv1bnmjhnKSYLfbFWpUl-gJxASeG69bupZgdaFyzxG1ONsUlERhSl8tSlbICHixV14BKzUUU4u7u56lO08GytfUPxg292idU3N40ePWxCEUbbO7nRkhGWgubtwA3MEPOBufMu4p8Fk97j-Ck7yrMqPH70AMmyw_GalXsbngkTIxIBKoL3Sv-55le-xWZm5KOkgluYtBD0mxSZnYceCZPKFkJA', 'token_type': 'access_token', 'expires_in': 3600}
      
# # CreateAccessToken()


# def RequestToPay():
#       accesToken = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjllODRhMTNhLWI5MzEtNDJiOS1hZDdiLTY0MzQwNDExYzUwMCIsImV4cGlyZXMiOiIyMDI0LTExLTEyVDA5OjIxOjU0LjYwMyIsInNlc3Npb25JZCI6Ijk5YTVmNjc5LTcwNGUtNDUzNC05MDljLTI2MWM2NTQ4M2ViNyJ9.RHB6Hoyqo34TwEu6KSLH_3zzgsYjHMNbiOjLs4wCf_2pislE08VsCjyzgWl4AqMGl2n5vTpMTWo2RkNLxKPbJvzf7njiHsFuiAETCg1jEMGolQT5ClSjC-Zvtym23aWJOXXPkD3-V0rpxdeQyP89HvVeb8bHeiMpHFhNoL3JiKP_AohSB7_yUU5QTvBCfx9hnv5nAVfk5-JbnaJ600rtBxvSlfllxi_3yJCEMmeJ44ro9sGlBXZ1AW8esneUdWkYta8tQy8BPEKlg4D5HDAAIuMY45Zqv_pcRn4CGHOsdcIhZybGie_KTxnOobMM_C7qguj29AOFKVOiAj3E4IwUHA'
#       headers = {'Accept': '*/*',
#                  'Content-Type': 'application/json',
#                  'Ocp-Apim-Subscription-Key': '55d237aeb9b04db59cbeb8751f6e8df4',
#                  'Authorization': accesToken,
#                  'X-Reference-Id': '10ae6c43-cde0-4383-98b5-6b379475750d',  #THIS IS FORTHE TRASACTION NOT FOR THE CREATED USER 
#             #      'X-Callback-Url': "https://webhook.site/fc2a2731-9a9b-476e-a40c-5aabf5592dd3",
#                  'X-Target-Environment': "sandbox"
#       }
      
#       body={
#             "amount": "10.0",
#             "currency": "EUR",
#             "externalId": "12345678",
#             "payer": {
#                   "partyIdType": "MSISDN",
#                   "partyId": "12345678"
#             },
#             "payerMessage": "testing",
#             "payeeNote": "testing1"
#             }
#       r = requests.post('https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay',json=body, headers = headers)

#       print(r)
# RequestToPay()      
