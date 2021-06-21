import base64
import Crypto.Random

def generate_key(bits, encode=False):
    content = Crypto.Random.get_random_bytes(bits // 8)

    if(encode):
        return base64.b64encode(content)

    return content

if __name__ == "__main__":
    print(generate_key(32))
