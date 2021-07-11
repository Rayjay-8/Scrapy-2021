import js2py
import os
import urllib.parse

va = """
var t = {
compressToBase64: function(e) {
if (null == e)
return "";
var i = t._compress(e, 6, (function(t) {
return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".charAt(t)
}
));
switch (i.length % 4) {
default:
case 0:
return i;
case 1:
return i + "===";
case 2:
return i + "==";
case 3:
return i + "="
}
},
_compress: function(t, e, i) {
if (null == t)
return "";
var n = void 0
, a = void 0
, o = {}
, r = {}
, s = ""
, l = ""
, u = ""
, c = 2
, d = 3
, f = 2
, h = []
, p = 0
, m = 0
, v = void 0;
for (v = 0; v < t.length; v += 1)
if (s = t.charAt(v),
Object.prototype.hasOwnProperty.call(o, s) || (o[s] = d++,
r[s] = !0),
l = u + s,
Object.prototype.hasOwnProperty.call(o, l))
u = l;
else {
if (Object.prototype.hasOwnProperty.call(r, u)) {
    if (u.charCodeAt(0) < 256) {
        for (n = 0; n < f; n++)
            p <<= 1,
            m == e - 1 ? (m = 0,
            h.push(i(p)),
            p = 0) : m++;
        for (a = u.charCodeAt(0),
        n = 0; n < 8; n++)
            p = p << 1 | 1 & a,
            m == e - 1 ? (m = 0,
            h.push(i(p)),
            p = 0) : m++,
            a >>= 1
    } else {
        for (a = 1,
        n = 0; n < f; n++)
            p = p << 1 | a,
            m == e - 1 ? (m = 0,
            h.push(i(p)),
            p = 0) : m++,
            a = 0;
        for (a = u.charCodeAt(0),
        n = 0; n < 16; n++)
            p = p << 1 | 1 & a,
            m == e - 1 ? (m = 0,
            h.push(i(p)),
            p = 0) : m++,
            a >>= 1
    }
    0 == --c && (c = window.Math.pow(2, f),
    f++),
    delete r[u]
} else
    for (a = o[u],
    n = 0; n < f; n++)
        p = p << 1 | 1 & a,
        m == e - 1 ? (m = 0,
        h.push(i(p)),
        p = 0) : m++,
        a >>= 1;
0 == --c && (c = window.Math.pow(2, f),
f++),
o[l] = d++,
u = String(s)
}
if ("" !== u) {
if (Object.prototype.hasOwnProperty.call(r, u)) {
if (u.charCodeAt(0) < 256) {
    for (n = 0; n < f; n++)
        p <<= 1,
        m == e - 1 ? (m = 0,
        h.push(i(p)),
        p = 0) : m++;
    for (a = u.charCodeAt(0),
    n = 0; n < 8; n++)
        p = p << 1 | 1 & a,
        m == e - 1 ? (m = 0,
        h.push(i(p)),
        p = 0) : m++,
        a >>= 1
} else {
    for (a = 1,
    n = 0; n < f; n++)
        p = p << 1 | a,
        m == e - 1 ? (m = 0,
        h.push(i(p)),
        p = 0) : m++,
        a = 0;
    for (a = u.charCodeAt(0),
    n = 0; n < 16; n++)
        p = p << 1 | 1 & a,
        m == e - 1 ? (m = 0,
        h.push(i(p)),
        p = 0) : m++,
        a >>= 1
}
0 == --c && (c = window.Math.pow(2, f),
f++),
delete r[u]
} else
for (a = o[u],
n = 0; n < f; n++)
    p = p << 1 | 1 & a,
    m == e - 1 ? (m = 0,
    h.push(i(p)),
    p = 0) : m++,
    a >>= 1;
0 == --c && (c = window.Math.pow(2, f),
f++)
}
for (a = 2,
n = 0; n < f; n++)
p = p << 1 | 1 & a,
m == e - 1 ? (m = 0,
h.push(i(p)),
p = 0) : m++,
a >>= 1;
for (; ; ) {
if (p <<= 1,
m == e - 1) {
h.push(i(p));
break
}
m++
}
return h.join("")
}
};
"""


lista = ""
a = 34 #random valueId
def final(st):
    aa = len(st) % 4
    if aa == 1:
        st += "==="
    elif aa == 2:
        st += "=="
    elif aa == 3:
        st += "="
    elif aa == 0:
        pass
    else:
        print("Valor inesperado")

    confirmacao = ""
    if a < 16:
        confirmacao = "0" + hex(a)[2:]
    else:
        confirmacao = hex(a)[2:]
    st = st[:2] + confirmacao + st[2:]
    ffff = urllib.parse.quote_plus(st)
    return "https://br.banggood.com/load/product/ajaxProduct.html?sq="+ffff

def stringToByte(strg):
    e = []
    arr = bytes(strg, 'utf-8')
    for byte in arr:
        e.append(byte)
    return e

def get_frete(url):
    global va,a,lista
    URL_BEFORE =url
    #ipt ="products_id=1834978&isNew=1&warehouse=CN"
    result = "isNew=1"
    try:
        a1 = URL_BEFORE.split("-p-")
        a2 = a1[1].split(".")[0]
        print("Id produto == "+a2)
        result += "&products_id="+a2
    except:
        pass
    try:
        b1 = URL_BEFORE.split("cur_warehouse=")
        b2 = b1[1].split("&")[0]
        result += "&warehouse="+b2
    except:
        pass
    ipt =result
    r1 = stringToByte(ipt)
    for i in r1:
        value = ~((i+a) % 256)
        value2 = hex(abs(value))[2:]
        lista += value2
    key = lista
    va += ';t.compressToBase64("'+key+'")'
    f = js2py.eval_js( va )
    return final(f)

# Exemplo
print(get_frete("https://br.banggood.com/EU-DIRECT-ADO-A20-Up-To-350W-36V-10_4Ah-20-inch-Electric-Bike-25km-or-h-Max-Speed-80Km-Mileage-120Kg-Max-Load-Large-Frame-Releasable-Max-Speed-Electric-Bicycle-p-1838718.html?cur_warehouse=CN&utmid=18621&cs=44&cs_md=1&cs_at=0&ID=6287830"))
