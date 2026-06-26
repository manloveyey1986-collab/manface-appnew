
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

# บังคับใช้ธีมพรีเมียมสีชมพูอ่อนสไตล์ Luxury Minimalist ผ่าน CSS ขั้นสูงที่คุณออกแบบ
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
# SECTION 2: CORE DATABASE ARCHITECTURE (SESSION STATE) & CLOUD SERVER
# =========================================================================

# 🌐 ฐานข้อมูลเซิร์ฟเวอร์ส่วนกลาง (เพื่อให้ทุกคนเห็นโพสต์ แชท และเพื่อนตรงกันทันทีแบบแอปดัง)
@st.cache_resource
def init_shared_cloud_database():
    return {
        "users": {"admin": "1234", "แมนเฟซ": "1234"},
        "friends_matrix": {"admin": [], "แมนเฟซ": []},
        "posts_db": [
            {
                "id": 1,
                "user": "กวินท์ ดูวาล",
                "time": "10 นาทีที่แล้ว",
                "text": "ระบบแอป Manface ตัวใหม่รันโค้ดยาวลื่นไหลมากครับ อัปโหลดรูปภาพได้จริงด้วย โคตรตึง! 🔥",
                "image": None,
                "likes": 84,
                "comments": [{"user": "สมชาย ใจดี", "text": "สวยงามมากครับแอปนี้"}]
            },
            {
                "id": 2,
                "user": "ระบบอัตโนมัติ",
                "time": "1 ชั่วโมงที่แล้ว",
                "text": "ยินดีต้อนรับสู่โครงสร้างระบบ Super App ใช้งานได้จริงทุกหมวดหมู่ เลือกเมนูด้านซ้ายเพื่อเริ่มสนุกได้เลยครับ",
                "image": None,
                "likes": 29,
                "comments": []
            }
        ],
        "global_chats": [
            {"sender": "ระบบ", "text": "ยินดีต้อนรับสู่ห้องแชทด่วนของทุกคนคราบ!", "time": "12:00"}
        ]
    }

cloud_db = init_shared_cloud_database()

# ตั้งค่าสถานะประจำเครื่องของผู้เข้าชม (รูปแบบเดิม)
if 'page' not in st.session_state:
    st.session_state.page = "Feed"

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'current_user' not in st.session_state:
    st.session_state.current_user = {"name": "นายแมนเฟซ พรีเมียม", "avatar": "💗"}

if 'ai_messages' not in st.session_state:
    st.session_state.ai_messages = [
        {"role": "assistant", "content": "สวัสดีค่ะ! ฉันคือ Meta AI ผู้ช่วยอัจฉริยะในธีมสีชมพูของคุณ วันนี้มีอะไรให้ฉันช่วยวิเคราะห์หรือเขียนโค้ดไหมคะ?"}
    ]

if 'market_products' not in st.session_state:
    st.session_state.market_products = [
        {"id": 101, "title": "iPhone 15 Pro Max 256GB สภาพ 99%", "price": 25000, "img": None, "owner": "ร้านโมบายพรีเมียม"},
        {"id": 102, "title": "รองเท้าผ้าใบสปอร์ต Limited Edition", "price": 12000, "img": None, "owner": "สมชาย สปอร์ต"},
        {"id": 103, "title": "หูฟังไร้สายขจัดเสียงรบกวน (ชมพูพาสเทล)", "price": 3500, "img": None, "owner": "Gadget Studio"}
    ]

if 'shopping_cart' not in st.session_state:
    st.session_state.shopping_cart = []

if 'game_number' not in st.session_state:
    st.session_state.game_number = random.randint(1, 100)
if 'game_count' not in st.session_state:
    st.session_state.game_count = 0

def switch_page(target):
    st.session_state.page = target

# =========================================================================
# 📝 ประตูล็อกอินเข้าสู่ระบบ (ถ้ายังไม่ล็อกอิน ให้สมัครสมาชิกตรงนี้ก่อน)
# =========================================================================
if not st.session_state.logged_in:
    st.title("💖 ยินดีต้อนรับสู่ Manface Super App Pro")
    st.write("กรุณาสมัครสมาชิก หรือ เข้าสู่ระบบเพื่อเชื่อมต่อเครือข่ายออนไลน์ร่วมกับคนอื่น")
    
    tab1, tab2 = st.tabs(["➡️ เข้าสู่ระบบ (Login)", "📝 สมัครสมาชิก (Register)"])
    with tab1:
        log_u = st.text_input("ชื่อผู้ใช้งาน (Username):", key="gate_u").strip()
        log_p = st.text_input("รหัสผ่าน (Password):", type="password", key="gate_p").strip()
        if st.button("ตกลงเข้าสู่ระบบ", type="primary"):
            if log_u in cloud_db["users"] and cloud_db["users"][log_u] == log_p:
                st.session_state.logged_in = True
                st.session_state.current_user = {"name": log_u, "avatar": "💗"}
                st.success("เข้าสู่ระบบสำเร็จ!")
                st.rerun()
            else:
                st.error("Username หรือ Password ไม่ถูกต้องคราบ")
    with tab2:
        reg_u = st.text_input("ตั้งชื่อผู้ใช้งาน (ภาษาอังกฤษ):", key="gate_reg_u").strip()
        reg_p1 = st.text_input("ตั้งรหัสผ่าน:", type="password", key="gate_reg_p1").strip()
        reg_p2 = st.text_input("ยืนยันรหัสผ่านอีกครั้ง:", type="password", key="gate_reg_p2").strip()
        if st.button("ยืนยันการสมัครสมาชิก"):
            if not reg_u or not reg_p1: st.error("กรุณากรอกข้อมูลให้ครบถ้วน")
            elif reg_p1 != reg_p2: st.error("รหัสผ่านไม่ตรงกัน")
            elif reg_u in cloud_db["users"]: st.error("ชื่อนี้มีคนใช้แล้ว")
            else:
                cloud_db["users"][reg_u] = reg_p1
                cloud_db["friends_matrix"][reg_u] = []
                st.success("สมัครสมาชิกสำเร็จ! สลับไปล็อกอินได้เลยคราบ")

# =========================================================================
# SECTION 3: PREMIUM SIDEBAR NAVIGATION (รูปแบบเดิมเป๊ะๆ)
# =========================================================================
else:
    # ตรวจสอบลิสต์เพื่อนหลังบ้าน
    if st.session_state.current_user["name"] not in cloud_db["friends_matrix"]:
        cloud_db["friends_matrix"][st.session_state.current_user["name"]] = []

    my_name = st.session_state.current_user["name"]

    with st.sidebar:
        st.markdown("<h1 style='color: #FF1493; text-align: center; margin-bottom: 0px;'>💗 Manface</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #DB7093; font-size: 14px;'>Super App Ecosystem Pro</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            col_av, col_name = st.columns(2)
            with col_av:
                st.markdown(f"<h2>{st.session_state.current_user['avatar']}</h2>", unsafe_allow_html=True)
            with col_name:
                st.markdown(f"**{st.session_state.current_user['name']}**")
                st.caption("status: สมาชิกออนไลน์")
                
        st.write("---")
        st.markdown("### 🏠 ฟังก์ชันหลัก")
        if st.button("🗞️ ฟีดข่าวสังคม (News Feed)"): switch_page("Feed")
        if st.button("🤖 Meta AI อัจฉริยะ (Chatbot)"): switch_page("MetaAI")
        if st.button("👥 ระบบเครือข่ายเพื่อน (Friends)"): switch_page("FriendsList")
        if st.button("💬 ห้องแชทสดทุกคน (Global Chat)"): switch_page("GlobalChat")
        
        st.markdown("### 🛍️ ตลาดและความบันเทิง")
        if st.button("🛒 มาร์เก็ตเพลส (Marketplace)"): switch_page("Marketplace")
        if st.button("🎮 ศูนย์รวมเกมส์ (Gaming Hub)"): switch_page("Gaming")
        st.markdown("### 📈 ข้อมูลหลังบ้านธุรกิจ")
        if st.button("📊 ตัวจัดการโฆษณา (Ads Manager)"): switch_page("Ads")
        st.write("---")
        if st.button("🚪 ออกจากระบบ (Logout)"):
            st.session_state.logged_in = False
            st.rerun()
        st.caption("เวอร์ชันคอนเซ็ปต์ใช้งานจริง • v2.5.0")

    # =========================================================================
    # SECTION 4: SYSTEM MODULES AND PAGES FUNCTIONALITY (รูปแบบเดิม+เชื่อมออนไลน์จริง)
    # =========================================================================
    if st.session_state.page == "Feed":
        st.markdown("<h2 style='color: #DB7093;'>🗞️ ฟีดข่าวและชุมชน Manface</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("✍️ **คุณกำลังคิดอะไรอยู่? สร้างโพสต์ใหม่เลย**")
            input_text = st.text_area("เขียนข้อความบรรยาย...", key="new_post_text")
            upload_img = st.file_uploader("📸 แนบรูปภาพประกอบโพสต์ของคุณ", type=["png", "jpg", "jpeg"])
            
            if st.button("🚀 เเพร่เผยโพสต์ลงกระดานข่าว"):
                if input_text.strip() or upload_img is not None:
                    final_img = None
                    if upload_img is not None:
                        final_img = Image.open(upload_img)
