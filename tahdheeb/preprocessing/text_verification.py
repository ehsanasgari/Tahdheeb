import re
import os, sys
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
module_path = os.path.join(current_dir, '..')
sys.path.append(module_path)
from arabic_utility.arbchar import ArabicChars
from arabic_utility.num_util import ArabicNumerics
from arabic_utility.diac_util import ArabicDiacritics

class TextVerify(object):
    def __init__(self):
        # Define the set of allowed characters and create a regular expression pattern
        self.allowed_chars_pattern = re.compile(
            r'^[+"\'()\-\.:,!?;،؛»«؟<>ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي0123456789% \u064b\u064c\u064d\u0652\u064e\u064f\u0650\u0651\u0652\u0653\u0670\u06d6\u06d7\u06d8\u06d9\u06da\u06db\u06dc\u06e9\u06e7\u06e8]*$')

        # Define the regex for non-Arabic characters
        self.non_arabic_regex = re.compile(
            "[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD.0-9\s.,!?;،:؛»«؟]+")

    def check_ifarabic_content(self, s):
        return bool(self.allowed_chars_pattern.match(s))

    def is_mostly_arabic(self, text, threshold=0.8):

        # Remove non-Arabic characters
        filtered_text = self.non_arabic_regex.sub('', text)

        # Calculate the proportion of Arabic content
        proportion_arabic = len(filtered_text) / len(text) if text else 0

        # Check if the majority of the text is Arabic
        return proportion_arabic >= threshold