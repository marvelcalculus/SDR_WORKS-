import streamlit as st

st.set_page_config(page_title="SolidWorks Dimension Editor", layout="centered")

st.title("🔧 SolidWorks Outrigger Editor")


st.markdown("Enter values below to update the model. All units are in `mm`.")

# GVW input
gvw = st.number_input("Gross Vehicle Weight (GVW) in Tons",
                      min_value=0.0, value=10.0)
sq_tube_thk = st.selectbox("Select SQ Tube Thickness", options=[10.0, 12.0])


# Auto-classify values based on GVW
if 7 <= gvw <= 8.5:
    # GVW 7 - 8.5
    fc_inner_width = 170
    fc_inner_height = 122
    thickness_fc = 10

    mf_inner_height = 127
    mf_outer_height = 150
    mf_inner_width = 190
    mf_outer_width = 275
    mf_c2c = 235
    mf_c2c_vertical = 50
    mf_edge2c = 22
    mf_nut_dia = 17

    inner_width = 150
    sq_tube_thk = 10

elif 9 <= gvw <= 13:
    # GVW 9 - 13
    fc_inner_width = 221
    fc_inner_height = 142
    thickness_fc = 10

    mf_inner_height = 141
    mf_outer_height = 165
    mf_inner_width = 241
    mf_outer_width = 340
    mf_c2c = 295
    mf_c2c_vertical = 55
    mf_edge2c = 22
    mf_nut_dia = 19

    inner_width = 201
    sq_tube_thk = 10

elif 14 <= gvw <= 23:
    # GVW 14 - 23
    if sq_tube_thk == 12.0:
        fc_inner_width = 284
        fc_inner_height = 172
        thickness_fc = 10

        mf_inner_height = 162
        mf_outer_height = 192
        mf_inner_width = 304
        mf_outer_width = 414
        mf_c2c = 369
        mf_c2c_vertical = 55
        mf_edge2c = 29
        mf_nut_dia = 21

        inner_width = 260
    else:
        fc_inner_width = 280
        fc_inner_height = 170
        thickness_fc = 10

        mf_inner_height = 160
        mf_outer_height = 190
        mf_inner_width = 300
        mf_outer_width = 410
        mf_c2c = 365
        mf_c2c_vertical = 55
        mf_edge2c = 29
        mf_nut_dia = 21

        inner_width = 260

else:
    # Default
    fc_inner_width = 0
    fc_inner_height = 0
    thickness_fc = 0

    mf_inner_height = 0
    mf_outer_height = 0
    mf_inner_width = 0
    mf_outer_width = 0
    mf_c2c = 0
    mf_c2c_vertical = 0
    mf_edge2c = 0
    mf_nut_dia = 0

    inner_width = 0
    sq_tube_thk = 0

st.markdown(f"### Auto-selected Inner Width SQT: `{inner_width} mm`")


# Input fields


if st.button("💾 Save & Generate File"):
    content = f'''

########### FC ##########
"FC_INNER WIDTH" = {fc_inner_width}mm
"FC_INNER HEIGHT" = {fc_inner_height}mm
"THICKNESS_FC" = {thickness_fc}mm

###### MOUNTING FLANGE ######
"MF_INNER HEIGHT" = {mf_inner_height}mm
"MF_OUTER HEIGHT" = {mf_outer_height}mm
"MF_INNER WIDTH" = {mf_inner_width}mm
"MF_OUTER WIDTH" = {mf_outer_width}mm
"MF_C2C" = {mf_c2c}mm
"MF C2C Vertical" = {mf_c2c_vertical}mm
"MF EDGE2C " = {mf_edge2c}mm
"MF_NUT DIAMETER" = {mf_nut_dia}mm

###### OUTER SQ TUBE ######
"INNER WIDTH" = {inner_width}mm
"SQ TUBE THK" = {sq_tube_thk}mm
'''

    st.success("✅ Equations generated successfully!")

    st.download_button(
        label="📥 Download Equations.txt",
        data=content,
        file_name="PARAMETRIC RELATIONS.txt",
        mime="text/plain"
    )
