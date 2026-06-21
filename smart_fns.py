import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="SMART FNS - Plateforme Médicale", page_icon="🩺")

# العنوان
st.title("🩺 SMART FNS - Plateforme Médicale")
st.subheader("مرحباً بكم دكاترة المستقبل")

# الترحيب
st.markdown("""
هذه المنصة مخصصة لمراجعة الحالات السريرية والأسئلة الطبية. 
يرجى اختيار القسم الذي ترغبون في مراجعته من القائمة الجانبية.
""")

# الأزرار
st.divider()
st.write("### قائمة الأقسام المتاحة:")
if st.button("1. مراجعة الحالات السريرية"):
    st.write("سوف تظهر الحالات هنا قريباً...")
if st.button("2. الأسئلة التخصصية (QCM)"):
    st.write("سوف تظهر الأسئلة هنا قريباً...")

# التواصل
st.sidebar.info("للتواصل مع الدكتورة: [أضيفي بريدك هنا]")
