### 3장\_공개키 암호 (Public-key Cryptography)

대칭키 암호의 문제점인 키의 전달에서 발생하는 취약점을 해결하고자 만들어진 암호 방식 <br />

Public key, Private key가 한 쌍으로 존재하여, <br />

- 개인키 암호화 -> 공개키 복호화 <br />
- 공개키 암호화 -> 개인키 복호화 <br />
  의 방식으로 동작합니다

그래서 공개키 암호를 비대칭키 암호라고도 부릅니다.

종류로는 <br />
DH (Diffie-Hellman), DSA (Digital Signature Algorithm), ECDH (Elliptic Curve DH), ECDSA (Elliptic Curve DSA), ElGamal, RSA <br />
가 있습니다.

#### 공개키의 원리?

원리는 간단합니다 <br />
대칭키는 XOR 연산이 원리였다면, <br />
공개키는 특정 정보 없이는 매우 풀기 어려운 수학문제를 기반으로 합니다 <br />

- 매우 큰 수의 소인수분해 <br />
  ex) RSA (Rivest-Shamir-Adleman)

c = a x b 일 때, c를 가지고 a, b를 구하여라 <br />
c (public) / a (private) <br />
c / a = b (easy) | c = a x ? (hard) <br />

- 이산로그방정식의 해 구하기 <br />
  Elliptic Curve Cipher <br />
  ex) ECDH, ECDSA

#### 공개키 암호, 서명, 공개키 기반 구조

- 공개키 암호 : 개인키로 암호화 - 공개키로 복호화 <br />
- 공개키 서명 : 암호화된 정보가 특정 사람이 암호화하여 보냈다는 걸 확신할 수 있게 해주는 방식 <br />
- 공개키 기반 구조 (PKI) : 공개키와 개인키가 위조된 경우 해당 정보가 위조되었는 지를 알 수 없는 등의 문제를 해결하기 위한 디지털 인증서들
