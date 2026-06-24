"""
config.py
Saare paths aur settings ek jagah rakhne ke liye.
Advantage: kahin badalna ho to sirf YAHAN badlo, baaki saari files apne aap update.
"""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

RAW_DIR = ROOT / "data" / "raw"

RESULTS_DIR = ROOT / "results" 

DATA_FILES = {
    "benign":      RAW_DIR / "benign.csv",
    "dos_icmp":    RAW_DIR / "dos_icmp.csv",
    "dos_syn":     RAW_DIR / "dos_syn.csv",
    "brute_force": RAW_DIR / "brute_force.csv",
    "port_scan":   RAW_DIR / "port_scan.csv",
}

# har file se kitni rows lena
SAMPLE_ROWS = 20000

#Preprocessing Setting
# wo columns jo hatane hain (IP/time/port — model ko cheating se rokte hain)
DROP_COLUMNS = ['Flow ID', 'Src IP', 'Dst IP', 'Timestamp', 'Src Port', 'Dst Port']

# TRAIN/TEST SPLIT SETTINGS
TEST_SIZE = 0.2        # 20% test, 80% train
RANDOM_STATE = 42      # har baar same result (consistency)