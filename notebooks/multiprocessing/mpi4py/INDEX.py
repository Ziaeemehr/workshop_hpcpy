#!/usr/bin/env python3
"""
Quick Reference Index for MPI4py Scripts
Run this to see a summary of all available examples
"""

scripts = {
    "Point-to-Point Communication": {
        "00_send_recieve.py": "Blocking send/receive between two processes",
        "01_send_recieve_nonblocking.py": "Async send/receive with isend/irecv and wait",
        "02_send_np_array.py": "Efficient numpy array transfer using typed buffers",
    },
    "Collective: Broadcast": {
        "03_bcast.py": "Broadcast complex data from root to all processes",
        "06_broadcasting_np_array.py": "Typed broadcast for efficient numpy arrays",
        "07_broadcasting_torch.py": "Broadcast PyTorch tensors (torch optional)",
    },
    "Collective: Scatter": {
        "04_scattering_obj.py": "Scatter scalar objects to each process",
        "04_scattering_dictionary.py": "Scatter list of dictionaries with arrays",
        "08_scattering_np_array.py": "Scatter 2D array rows to processes",
        "10_scattering_3D_np_array.py": "Scatter 3D array slices to processes",
        "09_scattering_tensor.py": "Scatter PyTorch tensors via numpy (torch optional)",
    },
    "Collective: Gather": {
        "05_gathering_obj.py": "Gather scalar objects from all processes",
        "05_gathering_array.py": "Gather variable-sized arrays to root",
        "05_gathering_list.py": "Gather lists of objects from all processes",
        "05_gathering_dictionary.py": "Gather dictionaries from all processes",
        "11_gathering_np_array.py": "Gather equal-sized arrays to 2D array",
        "12_gathering_3D_np_array.py": "Gather 2D arrays to 3D array",
    },
    "Advanced Patterns": {
        "13_scatter_list_of_arry_gather_list_of_array.py": 
            "Hybrid: MPI scatter/gather + local multiprocessing",
    }
}

if __name__ == "__main__":
    print("\n" + "="*80)
    print(" "*20 + "MPI4py EXAMPLES QUICK REFERENCE")
    print("="*80 + "\n")
    
    for category, items in scripts.items():
        print(f"📁 {category}")
        print("-" * 80)
        for script, description in items.items():
            print(f"  • {script:<40} → {description}")
        print()
    
    print("="*80)
    print("\n📖 Documentation:")
    print("  • README.md - Complete guide with concepts, patterns, and best practices")
    print("  • REVIEW_REPORT.md - Detailed review of all changes and improvements")
    print("\n🚀 Quick Start:")
    print("  $ conda activate hpc")
    print("  $ mpirun -np 4 python 03_bcast.py")
    print("\n💡 Learn More:")
    print("  $ cat README.md")
    print("\n" + "="*80)
