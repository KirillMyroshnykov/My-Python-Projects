import hashlib

secret_key = 'yzbqklnj'

i = 0

message = secret_key + str(i)

md5_code = hashlib.md5(message.encode()).hexdigest()

while md5_code[:6] != '000000':
    i += 1
    message = secret_key + str(i)
    md5_code = hashlib.md5(message.encode()).hexdigest()

# print(message)
# print(md5_code)
print(i)