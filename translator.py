from pathlib import Path
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("file", help="path to opt file", type=str)

args = parser.parse_args()

path_str = args.file
path = Path(path_str)
data = np.fromfile(str(path.resolve()))
data_cleaned = data[2:]
data_opt = data_cleaned.astype(dtype=np.dtype(">f8"))

# save file to current directory
data_opt.tofile(path.stem + ".opt")
