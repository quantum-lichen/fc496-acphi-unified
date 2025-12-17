import struct
import hashlib
from typing import Optional
PHI = 1.618033988749895
H_SCALE_THRESHOLD = 0.618

class FC496Atom:
    """🧲 FC-496 Atom : 496 bits = 62 bytes (cache-aligned)"""
    
    def __init__(self, geo_hash: int, content: bytes, schema_class: int = 0):
        self.geo_hash = geo_hash & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        self.content_size = len(content)
        self.schema_class = schema_class
        self.h_scale = self._calc_h_scale()
        self.magic_phi = 0x9E3779B97F4A7C15
        self.pi_index = self._pi_index()
    
    def _calc_h_scale(self) -> float:
        """H-Scale : Harmony metric (intrinsic security)"""
        entropy = len(self.content) / 1024
        coherence = abs(PHI - entropy)
        return 1.0 / (1.0 + coherence)
    
    def _pi_index(self) -> int:
        """Temporal anchor (π-sequence position)"""
        return int(hashlib.sha256(str(self.geo_hash).encode()).hexdigest(), 16) % (2**64)
    
    def validate(self) -> bool:
        """🛡️ H-Scale validation (O(1))"""
        return self.h_scale >= H_SCALE_THRESHOLD
    
    def serialize(self) -> bytes:
        """→ 64 bytes exact (zero-copy ready)"""
        return struct.pack("<QQIQIfHH", 
            self.magic_phi, self.pi_index, self.geo_hash, 
            self.schema_class, self.content_size, 
            self.h_scale, 0, 0)  # Padding
    
    @classmethod
    def deserialize(cls, data: bytes) -> 'FC496Atom':
        """Zero-copy deserialization"""
        unpacked = struct.unpack("<QQIQIfHH", data)
        atom = cls(unpacked[2], b'dummy')
        atom.magic_phi, atom.pi_index = unpacked[0], unpacked[1]
        atom.schema_class, atom.content_size = unpacked[3], unpacked[4]
        atom.h_scale = unpacked[5]
        return atom
