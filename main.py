"""
Run the full project
"""

import subprocess
import sys

def main():
    """Running the full project."""
    print("**Let's import all the data**")
    subprocess.run([sys.executable, "scripts/ingest.py"], check=True)

    print("\n**Running analysis**")
    subprocess.run([sys.executable, "scripts/analysis.py"], check=True)

    print("\n** Project complete.  Charts saved in outputs folder.**")

if __name__ == "__main__":
    main()