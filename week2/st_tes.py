import streamlit as st

# 页面配置项
st.set_page_config(page_title="Streamlit入门演示",
                   page_icon="😊",
                   layout="wide",
                   initial_sidebar_state=None, # 侧边栏状态
                   menu_items={
                       'Get Help': 'https://streamlit.io/',
                       'About': 'This is a streamlit demo'
                   }
)

# 标题
st.title("Streamlit 入门演示")
st.header("一级标题")
st.subheader("二级标题")

# 段落文字
st.write("布偶是起源于美国 60 年代的**大型半长毛猫**，被叫做仙女猫，抱起来全身放松软乎乎像布娃娃，因此得名")

# 图片
st.image("E:\\Agent_learning\\week2\\resources\\DM.jpg")

# 音频
st.audio("E:\\Agent_learning\\week2\\resources\\hi.mp3")

# 视频
st.video("E:\\Agent_learning\\week2\\resources\\hii.mp4")

# 表格
student_data = {
    "姓名":['wl','lxl','yyc'],
    'code':['23009200123','23009101344','23009200396']
}
st.table(student_data)

# 输入框
name = st.text_input('Please input your name:')
st.write(f"Your name is {name}")

password = st.text_input('Please input your password:',type='password')
st.write(f"Your password is {password}")

# 单选按钮
gender = st.radio("Please select your gender",['male','female','unknown'])
st.write(f"Your gender is {gender}")