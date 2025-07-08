import streamlit as st
import pandas as pd
from io import BytesIO
import zipfile

st.set_page_config(page_title="CSV ➜ Excel Converter", layout="wide")
st.title("📂 Upload hàng loạt file CSV ➜ Tự động chuyển thành Excel (.xlsx)")

uploaded_files = st.file_uploader("📤 Chọn nhiều file CSV", type="csv", accept_multiple_files=True)

if uploaded_files:
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for uploaded_file in uploaded_files:
            df = pd.read_csv(uploaded_file)
            output = BytesIO()
            excel_filename = uploaded_file.name.replace(".csv", ".xlsx")
            df.to_excel(output, index=False, engine='openpyxl')
            zip_file.writestr(excel_filename, output.getvalue())

    st.success(f"✅ Đã xử lý {len(uploaded_files)} file CSV và chuyển sang Excel!")

    # Tải về file ZIP chứa các Excel
    st.download_button(
        label="📥 Tải tất cả file Excel (.xlsx) trong 1 file ZIP",
        data=zip_buffer.getvalue(),
        file_name="converted_excels.zip",
        mime="application/zip"
    )
