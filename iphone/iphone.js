function N(t, r, e) {
  return r in t
    ? Object.defineProperty(t, r, { value: e, enumerable: true, configurable: true, writable: true })
    : (t[r] = e), t;
}

function T(r) {
  if (!(this instanceof T)) throw new TypeError("Cannot call a class as a function");
  N(this, "accountName", void 0);
  N(this, "_privateValue", void 0);
  N(this, "_publicValue", void 0);
  this.accountName = r;
}

const obj = new T(123456);
console.log(obj);
