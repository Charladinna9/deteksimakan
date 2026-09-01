import streamlit as st
from PIL import Image
from ultralytics import YOLO


# ============================================================
# KONFIGURASI
# ============================================================

st.set_page_config(
    page_title="MBG Nutrition",
    layout="wide",
    page_icon="🍲"
)


# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #F8F9FA;
    color: #2C3E50;
}

[data-testid="stHeader"] {
    background: rgba(255, 255, 255, 0);
}

[data-testid="stAppViewBlockContainer"] {
    max-width: 1240px;
    padding-top: 2.5rem;
}

h1, h2, h3, p, label,
[data-testid="stMarkdownContainer"] {
    color: #2C3E50;
}

div[data-testid="stButton"] > button {
    width: 100%;
    background: #E67E22;
    border: 1px solid #E67E22;
    border-radius: 10px;
    color: #FFFFFF;
    font-weight: 700;
    min-height: 2.8rem;
}

div[data-testid="stButton"] > button:hover {
    background: #CF6D17;
    border-color: #CF6D17;
    color: #FFFFFF;
}

[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E8ECEF;
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(44, 62, 80, 0.05);
    padding: 0.85rem;
}

[data-testid="stFileUploader"] {
    background: #FFFFFF;
    border: 1px dashed #A9DFBF;
    border-radius: 14px;
    padding: 0.5rem;
}

.app-hero {
    background: linear-gradient(125deg, #1E9E55, #2ECC71);
    border-radius: 18px;
    box-shadow: 0 12px 30px rgba(46, 204, 113, 0.20);
    color: #FFFFFF;
    margin-bottom: 1.75rem;
    padding: 2rem 2.25rem;
}

.app-hero div {
    color: #FFFFFF;
}

.app-kicker {
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    opacity: 0.9;
}

.app-hero-title {
    font-size: 2.1rem;
    font-weight: 750;
    line-height: 1.2;
    margin: 0.4rem 0;
}

.app-hero-copy {
    font-size: 1rem;
    opacity: 0.93;
}

.section-kicker {
    color: #2ECC71;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
}

.section-title {
    color: #2C3E50;
    font-size: 1.45rem;
    font-weight: 750;
    margin: 0.15rem 0 0.8rem;
}

.food-chip {
    background: #EAF8F0;
    border-radius: 999px;
    color: #197A43;
    display: inline-block;
    font-size: 0.9rem;
    font-weight: 650;
    margin: 0 0.45rem 0.45rem 0;
    padding: 0.45rem 0.8rem;
}

.image-card-title {
    color: #2C3E50;
    font-size: 0.95rem;
    font-weight: 700;
    margin-bottom: 0.65rem;
}

.info-card {
    background: #FFFFFF;
    border: 1px solid #E8ECEF;
    border-radius: 12px;
    padding: 1rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return YOLO("best.pt")


try:
    model = load_model()
except Exception as e:
    st.error("Model YOLO tidak ditemukan.")
    st.code("models/best.pt")
    st.error(f"Detail error: {e}")
    st.stop()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="app-hero">
        <div class="app-kicker">Asisten Gizi Pintar</div>
        <div class="app-hero-title">
            Kenali isi piring, pahami gizinya.
        </div>
        <div class="app-hero-copy">
            Unggah foto makanan untuk mendapatkan deteksi menu
            menggunakan model YOLOv11.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# INFORMASI MODEL
# ============================================================

with st.expander("ℹ️ Informasi Model"):

    st.write("Model yang digunakan: **YOLOv11**")

    st.write(
        f"Jumlah kelas pada model: **{len(model.names)} kelas**"
    )

    st.write("Daftar kelas:")

    class_names = list(model.names.values())

    st.write(", ".join(class_names))


# ============================================================
# UPLOAD / CAMERA
# ============================================================

st.markdown(
    """
    <div class='section-kicker'>Langkah 1</div>
    <div class='section-title'>Upload foto piring makanan</div>
    """,
    unsafe_allow_html=True,
)

sumber_foto = st.radio(
    "Sumber foto",
    ["Upload Foto", "Buka Kamera"],
    horizontal=True,
)


if sumber_foto == "Upload Foto":

    uploaded_file = st.file_uploader(
        "Pilih Foto",
        type=["jpg", "jpeg", "png"],
    )

else:

    st.info(
        "Izinkan akses kamera pada browser, arahkan kamera "
        "ke piring makanan, lalu tekan tombol ambil foto."
    )

    uploaded_file = st.camera_input(
        "Ambil foto makanan"
    )


# ============================================================
# PROSES DETEKSI
# ============================================================

if uploaded_file:

    image = Image.open(uploaded_file)

    st.markdown(
        """
        <div class='section-kicker'>Hasil analisis</div>
        <div class='section-title'>
            Perbandingan foto dan deteksi AI
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(
        2,
        gap="large"
    )


    # --------------------------------------------------------
    # FOTO ASLI
    # --------------------------------------------------------

    with col1:

        with st.container(border=True):

            st.markdown(
                "<div class='image-card-title'>Foto yang diupload</div>",
                unsafe_allow_html=True,
            )

            st.image(
                image,
                use_container_width=True
            )


    # --------------------------------------------------------
    # YOLO DETECTION
    # --------------------------------------------------------

    results = model(
        image,
        conf=0.5
    )

    annotated = results[0].plot()


    # --------------------------------------------------------
    # FOTO HASIL DETEKSI
    # --------------------------------------------------------

    with col2:

        with st.container(border=True):

            st.markdown(
                "<div class='image-card-title'>Hasil deteksi YOLO</div>",
                unsafe_allow_html=True,
            )

            st.image(
                annotated,
                use_container_width=True
            )


    st.success(
        "Deteksi selesai!"
    )


    # ========================================================
    # MAKANAN TERDETEKSI
    # ========================================================

    st.markdown(
        """
        <div class='section-kicker'>Menu terdeteksi</div>
        <div class='section-title'>
            Makanan dalam piring Anda
        </div>
        """,
        unsafe_allow_html=True,
    )


    detected_foods = []


    for box in results[0].boxes:

        class_id = int(box.cls[0])

        nama_makanan = model.names[class_id]

        confidence = float(box.conf[0])

        detected_foods.append(
            (
                nama_makanan,
                confidence
            )
        )


    # ========================================================
    # TIDAK ADA DETEKSI
    # ========================================================

    if len(detected_foods) == 0:

        st.warning(
            "Tidak ada makanan yang terdeteksi."
        )

    else:

        # ----------------------------------------------------
        # HAPUS DUPLIKAT NAMA MAKANAN
        # ----------------------------------------------------

        unique_foods = {}

        for nama, confidence in detected_foods:

            if (
                nama not in unique_foods
                or confidence > unique_foods[nama]
            ):

                unique_foods[nama] = confidence


        # ----------------------------------------------------
        # CHIP MAKANAN
        # ----------------------------------------------------

        chips = ""

        for nama, confidence in unique_foods.items():

            chips += (
                f"<span class='food-chip'>"
                f"✓ {nama.title()} "
                f"({confidence * 100:.1f}%)"
                f"</span>"
            )


        st.markdown(
            chips,
            unsafe_allow_html=True
        )


        # ====================================================
        # TABEL HASIL DETEKSI
        # ====================================================

        st.markdown(
            """
            <div class='section-kicker'>Detail deteksi</div>
            <div class='section-title'>
                Tingkat kepercayaan model
            </div>
            """,
            unsafe_allow_html=True,
        )


        import pandas as pd


        detection_data = []


        for nama, confidence in detected_foods:

            detection_data.append(
                {
                    "Makanan": nama.title(),
                    "Confidence": f"{confidence * 100:.2f}%"
                }
            )


        df_detection = pd.DataFrame(
            detection_data
        )


        st.dataframe(
            df_detection,
            use_container_width=True,
            hide_index=True,
        )


        # ====================================================
        # RINGKASAN
        # ====================================================

        st.markdown(
            """
            <div class='section-kicker'>Ringkasan</div>
            <div class='section-title'>
                Hasil deteksi makanan
            </div>
            """,
            unsafe_allow_html=True,
        )


        metric_cols = st.columns(3)


        with metric_cols[0]:

            st.metric(
                "Jumlah Objek",
                len(detected_foods)
            )


        with metric_cols[1]:

            st.metric(
                "Jenis Makanan",
                len(unique_foods)
            )


        with metric_cols[2]:

            rata_confidence = (
                sum(
                    confidence
                    for _, confidence in detected_foods
                )
                / len(detected_foods)
            )

            st.metric(
                "Rata-rata Confidence",
                f"{rata_confidence * 100:.1f}%"
            )


        # ====================================================
        # INFORMASI NILAI GIZI
        # ====================================================

        st.markdown(
            """
            <div class='section-kicker'>Nilai gizi</div>
            <div class='section-title'>
                Estimasi nilai gizi
            </div>
            """,
            unsafe_allow_html=True,
        )


        st.info(
            """
            Database telah dihapus dari aplikasi.

            Oleh karena itu, data nilai gizi TKPI tidak lagi
            diambil dari database. Deteksi makanan tetap dapat
            berjalan menggunakan model YOLOv11.

            Jika ingin menampilkan energi, protein, lemak,
            karbohidrat, dan serat, data TKPI dapat dimasukkan
            langsung ke dalam kode Python sebagai data lokal.
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Sistem Deteksi Makanan Program Makan Bergizi Gratis (MBG) "
    "Menggunakan YOLOv11"
)