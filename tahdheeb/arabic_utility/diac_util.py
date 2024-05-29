# -*- coding: utf-8 -*-

import re
class ArabicDiacritics(object):
    # REVIEWED: Compile the regular expression for detecting Arabic diacritics
    # | Unicode | Diacritic | Name (English)      | Name (Arabic)       | Description                                          |
    # |---------|-----------|---------------------|---------------------|------------------------------------------------------|
    # | \u064b  | ً         | Tanwin Fathah       | تَنوين الفتح        | Indicates a nun sound after the vowel (an).          |
    # | \u064c  | ٌ         | Tanwin Dammah       | تَنوين الضم          | Indicates a nun sound after the vowel (un).          |
    # | \u064d  | ٍ         | Tanwin Kasrah       | تَنوين الكسر         | Indicates a nun sound after the vowel (in).          |
    # | \u064e  | َ         | Fathah              | فتحة                | Represents a short "a" sound.                        |
    # | \u064f  | ُ         | Dammah              | ضمة                | Represents a short "u" sound.                        |
    # | \u0650  | ِ         | Kasrah              | كسرة               | Represents a short "i" sound.                        |
    # | \u0651  | ّ         | Shaddah             | شدة                | Indicates gemination or doubling of a consonant.     |
    # | \u0652  | ْ         | Sukun               | سكون               | Indicates the absence of a vowel.                    |
    # | \u0653  | ٓ         | Maddah              | مدّة                | Indicates a long vowel sound.                        |
    # | \u0670  | ٰ         | Superscript Alif    | ألف خنجرية         | Indicates a short "a" sound, mainly in Quranic text. |
    diacritics = "\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652\u0653\u0670"
    diacritics_re = re.compile(F"[{diacritics}]")
    # Quranic Symbols to be included
    # | Unicode | Diacritic | Name (English)      | Name (Arabic)       | Description                                          |
    # |---------|-----------|---------------------|---------------------|------------------------------------------------------|
    # | \u06d6  | ۖ         | Small High Ligature Sad with Lam with Alef Maksura | علامة وقف  | Indicates a small high ligature of Sad with Lam with Alef Maksura, used as a stop mark.          |
    # | \u06d7  | ۗ         | Small High Ligature Qaf with Lam with Alef Maksura | علامة وقف  | Indicates a small high ligature of Qaf with Lam with Alef Maksura, used as a stop mark.          |
    # | \u06d8  | ۘ         | Small High Meem Initial Form                     | علامة وقف  | Represents the small high initial form of Meem, used as a stop mark.                              |
    # | \u06d9  | ۙ         | Small High Lam Alef                              | علامة وقف  | Indicates a small high Lam Alef, used as a stop mark.                                             |
    # | \u06da  | ۚ         | Small High Jeem                                  | علامة وقف  | Represents a small high Jeem, used as a stop mark.                                                |
    # | \u06db  | ۛ         | Small High Three Dots                            | علامة وقف  | Indicates a small high three dots, used as a stop mark.                                           |
    # | \u06dc  | ۜ         | Small High Seen                                  | علامة وقف  | Represents a small high Seen, used as a stop mark.                                                |
    # | \u06e9  | ۩         | Place of Sajda                                   | علامة السجدة | Indicates the place where a prostration should be made during the recitation of the Quran.         |
    # | \u06e7  | ۧ         | Small High Yeh                                   | علامة وقف  | Represents a small high Yeh, used as a stop mark.                                                 |
    # | \u06e8  | ۨ         | Small High Noon                                  | علامة وقف  | Indicates a small high Noon, used as a stop mark.                                                 |
    quranic_symbols = "\u06d6\u06d7\u06d8\u06d9\u06da\u06db\u06dc\u06e9\u06e7\u06e8"
    quranic_symbols_re = re.compile(F"[{quranic_symbols}]")
    def __init__(self):
        pass

    @staticmethod
    def remove_diacritics( text):
        return ArabicDiacritics.diacritics_re.sub('', text)

    @staticmethod
    def contains_diacritics( word):
        return bool(ArabicDiacritics.diacritics_re.search(word))

    @staticmethod
    def contains_10per_diacritics( word):
        return (len(ArabicDiacritics.diacritics_re.findall(word)) / len(word)) > 0.1