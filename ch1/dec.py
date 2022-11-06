import enc


def decryption():
    print('Decryption')


if __name__ == '__main__':
    print('dec.py가 메인임')
    enc.encryption()
    decryption()
else:
    print('dec.py가 다른 모듈에서 import되어 사용됨')

'''
enc import 후 if __name__ == '__main__' 들어간 후 else 문 수행 (dec.py 실행했으므로)
dec.py의 if __name__ == '__main__' 들어가서 수행

실행결과
enc.py가 다른 모듈에서 import되어 사용됨
dec.py가 메인임
Encryption
Decryption
'''
