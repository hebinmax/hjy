import streamlit as st
import os

# 创建侧边栏内容

page1 = st.Page('pages/page1.py', title='图片')
page2 = st.Page('pages/page2.py', title='视频')
st.navigation([page1, page2]).run()

# 创建三个 Tab
# tab1, tab2, tab3 = st.tabs(["第一页", "第二页", "第三页"])
# image_count = len([name for name in osa.listdir('images') if os.path.isfile(os.path.join('images', name))])
# with tab1:
#     #获取文件夹里面的图片数量
#     for i in range(1,17):
#         st.image("images/" + str(i) +".jpg", caption="", use_container_width=True)
#
#
# with tab2:
#     for i in range(17,34):
#         st.image("images/" + str(i + 1) + ".jpg", caption="", use_container_width=True)
#
# with tab3:
#     for i in range(34, image_count):
#         st.image("images/" + str(i + 1) + ".jpg", caption="", use_container_width=True)
