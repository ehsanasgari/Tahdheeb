import re
import os, sys
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
module_path = os.path.join(current_dir, '..')
sys.path.append(module_path)
from arabic_utility.arbchar_util import ArabicChars
from arabic_utility.num_util import ArabicNumerics
from arabic_utility.diac_util import ArabicDiacritics

class ArabicTextVerify(object):
    def __init__(self):
        self.ArabicChars = ArabicChars()

    def check_arabic_ratio(self, text):

        # Remove non-Arabic characters
        filtered_text = self.ArabicChars.allowed_only_arabic_chars_pattern_normalized.sub('', text)

        # Calculate the proportion of Arabic content
        return len(filtered_text) / len(text) if text else 0

    def contains_diacritics(self, text):
        return bool(ArabicDiacritics.diacritics_re.search(text))

    def diacritics_ratio( word):
        return (len(ArabicDiacritics.diacritics_re.findall(word)) / len(word))