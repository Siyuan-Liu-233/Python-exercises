import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy as np

text_from_file_with_apath = open('1.txt').read()
mask_x=np.array(Image.open('1.jpg'))
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wordlist_after_jieba=set(wordlist_after_jieba)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(mask=mask_x,width=800,height=400,max_font_size=84,min_font_size=16,font_path=r"C:\Windows\Fonts\STSONG.ttf").generate(wl_space_split)


plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
