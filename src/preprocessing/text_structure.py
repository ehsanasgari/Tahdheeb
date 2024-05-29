# -*- coding: utf-8 -*-

import os, sys
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
module_path = os.path.join(current_dir, '..')
sys.path.append(module_path)
from arabic_utility.punc_util import ArabicPunctuations
from arabic_utility.num_util import ArabicNumerics
from arabic_utility.arbchar_util import ArabicChars

import re

class ArabicStructure(object):
    def __init__(self):
        self.ArabicChars = ArabicChars()
        compile_patterns = lambda patterns: [(re.compile(pattern), repl) for pattern, repl in patterns]
        self.punctuation_add_spacing_patterns = compile_patterns([
                # remove space before and after quotation
                ('" ([^\n"]+) "', r'"\1"'),
                (" ([" + ArabicPunctuations.punc_after + "])", r"\1"),  # remove space before
                ("([" + ArabicPunctuations.punc_before + "]) ", r"\1"),  # remove space after
                # put space after . and :
                (
                    "([" + ArabicPunctuations.punc_after[:3] + "])([^ " + ArabicPunctuations.punc_after + r"\d"+ArabicNumerics.arabic_number_translation_dst+ArabicNumerics.arabic_number_translation_dst+"])",
                    r"\1 \2",
                ),
                (
                    "([" + ArabicPunctuations.punc_after[3:] + "])([^ " + ArabicPunctuations.punc_after + "])",
                    r"\1 \2",
                ),  # put space after
                (
                    "([^ " + ArabicPunctuations.punc_before + "])([" + ArabicPunctuations.punc_before + "])",
                    r"\1 \2",
                ),  # put space before
                # put space after number; e.g.,  طول ۹متر ->  طول ۹ متر
                (r"(\d)(["+self.ArabicChars.arabic_all_alpha+"])", r"\1 \2"),
                # put space after number; e.g.,  طول۹ ->  طول ۹
                (r"(["+self.ArabicChars.arabic_all_alpha+"])(\d"+ArabicNumerics.arabic_number_translation_src+ArabicNumerics.arabic_number_translation_dst+")", r"\1 \2")])
        self.pattern_spaces = re.compile(r'\s+')

    def preprocess(self,text, remove_english=False):
        """
        :param text: str
        :return: add space before and after of punctuations
        """
        if remove_english:
            en_chars = re.compile(r'[a-zA-Z]')
            text = re.sub(en_chars, '', text)

        for pattern, repl in self.punctuation_add_spacing_patterns:
            text = pattern.sub(repl, text)
        text = re.sub(self.pattern_spaces, ' ', text)
        return text
