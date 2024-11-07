import sqlite3

conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()


cur.execute("DELETE FROM gold_products")
conn.commit()
conn.close()

# # Prepare the data for the request
# import requests
# import hmac
# import hashlib
# # from Crypto.Cipher import AES
# # from Crypto.Random import get_random_bytes
# import base64

# # Secret provided by the API
# secret_key = b'YOUR_SECRET_KEY'

# # Payload to be sent
# payload = '{"data":"sample"}'  # Example payload

# # Step 1: Create the signature
# signature = hmac.new(secret_key, payload.encode('utf-8'), hashlib.sha256).digest()

# # Step 2: Encrypt the signature with AES
# aes_key = get_random_bytes(16)  # AES key (128-bit)
# cipher = AES.new(aes_key, AES.MODE_CBC)
# iv = cipher.iv

# # Padding the signature for AES
# padding_length = AES.block_size - len(signature) % AES.block_size
# padded_signature = signature + bytes([padding_length]) * padding_length

# encrypted_signature = cipher.encrypt(padded_signature)
# # Base64 encode for headers
# x_signature = base64.b64encode(encrypted_signature).decode('utf-8')
# x_key = base64.b64encode(aes_key + iv).decode('utf-8')

# print("x-signature:", x_signature)
# print("x-key:", x_key)

# headers = {
#     'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
#     'Content-Type': 'application/json',
#     'X-Country': 'UG',
#     'X-Currency': 'UGX',
#     'x-signature': x_signature,
#     'x-key': x_key
# }

# response = requests.post('https://openapiuat.airtel.africa/merchant/v2/payments/', json=payload, headers=headers)
# print(response.json())

