import os
import glob
from shutil import copyfile

__SRC_DIR = "./txt"
txt_filepath_list = glob.glob(os.path.join(__SRC_DIR, "*.txt"))

for filepath in txt_filepath_list:
	basename = os.path.basename(filepath)
	with open(filepath, 'r', encoding="utf-8") as fp:
		raw = fp.readlines()

	text = "  <br>".join(raw)
	text = text.replace("\n", "<br>")
	text = text.replace("#", " - ")

	with open(basename + ".md", 'w', encoding="utf-8") as fp:
		fp.write(text)