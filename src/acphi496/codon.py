import hashlib

class ACPhi496Codon:
    """🧠 ACΦ-496 Codon : Knowledge atom"""
    
    TYPES = {
        0x01: "IMMUTABLE_TRUTH",
        0x02: "CAUSAL_AXIOM", 
        0x03: "ETHICAL_PRINCIPLE"
    }
    
    def __init__(self, axiom_type: int, payload: str):
        self.axiom_type = axiom_type
        self.payload = payload.encode()[:400]  # 400 bits max
        self.promoter = b'\x01' * 24  # π-Time
        self.phi_crc = self._calc_phi_crc()
    
    def _calc_phi_crc(self) -> bytes:
        """φ-based checksum"""
        h = hashlib.sha256(self.payload + self.promoter).digest()
        return h[:16]
    
    def validate(self) -> bool:
        return hashlib.sha256(self.phi_crc).hexdigest()[:8] == \
               hashlib.sha256(self.payload).hexdigest()[:8]
    
    def __repr__(self):
        return f"ACΦ({self.TYPES.get(self.axiom_type, 'UNKNOWN')[:20]})"
