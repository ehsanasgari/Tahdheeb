import os,sys
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
module_path = os.path.join(current_dir, '..')
sys.path.append(module_path)
from src.preprocessing.text_content import ArabicTextProcess
from src.preprocessing.text_verification import ArabicTextVerify
from src.preprocessing.text_structure import ArabicStructure


text = 'الـــــــــسلام    عليكم . كيـــف    حالك ؟ أتـــمنى أن تكون بــــــخير .أ نحنو  هنا للمســـــاعدة ...هل  تريــــد شيء مـــا؟  الرجـــــــاء    إبلاغن ا بــــأي وقــــت! في ٢دقيقه شكرا ، جزيــــلا Thanks!'

# fixing punc issue and text structure
ATB = ArabicStructure()
# preprocessing the text
ASP = ArabicTextProcess()

ATP=ArabicTextVerify()
print('Ratio of Arabic text:', ATP.check_arabic_ratio(text))

print('\ntext before struct improving:\n', text, '\n-----------\n')
text = ATB.preprocess(text, remove_english=True)
print('\ntext after struct improving:\n', text, '\n-----------\n')
text = ASP.get_arabic_normal(text,  extensive_normalization=False)
print('\ntext after normalizing:\n', text, '\n-----------\n')
text = ASP.get_arabic_normal(text, extensive_normalization=True)
print('\ntext after extensive normalizing:\n', text, '\n-----------\n')




