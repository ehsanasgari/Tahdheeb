# Tahdheeb (تهذیب)

## Overview

Tahdheeb (تهذیب) is an Arabic Preprocessing Library developed at Qatar Computing Research. 
This library provides tools for preprocessing Arabic text, including normalization, diacritics handling, number normalization, punctuation correction, and more.

### Develpers
- Ehsaneddin Asgari 
- Yassine Elkheir

## Features

- **Normalization:** Standardizes Arabic text by normalizing character variations and numbers.
- **Diacritics Handling:** Removes or processes Arabic diacritics.
- **Punctuation Correction:** Corrects punctuation usage in Arabic text.
- **Determine Arabic Ratio:** Output the arabic ration.

## Installation

You can install Tahdheeb using pip:

```bash
pip install src
```

## Example Usage

The following example demonstrates how to use the `Tahdheeb` library for preprocessing Arabic text, including fixing punctuation issues, improving text structure, and normalizing the text. 

### Code Example

```python
from src.preprocessing.text_content import ArabicTextProcess
from src.preprocessing.text_verification import ArabicTextVerify
from src.preprocessing.text_structure import ArabicStructure

text = 'الـــــــــسلام    عليكم . كيـــف    حالك ؟ أتـــمنى أن تكون بــــــخير .أ نحنو  هنا للمســـــاعدة ...هل  تريــــد شيء مـــا؟  الرجـــــــاء    إبلاغن ا بــــأي وقــــت! في ٢دقيقه شكرا ، جزيــــلا Thanks!'

# Initialize the classes
ATB = ArabicStructure()
ASP = ArabicTextProcess()
ATP = ArabicTextVerify()

# Check the ratio of Arabic text
print('Ratio of Arabic text:', ATP.check_arabic_ratio(text))

print('\nText before structure improvement:\n', text, '\n-----------\n')

# Preprocess the text to fix structure and remove English text
text = ATB.preprocess(text, remove_english=True)
print('\nText after structure improvement:\n', text, '\n-----------\n')

# Normalize the text (basic normalization)
text = ASP.get_arabic_normal(text, extensive_normalization=False)
print('\nText after normalizing:\n', text, '\n-----------\n')

# Normalize the text (extensive normalization)
text = ASP.get_arabic_normal(text, extensive_normalization=True)
print('\nText after extensive normalizing:\n', text, '\n-----------\n')
```

### Explanation

#### Import Libraries

```python
from src.preprocessing.text_content import ArabicTextProcess
from src.preprocessing.text_verification import ArabicTextVerify
from src.preprocessing.text_structure import ArabicStructure
```

#### Original Text

The sample text contains various errors such as character repetition, incorrect punctuation, and mixed language content.

```python
text = 'الـــــــــسلام    عليكم . كيـــف    حالك ؟ أتـــمنى أن تكون بــــــخير .أ نحنو  هنا للمســـــاعدة ...هل  تريــــد شيء مـــا؟  الرجـــــــاء    إبلاغن ا بــــأي وقــــت! في ٢دقيقه شكرا ، جزيــــلا Thanks!'
```

#### Initialize the Classes

Initialize the classes for structure improvement, text processing, and text verification.

```python
ATB = ArabicStructure()
ASP = ArabicTextProcess()
ATP = ArabicTextVerify()
```

#### Check the Ratio of Arabic Text

Verify how much of the text is in Arabic.

```python
print('Ratio of Arabic text:', ATP.check_arabic_ratio(text))
```

#### Before Structure Improvement

Print the original text before any processing.

```python
print('\nText before structure improvement:\n', text, '\n-----------\n')
```

#### Structure Improvement

Preprocess the text to fix punctuation issues and remove English text.

```python
text = ATB.preprocess(text, remove_english=True)
print('\nText after structure improvement:\n', text, '\n-----------\n')
```

#### Basic Normalization

Normalize the text with basic normalization.

```python
text = ASP.get_arabic_normal(text, extensive_normalization=False)
print('\nText after normalizing:\n', text, '\n-----------\n')
```

#### Extensive Normalization

Normalize the text with extensive normalization.

```python
text = ASP.get_arabic_normal(text, extensive_normalization=True)
print('\nText after extensive normalizing:\n', text, '\n-----------\n')
```

### Output

This example will output the following information at each step:

1. The ratio of Arabic text in the original input.
2. The original text before any processing.
3. The text after fixing structural issues and removing English text.
4. The text after basic normalization.
5. The text after extensive normalization.

This step-by-step process ensures that the Arabic text is cleaned, normalized, and ready for further processing or analysis.

## Notes
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