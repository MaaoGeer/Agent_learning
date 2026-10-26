import streamlit as st
from openai import OpenAI
import json
from datetime import datetime
import os

# 页面配置项
st.set_page_config(page_title="AI智能伴侣",
                   page_icon="🤖",
                   layout="wide",
                   initial_sidebar_state="expanded", # 侧边栏状态
)

# 保存当前会话
def save_session():
    if st.session_state.curr_session:
        session_data = {
            "name": st.session_state.name,
            "character": st.session_state.character,
            "curr_session": st.session_state.curr_session,
            "messages": st.session_state.messages
        }
        if not os.path.exists(f"./sessions"):
            os.mkdir(f"./sessions")
        with open(f"./sessions/{st.session_state.curr_session}.json", "w", encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

# 生成新会话信息
def new_session():
    st.session_state.curr_session = datetime.now().strftime("%Y%m%d_%H%M%S")
    st.session_state.messages = []

# 加载所有会话信息
def load_session():
     sess_list = []
     file_list = os.listdir(f"./sessions")
     for file in file_list:
         if file.endswith(".json"):
             sess_list.append(file[:-5])

     sess_list.sort(reverse=True)
     return sess_list

# 加载会话
def display_session(session):
    try:
        with open("./sessions/" + session + ".json", "r", encoding='utf-8') as f:
            session_data = json.load(f)
            st.session_state.curr_session = session_data["curr_session"]
            st.session_state.messages = session_data["messages"]
            st.session_state.character = session_data["character"]
            st.session_state.name = session_data["name"]

    except Exception as e:
        st.error('会话不存在!')

# 删除历史会话
def delete_session(session):
    if os.path.exists(f"./sessions/{session}.json"):
        os.remove(f"./sessions/{session}.json")
        if session == st.session_state.curr_session:
            st.session_state.messages = []
            st.session_state.curr_session = None

# 标题
st.title("AI智能伴侣")

client = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

# 历史消息
if "messages" not in st.session_state:
    st.session_state.messages = []

if "curr_session" not in st.session_state:
    st.session_state.curr_session = datetime.now().strftime("%Y%m%d_%H%M%S")

if "name" not in st.session_state:
    st.session_state.name = "大鲸鱼"

if "character" not in st.session_state:
    st.session_state.character = "请你用温柔可爱的语气回答客户问题，回答以'喵'+'表达当前心情的颜文字'结束"

st.text(f"会话名称{st.session_state.curr_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])


# 侧边栏
with st.sidebar:
    st.subheader("智能体控制面板")

    # 新建回话
    if st.button("新建会话",width="stretch",icon="🌏"):
        save_session()
        if st.session_state.messages:
            new_session()
            save_session()
            st.rerun()

    # 会话历史
    st.text("历史会话")
    sess_list = load_session()
    for sess in sess_list:
        col1,col2 = st.columns([4,1])
        with col1:
            # 加载会话信息
            if st.button(sess,width="stretch",icon="📜", type="primary" if st.session_state.curr_session == sess else "secondary"):
                if st.session_state.messages:
                    save_session()

                display_session(sess)
                st.rerun()

        with col2:
            # 删除会话信息
            if st.button("", width="stretch", icon="❌", key=sess):  # 使用key为每个删除按钮赋予唯一标识
                delete_session(sess)
                st.rerun()

    name = st.text_input("智能体名字", placeholder="请输入昵称", value=st.session_state.name)
    if name:
        st.session_state.name = name
    character = st.text_area("智能体性格", placeholder="请输入性格",value=st.session_state.character)
    if character:
        st.session_state.character = character

system_prompt = f"你的名字叫{name},{character}"
st.session_state.system_settings = [{"role": "system", "content": system_prompt }]



prompt = st.chat_input("Say something")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # noinspection bad-argument-type
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[*st.session_state.system_settings,*st.session_state.messages],  # 列表解包，将列表中的每个元素提取出来，等价于system_setting+st.session_state.messages
        stream=True
    )
    # 非流式输出回应方式
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    # 流式输出
    res_message = ""
    full_message = st.empty()   # 创建一个空组件
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            res_message += content or ""
            full_message.chat_message("assistant").write(res_message)

    st.session_state.messages.append({"role": "assistant", "content": res_message})


if st.session_state.messages:
    save_session()
