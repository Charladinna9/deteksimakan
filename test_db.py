import psycopg2
import streamlit as st

try:
    conn = psycopg2.connect(
        host=st.secrets["supabase"]["host"],
        port=st.secrets["supabase"]["port"],
        user=st.secrets["supabase"]["user"],
        password=st.secrets["supabase"]["password"],
        database=st.secrets["supabase"]["database"]
    )

    st.success("✅ BERHASIL TERHUBUNG KE SUPABASE")
    conn.close()

except Exception as e:
    st.error(f"❌ Gagal koneksi ke Supabase: {e}")
    print(f"❌ ERROR ASLI: {e}")