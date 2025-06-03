import streamlit as st
import os


st.title(':rainbow[何瑾渝小帅哥的靓爸靓妈]')

# 创建三个 Tab
tab1, tab2, tab3 = st.tabs(["第一页", "第二页", "第三页"])
image_count = len([name for name in os.listdir('images') if os.path.isfile(os.path.join('images', name))])
with tab1:
    st.video("video/1.mp4", format="video/mp4")
with tab2:
    pass
with tab3:
    pass
