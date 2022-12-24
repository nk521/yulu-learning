import requests
import os
from Crypto.Cipher import AES
import binascii

jwt_key = os.environ.get("YULU_JWT")

headers = {
    "Host": "ipa.passion.bike",
    "Accept": "application/json",
    "Authorization": f"Bearer {jwt_key}",
    "Accept-Language": "en",
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "okhttp/4.9.1",
}

# rest of the data doesn't really matter
json_data = {
    "bikeQrCode": "5005028",
    "latitude": 28.630718048073033,  # any available city's lat long
    "longitude": 77.000000000000000,
    "sourcetype": "android",
    "version_code": 4417000,
}


response = requests.post(
    "https://ipa.passion.bike/s/ride-request-unlock",
    headers=headers,
    json=json_data,
)
print(response.text)

response_json = response.json()

if not response_json.get("bike", 0):
    print("fucked up")

iv = response_json["bike"]["device_info"]["iv"].encode()
encrypted_text = binascii.unhexlify(
    response_json["bike"]["device_info"]["encryptedData"]
)
key = b"SSNUBSMCRNPASCAS"  # 53534e5542534d43524e504153434153
expected = b"00112233445566778899aabbccddeeff\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10"

cipher = AES.new(key, AES.MODE_CBC, iv=binascii.unhexlify(iv))

if cipher.decrypt(encrypted_text) == expected:
    print("good key")
