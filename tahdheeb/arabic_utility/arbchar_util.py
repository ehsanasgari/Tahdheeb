# -*- coding: utf-8 -*-

import re
import os,sys
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
module_path = os.path.join(current_dir, '..')
sys.path.append(module_path)
from arabic_utility.num_util import ArabicNumerics
from arabic_utility.punc_util import ArabicPunctuations
from arabic_utility.diac_util import ArabicDiacritics

import string

class ArabicChars(object):
    arabic_normalizations = {'chars':
                             # Pair-REVIEWED Horuf
                                 [(r"ٰا|ﺍ|ﺎ", r"ا"),
                                  (r"ﺐ|ﺏ|ﺑ|ٮ|ﺏ|ﺑ", r"ب"),
                                  (r"ﭖ|ﭗ|ﭙ|ﺒ|ﭘ|پ", r"ب"),
                                  (r"ﭡ|ٺ|ٹ|ﭞ|ٿ|ټ|ﺕ|ﺗ|ﺖ|ﺘ", r"ت"),
                                  (r"ﺙ|ﺛ", r"ث"),
                                  (r"ﺝ|ڃ|ﺠ|ﺟ|ﺠ", r"ج"),
                                  (r"چ|ڃ|ﭽ|ﭼ|ج|ﺟ", r"ج"),
                                  (r"ﺢ|ﺤ|څ|ځ|ﺣ|ﳊ", r"ح"),
                                  (r"ﺥ|ﺦ|ﺨ|ﺧ", r"خ"),
                                  (r"ڏ|ډ|ﺪ|ﺩ", r"د"),
                                  (r"ﺫ|ﺬ|ﻧ", r"ذ"),
                                  (r"ڙ|ڗ|ڒ|ڑ|ڕ|ﺭ|ﺮ", r"ر"),
                                  (r"ﺰ|ﺯ", r"ز"),
                                  (r"ژ|ﮊ", r"ج"),
                                  (r"ݭ|ݜ|ﺱ|ﺲ|ښ|ﺴ|ﺳ", r"س"),
                                  (r"ﺵ|ﺶ|ﺸ|ﺷ", r"ش"),
                                  (r"ﺺ|ﺼ|ﺻ", r"ص"),
                                  (r"ﺽ|ﺾ|ﺿ|ﻀ", r"ض"),
                                  (r"ﻁ|ﻂ|ﻃ|ﻄ", r"ط"),
                                  (r"ﻆ|ﻇ|ﻈ", r"ظ"),
                                  (r"ڠ|ﻉ|ﻊ|ﻋ|ﻌ", r"ع"),
                                  (r"ﻏ|ﻎ|ۼ|ﻍ|ﻐ|ﻏ|ﻐ", r"غ"),
                                  (r"ﻒ|ﻑ|ﻔ|ﻓ|ڨ|ڤ", r"ف"),
                                  (r"ﻕ|ﻖ|ﻗ|ﻘ", r"ق"),
                                  (r"ﮚ|ﮒ|ﮓ|ﮕ|ﮔ|گ", r"غ"),
                                  (r"ﻝ|ﻞ|ﻠ|ڵ|ﳌ|ﻟ", r"ل"),
                                  (r"ﻡ|ﻤ|ﻢ|ﻣ", r"م"),
                                  (r"ڼ|ﻦ|ﻥ|ﻨ", r"ن"),
                                  (r"ۅ|ވ|ﻭ|ۊ|ۉ|ﻮ|ۇ|و|ﯙ|ۏ|ۈ|ۆ|ۋ", r"و"),
                                  (r'ﺆ|ؤ', r'ؤ'),
                                  (r"ﺌ|ئ|ﺋ", r"ئ"),
                                  (r"ﻬ|ھ|ﻩ|ﻫ|ﻪ|ۀ|ە|ہ", r"ه"),
                                  (r"ڭ|ﻚ|ﮎ|ﻜ|ﮏ|ګ|ﻛ|ﮑ|ﮐ|ڪ|ک", r"ك"),
                                  (r"ﭛ|ﻱ|ﻲ|ں|ﻳ|ﻴ|ې|ﯾ|ؿ|ﯿ|ێ|ے|ۑ", r"ي"),
                                  (r"ﻯ|ۍ|ﻰ|ﯼ|ﯽ|ى|ی|یٰ|ی", r"ى"),
                                  (r"ة|ة|ﺓ|ﺔ", r"ة"),
                                  (r"ٳ|إ|ﺇ", r"إ"),
                                  (r"ٔ|۪|ﺀ|ء", r"ء"),
                                  (r"ﺂ|ﺁ|آ", r"آ"),
                                  (r"ﺄ|ﺃ|أ|ٲ", r"أ"),
                                  (r"ٱ|ﭑ|ﭐ", r"ا")],
                             'diac':
                             # Diacretics
                                 [("ﹰ|\u0653", "\u064b"),
                                  ("\u08f1", "\u064c"),
                                  ("\u08f2", "\u064d"),
                                  ("\u06ea|\u06e2|\u06df|\u06e0", ""),
                                  # Sokun
                                  ("\u06e1", "\u0652")],
                             'punc':
                             # Puncuations
                                 [(r"：", r":"),
                                  (r"■|·", r"."),
                                  (r"–", r"-"),
                                  (r"›", r">"),
                                  (r"‹", r"<"),
                                  (r"…", r"..."),
                                  (r"–", r"-"),
                                  (r"﴾", r"("),
                                  (r"﴿", r")"),
                                  (r"’|‘", r"'"),
                                  (r"″", r'"')]
                             }
    replacements = [
        ("﷽", "بسم الله الرحمن الرحیم"),
        ("﷼", "ریال"),
        ("ﷰ|ﷹ", "صلى"),
        ("ﷲ", "الله"),
        ("ﷳ", "اکبر"),
        ("ﷴ", "محمد"),
        ("ﷵ", "صلعم"),
        (r"ﵹ", r"غمم"),
        (r"ﵟ", r"سمح"),
        ("ﷶ", "رسول"),
        ("ﷷ", "علیه"),
        ("ﷸ", "وسلم"),
        ("ﻵ|ﻶ|ﻷ|ﻸ|ﻹ|ﻺ|ﻻ|ﻼ", "لا"),
    ]

    arabic_normalizations_2nd_phase_extensive = [
        # REVIEWED Horuf
        (r"ا|إ|أ", r"ا"),
        (r"ؤ|و", r"و"),
        (r"ه|ة", r"ه"),
        (r"ي|ى", r"ى"),
    ]

    # used from HAZM
    persion_translation_src = "ؠػػؽؾؿكيٮٯٷٸٹٺٻټٽٿڀځٵٶٷٸٹٺٻټٽٿڀځڂڅڇڈډڊڋڌڍڎڏڐڑڒړڔڕږڗڙښڛڜڝڞڟڠڡڢڣڤڥڦڧڨڪګڬڭڮڰڱڲڳڴڵڶڷڸڹںڻڼڽھڿہۂۃۄۅۆۇۈۉۊۋۏۍێېۑےۓەۮۯۺۻۼۿݐݑݒݓݔݕݖݗݘݙݚݛݜݝݞݟݠݡݢݣݤݥݦݧݨݩݪݫݬݭݮݯݰݱݲݳݴݵݶݷݸݹݺݻݼݽݾݿࢠࢡࢢࢣࢤࢥࢦࢧࢨࢩࢪࢫࢮࢯࢰࢱࢬࢲࢳࢴࢶࢷࢸࢹࢺࢻࢼࢽﭐﭑﭒﭓﭔﭕﭖﭗﭘﭙﭚﭛﭜﭝﭞﭟﭠﭡﭢﭣﭤﭥﭦﭧﭨﭩﭮﭯﭰﭱﭲﭳﭴﭵﭶﭷﭸﭹﭺﭻﭼﭽﭾﭿﮀﮁﮂﮃﮄﮅﮆﮇﮈﮉﮊﮋﮌﮍﮎﮏﮐﮑﮒﮓﮔﮕﮖﮗﮘﮙﮚﮛﮜﮝﮞﮟﮠﮡﮢﮣﮤﮥﮦﮧﮨﮩﮪﮫﮬﮭﮮﮯﮰﮱﺀﺁﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴىكي“” "
    persion_translation_dst = (
        'یککیییکیبقویتتبتتتبحاوویتتبتتتبحححچدددددددددررررررررسسسصصطعففففففققکککککگگگگگللللنننننهچهههوووووووووییییییهدرشضغهبببببببححددرسعععففکککممنننلررسححسرحاایییووییحسسکببجطفقلمییرودصگویزعکبپتریفقنااببببپپپپببببتتتتتتتتتتتتففففححححححححچچچچچچچچددددددددژژررککککگگگگگگگگگگگگننننننههههههههههییییءاااووااییییااببببتتتتثثثثججججححححخخخخددذذررززسسسسششششصصصصضضضضططططظظظظععععغغغغففففققققککککللللممممننننههههوویییییییکی"" '
    )
    def __init__(self):

        # Numbers
        self.arabic_num = ArabicNumerics.arabic_number_translation_src
        self.english_num = ArabicNumerics.arabic_number_translation_dst

        # Arabic chars
        templ1 = ''.join([y + ''.join(x.split('|')) for x, y in ArabicChars.arabic_normalizations['chars']])
        templ2 = ''.join([''.join(x.split('|')) for x, y in ArabicChars.replacements])
        self.arabic_all_alpha = ArabicChars.sort_char_list(templ1+templ2)
        self.arabic_normal_alpha = ArabicChars.sort_char_list(''.join([y for x,y in ArabicChars.arabic_normalizations['chars']]))

        # Diac. chars
        self.base_diac = ArabicDiacritics.diacritics
        self.arabic_all_diac = ArabicChars.sort_char_list(self.base_diac+
            ''.join([y + ''.join(x.split('|')) for x, y in ArabicChars.arabic_normalizations['diac']]))
        self.arabic_normal_diac_quranic = ArabicChars.sort_char_list(ArabicDiacritics.quranic_symbols)
        self.arabic_normal_diac = ArabicChars.sort_char_list(self.base_diac+''.join([y for x, y in ArabicChars.arabic_normalizations['diac']]))

        # Punc. chars
        self.english_punc = string.punctuation
        self.base_punc = self.english_punc+'\t \n'+string.punctuation+ArabicPunctuations.punc_before+ArabicPunctuations.punc_others+ArabicPunctuations.punc_after
        self.arabic_all_punc = ArabicChars.sort_char_list(self.base_punc+''.join([y + ''.join(x.split('|')) for x, y in ArabicChars.arabic_normalizations['punc']]))
        self.arabic_normal_punc = ArabicChars.sort_char_list(self.base_punc+''.join([y for x, y in ArabicChars.arabic_normalizations['punc']]))

        # Define the regex for non-Arabic characters
        # | Component                                          | Description                                                                                   | Examples                        |
        # |----------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------|
        # | `[^...]`                                           | Matches any character not in the brackets (negation)                                          | Any character not specified below |
        # | `0-9`                                              | Digits (0-9)                                                                                  | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9    |
        # | `\u0600-\u06ff`                                    | Arabic                                                                                       | ا, ب, ت, ث, ج, ح, خ             |
        # | `\u0750-\u077f`                                    | Arabic Supplement                                                                            | ݐ, ݑ, ݒ, ݓ, ݔ, ݕ, ݖ          |
        # | `\ufb50-\ufbc1`                                    | Arabic Presentation Forms-A                                                                  | ﭐ, ﭑ, ﭒ, ﭓ, ﭔ, ﭕ, ﭖ, ﭗ          |
        # | `\ufbd3-\ufd3f`                                    | Arabic Presentation Forms-A (continuation)                                                   | ﭙ, ﭚ, ﭛ, ﭜ, ﭝ, ﭞ, ﭟ, ﭠ          |
        # | `\ufd50-\ufd8f`                                    | Arabic Presentation Forms-A (additional range)                                               | ﵐ, ﵑ, ﵒ, ﵓ, ﵔ, ﵕ, ﵖ, ﵗ          |
        # | `\ufe70-\ufefc`                                    | Arabic Presentation Forms-B                                                                  | ﹰ, ﹱ, ﹲ, ﹳ, ﹴ, ﹵, ﹶ, ﹷ          |
        # | `\uFDF0-\uFDFD`                                    | Arabic characters used in Quranic text                                                       | ﷺ               |
        # | `.`                                                | Period                                                                                       | .                               |
        # | `\s`                                               | Whitespace characters (space, tab, newline, etc.)                                            | (space), (tab), (newline)       |
        # | `,`                                                | Comma                                                                                        | ,                               |
        # | `!`                                                | Exclamation mark                                                                             | !                               |
        # | `?`                                                | Question mark                                                                                | ?                               |
        # | `;`                                                | Semicolon                                                                                    | ;                               |
        # | `،`                                                | Arabic comma                                                                                 | ،                               |
        # | `:`                                                | Colon                                                                                        | :                               |
        # | `؛`                                                | Arabic semicolon                                                                             | ؛                               |
        # | `»«`                                               | Arabic quotation marks                                                                       | » «                             |
        # | `؟`                                                | Arabic question mark                                                                         | ؟                               |
        # | `+`                                                | Matches one or more of the preceding token                                                   |                                 |

        # Normalized Characterset in Arabic
        self.norm_in_arabic = ArabicChars.sort_char_list(self.arabic_normal_alpha+self.arabic_normal_punc+self.arabic_normal_diac+self.english_num) #,self.arabic_normal_diac_quranic
        temp_str = '[^\w'+self.norm_in_arabic+']+'
        self.allowed_chars_pattern_normalized = re.compile(temp_str)
        temp_str = '[^'+self.norm_in_arabic+']+'
        self.allowed_only_arabic_chars_pattern_normalized = re.compile(temp_str)
        self.non_arabic_regex = re.compile(
            "[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD.0-9\s.,!?;،:؛»«؟]+")

        self.repetition_normalized = ArabicChars.sort_char_list(self.arabic_normal_alpha+"!?؟")
    @staticmethod
    def sort_char_list(charlist_str):
        unique_charlist = list(set(list(charlist_str)))
        unique_charlist.sort()
        return ''.join(unique_charlist)
