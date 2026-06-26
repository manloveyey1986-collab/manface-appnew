import streamlit as st
import pandas as pd
import numpy as np
import random
from PIL import Image
import datetime

# =========================================================================
# SECTION 1: CONFIGURATION & PREMIUM LUXURY PINK STYLING (CSS ธีมสีชมพู)
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
# SECTION 2: 📦 ฐานข้อมูลจำลองส่วนกลางร่วมกัน
# =========================================================================
@st.cache_resource
def get_internal_facebook_db():
    return {
        "users": {"admin": "1234", "manface": "1234"},
        "posts": [
            {
                "id": 1,
                "user": "กวินท์ ดูวาล",
                "time": "10 นาทีที่แล้ว",
                "text": "ระบบแอป Manface ตัวใหม่รันโค้ดยาวลื่นไหลมากครับ อัปโหลดรูปภาพได้จริงด้วย โคตรตึง! 🔥",
                "image": None,
                "likes": 84,
                "comments": [{"user": "สมชาย ใจดี", "text": "สวยงามมากครับแอปนี้"}]
            }
        ],
        "chats": [{"sender": "ระบบ", "text": "ยินดีต้อนรับสู่ห้องแชทสด Messenger คราบ"}],
        "friends": {"admin": [], "manface": []}
    }

db = get_internal_facebook_db()

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
# 📝 หน้าต่างประตูล็อกอินเข้าสู่ระบบ (ต้องผ่านจุดนี้ก่อนเข้าใช้งานแอป)
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
            if not reg_u or not reg_p1: 
                st.error("กรุณากรอกข้อมูลให้ครบถ้วน")
            elif reg_p1 != reg_p2: 
                st.error("รหัสผ่านสองช่องไม่ตรงกัน")
            elif reg_u in db["users"]: 
                st.error("ชื่อผู้ใช้งานนี้ถูกใช้ไปแล้ว")
            else:
                db["users"][reg_u] = reg_p1
                db["friends"][reg_u] = []
                st.success("สมัครสมาชิกสำเร็จ! สลับไปที่แท็บ 'เข้าสู่ระบบ' ได้เลยคราบ")
# =========================================================================
# 🏠 โซนหน้าต่างแอปพลิเคชันหลัก (เมื่อล็อกอินสำเร็จแล้ว)
# =========================================================================
else:
    my_name = st.session_state.username
    if my_name not in db["friends"]: 
        db["friends"][my_name] = []
    my_friends = db["friends"][my_name]

    # SECTION 3: PREMIUM SIDEBAR NAVIGATION (แถบนำทาง)
    with st.sidebar:
        st.markdown("<h1 style='color: #FF1493; text-align: center; margin-bottom: 0px;'>💗 Manface</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #DB7093; font-size: 14px;'>Super App Ecosystem Pro</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown(f"🧑‍💻 **{my_name}**")
            st.caption("สถานะ: สมาชิกพรีเมียม")
                
        st.write("---")
        st.markdown("### 🏠 ฟังก์ชันหลัก (Facebook Features)")
        if st.button("🗞️ ฟีดข่าวสังคม (News Feed)", key="nav_feed"): 
            switch_page("Feed")
            st.rerun()
        if st.button("🤖 Meta AI อัจฉริยะ (Chatbot)", key="nav_ai"): 
            switch_page("MetaAI")
            st.rerun()
        if st.button("👥 ระบบเครือข่ายเพื่อน (Friends)", key="nav_friends"): 
            switch_page("FriendsList")
            st.rerun()
        if st.button("💬 ห้องแชทสดทุกคน (Messenger)", key="nav_chat"): 
            switch_page("GlobalChat")
            st.rerun()
        
        st.markdown("### 🛍️ ตลาดและความบันเทิง")
        if st.button("🛒 มาร์เก็ตเพลส (Marketplace)", key="nav_market"): 
            switch_page("Marketplace")
            st.rerun()
        if st.button("🎮 ศูนย์รวมเกมส์ (Gaming Hub)", key="nav_game"): 
            switch_page("Gaming")
            st.rerun()
        st.write("---")
        if st.button("🚪 ออกจากระบบ (Logout)", key="nav_logout"):
            st.session_state.logged_in = False
            st.rerun()
        st.caption("เวอร์ชันคอนเซ็ปต์ใช้งานจริง • v2.5.0")

    # SECTION 4: SYSTEM MODULES AND PAGES FUNCTIONALITY
    # เมนูที่ 1: NEWS FEED (บอร์ดฟีดข่าวสารหลัก)
    if st.session_state.page == "Feed":
        st.markdown("<h2 style='color: #DB7093;'>🗞️ ฟีดข่าวและชุมชน Manface</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("✍️ **คุณกำลังคิดอะไรอยู่? สร้างโพสต์ใหม่เลย**")
            input_text = st.text_area("เขียนข้อความบรรยาย...", key="feed_post_text")
            upload_img = st.file_uploader("📸 แนบรูปภาพประกอบโพสต์ของคุณ", type=["png", "jpg", "jpeg"], key="feed_image_file")
            
            if st.button("🚀 เผยแพร่โพสต์ลงกระดานข่าว", key="btn_publish_post"):
                if input_text.strip() or upload_img is not None:
                    final_img = None
                    if upload_img is not None:
                        final_img = Image.open(upload_img)
                        
                    new_post_data = {
                        "id": len(db["posts"]) + 1,
                        "user": my_name,
                        "time": datetime.datetime.now().strftime("%H:%M:%S"),
                        "text": input_text,
                        "image": final_img,
                        "likes": 0,
                        "comments": []
                    }
                    db["posts"].insert(0, new_post_data)
                    st.balloons()
                    st.rerun()
                else:
                    st.warning("ระบบไม่สามารถอัปโหลดโพสต์ว่างเปล่าได้")

        st.write("---")
        
        for p_idx, post in enumerate(db["posts"]):
            with st.container(border=True):
                st.markdown(f"🗣️ **{post['user']}**  •  <span style='color: gray; font-size: 12px;'>{post['time']}</span>", unsafe_allow_html=True)
                if post['text']:
                    st.write(post['text'])
                    
                if post['image'] is not None:
                    try:
                        st.image(post['image'], use_container_width=True)
                    except:
                        pass
                
                col_lk, _ = st.columns(2)
                with col_lk:
                    if st.button(f"❤️ ไฮป์ ({post['likes']})", key=f"lk_btn_{post['id']}_{p_idx}"):
                        post['likes'] += 1
                        st.rerun()
                
                if post['comments']:
                    st.markdown("<p style='font-size: 13px; font-weight: bold; color: #DB7093;'>💬 ความคิดเห็นของเพื่อนๆ:</p>", unsafe_allow_html=True)
                    for c in post['comments']:
                        st.markdown(f"<div style='margin-left: 20px; padding: 5px; border-bottom: 1px dashed #FFB6C1;'>🧑 <b>{c['user']}</b>: {c['text']}</div>", unsafe_allow_html=True)
                
                with st.form(key=f"comment_form_{post['id']}_{p_idx}", clear_on_submit=True):
                    c_text = st.text_input("เขียนความคิดเห็นของคุณ...", key=f"c_input_{post['id']}_{p_idx}")
                    if st.form_submit_button("ส่งคอมเมนต์"):
                        if c_text.strip():
                            new_comment = {"user": my_name, "text": c_text}
                            post['comments'].append(new_comment)
                            st.rerun()
    # เมนูที่ 2: FRIENDS NETWORK (ระบบค้นหาและเพิ่มเพื่อน)
    elif st.session_state.page == "FriendsList":
        st.markdown("<h2 style='color: #DB7093;'>👥 เครือข่ายการเพิ่มเพื่อนสมาชิกออนไลน์</h2>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("📌 เพื่อนของฉันตอนนี้")
            if not my_friends:
                st.info("คุณยังไม่มีรายชื่อเพื่อนในระบบ ลองค้นหาเพิ่มด้านขวาคราบ")
            else:
                for friend in my_friends: 
                    st.write(f"🧑 **{friend}** (เป็นเพื่อนกันแล้ว)")
        with c2:
            st.subheader("🔍 ค้นหาสมาชิกแอปรายอื่น")
            strangers = [u for u in db["users"] if u != my_name and u not in my_friends]
            if not strangers:
                st.success("คุณเป็นเพื่อนกับทุกคนในระบบเรียบร้อยแล้วคราบ!")
            else:
                for user in strangers:
                    col_u, col_b = st.columns(2)
                    with col_u: 
                        st.write(f"👤 ยูสเซอร์: **{user}**")
                    with col_b:
                        if st.button("➕ แอดเพื่อน", key=f"add_{user}"):
                            db["friends"][my_name].append(user)
                            db["friends"][user].append(my_name)
                            st.success(f"เป็นเพื่อนกับ {user} แล้ว!")
                            st.rerun()

    # เมนูที่ 3: MESSENGER (ห้องแชทสดพิมพ์คุยร่วมกัน)
    elif st.session_state.page == "GlobalChat":
        st.markdown("<h2 style='color: #DB7093;'>💬 ห้องแชทสด Messenger (ซิงค์ทุกเครื่อง)</h2>", unsafe_allow_html=True)
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

    # เมนูที่ 4: META AI CHATBOT (แชทบอทถามตอบจำลอง)
    elif st.session_state.page == "MetaAI":
        st.markdown("<h2 style='color: #DB7093;'>🤖 Meta AI อัจฉริยะ</h2>", unsafe_allow_html=True)
        for msg in st.session_state.ai_messages: 
            st.chat_message(msg["role"]).write(msg["content"])
        if prompt := st.chat_input("พิมพ์ข้อความเพื่อคุยกับ AI..."):
            st.session_state.ai_messages.append({"role": "user", "content": prompt})
            st.session_state.ai_messages.append({"role": "assistant", "content": f"รับทราบค่ะคุณแมนเฟซ: '{prompt}'"})
            st.rerun()

    # เมนูที่ 5: MARKETPLACE (หน้ากระดานตลาดช็อปปิ้ง)
    elif st.session_state.page == "Marketplace":
        st.markdown("<h2 style='color: #DB7093;'>🛒 มาร์เก็ตเพลสสินค้าพรีเมียม</h2>", unsafe_allow_html=True)
        cols = st.columns(3)
        for i, prod in enumerate(st.session_state.market_products):
            with cols[i % 3]:
                with st.container(border=True):
                    st.markdown(f"#### {prod['title']}")
                    st.write(f"💰 ราคา: **{prod['price']:,}** บาท")
                    if st.button(f"🛍️ ใส่รถเข็น", key=f"buy_{prod['id']}"):
                        st.session_state.shopping_cart.append(prod)
                        st.toast(f"เพิ่ม {prod['title']} ลงรถเข็นแล้ว!")
        if st.session_state.shopping_cart:
            st.write("---")
            st.subheader("🛒 ตะกร้าสินค้าของคุณ")
            for item in st.session_state.shopping_cart: 
                st.write(f"- {item['title']} : **{item['price']:,}** บาท")

    # เมนูที่ 6: GAMING HUB (เกมเดาตัวเลขแก้ไขช่องไฟ)
    elif st.session_state.page == "Gaming":
        st.markdown("<h2 style='color: #DB7093;'>🎮 ศูนย์รวมเกมส์ (Gaming Hub)</h2>", unsafe_allow_html=True)
        st.write("ระบบเกมเดาตัวเลขปริศนา 1 - 100")
        guess = st.number_input("ทายตัวเลขที่คิดว่าใช่:", min_value=1, max_value=100, step=1)
        if st.button("🎯 ส่งคำตอบที่ทาย"):
            st.session_state.game_count += 1
            if guess < st.session_state.game_number: 
                st.warning("📉 น้อยเกินไปคราบ! ลองทายตัวเลขที่มากกว่านี้ดู")
            elif guess > st.session_state.game_number: 
                st.warning("📈 มากเกินไปคราบ! ลองทายตัวเลขที่น้อยกว่านี้ดู")
            else:
                st.success(f"🎉 ถูกต้องนะคราบ! ตัวเลขคือ {st.session_state.game_number} ทายไป {st.session_state.game_count} ครั้ง")
                if st.button("🔄 เล่นใหม่อีกรอบ"):
                    st.session_state.game_number = random.randint(1, 100)
                    st.session_state.game_count = 0
                    st.rerun()
