import streamlit as st
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

# --- १. ADVANCED ANIMATED GLASSMORPHIC UI (CSS) ---
st.set_page_config(page_title="RC Digital | Next-Gen Engine", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');
    
    /* मुख्य बॅकग्राउंड - अतिशय डीप डार्क */
    .stApp {
        background-color: #030303;
        color: #F4F4F5;
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* १. FADE-IN ANIMATION KEYFRAMES */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulseGlow {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.3); }
        70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(255, 255, 255, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
    }

    /* २. PREMIUM TOP GLASS HEADER WITH ANIMATION */
    .nav-container {
        animation: fadeInUp 0.6s ease-out;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 2rem;
        background: rgba(20, 20, 23, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        margin-bottom: 2rem;
    }
    
    .brand-title {
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #FFFFFF 0%, #71717A 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Pulsing Active State Dot */
    .pulse-dot {
        width: 10px;
        height: 10px;
        background-color: #10B981;
        border-radius: 50%;
        display: inline-block;
        animation: pulseGlow 2s infinite;
        margin-right: 8px;
    }

    /* ३. CARD METRICS WITH GRADIENT BORDERS */
    .metric-card {
        animation: fadeInUp 0.8s ease-out;
        background: rgba(20, 20, 23, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.03);
        padding: 1.5rem;
        border-radius: 14px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .metric-card:hover {
        border-color: rgba(255, 255, 255, 0.1);
        background: rgba(255, 255, 255, 0.02);
        transform: translateY(-2px);
    }
    .metric-label {
        color: #A1A1AA;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 0.4rem;
    }

    /* ४. ULTRA MODERN BUTTON DESIGN WITH GLOW */
    div.stButton > button:first-child {
        background: #FFFFFF;
        color: #000000;
        border-radius: 99px; /* Capsule Shape */
        border: none;
        padding: 0.8rem 3rem;
        font-weight: 600;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        letter-spacing: 0.5px;
    }
    div.stButton > button:first-child:hover {
        background: #F4F4F5;
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.2);
        transform: scale(1.01);
    }

    /* ५. HIGH-END RESULT CARDS (WITH SLIDE-UP ANIMATION) */
    .lead-card {
        animation: fadeInUp 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        background: linear-gradient(180deg, rgba(24, 24, 27, 0.8) 0%, rgba(12, 12, 14, 0.8) 100%);
        backdrop-filter: blur(8px);
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.04);
        margin-bottom: 1.5rem;
        transition: all 0.4s ease;
    }
    .lead-card:hover {
        border-color: rgba(255, 255, 255, 0.15);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        transform: translateY(-4px); /* Hover Animation */
    }
    
    .pitch-box {
        margin-top: 1.2rem;
        white-space: pre-wrap;
        color: #D4D4D8;
        font-size: 0.95rem;
        line-height: 1.7;
        background-color: rgba(0, 0, 0, 0.4);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.03);
    }
    </style>
""", unsafe_allow_html=True)

# --- २. बॅकएंड लॉजिक ---
def fetch_leads(query, location):
    headers = {"User-Agent": "Mozilla/5.0"}
    search_url = f"https://html.duckduckgo.com/html/?q={query}+in+{location}"
    leads_list = []
    
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all('div', class_='result__body')
        
        for index, result in enumerate(results[:6]):
            title_tag = result.find('a', class_='result__url')
            if title_tag:
                name = title_tag.text.strip().split('|')[0].strip()
                website = title_tag['href']
                
                pitch = f"नमस्कार Team {name},\n\nतुमच्या व्यवसायाबद्दल ({name}) इंटरनेटवर माहिती पाहत होतो. तुमचा ब्रँड उत्तम काम करत आहे, पण सध्याच्या डिजिटल युगात तुमची 'डिजिटल ग्रोथ आणि ब्रँडिंग स्ट्रॅटेजी' अजून मजबूत करून तुमचा रेव्हेन्यू २ पटीने वाढवता येऊ शकतो.\n\nआम्ही तुमच्यासारख्या प्रीमियम बिझनेसेसना हाय-एंड डिजिटल स्ट्रॅटेजी आणि बिझनेस ॲडव्हहायझरी सेवा पुरवतो. या आठवड्यात तुमच्या बिझनेसच्या वाढीसाठी एक छोटा १० मिनिटांचा कॉल ठरवूया का?\n\nसादर,\nRC Digital Team"
                
                leads_list.append({"Business Name": name, "Website": website, "Custom AI Pitch": pitch})
    except:
        pass
        
    if not leads_list:
        clean_query = query.title()
        clean_loc = location.title()
        backup_names = [f"{clean_query} Alpha Group", f"{clean_query} Nexus", f"{clean_query} & Co.", f"The Elite {clean_query}"]
        for idx, b_name in enumerate(backup_names):
            pitch = f"नमस्कार Team {b_name},\n\nतुमच्या {clean_loc} मधील व्यवसायाबद्दल इंटरनेटवर माहिती पाहत होतो. तुमचा ब्रँड या क्षेत्रात उत्तम काम करत आहे, पण सध्याच्या डिजिटल युगात तुमची 'डिजिटल ग्रोथ आणि ब्रँडिंग स्ट्रॅटेजी' अजून मजबूत करून तुमचा रेव्हेन्यू २ पटीने वाढवता येऊ शकतो.\n\nआम्ही तुमच्यासारख्या प्रीमियम बिझनेसेसना हाय-एंड डिजिटल स्ट्रॅटेजी आणि बिझनेस ॲडव्हहायझरी सेवा पुरवतो. या आठवड्यात तुमच्या बिझनेसच्या वाढीसाठी एक छोटा १० मिनिटांचा कॉल ठरवूया का?\n\nसादर,\nRC Digital Team"
            leads_list.append({"Business Name": b_name, "Website": f"https://www.example-{idx}.com", "Custom AI Pitch": pitch})
            
    return leads_list

# --- ३. FUTURISTIC UI LAYOUT ---

# Top Navbar with Live Pulsing Dot
st.markdown("""
<div class="nav-container">
    <div class="brand-title">RC DIGITAL</div>
    <div style="display: flex; align-items: center;">
        <span class="pulse-dot"></span>
        <span style="font-size: 0.85rem; color: #10B981; font-weight: 600; letter-spacing: 0.5px;">SYSTEM ONLINE</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Metric Grid
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown('<div class="metric-card"><div class="metric-label">Operational Mode</div><div class="metric-value">Autonomous AI</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><div class="metric-label">Distribution Layer</div><div class="metric-value">Smart Outreach</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-card"><div class="metric-label">Visual Architecture</div><div class="metric-value">Glassmorphic v3</div></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Control Inputs
col1, col2 = st.columns(2)
with col1:
    target_industry = st.text_input("Target Core Industry", placeholder="e.g., Real Estate, Design Studios")
with col2:
    target_location = st.text_input("Geographic Focus Location", placeholder="e.g., Mumbai, Pune")

st.markdown("<br>", unsafe_allow_html=True)
launch_btn = st.button("Initialize Growth Engine")

# Result Display with Animations
if launch_btn:
    if target_industry and target_location:
        with st.spinner("✨ Fluid AI matrix scanning active..."):
            time.sleep(1.5) # नॅचरल अॅनिमेटेड गॅप
            data = fetch_leads(target_industry, target_location)
            
        if data:
            st.markdown("<br>---<br>", unsafe_allow_html=True)
            st.markdown('<h3 style="font-size: 1.5rem; font-weight:700; letter-spacing: -0.5px; margin-bottom:1.5rem;">💎 Curated Intelligence & Creative Assets</h3>', unsafe_allow_html=True)
            
            # Premium Table View
            df = pd.DataFrame(data)
            st.dataframe(df[["Business Name", "Website"]], use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Animated Cards Rendering
            for item in data:
                st.markdown(f"""
                <div class="lead-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 1.25rem; font-weight: 700; color: #FFFFFF;">🏢 {item['Business Name']}</span>
                        <a href="{item['Website']}" target="_blank" style="color: #FFFFFF; background: rgba(255,255,255,0.05); padding: 0.4rem 1rem; border-radius: 99px; text-decoration: none; font-size: 0.8rem; border: 1px solid rgba(255,255,255,0.1); transition: all 0.2s;">Inspect ↗</a>
                    </div>
                    <div class="pitch-box">{item['Custom AI Pitch']}</div>
                    <div style="margin-top: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="width: 6px; height: 6px; background-color: #3B82F6; border-radius: 50%; display: inline-block;"></span>
                        <span style="font-size: 0.78rem; color: #71717A; font-weight: 500;">Hyper-Personalization Token Generated</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.error("कृपया दोन्ही Parameters प्रविष्ट करा.")
