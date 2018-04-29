import random
# y^2= x^3 + ax + b where a=0 and b=7 which is the secp256k1 curve bitcoin uses

Pcurve = (2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1) # The proven prime
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field
Acurve = 0
Bcurve = 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
GPoint = (Gx,Gy) # This is our generator point. Trillions of dif ones possible

privKey = 0x95467A77DE3729968FC03762CE2E77358721B5783B374DA45AC0293E350FD1B5 #75263518707598184987916378021939673586055614731957507592904438851787542395619 #0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E
randNumber = 28695618543805844332113829720373285210420739438570883203839696518176414791234
HashOfThingToSign = 86032112319101611046176971828093669637772856272773459297323797145286374828050


def generatePrivateKey():
    privateKeyArray = []
    for i in range(0, 256):
        bit = random.randint(1,100)
        if bit > 50:
            bit = 1
        else:
            bit = 0
        privateKeyArray.append(str(bit))

    privateKeyBinary = int(''.join(privateKeyArray))
    privateKeyDecimal = int(str(privateKeyBinary), 2)
    privateKeyHex = hex(privateKeyDecimal)


    if privateKeyDecimal > 115792089237316195423570985008687907852837564279074904382605163141518161494336:
        raise Exception("Private key generation not in range please retry")

    print("Private Key Binary: " + str(privateKeyBinary))
    print("Private Key Decimal: " + str(privateKeyDecimal))
    print("Private Key Hex: " + str(privateKeyHex))

    return int(privateKeyHex, 16)

def modinv(a,n=Pcurve): #Extended Euclidean Algorithm/'division' in elliptic curves
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = high//low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n

def ECadd(a,b): # Not true addition, invented for EC. Could have been called anything.
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) % Pcurve # lambda = (Yq -Yp)/(Xq - Xp) where q and p are the point to be added
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve # Xr = lambda^2 - Xp - Xq where r is the resultant point
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve # Yr = lambda(Xp -Xr) - Yp where r is the resultant point
    return (x,y)

def ECdouble(a): # This is called point doubling, also invented for EC.
    Lam = ((3*a[0]*a[0]+Acurve) * modinv((2*a[1]),Pcurve)) % Pcurve # Lambda = (3Xp^2 + a)/2Yp
    x = (Lam*Lam-2*a[0]) % Pcurve # lambda^2 - 2Xp = Xr
    y = (Lam*(a[0]-x)-a[1]) % Pcurve # lambda(Xp - Xr) - Yp = Yr
    return (x,y)

def EccMultiply(GenPoint,ScalarHex): #Double & add. Not true multiplication
    if ScalarHex == 0 or ScalarHex >= N:
        raise Exception("Invalid Scalar/Private Key")
    scalarBin = str(bin(ScalarHex))[2:]
    Q = GenPoint
    for i in range (1, len(scalarBin)): # This is invented EC multiplication.
        Q = ECdouble(Q) # print "DUB", Q[0]; print
        if scalarBin[i] == "1":
            Q = ECadd(Q,GenPoint) # print "ADD", Q[0]; print

    print(Q)
    return Q

def generatePublicKey(privateKey):
    publicKey = EccMultiply(GPoint, privateKey)
    print("******* Public Key Generation *********")
    print("the private key:" + str(privateKey))
    print("the uncompressed public key (not address): " + str(publicKey))
    print("the uncompressed public key (HEX): " + "04" + "064" + str(publicKey[0]) + "064" + str(publicKey[1]))
    print("the official Public Key - compressed:")
    if publicKey[1] % 2 == 1: # If the Y value for the Public Key is odd.
        print("03"+str(hex(publicKey[0])[2:]).zfill(64))
    else: # Or else, if the Y value is even.
        print("02"+str(hex(publicKey[0])[2:]).zfill(64))
    return publicKey

# s = 0
# r = 0
# xPublicKey = 0
# yPublicKey = 0

def signatureGeneration():
    xPublicKey, yPublicKey = EccMultiply((Gx, Gy), privKey)
    xRandSignPoint, yRandSignPoint = EccMultiply((Gx, Gy), randNumber)
    r = xRandSignPoint % N
    s = ((HashOfThingToSign + r * privKey ) * (modinv(randNumber, N))) % N
    print("the signature is (r,s) " + "(" + str(r) + "," + str(s) + ")")
    return (r, s)

def signatureVerification(r, s):
    w = modinv(s, N)
    xu1, yu1 = EccMultiply((Gx, Gy), (HashOfThingToSign * w) % N)
    xu2, yu2 = EccMultiply((xPublicKey, yPublicKey), (r*w) % N)
    x, y = ECadd((xu1, yu1), (xu2, yu2))
    print(r == x)


pKey = generatePrivateKey()
xPublicKey, yPublicKey = generatePublicKey(privKey)

r, s = signatureGeneration()
signatureVerification(r, s)
