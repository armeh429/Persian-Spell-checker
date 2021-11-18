#!/usr/bin/env python
# coding: utf-8

# In[14]:


# my eddited code from :
#!/usr/bin/python
# -*- coding: utf-8  -*-
#
# Reza(User:reza1615), 2011
#
# Distributed under the terms of GNU Lesser General Public License (LGPL 2.1)
#coding:utf8
# add some line to avoid charechter repitation in each words 

import codecs,re
def arabic_to_farsi(text):
    text = re.sub(u'[كﮑﮐﮏﮎﻜﻛﻚﻙ]', u'ک', text)
    text = re.sub(u'[ىىىﻴﻢﻳﻲﻱﻰىىﻯي]', u'ی', text)
    return text

text2 = codecs.open('seller01.txt',u'r' ,u'utf8' )
text = text2.read()
text = re.sub(u'[چ]{2,}', u'چ' , text)
text = re.sub(u'[ج]{2,}', u'ج' , text)
text = re.sub(u'[ح]{2,}', u'ح' , text)
text = re.sub(u'[خ]{2,}', u'خ' , text)
text = re.sub(u'[ه]{2,}', u'ه' , text)
text = re.sub(u'[ع]{2,}', u'ع' , text)
text = re.sub(u'[غ]{2,}', u'غ' , text)
text = re.sub(u'[ف]{2,}', u'ف' , text)
text = re.sub(u'[ق]{2,}', u'ق' , text)
text = re.sub(u'[ث]{2,}', u'ث' , text)
text = re.sub(u'[ص]{2,}', u'ص' , text)
text = re.sub(u'[ض]{2,}', u'ض' , text)
text = re.sub(u'[پ]{2,}', u'پ' , text)
text = re.sub(u'[گ]{2,}', u'گ' , text)
text = re.sub(u'[ک]{2,}', u'ک' , text)
text = re.sub(u'[م]{2,}', u'م' , text)
text = re.sub(u'[ن]{2,}', u'ن' , text)
text = re.sub(u'[ت]{2,}', u'ت' , text)
text = re.sub(u'[ا]{2,}', u'ا' , text)
text = re.sub(u'[ل]{2,}', u'ل' , text)
text = re.sub(u'[ب]{2,}', u'ب' , text)
text = re.sub(u'[ی]{2,}', u'ی' , text)
text = re.sub(u'[س]{2,}', u'س' , text)
text = re.sub(u'[ش]{2,}', u'ش' , text)
text = re.sub(u'[و]{2,}', u'و' , text)
text = re.sub(u'[د]{2,}', u'د' , text)
text = re.sub(u'[ذ]{2,}', u'ذ' , text)
text = re.sub(u'[ر]{2,}', u'ر' , text)
text = re.sub(u'[ز]{2,}', u'ز' , text)
text = re.sub(u'[ط]{2,}', u'ط' , text)
text = re.sub(u'[ظ]{2,}', u'ظ' , text)
text=re.sub(u'[۰۱۲۳۴۵۶۷۸۹٠١١٢٣٤٥٦٧٧٨٨٩٩●]',u' ',text)
text=re.sub(u'[\·\♦\٭\\,\^\|\˝\٬\’\”\‹\▪\○¼ç½éêüəıœ™Ááàäāćíłñū©ٰٔ]',u' ',text)
text=re.sub(u'[ًٌٍَُِّْ]',u' ',text)
text=re.sub(u'[]',u' ',text)
text=re.sub(u'[\–\—…°≈≠±≤≥\−×÷√٪→←↔↑↓\#\٫]',u' ',text) 
text=text.replace(u'•',u' ').replace(u'ˈ',u' ').replace(u'؛',u' ').replace(u'/',u' ').replace(u'ۀ',u'هٔ').replace(u"﴿",u' ').replace(u"﴾",u' ').replace(u"'",u' ').replace(u'\\',u' ').replace(u'[',u' ').replace(u']',u' ').replace(u'?',u' ').replace(u'؟',u' ').replace(u')',u' ').replace(u'_',u' ').replace(u'(u',u' ').replace(u'}',u' ').replace(u'{',u' ').replace(u'.',u' ').replace(u'>',u' ').replace(u'<',u' ')
text=text.replace(u'`',u' ').replace(u'\t',u' ').replace(u'=',u' ').replace(u'»',u' ').replace(u'«',u' ').replace(u'~',u' ').replace(u'!',u' ').replace(u'@',u' ').replace(u'$',u' ').replace(u',u',u' ').replace(u'%',u' ').replace(u'،',u' ').replace(u'-',u' ').replace(u';',u' ').replace(u':',u' ').replace(u'*',u' ').replace(u'"',u' ').replace(u'&',u' ').replace(u'#',u' ').replace(u'+',u' ')
text=re.sub(u'[\n\r]{2,}',u'\n',text)
text = re.sub(u'(\u202A|\u202B|\u202C|\u202D|\u202E|\u200F|\uFEFF|\u2003|\¬|\­)',u'\u200C', text)#حذف کارکترهای تغییرجهت
text = re.sub(u'‌{2,}', u'‌', text) # پشت‌سرهم
text = re.sub(u'‌(?![ئاآأإژزرذدوؤةبپتثجچحخسشصضطظعغفقکگلمنهیيًٌٍَُِّْٰٓٔ]|[\u0900-\u097F]|ֹ)', u'', text) # در پس
text = re.sub(u'(?<![ئبپتثجچحخسشصضطظعغفقکگلمنهیيًٌٍَُِّْٰٓٔ]|[\u0900-\u097F]|f|ֹ)‌', u'', text) # در پیش
text=text.replace(u'­',u' ').replace(u'­',u' ').replace(u'ـ',u' ').replace(u'ـ',u' ').replace(u'ـ',u' ').replace(u'ـ',u' ').replace(u'',u' ')
text=text.replace(u'',u' ')
text = re.sub(u'‌{2,}', u'‌', text) # پشت‌سرهم
text = re.sub(u'(\u00A0)',u' ', text).replace(u'(',u' ').replace(u')',u' ')
text=text.replace(u'    ',u' ').replace(u'    ',u' ').replace(u'   ',u' ').replace(u'  ',u' ').replace(u'  ',u' ').replace(u'  ',u' ')
text=arabic_to_farsi(text)

with codecs.open('FinallResult-list-2.txt',mode = 'w',encoding = 'utf8') as f:
    f.write(text.strip())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




