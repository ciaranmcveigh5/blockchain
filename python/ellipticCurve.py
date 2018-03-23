import random
# y^2= x^3 + ax + b where a=0 and b=7 which is the secp256k1 curve bitcoin uses

Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field
Acurve = 0; Bcurve = 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
GPoint = (Gx,Gy) # This is our generator point. Trillions of dif ones possible

Gx_Compressed = hex(Gx)
print(Gx_Compressed)

privateKeyArray = []

for i in range(0, 256):
    bit = random.randint(0,100)
    if bit > 50:
        bit = 1
    else:
        bit = 0
    privateKeyArray.append(str(bit))


privateKeyBinary = int(''.join(privateKeyArray))
print(privateKeyBinary)

privateKeyDecimal = int(str(privateKeyBinary), 2)
privateKeyHex = hex(privateKeyDecimal)

print(privateKeyDecimal)
if privateKeyDecimal <= 115792089237316195423570985008687907852837564279074904382605163141518161494336:
    print('true')
print(privateKeyHex)

def modinv(a,n=Pcurve): #Extended Euclidean Algorithm/'division' in elliptic curves
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = high/low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n

def ECadd(a,b): # Not true addition, invented for EC. Could have been called anything.
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) % Pcurve # lambda = (Yq -Yp)/(Xq - Xp) where q and p are the point to be added
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve # Xr = lambda^2 - Xp - Xq where r is the resultant point
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve # Yr = lambda(Xp -Xr) - Yp where r is the resultant point
    return (x,y)