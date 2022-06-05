from matplotlib.pyplot import axis
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlitt超超入門')

st.write("Display Imageだよ")

Image.open('DSC_4372.jpg')

img = Image.open('DSC_4372.jpg')
st.image(img, caption='Hayato', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69, 139.70],
#     columns=['lat', 'lon']
# )

#st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

"""
#章
##節
###項

```python
from matplotlib.pyplot import axis
import streamlit as st
import numpy as np
import pandas as pd


```
"""