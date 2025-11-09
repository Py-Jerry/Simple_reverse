

get_keyencryptLong = function(text) {
            var _this = this;
            var maxLength = (this.n.bitLength() + 7 >> 3) - 11;
            try {
                var ct_1 = "";
                if (text.length > maxLength) {
                    var lt = text.match(/.{1,117}/g);
                    lt.forEach(function(entry) {
                        var t1 = _this.encrypt(entry);
                        ct_1 += t1
                    });
                    return hex2b64(ct_1)
                }
                var t = this.encrypt(text);
                var y = hex2b64(t);
                return y
            } catch (ex) {
                return false
            }
        }
function encryptLong (str) {

    var encrypted = encryptLong(str) || "";
    var uncrypted = this.getKey().decryptLong(encrypted) || "";
    var count = 0;
    var reg = /null$/g;
    while (reg.test(uncrypted)) {
        count++;
        encrypted = this.getKey().encryptLong(str) || "";
        uncrypted = this.getKey().decryptLong(encrypted) || "";
        if (count > 10) {
            break
        }
    }
    return encrypted

}
var test_result = encryptLong("\"{\"version\":\"CH4\",\"year\":\"2025\"}\"")
console.log(test_result)