import time
from src.unified.stack import UnifiedStack
from src.acphi496.codon import ACPhi496Codon

def benchmark(n=10000):
    print(f"📊 Benchmark: {n} atoms")
    
    stack = UnifiedStack()
    payloads = [f"Axiom_{i}" for i in range(n)]
    
    start = time.time()
    for i, payload in enumerate(payloads):
        codon = ACPhi496Codon(0x01, payload)
        stack.transmute(codon)
    
    duration = time.time() - start
    print(f"✅ {n} atoms/s: {n/duration:.0f}")
    print(f"⏱️  {duration*1000/n:.2f}ms/atom")
