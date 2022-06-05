from matplotlib.pyplot import axis
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlitt超超入門')

st.write("プレグレスバーの表示")
'スタート'


latest_itertion= st.empty()
bar = st.progress(0)
bar2 = st.progress(0)

for i in range(100):
    latest_itertion.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done'

left_column, right_column= st.beta_columns(2)

button= left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander= st.beta_expander('問い合わせ')
expander.write('問い合わせを開く')

# text = st.text_input('あなたの趣味を教えて下さい')
# condition= st.slider('あなたの今の調子は?', 0, 100, 50)








# # 写真の読み込みの実験
# img= st.file_uploader('Upload a image')
# data = Image.open(img)
# 'あなたの趣味', text
# 'コンディション:', condition
# 'img:', img,
# 'data', data
# st.image(data, caption='Hayato', use_column_width=True)
# # st.image(img, caption='あなたの写真', )



