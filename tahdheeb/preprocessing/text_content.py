# -*- coding: utf-8 -*-

import re
import os, sys
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
module_path = os.path.join(current_dir, '../')
sys.path.append(module_path)
from arabic_utility.arbchar_util import ArabicChars
from arabic_utility.num_util import ArabicNumerics
from arabic_utility.diac_util import ArabicDiacritics

class ArabicTextProcess(object):
    def __init__(self):

        self.arabic_normalizations_2nd_phase_extensive = [
            # REVIEWED Horuf
            (r"ا|إ|أ", r"ا"),
            (r"ؤ|و", r"و"),
            (r"ه|ة", r"ه"),
            (r"ي|ى", r"ى"),
        ]

        self.alpha_regex = dict()
        for _, arabic_normalizations in ArabicChars.arabic_normalizations.items():
            for x, y in arabic_normalizations:
                self.alpha_regex[y] = re.compile(x)

        self.beta_regex = dict()
        for x, y in self.arabic_normalizations_2nd_phase_extensive:
            self.beta_regex[y] = re.compile(x)

        self.number_translate = str.maketrans(
            dict(zip(list(ArabicNumerics.arabic_number_translation_src), list(ArabicNumerics.arabic_number_translation_dst))))

        # used from HAZM
        self.persion_translation_src = "ؠػػؽؾؿكيٮٯٷٸٹٺٻټٽٿڀځٵٶٷٸٹٺٻټٽٿڀځڂڅڇڈډڊڋڌڍڎڏڐڑڒړڔڕږڗڙښڛڜڝڞڟڠڡڢڣڤڥڦڧڨڪګڬڭڮڰڱڲڳڴڵڶڷڸڹںڻڼڽھڿہۂۃۄۅۆۇۈۉۊۋۏۍێېۑےۓەۮۯۺۻۼۿݐݑݒݓݔݕݖݗݘݙݚݛݜݝݞݟݠݡݢݣݤݥݦݧݨݩݪݫݬݭݮݯݰݱݲݳݴݵݶݷݸݹݺݻݼݽݾݿࢠࢡࢢࢣࢤࢥࢦࢧࢨࢩࢪࢫࢮࢯࢰࢱࢬࢲࢳࢴࢶࢷࢸࢹࢺࢻࢼࢽﭐﭑﭒﭓﭔﭕﭖﭗﭘﭙﭚﭛﭜﭝﭞﭟﭠﭡﭢﭣﭤﭥﭦﭧﭨﭩﭮﭯﭰﭱﭲﭳﭴﭵﭶﭷﭸﭹﭺﭻﭼﭽﭾﭿﮀﮁﮂﮃﮄﮅﮆﮇﮈﮉﮊﮋﮌﮍﮎﮏﮐﮑﮒﮓﮔﮕﮖﮗﮘﮙﮚﮛﮜﮝﮞﮟﮠﮡﮢﮣﮤﮥﮦﮧﮨﮩﮪﮫﮬﮭﮮﮯﮰﮱﺀﺁﺃﺄﺅﺆﺇﺈﺉﺊﺋﺌﺍﺎﺏﺐﺑﺒﺕﺖﺗﺘﺙﺚﺛﺜﺝﺞﺟﺠﺡﺢﺣﺤﺥﺦﺧﺨﺩﺪﺫﺬﺭﺮﺯﺰﺱﺲﺳﺴﺵﺶﺷﺸﺹﺺﺻﺼﺽﺾﺿﻀﻁﻂﻃﻄﻅﻆﻇﻈﻉﻊﻋﻌﻍﻎﻏﻐﻑﻒﻓﻔﻕﻖﻗﻘﻙﻚﻛﻜﻝﻞﻟﻠﻡﻢﻣﻤﻥﻦﻧﻨﻩﻪﻫﻬﻭﻮﻯﻰﻱﻲﻳﻴىكي“” "
        self.persion_translation_dst = (
            'یککیییکیبقویتتبتتتبحاوویتتبتتتبحححچدددددددددررررررررسسسصصطعففففففققکککککگگگگگللللنننننهچهههوووووووووییییییهدرشضغهبببببببححددرسعععففکککممنننلررسححسرحاایییووییحسسکببجطفقلمییرودصگویزعکبپتریفقنااببببپپپپببببتتتتتتتتتتتتففففححححححححچچچچچچچچددددددددژژررککککگگگگگگگگگگگگننننننههههههههههییییءاااووااییییااببببتتتتثثثثججججححححخخخخددذذررززسسسسششششصصصصضضضضططططظظظظععععغغغغففففققققککککللللممممننننههههوویییییییکی"" '
        )

        # used from HAZM
        self.extra_patterns = [
            (re.compile(r" {2,}"), " "),  # remove extra spaces
            (re.compile(r"\n{3,}"), "\n\n"),  # remove extra newlines
            (re.compile(r"\u200c{2,}"), "\u200c"),  # remove extra ZWNJs
            (re.compile(r"\u200c{1,} "), " "),  # remove unneded ZWNJs before space
            (re.compile(r" \u200c{1,}"), " "),  # remove unneded ZWNJs after space
            (re.compile(r"\b\u200c*\B"), ""),  # remove unneded ZWNJs at the beginning of words
            (re.compile(r"\B\u200c*\b"), ""),  # remove unneded ZWNJs at the end of words
            (re.compile(r"[ـ\r]"), ""),  # remove keshide, carriage returns
        ]

        # used from HAZM
        self.arabic_style_patterns = [
            (re.compile(r'"([^\n"]+)"'), r"«\1»"),  # replace quotation with gyoome
            (re.compile(r"([\d+])\.([\d+])"), r"\1٫\2"),  # replace dot with momayez
            # (re.compile(r" ?\.\.\."), " …"),  # replace 3 dots
        ]

        # modified from HAZM
        self.general_repeat = (
            re.compile(r'([ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي!?؟])\1{2,}')
        )


    def get_arabic_normalized_pretokenization(self, text, remove_non_arabic=True):

        for old, new in ArabicChars.replacements:
            text = re.sub(old, new, text)

        # normalize the chars
        for alternative, regx in self.alpha_regex.items():
            text = re.sub(regx, alternative, text)

        # normalize the numbers
        text = text.translate(self.number_translate)

        # fix punc
        for x, y in self.extra_patterns + self.arabic_style_patterns:
            text = re.sub(x, y, text)

        # remove repeats
        matches = re.finditer(self.general_repeat, text)

        for m in matches:
            word = m.group()
            # no_repeat = re.sub(self.general_repeat, r"\1", word)
            two_repeat = re.sub(self.general_repeat, r"\1\1", word)
            text = text.replace(word, two_repeat)

        allowed_chars_pattern = re.compile(
            r'[^\w+"\'()\-\.:,!?;،؛»«؟<>ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي0123456789% \u064b\u064c\u064d\u0652\u064e\u064f\u0650\u0651\u0652\u0653\u0670\u06d6\u06d7\u06d8\u06d9\u06da\u06db\u06dc\u06e9\u06e7\u06e8]+')

        cleaned_text = text
        if remove_non_arabic:
            en_chars = re.compile(r'[a-zA-Z]')
            cleaned_text = re.sub(en_chars, '', text)
        cleaned_text = re.sub(allowed_chars_pattern, '', cleaned_text)

        return cleaned_text

    def get_arabic_normalized(self, text):

        for old, new in self.replacements:
            text = re.sub(old, new, text)

        # normalize the chars
        for alternative, regx in self.alpha_regex.items():
            text = re.sub(regx, alternative, text)

        # normalize the numbers
        text = text.translate(self.number_translate)

        for x, y in self.extra_patterns + self.arabic_style_patterns:
            text = re.sub(x, y, text)

        matches = re.finditer(self.general_repeat, text)

        for m in matches:
            word = m.group()
            # no_repeat = re.sub(self.general_repeat, r"\1", word)
            two_repeat = re.sub(self.general_repeat, r"\1\1", word)
            text = text.replace(word, two_repeat)

        return text
