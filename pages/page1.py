import streamlit as st
import os

st.title(':rainbow[何瑾渝小帅哥的私照]')
# 创建三个 Tab
tab1, tab2, tab3 = st.tabs(["第一页", "第二页", "第三页"])
image_count = len([name for name in os.listdir('images') if os.path.isfile(os.path.join('images', name))])
with tab1:
    #获取文件夹里面的图片数量
    for i in range(1,17):
        st.image("images/" + str(i) +".jpg", caption="", use_container_width=True)
    st.title(":rainbow[到底了]")

with tab2:
    for i in range(17,34):
        st.image("images/" + str(i + 1) + ".jpg", caption="", use_container_width=True)
    st.title(":rainbow[到底了]")
with tab3:
    for i in range(34, image_count):
        st.image("images/" + str(i + 1) + ".jpg", caption="", use_container_width=True)
    st.title(":rainbow[到底了]")