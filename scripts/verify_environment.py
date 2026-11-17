#!/usr/bin/env python3
"""
Environment Verification Test for AITR Lab 02
Checks hardware acceleration, library compatibility, and determinism.
"""

import sys
import os

def run_environment_diagnostics():
    print("=" * 60)
    print("AITR Lab 02: Environment Compatibility & Diagnostic Test")
    print("=" * 60)
    
    # 1. Python version check
    py_ver = sys.version_info
    print(f"Python Version: {py_ver.major}.{py_ver.minor}.{py_ver.micro}")
    if py_ver < (3, 9):
        print("[-] WARNING: Python 3.9+ recommended.")
    else:
        print("[+] Python version compatible.")
        
    # 2. Dependency imports
    dependencies = [
        "torch",
        "transformers",
        "datasets",
        "accelerate",
        "numpy",
        "pandas",
        "matplotlib"
    ]
    
    missing = []
    versions = {}
    for pkg in dependencies:
        try:
            mod = __import__(pkg)
            ver = getattr(mod, "__version__", "unknown")
            versions[pkg] = ver
            print(f"[+] {pkg:<15} : {ver}")
        except ImportError as e:
            print(f"[-] {pkg:<15} : MISSING ({e})")
            missing.append(pkg)
            
    if missing:
        print("\n[!] Failure Diagnostic: Missing packages detected.")
        print(f"    Run: pip install {' '.join(missing)}")
        return False
        
    # 3. Hardware & Acceleration Check
    import torch
    cuda_avail = torch.cuda.is_available()
    print("-" * 60)
    if cuda_avail:
        gpu_name = torch.cuda.get_device_name(0)
        gpu_count = torch.cuda.device_count()
        vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)
        print(f"[+] CUDA Available   : True ({gpu_count} GPU detected)")
        print(f"[+] GPU Device       : {gpu_name}")
        print(f"[+] Total VRAM       : {vram_gb:.2f} GB")
        device = "cuda"
    else:
        print("[-] CUDA Available   : False (Falling back to CPU mode)")
        print("[*] Note: For full 7B model execution, Google Colab T4/L4 GPU is recommended.")
        device = "cpu"
        
    # 4. Computation Sanity Check
    print("-" * 60)
    try:
        x = torch.randn(128, 128, device=device)
        y = torch.matmul(x, x)
        print(f"[+] Tensor Math Test : Passed on {device.upper()} (Shape: {y.shape})")
    except Exception as e:
        print(f"[-] Tensor Math Test : FAILED ({e})")
        return False
        
    # 5. Determinism Check
    import numpy as np
    import random
    SEED = 42
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    if cuda_avail:
        torch.cuda.manual_seed_all(SEED)
    print(f"[+] Determinism Test : Random seed frozen at SEED = {SEED}")
    
    print("=" * 60)
    print("[SUCCESS] Environment verification completed successfully.")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = run_environment_diagnostics()
    sys.exit(0 if success else 1)
