import streamlit as st

# App description
st.title("Milan Criteria for Liver Transplantation")
st.write("""
This app calculates whether a patient with hepatocellular carcinoma (HCC) meets the Milan Criteria for liver transplantation.
The Milan Criteria include:
- A single tumor ≤ 5 cm in diameter
- Up to 3 tumors, none exceeding 3 cm in diameter
- No evidence of vascular invasion
""")

# Input fields for tumor characteristics
st.header("Patient Tumor Characteristics")
num_tumors = st.number_input("Number of Tumors", min_value=1, max_value=10, value=1, step=1)
tumor_sizes = []
for i in range(num_tumors):
    size = st.number_input(f"Size of Tumor {i+1} (cm)", min_value=0.1, max_value=20.0, value=1.0, step=0.1)
    tumor_sizes.append(size)

# Input field for vascular invasion
vascular_invasion = st.selectbox("Evidence of Vascular Invasion", ("No", "Yes"))

# Calculate eligibility based on Milan Criteria
eligible = False
if vascular_invasion == "No":
    if num_tumors == 1 and tumor_sizes[0] <= 5.0:
        eligible = True
    elif num_tumors <= 3 and all(size <= 3.0 for size in tumor_sizes):
        eligible = True

# Display result
st.header("Eligibility Result")
if eligible:
    st.success("The patient meets the Milan Criteria for liver transplantation.")
else:
    st.error("The patient does NOT meet the Milan Criteria for liver transplantation.")
