// 假设这是从 c.config 获取的值
const rsaModulus = "YOUR_RSA_MODULUS_HEX_STRING"; // 请替换为实际的模数（16进制字符串或Base64编码字符串）
const rsaExponent = "10001"; // 公钥指数，通常是 10001 (16进制)，对应十进制 65537
import JSEncrypt from 'jsencrypt';
// 创建 JSEncrypt 实例
const encryptor = new JSEncrypt();
const publicKeyPem = 'd3bcef1f00424f3261c89323fa8cdfa12bbac400d9fe8bb627e8d27a44bd5d59dce559135d678a8143beb5b8d7056c4e1f89c4e1f152470625b7b41944a97f02da6f605a49a93ec6eb9cbaf2e7ac2b26a354ce69eb265953d2c29e395d6d8c1cdb688978551aa0f7521f290035fad381178da0bea8f9e6adce39020f513133fb'
encryptor.setPublicKey(publicKeyPem);

// 要加密的数据
const plainText = "123456";

// 执行加密
const encryptedData = encryptor.encrypt(plainText);

if (encryptedData) {
    // 加密成功，encryptedData 是Base64编码的字符串
    console.log("加密后的数据 (Base64):", encryptedData);
    // 你可以将其发送到服务器
} else {
    console.error("加密失败");
}

// rsaPassword = function (e){
//                         var t = new encryptor.default;
//                         return t.setPublic(publicKeyPem, 10001),
//                         t.encrypt(e)
//                     }