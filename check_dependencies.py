#!/usr/bin/env python
"""
Script to check the availability and versions of HPC Python dependencies.
Displays a table with package information and CUDA support where applicable.
"""

import sys
from importlib import import_module
from packaging import version
import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

def get_package_version(package_name):
    """Get the version of an installed package."""
    try:
        module = import_module(package_name)
        return getattr(module, '__version__', 'N/A')
    except ImportError:
        return None

def check_cuda_support():
    """Check if CUDA is available for GPU packages."""
    cuda_info = {}
    
    # Check CUDA for CuPy
    try:
        import cupy as cp
        if cp.cuda.is_available():
            cuda_info['cupy'] = 'Yes'
        else:
            cuda_info['cupy'] = 'No'
    except ImportError:
        cuda_info['cupy'] = 'N/A'
    
    # Check CUDA for JAX
    try:
        import jax
        devices = jax.devices()
        has_gpu = any('gpu' in str(d).lower() or 'cuda' in str(d).lower() for d in devices)
        cuda_info['jax'] = 'Yes' if has_gpu else 'CPU only'
    except ImportError:
        cuda_info['jax'] = 'N/A'
    
    # Check CUDA for Numba
    try:
        from numba import cuda
        if cuda.is_available():
            cuda_info['numba'] = 'Yes'
        else:
            cuda_info['numba'] = 'No'
    except (ImportError, AttributeError):
        cuda_info['numba'] = 'N/A'
    
    return cuda_info

def main():
    """Main function to check and display dependency information."""
    
    console = Console()
    
    # List of packages to check
    packages = {
        'numpy': 'NumPy',
        'numba': 'Numba',
        'jax': 'JAX',
        'cupy': 'CuPy',
        'sklearn': 'scikit-learn',
        'networkx': 'NetworkX',
        'matplotlib': 'Matplotlib',
    }
    
    # Check for dependencies with CUDA support
    cuda_packages = ['cupy', 'jax', 'numba']
    
    console.print("\n[bold cyan]High-Performance Computing Python Dependencies Check[/bold cyan]\n")
    
    # Get CUDA information
    cuda_info = check_cuda_support()
    
    # Check each package
    available_packages = []
    missing_packages = []
    
    for package_name, display_name in packages.items():
        version_str = get_package_version(package_name)
        if version_str is None:
            missing_packages.append(display_name)
        else:
            cuda_support = cuda_info.get(package_name, 'N/A') if package_name in cuda_packages else '-'
            available_packages.append({
                'Package': display_name,
                'Version': version_str,
                'CUDA Support': cuda_support
            })
    
    # Create and display table of available packages
    if available_packages:
        table = Table(title="✓ Installed Packages", show_header=True, header_style="bold magenta")
        table.add_column("Package", style="cyan")
        table.add_column("Version", style="green")
        table.add_column("CUDA Support", style="yellow")
        
        for pkg in available_packages:
            cuda_style = "green" if pkg['CUDA Support'] == 'Yes' else "yellow" if pkg['CUDA Support'] == 'CPU only' else "dim"
            table.add_row(
                pkg['Package'],
                pkg['Version'],
                pkg['CUDA Support'],
                style=cuda_style if pkg['CUDA Support'] != '-' else None
            )
        
        console.print(table)
    
    # Display missing packages
    if missing_packages:
        console.print(f"\n[bold red]✗ Missing Packages ({len(missing_packages)})[/bold red]")
        for pkg in missing_packages:
            console.print(f"  [red]•[/red] {pkg}")
    
    # Summary
    total = len(available_packages) + len(missing_packages)
    installed = len(available_packages)
    summary_text = f"[bold]Summary:[/bold] [green]{installed}[/green]/[cyan]{total}[/cyan] packages installed"
    console.print(f"\n{summary_text}\n")
    
    # GPU/CUDA Status Panel
    cuda_status = []
    for pkg_name in cuda_packages:
        status = cuda_info.get(pkg_name, 'N/A')
        display_name = packages.get(pkg_name, pkg_name)
        status_color = "green" if status == 'Yes' else "yellow" if status == 'CPU only' else "red"
        cuda_status.append(f"  [cyan]{display_name:12}[/cyan]: [{status_color}]{status}[/{status_color}]")
    
    panel = Panel(
        "\n".join(cuda_status),
        title="[bold]GPU/CUDA Status[/bold]",
        border_style="blue",
        expand=False
    )
    console.print(panel)
    
    # Return exit code
    return 0 if not missing_packages else 1

if __name__ == '__main__':
    main()
