import os
import glob
from shutil import copyfile

__SRC_DIR = "./txt"
txt_filepath_list = glob.glob(os.path.join(__SRC_DIR, "*.txt"))

for filepath in txt_filepath_list:
	basename = os.path.basename(filepath)
	copyfile(filepath, basename+".md")

