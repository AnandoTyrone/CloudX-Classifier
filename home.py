import streamlit as st

def show_home():
    # HEADER UTAMA SIMETRIS
    st.markdown("<h1 style='text-align: center; color: #0369a1; font-family: sans-serif; font-weight: 800; font-size: 2.5rem; margin-bottom: 0px;'>☁️ Welcome to CloudX Intelligent</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #475569; font-size: 1.15rem; margin-top: 5px; margin-bottom: 0px;'>Platform Edukasi dan Identifikasi Jenis Awan Berbasis Komputer Visi & Deep Learning</p>", unsafe_allow_html=True)
    
    # Bar Penyelaras Desain
    st.markdown("<div class='premium-bar'></div>", unsafe_allow_html=True)
    
    # PENGANTAR SISTEM
    st.markdown("<h3 style='text-align: center; color: #0f172a; font-weight: 700;'>🌌 Mengenal Sistem Klasifikasi Awan Howard-CloudX</h3>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: justify; color: #334155; line-height: 1.6; font-size: 1rem;'>
    Awan adalah massa terlihat dari tetesan air terkompresi atau kristal beku yang menggantung di atmosfer di atas permukaan bumi. 
    Mengidentifikasi jenis awan sangat krusial bagi bidang <b>meteorologi, prakiraan cuaca, dan keselamatan navigasi penerbangan</b>.
    Aplikasi ini dilatih menggunakan dataset <b>Howard-Cloud-X</b> untuk mengenali 10 Jenis Awan Dasar berdasarkan ketinggian pembentukannya.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #0f172a; font-weight: 700; margin-bottom: 1.5rem;'>📚 Teori & Karakteristik 10 Jenis Awan</h3>", unsafe_allow_html=True)
    
    # KARTU EKSPANDER DENGAN BAR AKSEN YANG SIMETRIS
    st.markdown("<div style='border-left: 5px solid #38bdf8; padding-left: 10px; margin-bottom: 10px;'><h5 style='margin:0; color:#0369a1;'>🔵 1. AWAN TINGGI (Ketinggian > 6.000 meter - Kristal Es)</h5></div>", unsafe_allow_html=True)
    with st.expander("Lihat Detail Karakteristik Awan Tinggi"):
        st.markdown("""
        * **Cirrus:** Awan tipis, halus, dan berserat seperti bulu ayam. Menandakan cuaca cerah namun bisa menjadi simbol perubahan pola cuaca atmosfer.
        * **Cirrocumulus:** Terlihat seperti kumpulan bintik-bintik kecil atau pola sisik ikan yang berjejer rapi di langit.
        * **Cirrostratus:** Berbentuk seperti kelambu tipis, halus, dan putih transparan yang menutupi langit, sering memicu fenomena indah **Halo Matahari**.
        """)
        
    st.markdown("<div style='border-left: 5px solid #22c55e; padding-left: 10px; margin-bottom: 10px;'><h5 style='margin:0; color:#16a34a;'>🟢 2. AWAN MENENGAH (Ketinggian 2.000 - 6.000 meter)</h5></div>", unsafe_allow_html=True)
    with st.expander("Lihat Detail Karakteristik Awan Menengah"):
        st.markdown("""
        * **Altocumulus:** Berbentuk seperti gumpalan-gumpalan kapas tebal yang berlapis, bergelombang, atau berwujud makarel langit. Berwarna putih hingga abu-abu pucat.
        * **Altostratus:** Lapisan awan tebal abu-abu atau kebiruan yang menyelimuti langit luas. Matahari hanya terlihat samar-samar (seperti kaca buram).
        """)
        
    st.markdown("<div style='border-left: 5px solid #eab308; padding-left: 10px; margin-bottom: 10px;'><h5 style='margin:0; color:#ca8a04;'>🟡 3. AWAN RENDAH (Ketinggian < 2.000 meter)</h5></div>", unsafe_allow_html=True)
    with st.expander("Lihat Detail Karakteristik Awan Rendah"):
        st.markdown("""
        * **Stratocumulus:** Awan berbentuk bola-bola besar atau gumpalan bergelombang abu-abu tipis. Jarang menghasilkan hujan berat, umumnya hanya cuaca mendung stabil.
        * **Stratus:** Lapisan awan abu-abu seragam yang sangat rendah dekat permukaan bumi, menyerupai kabut tinggi. Sering menghasilkan gerimis halus (*drizzle*).
        """)
        
    st.markdown("<div style='border-left: 5px solid #ef4444; padding-left: 10px; margin-bottom: 10px;'><h5 style='margin:0; color:#dc2626;'>🔴 4. AWAN PERKEMBANGAN VERTIKAL (Konveksi Aktif)</h5></div>", unsafe_allow_html=True)
    with st.expander("Lihat Detail Karakteristik Awan Vertikal"):
        st.markdown("""
        * **Cumulus:** Awan padat berwujud tajam gembung dengan puncak menyerupai kubis/popcorn putih cerah jika terkena matahari. Menandakan cuaca cerah stabil.
        * **Cumulonimbus:** Awan badai raksasa menjulang tinggi hingga batas troposfer. **Sangat berbahaya bagi penerbangan** karena memicu petir, turbulensi hebat, angin putung beliung, dan hujan es.
        * **Nimbostratus:** Lapisan awan abu-abu gelap, sangat tebal, dan tidak berbentuk yang menghasilkan hujan atau salju yang stabil dalam durasi yang lama.
        """)

    st.markdown("<br><div class='premium-bar' style='height: 2px; opacity:0.3;'></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>CloudX Project • Menggunakan Arsitektur MobileNetV2 Fine-Tuning</p>", unsafe_allow_html=True)