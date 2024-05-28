# Tahdheeb (تهذیب)

## Overview

Tahdheeb (تهذیب) is an Arabic Preprocessing Library developed by Ehsaneddin Asgari and Yassine Elkheir at Qatar Computing Research. 
This library provides tools for preprocessing Arabic text, including normalization, diacritics handling, number normalization, punctuation correction, and more.

## Features

- **Normalization:** Standardizes Arabic text by normalizing character variations and numbers.
- **Diacritics Handling:** Removes or processes Arabic diacritics.
- **Punctuation Correction:** Corrects punctuation usage in Arabic text.
- **Other Utilities:** Additional tools for text preprocessing.

## Installation

You can install Tahdheeb using pip:

```bash
pip install tahdheeb
```


## Quick Start

### Normalization
Normalize Arabic text by normalizing character variations and numbers.

### Diacretics

| Unicode | Diacritic | Name (English)      | Name (Arabic)       | Description                                          |
|---------|-----------|---------------------|---------------------|------------------------------------------------------|
| \u064b  | ً         | Tanwin Fathah       | تَنوين الفتح        | Indicates a nun sound after the vowel (an).          |
| \u064c  | ٌ         | Tanwin Dammah       | تَنوين الضم          | Indicates a nun sound after the vowel (un).          |
| \u064d  | ٍ         | Tanwin Kasrah       | تَنوين الكسر         | Indicates a nun sound after the vowel (in).          |
| \u064e  | َ         | Fathah              | فتحة                | Represents a short "a" sound.                        |
| \u064f  | ُ         | Dammah              | ضمة                | Represents a short "u" sound.                        |
| \u0650  | ِ         | Kasrah              | كسرة               | Represents a short "i" sound.                        |
| \u0651  | ّ         | Shaddah             | شدة                | Indicates gemination or doubling of a consonant.     |
| \u0652  | ْ         | Sukun               | سكون               | Indicates the absence of a vowel.                    |
| \u0653  | ٓ         | Maddah              | مدّة                | Indicates a long vowel sound.                        |
| \u0670  | ٰ         | Superscript Alif    | ألف خنجرية         | Indicates a short "a" sound, mainly in Quranic text. |


## 