Pcurve = (2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1) # The proven prime
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field
Acurve = 0
Bcurve = 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
GPoint = (Gx,Gy) # This is our generator point. Trillions of dif ones possible

privKey = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E

def modinv(a,n=Pcurve): #Extended Euclidean Algorithm/'division' in elliptic curves
    lm = 1
    hm = 0
    low = a % n
    high = n
    while low > 1:
        ratio = high/low
        nm = hm-lm*ratio
        new = high-low*ratio
        lm = nm
        low = new
        hm = lm
        high = low
    return lm % n

def ECadd(a,b): # Not true addition, invented for EC. Could have been called anything.
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) % Pcurve
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
    return (x,y)