
import re
import os,sys
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
module_path = os.path.join(current_dir, '..')
sys.path.append(module_path)
from tahdheeb.preprocessing.text_content import ArabicTextProcess
from tahdheeb.preprocessing.text_structure import ArabicStructure

text = 'سال ( تنت ٢ ) ٣متر. و الي : ds '

ATB = ArabicStructure()
text = ATB.preprocess(text)
ASP = ArabicTextProcess()
text = ASP.get_arabic_normalized_pretokenization(text)

print(text)