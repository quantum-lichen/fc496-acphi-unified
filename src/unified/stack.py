from typing import Optional, Dict
from src.fc496.atom import FC496Atom
from src.acphi496.codon import ACPhi496Codon
import hashlib

class UnifiedStack:
    """🌌 FC-496 + ACΦ-496 Full-Stack"""
    
    def __init__(self):
        self.fc_atoms: Dict[int, FC496Atom] = {}
        self.ac_codons = []
    
    def transmute(self, codon: ACPhi496Codon) -> FC496Atom:
        """🔄 ACΦ → FC-496 (Bidirectional)"""
        geo_hash = int(hashlib.sha256(codon.payload).hexdigest(), 16)
        atom = FC496Atom(geo_hash, codon.payload, codon.axiom_type)
        if atom.validate():
            self.fc_atoms[geo_hash] = atom
            self.ac_codons.append(codon)
            return atom
        raise ValueError(f"H-Scale failure: {atom.h_scale}")
    
    def read_zero_copy(self, geo_hash: int) -> Optional[FC496Atom]:
        """⚡ O(1) Zero-copy read"""
        return self.fc_atoms.get(geo_hash)
    
    def stats(self) -> dict:
        """📊 Stats"""
        return {
            "atoms": len(self.fc_atoms),
            "codons": len(self.ac_codons),
            "valid_hscale": sum(1 for a in self.fc_atoms.values() if a.h_scale >= 0.618)
        }
