import streamlit as st
import pandas as pd
import numpy as np
import random
from PIL import Image
import datetime

# =========================================================================
# SECTION 1: CONFIGURATION & PREMIUM LUXURY PINK STYLING (CSS รองรับระบบใหม่)
# =========================================================================
st.set_page_config(
    layout="wide", 
    page_title="Manface Super App Pro", 
    page_icon="♾️",
    initial_sidebar_state="expanded"
)

# ปรับแต่งสไตล์หรูหราสีชมพูอ่อน พร้อม CSS ตกแต่งสตอรี่, คลิปสั้น Reels และแชทบับเบิ้ล
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
        .story-container {
            display: flex;
            gap: 10px;
            overflow-x: auto;
            padding: 10px 0px;
        }
        .chat-bubble {
            padding: 10px 15px;
            border-radius: 15px;
            margin-bottom: 5px;
            max-width: 70%;
        }
        .reels-box {
            background-color: #000000;
            color: #FFFFFF;
            border-radius: 15px;
            padding: 10px;
            text-align: center;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }
        .noti-box {
            background-color: #FFF0F5;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 5px;
            border-left: 4px solid #FF1493;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# SECTION 2: 📦 ADVANCED FACEBOOK ARCHITECTURE DATABASE (จำลองหลังบ้านเสถียรสูง)
# =========================================================================
@st.cache_resource
def get_ultimate_facebook_db():
    return {
        "users": {"admin": "1234", "manface": "1234"},
        "user_profiles": {
            "admin": {"avatar": None, "bio": "ผู้ดูแลระบบ Manface App"},
            "manface": {"avatar": None, "bio": "สวัสดีครับยินดีต้อนรับทุกคนคราบ"}
        },
        "posts": [
            {
                "id": 1,
                "user": "manface",
                "time": "10 นาทีที่แล้ว",
                "text": "ยินดีต้อนรับสู่ Manface Super App Pro เวอร์ชันอัปเกรดความบันเทิงและฟังก์ชันเหมือน Facebook คราบ! ♾️💖",
                "image": None,
                "video": None,
                "likes": 128,
                "comments": []
            }
        ],
        "stories": [
            {"user": "ระบบอัตโนมัติ", "text": "ยินดีต้อนรับ!", "image": None, "video": None, "music": "ไม่มีเสียงเพลง"}
        ],
        "reels": [
            {"id": 501, "title": "รีวิวแอป Manface Pro ตัวแรงประจำปี 2026 🎬", "video": None, "likes": 450, "user": "admin"}
        ],
        "chats": [],
        "market_products": [
            {"id": 101, "title": "iPhone 15 Pro Max 256GB สภาพ 99%", "price": 25000, "owner": "admin", "image": None}
        ],
        "friends": {"admin": ["manface"], "manface": ["admin"]},
        "notifications": {
            "admin": ["🔔 ยินดีต้อนรับเข้าสู่ระบบจัดการแอปพลิเคชันคราบ"],
            "manface": ["🔔 ยินดีต้อนรับเข้าสู่ระบบจัดการแอปพลิเคชันคราบ"]
        }
    }

db = get_ultimate_facebook_db()

# ตั้งค่าสถานะตัวแปรสเตทประจำเครื่องผู้ใช้งาน
if 'page' not in st.session_state: st.session_state.page = "Feed"
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'ai_messages' not in st.session_state: st.session_state.ai_messages = [{"role": "assistant", "content": "สวัสดีค่ะ! ฉันคือ Meta AI ผู้ช่วยอัจฉริยะในธีมสีชมพูของคุณ"}]
if 'shopping_cart' not in st.session_state: st.session_state.shopping_cart = []
if 'game_number' not in st.session_state: st.session_state.game_number = random.randint(1, 100)
if 'game_count' not in st.session_state: st.session_state.game_count = 0
if 'active_chat_friend' not in st.session_state: st.session_state.active_chat_friend = ""
if 'search_query' not in st.session_state: st.session_state.search_query = ""

def switch_page(target):
    st.session_state.page = target
# =========================================================================
# 📝 GATEWAY: หน้าต่างระบบสมัครสมาชิก และ เข้าสู่ระบบ
# =========================================================================
if not st.session_state.logged_in:
    st.title("💖 ยินดีต้อนรับสู่ Manface Super App Pro")
    st.write("กรุณาสมัครสมาชิก หรือ เข้าสู่ระบบเพื่อเชื่อมต่อเครือข่ายออนไลน์จริง")
    
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
                db["user_profiles"][reg_u] = {"avatar": None, "bio": "สมาชิกใหม่พรีเมียมคราบ"}
                db["notifications"][reg_u] = ["🔔 ยินดีต้อนรับเข้าสู่ระบบจัดการแอปพลิเคชันคราบ"]
                st.success("สมัครสมาชิกสำเร็จ! สลับไปที่แท็บ 'เข้าสู่ระบบ' ได้เลยคราบ")

# =========================================================================
# 🏠 โซนหน้าต่างแอปพลิเคชันหลัก (เมื่อผู้ใช้งานผ่านการล็อกอินแล้ว)
# =========================================================================
else:
    my_name = st.session_state.username
    if my_name not in db["friends"]: db["friends"][my_name] = []
    if my_name not in db["notifications"]: db["notifications"][my_name] = []
    if my_name not in db["user_profiles"]: db["user_profiles"][my_name] = {"avatar": None, "bio": ""}
    
    my_friends = db["friends"][my_name]
    my_profile = db["user_profiles"][my_name]
    my_notis = db["notifications"][my_name]

    # SECTION 3: PREMIUM SIDEBAR NAVIGATION & SEARCH & NOTIFICATIONS
    with st.sidebar:
        st.markdown("<h1 style='color: #FF1493; text-align: center; margin-bottom: 0px;'>💗 Manface</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #DB7093; font-size: 12px;'>Super App Ecosystem Pro</p>", unsafe_allow_html=True)
        
        # 👤 ระบบอัปโหลด/โชว์รูปโปรไฟล์ของตนเองบนแถบข้าง
        with st.container(border=True):
            if my_profile["avatar"] is not None:
                st.image(my_profile["avatar"], width=80)
            else:
                st.markdown("<h2>👤</h2>", unsafe_allow_html=True)
            st.markdown(f"**{my_name}**")
            st.caption("สถานะ: สมาชิกพรีเมียม")
        
        # 🔍 1. เพิ่มช่องค้นหา (Search Bar) ส่วนกลางสไตล์แอปดัง
        st.session_state.search_query = st.text_input("🔍 ค้นหาเพื่อนหรือโพสต์ในแอป:", value=st.session_state.search_query)
        if st.session_state.search_query.strip():
            if st.button("❌ ล้างผลการค้นหา"):
                st.session_state.search_query = ""
                st.rerun()

        st.write("---")
        st.markdown("### 🏠 ฟังก์ชันหลัก (Facebook Features)")
        if st.button("🗞️ ฟีดข่าวและสตอรี่ (News Feed)", key="nav_feed"): 
            switch_page("Feed")
            st.rerun()
        if st.button("🎬 คลิปสั้นสุดมันส์ (Manface Reels)", key="nav_reels"): 
            switch_page("ReelsPage")
            st.rerun()
        if st.button("👤 โปรไฟล์ของฉัน (My Profile)", key="nav_profile"): 
            switch_page("MyProfilePage")
            st.rerun()
        if st.button("🔔 กล่องการแจ้งเตือน (Notifications)", key="nav_notis"): 
            switch_page("NotiPage")
            st.rerun()
        if st.button("🤖 Meta AI อัจฉริยะ (Chatbot)", key="nav_ai"): 
            switch_page("MetaAI")
            st.rerun()
        if st.button("👥 ระบบเครือข่ายเพื่อน (Friends)", key="nav_friends"): 
            switch_page("FriendsList")
            st.rerun()
        if st.button("💬 ห้องแชทส่วนตัว (Messenger DM)", key="nav_chat"): 
            switch_page("GlobalChat")
            st.rerun()
        
        st.markdown("### 🛍️ ตลาดและความบันเทิง")
        if st.button("🛒 มาร์เก็ตเพลสลงขายของ (Marketplace)", key="nav_market"): 
            switch_page("Marketplace")
            st.rerun()
        if st.button("🎮 ศูนย์รวมเกมส์ (Gaming Hub)", key="nav_game"): 
            switch_page("Gaming")
            st.rerun()
        st.write("---")
        if st.button("🚪 ออกจากระบบ (Logout)", key="nav_logout"):
            st.session_state.logged_in = False
            st.rerun()
        st.caption("เวอร์ชันคอนเซ็ปต์ใช้งานจริง • v3.5.0")
    # SECTION 4: SYSTEM MODULES AND PAGES FUNCTIONALITY
    # =========================================================================
    # เมนูที่ 1: NEWS FEED & STORIES (ฟีดข่าว, สตอรี่เวอร์ชันเต็ม)
    # =========================================================================
    if st.session_state.page == "Feed":
        st.markdown("<h2 style='color: #DB7093;'>🗞️ ฟีดข่าวและชุมชน Manface</h2>", unsafe_allow_html=True)
        
        # --- 💻 โหมดพิเศษ: แสดงผลลัพธ์การค้นหาข้อมูลกลางแอป ---
        if st.session_state.search_query.strip():
            st.markdown(f"#### 🔍 ผลการค้นหาสำหรับ: '{st.session_state.search_query}'")
            q = st.session_state.search_query.lower()
            
            # ค้นหาโพสต์
            found_posts = [p for p in db["posts"] if q in p["text"].lower() or q in p["user"].lower()]
            if found_posts:
                st.write("📌 โพสต์ที่เกี่ยวข้อง:")
                for fp in found_posts:
                    st.info(f"🗣️ **{fp['user']}**: {fp['text']} ({fp['time']})")
            else:
                st.write("❌ ไม่พบโพสต์ที่เกี่ยวข้อง")
            st.write("---")

        # --- 📸 2. ระบบแถบสตอรี่ (อัปโหลดรูป วิดีโอ และเลือกเสียงเพลงประกอบได้จริง) ---
        st.markdown("### 📸 สตอรี่ล่าสุด (Stories)")
        
        with st.expander("➕ สร้างสตอรี่ใหม่ (ใส่รูป/คลิป/เสียงเพลงประกอบ)"):
            s_text = st.text_input("1. พิมพ์ข้อความสั้นบรรยายสตอรี่:", key="st_txt_in")
            
            col_s1, col_s2 = st.columns(2)
            with col_s1:
                s_img = st.file_uploader("🖼️ อัปโหลดรูปภาพลงสตอรี่ (.png, .jpg)", type=["png", "jpg", "jpeg"], key="st_img_in")
            with col_s2:
                s_vid = st.file_uploader("🎞️ อัปโหลดวิดีโอลงสตอรี่ (.mp4)", type=["mp4"], key="st_vid_in")
                
            s_music = st.selectbox("🎵 เลือกเสียงเพลงประกอบสตอรี่ของคุณ:", [
                "🎵 ไม่ใส่เสียงเพลง", 
                "🎵 เพลงแดนซ์ตึง ๆ ประจำปี 2026", 
                "🎵 เพลงรักหวานซึ้งสีชมพู", 
                "🎵 เพลงฮิตติดเทรนด์ YouTube"
            ], key="st_mus_in")
            
            if st.button("แชร์สตอรี่ลงระบบ 🚀", key="btn_upload_story_full"):
                if s_text.strip() or s_img is not None or s_vid is not None:
                    final_s_img = Image.open(s_img) if s_img is not None else None
                    db["stories"].insert(0, {
                        "user": my_name,
                        "text": s_text,
                        "image": final_s_img,
                        "video": s_vid,
                        "music": s_music,
                        "time": datetime.datetime.now().strftime("%H:%M")
                    })
                    st.toast("✅ อัปโหลดสตอรี่ของคุณสำเร็จแล้ว!")
                    st.rerun()

        # วนลูปโชว์แถบสไลด์สตอรี่ของทุกคน
        cols_story = st.columns(min(len(db["stories"]), 5) + 1)
        for s_idx, story in enumerate(db["stories"]):
            if s_idx < 5:  # จำกัดโชว์สูงสุด 5 สตอรี่แรกเพื่อความสวยงาม
                with cols_story[s_idx]:
                    with st.container(border=True):
                        st.markdown(f"<p style='font-size:12px; font-weight:bold; color:#FF1493;'>👤 {story['user']}</p>", unsafe_allow_html=True)
                        if story.get("text"): st.write(story["text"])
                        if story.get("image") is not None: st.image(story["image"], use_container_width=True)
                        if story.get("video") is not None: st.video(story["video"])
                        st.caption(f"🎼 {story.get('music', 'ไม่มีเพลง')}")

        st.write("---")
        
        # --- ✍️ 3. กล่องสร้างโพสต์ฟีดข่าวสารหลัก (ข้อความ, รูปภาพ, วิดีโอ) ---
        with st.container(border=True):
            st.markdown("✍️ **คุณกำลังคิดอะไรอยู่? สร้างโพสต์ใหม่เลย**")
            input_text = st.text_area("เขียนข้อความบรรยาย...", key="feed_post_text")
            
            col_file1, col_file2 = st.columns(2)
            with col_file1:
                upload_img = st.file_uploader("📸 แนบรูปภาพประกอบโพสต์ของคุณ", type=["png", "jpg", "jpeg"], key="feed_image_file")
            with col_file2:
                upload_vid = st.file_uploader("🎥 แนบวิดีโอประกอบโพสต์ของคุณ (.mp4)", type=["mp4"], key="feed_video_file")
            
            if st.button("🚀 เผยแพร่โพสต์ลงกระดานข่าว", key="btn_publish_post"):
                if input_text.strip() or upload_img is not None or upload_vid is not None:
                    final_img = Image.open(upload_img) if upload_img is not None else None
                        
                    new_post_data = {
                        "id": int(datetime.datetime.now().timestamp()),
                        "user": my_name,
                        "time": datetime.datetime.now().strftime("%H:%M:%S"),
                        "text": input_text,
                        "image": final_img,
                        "video": upload_vid,
                        "likes": 0,
                        "comments": []
                    }
                    db["posts"].insert(0, new_post_data)
                    
                    # ส่งแจ้งเตือนหาเพื่อนทุกคนในระบบ
                    for user in db["users"]:
                        if user != my_name:
                            db["notifications"][user].insert(0, f"🔔 {my_name} ได้เพิ่มโพสต์ใหม่ลงในฟีดข่าวสารคราบ")
                            
                    st.balloons()
                    st.rerun()
                else:
                    st.warning("ระบบไม่สามารถอัปโหลดโพสต์ว่างเปล่าได้")

        st.write("---")
        
        # วนลูปแสดงผลรายการบอร์ดฟีดข่าวทั้งหมด พร้อมปุ่มลบโพสต์ตัวเอง
        for p_idx, post in enumerate(db["posts"]):
            with st.container(border=True):
                # แสดงรูปโปรไฟล์ของผู้โพสต์ (ถ้ามี)
                p_owner = post['user']
                if db["user_profiles"].get(p_owner, {}).get("avatar") is not None:
                    st.image(db["user_profiles"][p_owner]["avatar"], width=40)
                    
                st.markdown(f"🗣️ **{post['user']}**  •  <span style='color: gray; font-size: 12px;'>{post['time']}</span>", unsafe_allow_html=True)
                if post['text']: st.write(post['text'])
                if post['image'] is not None: st.image(post['image'], use_container_width=True)
                if post['video'] is not None: st.video(post['video'])
                
                col_lk, col_del = st.columns(2)
                with col_lk:
                    if st.button(f"❤️ ไฮป์ ({post['likes']})", key=f"lk_btn_{post['id']}_{p_idx}"):
                        post['likes'] += 1
                        st.rerun()
                with col_del:
                    if post['user'] == my_name:
                        if st.button("🗑️ ลบโพสต์", key=f"del_btn_{post['id']}_{p_idx}"):
                            db["posts"].pop(p_idx)
                            st.toast("ลบโพสต์เรียบร้อยแล้วคราบ!")
                            st.rerun()
                
                # โซนคอมเมนต์ความคิดเห็นใต้โพสต์
                if post['comments']:
                    for c in post['comments']:
                        st.markdown(f"<div style='margin-left: 20px; padding: 5px; border-bottom: 1px dashed #FFB6C1;'>🧑 <b>{c['user']}</b>: {c['text']}</div>", unsafe_allow_html=True)
                
                with st.form(key=f"comment_form_{post['id']}_{p_idx}", clear_on_submit=True):
                    c_text = st.text_input("เขียนความคิดเห็นของคุณ...", key=f"c_input_{post['id']}_{p_idx}")
                    if st.form_submit_button("ส่งคอมเมนต์"):
                        if c_text.strip():
                            post['comments'].append({"user": my_name, "text": c_text})
                            st.rerun()
    # =========================================================================
    # เมนูที่ 2: MANFACE REELS (ระบบคลิปสั้นสำหรับดูวิดีโอ)
    # =========================================================================
    elif st.session_state.page == "ReelsPage":
        st.markdown("<h2 style='color: #DB7093;'>🎬 คลิปสั้นสุดมันส์ (Manface Reels)</h2>", unsafe_allow_html=True)
        
        with st.expander("➕ เพิ่มคลิปสั้น Reels ใหม่ของคุณ 🚀"):
            r_title = st.text_input("กรอกชื่อคลิป/แฮชแท็กคำบรรยาย:", key="r_title_in")
            r_vid = st.file_uploader("🎞️ อัปโหลดวิดีโอคลิปสั้น (.mp4 เท่านั้น):", type=["mp4"], key="r_vid_in")
            if st.button("เผยแพร่คลิป Reels 🎬", type="primary"):
                if r_title.strip() and r_vid is not None:
                    db["reels"].insert(0, {
                        "id": int(datetime.datetime.now().timestamp()),
                        "title": r_title,
                        "video": r_vid,
                        "likes": 0,
                        "user": my_name
                    })
                    st.success("✅ อัปโหลดคลิปสั้น Reels ของคุณสำเร็จ!")
                    st.rerun()
                else:
                    st.error("กรุณากรอกหัวข้อบรรยายและแนบไฟล์วิดีโอก่อนคราบ")
                    
        st.write("---")
        
        # จัดแสดงบอร์ดรายการวิดีโอคลิปสั้นในแอป
        for r_idx, reel in enumerate(db["reels"]):
            st.markdown(f"<div class='reels-box'><h4>🎬 {reel['title']}</h4><p style='font-size:12px; color:#FFB6C1;'>👤 ผู้โพสต์: {reel['user']}</p></div>", unsafe_allow_html=True)
            if reel["video"] is not None:
                st.video(reel["video"])
            else:
                st.info("📹 คลิปตัวอย่างเริ่มต้นระบบคอนเซ็ปต์")
                
            col_rlk, _ = st.columns(2)
            with col_lk:
                if st.button(f"❤️ ถูกใจคลิปนี้ ({reel['likes']})", key=f"r_lk_{reel['id']}_{r_idx}"):
                    reel["likes"] += 1
                    st.rerun()
            st.write("---")

    # =========================================================================
    # เมนูที่ 3: NOTIFICATIONS (กล่องกระดานแสดงการแจ้งเตือนสไตล์ Facebook)
    # =========================================================================
    elif st.session_state.page == "NotiPage":
        st.markdown("<h2 style='color: #DB7093;'>🔔 กล่องการแจ้งเตือน (Notifications)</h2>", unsafe_allow_html=True)
        st.write("ติดตามข่าวสารและความเคลื่อนไหวของเพื่อน ๆ ในระบบ")
        
        if st.button("🗑️ ล้างการแจ้งเตือนทั้งหมด", key="btn_clear_notis"):
            db["notifications"][my_name] = []
            st.rerun()
            
        st.write("---")
        if not my_notis:
            st.info("ยังไม่มีการแจ้งเตือนใหม่ในตอนนี้คราบ")
        else:
            for noti in my_notis:
                st.markdown(f"<div class='noti-box'>{noti}</div>", unsafe_allow_html=True)

    # =========================================================================
    # เมนูที่ 4: MY PROFILE PAGE (หน้าต่างจัดการแก้ไขโปรไฟล์และอัปโหลดรูปตัวเอง)
    # =========================================================================
    elif st.session_state.page == "MyProfilePage":
        st.markdown("<h2 style='color: #DB7093;'>👤 หน้าโปรไฟล์ส่วนตัวของคุณ</h2>", unsafe_allow_html=True)
        
        col_pro1, col_pro2 = st.columns([1, 2])
        with col_pro1:
            st.subheader("🖼️ รูปโปรไฟล์ปัจจุบัน")
            if my_profile["avatar"] is not None:
                st.image(my_profile["avatar"], width=200)
            else:
                st.markdown("<h1 style='font-size:100px;'>👤</h1>", unsafe_allow_html=True)
                
            new_avatar = st.file_uploader("📸 อัปโหลด/เปลี่ยนรูปโปรไฟล์ของคุณ:", type=["png", "jpg", "jpeg"], key="pro_av_upload")
            if new_avatar is not None:
                my_profile["avatar"] = Image.open(new_avatar)
                st.success("✅ อัปเดตรูปอวาตาร์สำเร็จคราบ!")
                st.rerun()
                
        with col_pro2:
            st.subheader("✍️ แก้ไขข้อมูลประวัติย้อนหลัง")
            st.write(f"ชื่อผู้ใช้ในระบบ: **{my_name}**")
            current_bio = my_profile.get("bio", "")
            new_bio = st.text_area("คำแนะนำตัวของคุณ (Bio):", value=current_bio)
            
            if st.button("💾 บันทึกการแก้ไขข้อมูล", type="primary", key="btn_save_bio"):
                my_profile["bio"] = new_bio
                st.success("✅ อัปเดตข้อมูลประวัติคำแนะนำตัวเรียบร้อยคราบ!")
                st.rerun()
                
        st.write("---")
        st.subheader("📰 โพสต์ย้อนหลังของคุณ (My Posts)")
        
        # กรองและดึงข้อความเฉพาะของยูสเซอร์ที่เปิดดูมาแสดง
        my_own_posts = [p for p in db["posts"] if p["user"] == my_name]
        if not my_own_posts:
            st.info("คุณยังไม่เคยลงโพสต์อะไรเลย ลองไปโพสต์ที่หน้าฟีดข่าวดูนะคราบ")
        else:
            for op in my_own_posts:
                with st.container(border=True):
                    st.write(f"📅 โพสต์เมื่อเวลา: {op['time']}")
                    st.write(op['text'])
                    if op['image'] is not None: st.image(op['image'], width=300)
    # =========================================================================
    # เมนูที่ 5: FRIENDS NETWORK (ระบบจัดการเครือข่ายเพื่อน)
    # =========================================================================
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
                    if st.button(f"💬 ส่งข้อความแชทหา {friend}", key=f"chat_with_{friend}"):
                        st.session_state.active_chat_friend = friend
                        switch_page("GlobalChat")
                        st.rerun()
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
                            if user not in db["friends"]:
                                db["friends"][user] = []
                            db["friends"][user].append(my_name)
                            # ส่งการแจ้งเตือน
                            db["notifications"][user].insert(0, f"👥 {my_name} ได้เพิ่มคุณเป็นเพื่อนแล้วคราบ")
                            st.success(f"เป็นเพื่อนกับ {user} แล้ว!")
                            st.rerun()

    # =========================================================================
    # เมนูที่ 6: MESSENGER PRIVATE DM (ห้องแชทแยกคุยส่วนตัวแบบตัวต่อตัว)
    # =========================================================================
    elif st.session_state.page == "GlobalChat":
        st.markdown("<h2 style='color: #DB7093;'>💬 ห้องแชทส่วนตัว Messenger (คุยแบบตัวต่อตัว)</h2>", unsafe_allow_html=True)
        
        if not my_friends:
            st.info("กรุณาเพิ่มเพื่อนในระบบก่อนเริ่มใช้งานห้องแชทส่วนตัวคราบ")
        else:
            friend_list = ["-- เลือกเพื่อนที่จะคุย --"] + my_friends
            default_idx = 0
            if st.session_state.active_chat_friend in my_friends:
                default_idx = friend_list.index(st.session_state.active_chat_friend)
                
            selected_friend = st.selectbox("เลือกคู่สนทนา:", friend_list, index=default_idx)
            
            if selected_friend != "-- เลือกเพื่อนที่จะคุย --":
                st.session_state.active_chat_friend = selected_friend
                st.write(f"🟢 กำลังสนทนากับ: **{selected_friend}**")
                
                chat_box = st.container(height=350, border=True)
                with chat_box:
                    for chat in db["chats"]:
                        is_my_msg = (chat["sender"] == my_name and chat.get("receiver") == selected_friend)
                        is_friend_msg = (chat["sender"] == selected_friend and chat.get("receiver") == my_name)
                        
                        if is_my_msg:
                            st.markdown(f"<div style='text-align: right;'><span style='background-color:#FFB6C1; display:inline-block;' class='chat-bubble'><b>คุณ</b>: {chat['text']}</span></div>", unsafe_allow_html=True)
                        elif is_friend_msg:
                            st.markdown(f"<div style='text-align: left;'><span style='background-color:#FFF; border:1px solid #FFB6C1; display:inline-block;' class='chat-bubble'><b>{chat['sender']}</b>: {chat['text']}</span></div>", unsafe_allow_html=True)
                
                with st.form("send_private_msg", clear_on_submit=True):
                    chat_input = st.text_input("พิมพ์ข้อความแชทส่งหาเพื่อน...")
                    if st.form_submit_button("ส่งข้อความด่วน 🚀"):
                        if chat_input.strip():
                            db["chats"].append({
                                "sender": my_name, 
                                "receiver": selected_friend, 
                                "text": chat_input
                            })
                            # ส่งการแจ้งเตือนด่วน
                            db["notifications"][selected_friend].insert(0, f"💬 {my_name} ได้ส่งข้อความแชทหาคุณคราบ")
                            st.rerun()
            else:
                st.info("💡 กรุณาเลือกรายชื่อเพื่อนจากช่องด้านบนเพื่อเริ่มแชทคุยตัวต่อตัวคราบ")

    # =========================================================================
    # เมนูที่ 7: META AI CHATBOT (แชทบอทถามตอบจำลอง)
    # =========================================================================
    elif st.session_state.page == "MetaAI":
        st.markdown("<h2 style='color: #DB7093;'>🤖 Meta AI อัจฉริยะ</h2>", unsafe_allow_html=True)
        for msg in st.session_state.ai_messages: 
            st.chat_message(msg["role"]).write(msg["content"])
        if prompt := st.chat_input("พิมพ์ข้อความเพื่อคุยกับ AI..."):
            st.session_state.ai_messages.append({"role": "user", "content": prompt})
            st.session_state.ai_messages.append({"role": "assistant", "content": f"รับทราบค่ะคุณแมนเฟซ: '{prompt}'"})
            st.rerun()

    # =========================================================================
    # เมนูที่ 8: MARKETPLACE (มาร์เก็ตเพลสแบบสมาชิกโพสต์อัปโหลดรูปภาพสินค้าได้เองจริง)
    # =========================================================================
    elif st.session_state.page == "Marketplace":
        st.markdown("<h2 style='color: #DB7093;'>🛒 มาร์เก็ตเพลสลงประกาศขายของ (Marketplace)</h2>", unsafe_allow_html=True)
        
        tab_buy, tab_sell = st.tabs(["🛍️ เลือกซื้อสินค้าในตลาด", "➕ ลงประกาศขายของพรีเมียม"])
        
        with tab_buy:
            cols = st.columns(3)
            for i, prod in enumerate(db["market_products"]):
                with cols[i % 3]:
                    with st.container(border=True):
                        st.markdown(f"#### {prod['title']}")
                        st.write(f"💰 ราคา: **{prod['price']:,}** บาท")
                        st.caption(f"👤 ผู้ขาย: {prod['owner']}")
                        
                        # แสดงรูปภาพสินค้า (ถ้ามี)
                        if prod.get("image") is not None:
                            st.image(prod["image"], use_container_width=True)
                        
                        col_b1, col_b2 = st.columns(2)
                        with col_b1:
                            if st.button(f"🛍️ ใส่รถเข็น", key=f"buy_{prod['id']}_{i}"):
                                st.session_state.shopping_cart.append(prod)
                                st.toast(f"เพิ่ม {prod['title']} ลงรถเข็นแล้ว!")
                        with col_b2:
                            if prod['owner'] == my_name:
                                if st.button("❌ ลบสินค้า", key=f"del_prod_{prod['id']}_{i}"):
                                    db["market_products"].pop(i)
                                    st.toast("ลบรายการประกาศขายแล้วคราบ!")
                                    st.rerun()
                                    
            if st.session_state.shopping_cart:
                st.write("---")
                st.subheader("🛒 ตะกร้าสินค้าของคุณ")
                for item in st.session_state.shopping_cart: 
                    st.write(f"- {item['title']} : **{item['price']:,}** บาท")
                    
        with tab_sell:
            st.subheader("✍️ กรอกรายละเอียดสินค้าและอัปโหลดรูปภาพจริง")
            new_title = st.text_input("ชื่อสินค้า/หัวข้อประกาศ:", key="prod_title_in")
            new_price = st.number_input("ตั้งราคาขาย (บาท):", min_value=0, step=100, key="prod_price_in")
            prod_img = st.file_uploader("📸 อัปโหลดรูปภาพสินค้าประกวด (.png, .jpg)", type=["png", "jpg", "jpeg"], key="prod_img_upload")
            
            if st.button("📢 ยืนยันการส่งลงประกาศขายของ", type="primary", key="btn_confirm_sell"):
                if new_title.strip() and new_price > 0:
                    final_p_img = Image.open(prod_img) if prod_img is not None else None
                    new_prod_id = int(datetime.datetime.now().timestamp())
                    
                    db["market_products"].insert(0, {
                        "id": new_prod_id,
                        "title": new_title,
                        "price": new_price,
                        "owner": my_name,
                        "image": final_p_img
                    })
                    st.success("✅ อัปโหลดประกาศขายสินค้าพร้อมรูปภาพเข้าสู่ตลาดเรียบร้อย!")
                    st.rerun()
                else:
                    st.error("กรุณากรอกชื่อสินค้าและตั้งราคาให้มากกว่า 0 บาทคราบ")

    # =========================================================================
    # เมนูที่ 9: GAMING HUB
    # =========================================================================
    elif st.session_state.page == "Gaming":
        st.markdown("<h2 style='color: #DB7093;'>🎮 ศูนย์รวมเกมส์ (Gaming Hub)</h2>", unsafe_allow_html=True)
        st.write("ระบบเกมเดาตัวเลขปริศนา 1 - 100")
        guess = st.number_input("ทายตัวเลขที่คิดว่าใช่:", min_value=1, max_value=100, step=1)
        if st.button("🎯 ส่งคำตอบที่ทาย"):
            st.session_state.game_count += 1
            if guess < st.session_state.game_number: st.warning("📉 น้อยเกินไปคราบ!")
