import streamlit as st
from datetime import datetime

st.set_page_config(page_title="SolidWorks Dimension Editor", layout="centered")

st.title("🔧 SolidWorks Outrigger Editor")
st.image("images.jpeg", width=200)

st.markdown("Enter values below to update the model. All units are in `mm`.")

# GVW input
gvw = st.number_input("Gross Vehicle Weight (GVW) in Tons",
                      min_value=0.0, value=10.0)

# Auto-classify inner_width based on GVW
if 7.5 <= gvw <= 8.5:
    inner_width = 150.0
elif 9 <= gvw <= 13:
    inner_width = 200.0
elif 14 <= gvw <= 19:
    inner_width = 260.0
elif 20 <= gvw <= 23:
    inner_width = 280.0
elif 24 <= gvw <= 28:
    inner_width = 300.0
else:
    inner_width = 201.0  # Default/fallback value if GVW doesn't match

st.markdown(f"### Auto-selected Inner Width SQT: `{inner_width} mm`")

# Other input fields
r1 = st.number_input("Radius r1", min_value=0.0, value=10.0)
t1 = st.number_input("thickness t1", min_value=0.0, value=10.0)
t2 = st.number_input("thickness t2", min_value=0.0, value=10.0)
r4 = st.number_input("Radius r4", min_value=0.0, value=20.0)
mf_thick = st.number_input("MF Thick", min_value=0.0, value=49.5)
mf_cc_offset = st.number_input("MF CC Offset", min_value=0.0, value=22.5)
mf_top_offset = st.number_input(
    "MF Top Offset (Optional)", min_value=0.0, value=22.25)

if st.button("💾 Save & Update Model"):
    content = f'''"Radius r1" = {r1}mm
"thickness t1" = {t1}mm
"Radius r2" = "Radius r1" + "thickness t1"
"thickness t2" = {t2}mm
"Radius r3" = "Radius r2" + "thickness t2"
"Radius r4" = {r4}mm
"Inner Width SQT" = {inner_width}mm
"Outer Width SQT" = "Inner Width SQT" + 2*"thickness t1"
"MF Inner Width" = "Outer Width SQT" + 2*"thickness t2"
"MF Thick" = {mf_thick}mm
"MF Outer Width" = "MF Inner Width" + 2*"MF Thick"
"FC Height" = ("Inner Width SQT"/2)+45mm
"MF Height" = ("FC Height"/2) + 70mm
"MF CC Offset" = {mf_cc_offset}mm
"MF CC" = "MF Outer Width"-(2*"MF CC Offset")
"MF Top Offset" = "MF Height"+{mf_top_offset}mm
'''

 # Enable download of the file
  st.download_button(
        label="📥 Download Equations.txt",
        data=content,
        file_name="Equations.txt",
        mime="text/plain"
    )
