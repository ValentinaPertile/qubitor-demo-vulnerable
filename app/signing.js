// Falla plantada (Módulo D): firma con ECDSA, vulnerable a computación cuántica
// (algoritmo de Shor). La alternativa post-cuántica es ML-DSA (FIPS 204).
const crypto = require('crypto');

const { privateKey, publicKey } = crypto.generateKeyPairSync('ec', {
  namedCurve: 'P-256',
});

function firmar(mensaje) {
  return crypto.sign('sha256', Buffer.from(mensaje), privateKey);
}

function verificar(mensaje, firma) {
  return crypto.verify('sha256', Buffer.from(mensaje), publicKey, firma);
}

module.exports = { firmar, verificar };
