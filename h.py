
import streamlit as st
import pandas as pd
import numpy as np
import random
from PIL import Image
import datetime

# =========================================================================
# SECTION 1: CONFIGURATION & PREMIUM LUXURY PINK STYLING (CSS ขั้นสูง)
# =========================================================================
st.set_page_config(
    layout="wide", 
    page_title="Manface Super App Pro", 
    page_icon="♾️",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        .stApp { background-color: #FFF0F5; }
        [data-testid="stSidebar"] { background-color: #FFE4E1; box-shadow: 2px 0px 15px rgba(0,0,0,0.05); }
        [data-testid="stMetricContainer"] {
            background-color: #FFFFFF !important;
            border: 1px solid #FFB6C1 !important;
            padding: 15px !important;
            border-radius: 15px !important;
            box-shadow: 0px 4px 12px rgba(255, 182, 193, 0.2);
        }
        div.stButton > button:first-child {
            background-color: #FFB6C1; 
            color: #333333;
            border-radius: 25px;
            border: 1px solid #FFA07A;
            font-weight: bold;
            padding: 10px 20px;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            width: 100%;
        }
        div.stButton > button:first-child:hover {
            background-color: #FF69B4; 
            color: white;
            border-color: #FF1493;
            box-shadow: 0px 6px 15px rgba(255, 105, 180, 0.4);
            transform: translateY(-1px);
        }
        .stImage > img { border-radius: 12px !important; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); }
        .post-box {
            background-color: #FFFFFF;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 15px;
            border-left: 5px solid #FF69B4;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
        }
        .chat-bubble {
            padding: 10px 15px;
            border-radius: 15px;
            margin-bottom: 5px;
            max-width: 70%;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# SECTION 2: 📦 ระบบแชร์ข้อมูลภายใจแอป ความเร็วสูง (ไม่ล่ม 100%)
# =========================================================================
@st.cache_resource
def get_internal_db():
    return {
        "users": {"admin": "1234", "manface": "1234"},
        "posts": [
            {"user": "ระบบ", "time": "เริ่มต้น", "text": "ยินดีต้อนรับสู่ Manface Super App บอร์ดข่าวสารกลางแชร์ข้อมูลได้จริงแล้วคราบ!"}
        ],
        "chats": [
            {"sender": "ระบบ", "text": "ยินดีต้อนรับสู่ห้องแชทสดส่วนกลางของทุกคนคราบ"}
        ],
        "friends": {"admin": [], "manface": []}
    }

db = get_internal_db()

# ตัวแปรประจำเครื่องคนเปิดดู
if 'page' not in st.session_state: st.session_state.page = "Feed"
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'ai_messages' not in st.session_state: st.session_state.ai_messages = [{"role": "assistant", "content": "สวัสดีค่ะ! ฉันคือ Meta AI ผู้ช่วยอัจฉริยะในธีมสีชมพูของคุณ"}]
if 'shopping_cart' not in st.session_state: st.session_state.shopping_cart = []
if 'game_number' not in st.session_state: st.session_state.game_number = random.randint(1, 100)
if 'game_count' not in st.session_state: st.session_state.game_count = 0

if 'market_products' not in st.session_state:
    st.session_state.market_products = [
        {"id": 101, "title": "iPhone 15 Pro Max 256GB สภาพ 99%", "price": 25000, "owner": "ร้านโมบายพรีเมียม"},
        {"id": 102, "title": "รองเท้าผ้าใบสปอร์ต Limited Edition", "price": 12000, "owner": "สมชาย สปอร์ต"},
        {"id": 103, "title": "หูฟังไร้สายขจัดเสียงรบกวน (ชมพูพาสเทล)", "price": 3500, "owner": "Gadget Studio"}
    ]

def switch_page(target):
    st.session_state.page = target

# =========================================================================
# 📝 GATEWAY: หน้าต่างระบบสมัครสมาชิก และ เข้าสู่ระบบ
# =========================================================================
if not st.session_state.logged_in:
    st.title("💖 ยินดีต้อนรับสู่ Manface Super App Pro")
    st.write("กรุณาสมัครสมาชิก หรือ เข้าสู่ระบบเพื่อเชื่อมต่อสังคมออนไลน์จริง")
    
    tab1, tab2 = st.tabs(["➡️ เข้าสู่ระบบ (Login)", "📝 สมัครสมาชิก (Register)"])
    
    with tab1:
        st.subheader("🔑 ลงชื่อเข้าใช้งาน")
        log_u = st.text_input("ชื่อผู้ใช้งาน (Username):", key="gate_u").strip()
        log_p = st.text_input("รหัสผ่าน (Password):", type="password", key="gate_p").strip()
        if st.button("ตกลงเข้าสู่ระบบ", type="primary"):
            if log_u in db["users"] and db["users"][log_u] == log_p:
                st.session_state.logged_in = True
                st.session_state.username = log_u
                st.success("เข้าสู่ระบบสำเร็จคราบ!")
                st.rerun()
            else:
                st.error("ชื่อผู้ใช้งาน หรือ รหัสผ่านไม่ถูกต้องคราบ")
                
    with tab2:
        st.subheader("📝 สมัครสมาชิกใหม่")
        reg_u = st.text_input("ตั้งชื่อผู้ใช้งาน (ภาษาอังกฤษ):", key="gate_reg_u").strip()
        reg_p1 = st.text_input("ตั้งรหัสผ่าน:", type="password", key="gate_reg_p1").strip()
        reg_p2 = st.text_input("ยืนยันรหัสผ่านอีกครั้ง:", type="password", key="gate_reg_p2").strip()
        if st.button("ยืนยันการสมัครสมาชิก"):
            if not reg_u or not reg_p1: st.error("กรุณากรอกข้อมูลให้ครบถ้วน")
            elif reg_p1 != reg_p2: st.error("รหัสผ่านสองช่องไม่ตรงกัน")
            elif reg_u in db["users"]: st.error("ชื่อผู้ใช้งานนี้ถูกใช้ไปแล้ว")
            else:
                db["users"][reg_u] = reg_p1
                db["friends"][reg_u] = []
                st.success("สมัครสมาชิกสำเร็จ! สลับไปที่แท็บ 'เข้าสู่ระบบ' ได้เลยคราบ")

# =========================================================================
# SECTION 3 & 4: APPLICATION MAIN MODULES (ทำงานเมื่อเข้าสู่ระบบแล้ว)
# =========================================================================
else:
    my_name = st.session_state.username
    if my_name not in db["friends"]: db["friends"][my_name] = []
    my_friends = db["friends"][my_name]

    with st.sidebar:
        st.markdown("<h1 style='color: #FF1493; text-align: center; margin-bottom: 0px;'>💗 Manface</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #DB7093; font-size: 14px;'>Super App Ecosystem Pro</p>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f"**{my_name}** (ออนไลน์)")
        st.write("---")
        st.markdown("### 🏠 ฟังก์ชันหลัก")
        if st.button("🗞️ ฟีดข่าวสังคม (News Feed)"): switch_page("Feed")
        if st.button("🤖 Meta AI อัจฉริยะ (Chatbot)"): switch_page("MetaAI")
        if st.button("👥 ระบบเครือข่ายเพื่อน (Friends)"): switch_page("FriendsList")
        if st.button("💬 ห้องแชทสดทุกคน (Global Chat)"): switch_page("GlobalChat")
        st.markdown("### 🛍️ ตลาดและความบันเทิง")
        if st.button("🛒 มาร์เก็ตเพลส (Marketplace)"): switch_page("Marketplace")
        if st.button("🎮 ศูนย์รวมเกมส์ (Gaming Hub)"): switch_page("Gaming")
        st.write("---")
        if st.button("🚪 ออกจากระบบ (Logout)"):
            st.session_state.logged_in = False
            st.rerun()

    if st.session_state.page == "Feed":
        st.markdown("<h2 style='color: #DB7093;'>🗞️ ฟีดข่าวและชุมชน Manface (โพสต์เด้งเรียลไทม์)</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            input_text = st.text_area("เขียนข้อความบรรยาย...", key="new_post_text")
            if st.button("🚀 เผยแพร่โพสต์ลงกระดานข่าว"):
                if input_text.strip():
                    now_time = datetime.datetime.now().strftime("%H:%M:%S")
                    db["posts"].insert(0, {"user": my_name, "time": now_time, "text": input_text})
                    st.balloons()
                    st.rerun()
        st.write("---")
        for post in db["posts"]:
            with st.container(border=True):
                st.markdown(f"🗣️ **{post['user']}**  •  <span style='color: gray; font-size: 12px;'>{post['time']}</span>", unsafe_allow_html=True)
                st.write(post['text'])

    elif st.session_state.page == "FriendsList":
        st.markdown("<h2 style='color: #DB7093;'>👥 เครือข่ายการเพิ่มเพื่อนสมาชิกออนไลน์</h2>", unsafe_allow_html=True)
        st.subheader("📌 เพื่อนของฉันตอนนี้")
        if not my_friends: 
            st.info("คุณยังไม่มีรายชื่อเพื่อนในระบบ")
        else:
            for friend in my_friends: st.write(f"🧑 **{friend}** (เป็นเพื่อนกันแล้ว)")

    elif st.session_state.page == "GlobalChat":
        st.markdown("<h2 style='color: #DB7093;'>💬 ห้องแชทสดเครือข่ายสังคม (ซิงค์ทุกเครื่อง)</h2>", unsafe_allow_html=True)
        chat_box = st.container(height=350, border=True)
        with chat_box:
            for chat in db["chats"]:
                if chat["sender"] == my_name:
                    st.markdown(f"<div style='text-align: right;'><span style='background-color:#FFB6C1; display:inline-block;' class='chat-bubble'><b>คุณ</b>: {chat['text']}</span></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='text-align: left;'><span style='background-color:#FFF; border:1px solid #FFB6C1; display:inline-block;' class='chat-bubble'><b>{chat['sender']}</b>: {chat['text']}</span></div>", unsafe_allow_html=True)
        
        with st.form("send_live_msg", clear_on_submit=True):
            chat_input = st.text_input("พิมพ์ข้อความคุยแชทสด...")
            if st.form_submit_button("ส่งข้อความด่วน 🚀"):
                if chat_input.strip():
                    db["chats"].append({"sender": my_name, "text": chat_input})
                    st.rerun()

    elif st.session_state.page == "MetaAI":
