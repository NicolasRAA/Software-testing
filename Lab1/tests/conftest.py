# Garantiza que el paquete 'calc' (ubicado en Lab1/calc) sea importable
import os, sys

# .../Software-testing/Lab1
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
