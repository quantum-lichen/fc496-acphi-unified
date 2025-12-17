#!/usr/bin/env python3
from src.unified.stack import UnifiedStack
from src.acphi496.codon import ACPhi496Codon
import time

def demo_unified_stack():
    print("🌌 FC-496/ACΦ-496 UNIFIED STACK DEMO\n")
    
    stack = UnifiedStack()
    
    # 1. Créer axiomes ACΦ-496
    axioms = [
        ACPhi496Codon(0x01, "IA serves humanity"),
        ACPhi496Codon(0x02, "Truth is immutable"),
        ACPhi496Codon(0x03, "φ guides ethics")
    ]
    
    # 2. Transmuter → FC-496
    start = time.time()
    atoms = []
    for axiom in axioms:
        atom = stack.transmute(axiom)
        atoms.append(atom)
        print(f"🧬 Atom: geo_hash={hex(atom.geo_hash)[:16]}")
        print(f"✅ H-Scale: {atom.h_scale:.3f} ✓")
    
    # 3. Zero-copy read
    read_time = time.time() - start
    print(f"\n⚡ Transmute 3 atoms: {read_time*1000:.2f}ms")
    
    # 4. φ-Spiral lookup
    first_atom = stack.read_zero_copy(atoms[0].geo_hash)
    print(f"🔍 Zero-copy read: {first_atom.h_scale:.3f}")
    
    print("\n🎉 UNIFIED STACK OPERATIONAL!")
    print(f"📊 Stats: {len(stack.fc_atoms)} atoms | {len(stack.ac_codons)} codons")

if __name__ == "__main__":
    demo_unified_stack()
