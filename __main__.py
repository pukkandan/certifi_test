import certifi
import ssl


print(certifi.where())

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile=certifi.where())
