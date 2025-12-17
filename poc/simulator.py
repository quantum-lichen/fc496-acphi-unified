#!/usr/bin/env python3
import sys
import os
from pathlib import Path
import streamlit as st
import time

# 🔥 FIX PYTHONPATH (MAGIQUE)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.unified.stack import UnifiedStack
from src.acphi496.codon import ACPhi496Codon

st.set_page_config(page_title="FC-496 Demo", layout="wide", initial_sidebar_state="expanded")

st.title("🌌 **FC-496/ACΦ-496 Unified Stack**")
st.markdown("***Zero-Copy • φ-Spiral • H-Scale Security • AI-Native* 🧬⚡**")

# Sidebar
st.sidebar.title("⚙️ **Controls**")
num_atoms = st.sidebar.slider("Nombre d'atomes FC-496", 10, 5000, 100)
axiom_type = st.sidebar.selectbox("Type d'axiome", [0x01, 0x02, 0x03], 
    format_func=lambda x: ACPhi496Codon.TYPES.get(x, "UNKNOWN"))

if st.button("🚀 **Générer Génome**", type="primary", use_container_width=True):
    with st.spinner(f"🧬 Création de {num_atoms} atomes..."):
        stack = UnifiedStack()
        start = time.time()
        
        progress_bar = st.progress(0)
        for i in range(num_atoms):
            codon = ACPhi496Codon(axiom_type, f"IA serves humanity #{i}")
            atom = stack.transmute(codon)
            
            if i % 100 == 0:
                progress_bar.progress(i / num_atoms)
        
        duration = time.time() - start
        stats = stack.stats()
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Atoms", stats["atoms"])
        col2.metric("Codons", stats["codons"])
        col3.metric("Valid H-Scale", f"{stats['valid_hscale']}/{stats['atoms']}")
        col4.metric("Perf", f"{num_atoms/duration:.0f}/s")
        
        st.success(f"✅ **Génome créé en {duration*1000:.2f}ms**")
        
        # Top 5 atoms
        st.subheader("🔍 **Top 5 Atoms (Zero-Copy)**")
        for i, atom in enumerate(list(stack.fc_atoms.values())[:5]):
            st.code(f"{atom!r}", language="python")

st.markdown("---")
st.markdown("""
**© 2025 Quantum-Lichen - Demo only**  
⭐ [GitHub](https://github.com/quantum-lichen/fc496-acphi-unified) | 💚 [Discord](https://discord.gg/lichen)
""")

# Auto-run demo
if not st.sidebar.checkbox("Mode Manuel"):
    st.sidebar.button("🚀 Générer Génome")
