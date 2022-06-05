from matplotlib.pyplot import axis
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlitt超超入門')

st.write("InteractiveなWidget")

text = st.text_input('あなたの趣味を教えて下さい')
'あなたの趣味', text

condition= st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディション:', condition

rb = st.radio('選択式', ["はい", "いいえ"])
'選択:', rb



st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
# * optional kwarg unsafe_allow_html = True

st.button('Click me')
st.checkbox('I agree')
st.radio('Pick one', ['cats', 'dogs'])
st.selectbox('Pick one', ['cats', 'dogs'])
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
st.select_slider('Pick a size', ['S', 'M', 'L'])
st.text_input('First name')
st.number_input('Pick a number', 0, 10)
st.text_area('Text to translate')
st.date_input('Your birthday')
st.time_input('Meeting time')
st.file_uploader('Upload a CSV')
st.download_button('Download file', data)
st.camera_input("Take a picture")
st.color_picker('Pick a color')

# Image.open('DSC_4372.jpg')

# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

# 'あなたのすきな数字は', option, 'です'
# if st.checkbox('Show Image'):
#     img = Image.open('DSC_4372.jpg')
#     st.image(img, caption='Hayato', use_column_width=True)


