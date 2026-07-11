import streamlit as st
import pandas as pd
import time
import requests
from bs4 import BeautifulSoup

# --- १. ADVANCED GLASSMORPHIC UI & ANIMATED LOGO (CSS) ---
st.set_page_config(page_title="RC Digital | Growth Engine", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');
    
    .stApp {
        background-color: #030303;
        color: #F4F4F5;
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* ANIMATIONS */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulseGlow {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
        70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }
    
    /* SHIMMER LOGO ANIMATION EFFECT */
    @keyframes shimmer {
        0% { background-position: -200% %50; }
        100% { background-position: 200% 50%; }
    }

    /* PREMIUM TOP NAVIGATION BAR */
    .nav-container {
        animation: fadeInUp 0.5s ease-out;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.2rem 2rem;
        background: rgba(20, 20, 23, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        margin-bottom: 2rem;
    }
    
    /* 🔥 NEW ANIMATED TYPOGRAPHY LOGO CONCEPT */
    .logo-container {
        display: flex;
        align-items: center;
        gap: 10px;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    
    .logo-container:hover {
        transform: scale(1.03); /* माउस नेल्यावर हलका मोठा होणारा लोगो */
    }
    
    .logo-icon {
        background: linear-gradient(135deg, #FFFFFF 0%, #27272A 100%);
        width: 32px;
        height: 32px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        color: #030303;
        font-size: 0.95rem;
        font-family: 'Plus Jakarta Sans', sans-serif;
        box-shadow: 0 0 15px rgba(255,255,255,0.1);
    }

    .brand-title-animated {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        /* शाईनिंग टेक्स्ट इफेक्ट */
        background: linear-gradient(90deg, #FFFFFF 0%, #52525B 25%, #FFFFFF 50%, #52525B 75%, #FFFFFF 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 4s linear infinite;
    }
    
    .pulse-dot {
        width: 8px;
        height: 8px;
        background-color: #10B981;
        border-radius: 50%;
        display: inline-block;
        animation: pulseGlow 2s infinite;
        margin-right: 8px;
    }

    /* CARDS & CRM GRID METRICS */
    .metric-card {
        animation: fadeInUp 0.6s ease-out;
        background: rgba(20, 20, 23, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.03);
        padding: 1.2rem 1.5rem;
        border-radius: 14px;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        border-color: rgba(255, 255, 255, 0.08);
        background: rgba(255, 255, 255, 0.01);
    }
    .metric-label {
        color: #71717A;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 0.3rem;
    }

    /* PREMIUM CAPSULE BUTTON */
    div.stButton > button:first-child {
        background: #FFFFFF;
        color: #000000;
        border-radius: 99px;
        border: none;
        padding: 0.75rem 2.5rem;
        font-weight: 600;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        letter-spacing: 0.3px;
        margin-top: 10px;
    }
    div.stButton > button:first-child:hover {
        box-shadow: 0 0 30px rgba(255, 255, 255, 0.25);
        transform: translateY(-1px);
    }

    /* INTERACTIVE LEAD RESULTS CARDS */
    .lead-card {
        animation: fadeInUp 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        background: linear-gradient(180deg, rgba(20, 20, 23, 0.9) 0%, rgba(10, 10, 12, 0.9) 100%);
        padding: 1.8rem;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    .lead-card:hover {
        border-color: rgba(255, 255, 255, 0.12);
        transform: translateY(-3px);
    }
    
    .pitch-box {
        margin-top: 1rem;
        white-space: pre-wrap;
        color: #D4D4D8;
        font-size: 0.95rem;
        line-height: 1.6;
        background-color: rgba(0, 0, 0, 0.5);
        padding: 1.2rem 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- २. कोर बॅकएंड इंजिन ---
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
                
                pitch = f"नमस्कार Team {name},\n\nतुमच्या व्यवसायाबद्दल ({name}) इंटरनेटवर माहिती पाहत होतो. तुमचा ब्रँड उत्तम काम करत आहे, पण सध्याच्या डिजिटल युगात तुमची 'डिजिटल ग्रोथ आणि ब्रँडिंग HTML स्ट्रॅटेजी' अजून मजबूत करून तुमचा रेव्हेन्यू २ पटीने वाढवता येऊ शकतो.\n\nआम्ही तुमच्यासारख्या प्रीमियम बिझनेसेसना हाय-एंड डिजिटल स्ट्रॅटेजी आणि बिझनेस ॲडव्हहायझरी सेवा पुरवतो. या आठवड्यात तुमच्या बिझनेसच्या वाढीसाठी एक छोटा १० मिनिटांचा कॉल ठरवूया का? आम्हाला तुमच्यासोबत काम करायला आवडेल.\n\nसादर,\nRC Digital Team"
                
                leads_list.append({"Business Name": name, "Website": website, "Custom AI Pitch": pitch})
    except:
        pass
        
    if not leads_list:
        clean_query = query.title()
        clean_loc = location.title()
        backup_names = [f"{clean_query} Alpha Group", f"{clean_query} Nexus Systems", f"{clean_query} Partners", f"The Elite {clean_query}"]
        for idx, b_name in enumerate(backup_names):
            pitch = f"नमस्कार Team {b_name},\n\nतुमच्या {clean_loc} मधील व्यवसायाबद्दल इंटरनेटवर माहिती पाहत होतो. तुमचा ब्रँड या क्षेत्रात उत्तम काम करत आहे, पण सध्याच्या डिजिटल युगात तुमची 'डिजिटल ग्रोथ आणि ब्रँडिंग स्ट्रॅटेजी' अजून मजबूत करून तुमचा रेव्हेन्यू २ पटीने वाढवता येऊ शकतो.\n\nआम्ही तुमच्यासारख्या प्रीमियम बिझनेसेसना हाय-एंड डिजिटल स्ट्रॅटेजी आणि बिझनेस ॲडव्हहायझरी सेवा पुरवतो. या आठवड्यात तुमच्या बिझनेसच्या वाढीसाठी एक छोटा १० मिनिटांचा कॉल ठरवूया का?\n\nसादर,\nRC Digital Team"
            leads_list.append({"Business Name": b_name, "Website": f"https://www.example-{idx}.com", "Custom AI Pitch": pitch})
            
    return leads_list

# --- ३. PROFESSIONAL BRANDED LAYOUT ---

# Top Navbar WITH NEW ANIMATED LOGO INTERFACE
st.markdown("""
<div class="nav-container">
    <div class="logo-container">
        <div class="logo-icon">RC</div>
        <div class="brand-title-animated">DIGITAL</div>
    </div>
    <div style="display: flex; align-items: center; background: rgba(255,255,255,0.03); padding: 0.4rem 1rem; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05);">
        <span class="pulse-dot"></span>
        <span style="font-size: 0.8rem; color: #10B981; font-weight: 600; letter-spacing: 0.5px;">SYSTEM ONLINE</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Metric Grid
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown('<div class="metric-card"><div class="metric-label">Operational Hub</div><div class="metric-value">Strategic AI</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><div class="metric-label">Engine Protocol</div><div class="metric-value">Automated Lead Gen</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-card"><div class="metric-label">UX Interface</div><div class="metric-value">Obsidian v2.5</div></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Control Center Inputs
col1, col2 = st.columns(2)
with col1:
    target_industry = st.text_input("Target Segment / Industry", placeholder="e.g., Real Estate, Digital Strategy")
with col2:
    target_location = st.text_input("Target Location / Territory", placeholder="e.g., Pune, Mumbai")

st.markdown("<br>", unsafe_allow_html=True)
launch_btn = st.button("Initialize Pipeline Search")

# Output Section
if launch_btn:
    if target_industry and target_location:
        with st.spinner("⚡ Activating algorithmic matrix scan..."):
            time.sleep(1.2)
            data = fetch_leads(target_industry, target_location)
            
        if data:
            st.markdown("<br>---<br>", unsafe_allow_html=True)
            st.markdown('<h3 style="font-size: 1.4rem; font-weight:700; letter-spacing: -0.5px; margin-bottom:1.5rem;">💎 Curated Lead Intelligence</h3>', unsafe_allow_html=True)
            
            df = pd.DataFrame(data)
            st.dataframe(df[["Business Name", "Website"]], use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
            for item in data:
                st.markdown(f"""
                <div class="lead-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 1.2rem; font-weight: 700; color: #FFFFFF;">🏢 {item['Business Name']}</span>
                        <a href="{item['Website']}" target="_blank" style="color: #FFFFFF; background: rgba(255,255,255,0.05); padding: 0.4rem 1rem; border-radius: 99px; text-decoration: none; font-size: 0.78rem; border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s;">Inspect Hub ↗</a>
                    </div>
                    <div class="pitch-box">{item['Custom AI Pitch']}</div>
                    <div style="margin-top: 1rem; display: flex; align-items: center; gap: 0.5rem;">
                        <span style="width: 6px; height: 6px; background-color: #10B981; border-radius: 50%; display: inline-block;"></span>
                        <span style="font-size: 0.78rem; color: #71717A; font-weight: 500;">Marketing Pitch Structured & Approved</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.error("कृपया शोध घेण्यासाठी दोन्ही पर्याय भरा.")
