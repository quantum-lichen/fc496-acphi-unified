#!/usr/bin/env python3
import sys
import os
from pathlib import Path
import streamlit as st

# 🔥 FIX PYTHONPATH AUTOMATIQUE
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.fc496.atom import FC496Atom
from src.acphi496.codon import ACPhi496Codon
from src.unified.stack import UnifiedStack
import time

st.set_page_config(page_title="FC-496 Demo", layout="wide")

st.title("🌌 **FC-496/ACΦ-496 Unified Stack**")
st.markdown("***Zero-Copy • φ-Spiral • H-Scale Security • AI-Native***")

# Sidebar
st.sidebar.title("⚙️ Controls")
num_atoms = st.sidebar.slider("Nombre d'atomes", 10, 1000, 100)

if st.button("🚀 **Lancer Démo**", type="primary"):
    with st.spinner("Génération génome..."):
        stack = UnifiedStack()
        start = time.time()
        
        for i in range(num_atoms):
            codon = ACPhi496Codon(0x01, f"IA serves humanity #{i}")
            atom = stack.transmute(codon)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Atoms créés", len(stack.fc_atoms))
            with col2:
                st.metric("H-Scale", f"{atom.h_scale:.3f}")
        
        duration = time.time() - start
        
        st.success(f"✅ **Génome créé en {duration*1000:.2f}ms**")
        st.metric("Perf", f"{num_atoms/duration:.0f} atoms/s")
        
        # Tableau résultats
        st.subheader("📊 Atoms (Zero-Copy Read)")
        for atom in list(stack.fc_atoms.values())[:5]:
            st.write(f"**{hex(atom.geo_hash)[:16]}** → H-Scale: {atom.h_scale:.3f}")

st.markdown("---")
st.markdown("**© 2025 Quantum-Lichen - Demo only** | [Docs](https://github.com/quantum-lichen/fc496-acphi-unified)")
