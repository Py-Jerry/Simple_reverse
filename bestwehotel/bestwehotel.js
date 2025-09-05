const CryptoJS = require('crypto-js');

function l(e) {
    var n = CryptoJS.enc.Latin1.parse("h5LoginKey123456")
        , a = CryptoJS.enc.Latin1.parse("h5LoginIv1234567")
        , t = e
        , o = CryptoJS.AES.encrypt(t, n, {
        iv: a,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    return o.toString()
}

console.log(l('123456'));
function getRandom() {
    for (var e = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", n = 6, a = "", t = 0; t < n; t++) {
        var o = Math.floor(Math.random() * e.length);
        a += e.charAt(o)
    }
    return a
}
console.log(getRandom())