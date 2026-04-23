import streamlit as st
from datetime import date

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Athlete Tracker", page_icon="🏃", layout="centered")

st.title("🏃 Athlete Performance Tracker")
st.write("Track your training, sleep, nutrition, and performance in one place.")

# -----------------------------
# Session state initialization
# -----------------------------
if "training" not in st.session_state:
    st.session_state.training = []

if "sleep" not in st.session_state:
    st.session_state.sleep = []

if "nutrition" not in st.session_state:
    st.session_state.nutrition = []

if "performance" not in st.session_state:
    st.session_state.performance = []

# -----------------------------
# MENU
# -----------------------------
menu = st.selectbox(
    "Choose a category",
    ["Training", "Sleep", "Nutrition", "Performance"]
)

# =============================
# TRAINING TRACKER
# =============================
if menu == "Training":
    st.subheader("🏋️ Log Training Session")

    with st.form("training_form"):
        t_date = st.date_input("Date", value=date.today())
        sport = st.text_input("Sport / Activity (e.g. football, gym)")
        duration = st.number_input("Duration (minutes)", min_value=0)
        intensity = st.selectbox("Intensity", ["Low", "Medium", "High"])
        notes = st.text_area("Notes")

        submitted = st.form_submit_button("Add Training")

        if submitted and sport:
            st.session_state.training.append({
                "date": str(t_date),
                "sport": sport,
                "duration": duration,
                "intensity": intensity,
                "notes": notes
            })
            st.success("Training session added!")

    st.divider()
    st.subheader("📋 Training History")

    for t in reversed(st.session_state.training):
        st.write(f"📅 {t['date']} — {t['sport']} ({t['duration']} min, {t['intensity']})")
        if t["notes"]:
            st.caption(t["notes"])
        st.markdown("---")

# =============================
# SLEEP TRACKER
# =============================
elif menu == "Sleep":
    st.subheader("😴 Log Sleep")

    with st.form("sleep_form"):
        s_date = st.date_input("Date", value=date.today())
        hours = st.slider("Hours slept", 0, 12, 7)
        quality = st.selectbox("Sleep quality", ["Poor", "Average", "Good", "Excellent"])
        notes = st.text_area("Notes")

        submitted = st.form_submit_button("Add Sleep Data")

        if submitted:
            st.session_state.sleep.append({
                "date": str(s_date),
                "hours": hours,
                "quality": quality,
                "notes": notes
            })
            st.success("Sleep data added!")

    st.divider()
    st.subheader("📋 Sleep History")

    for s in reversed(st.session_state.sleep):
        st.write(f"📅 {s['date']} — {s['hours']}h ({s['quality']})")
        if s["notes"]:
            st.caption(s["notes"])
        st.markdown("---")

# =============================
# NUTRITION TRACKER
# =============================
elif menu == "Nutrition":
    st.subheader("🍽️ Log Nutrition")

    with st.form("nutrition_form"):
        n_date = st.date_input("Date", value=date.today())
        meal = st.text_input("Meal (e.g. breakfast, lunch)")
        food = st.text_area("What did you eat?")
        healthy = st.selectbox("Healthiness", ["Unhealthy", "Neutral", "Healthy"])

        submitted = st.form_submit_button("Add Meal")

        if submitted and meal:
            st.session_state.nutrition.append({
                "date": str(n_date),
                "meal": meal,
                "food": food,
                "healthy": healthy
            })
            st.success("Meal added!")

    st.divider()
    st.subheader("📋 Nutrition History")

    for n in reversed(st.session_state.nutrition):
        st.write(f"📅 {n['date']} — {n['meal']} ({n['healthy']})")
        st.caption(n["food"])
        st.markdown("---")

# =============================
# PERFORMANCE TRACKER
# =============================
elif menu == "Performance":
    st.subheader("📊 Log Performance")

    with st.form("performance_form"):
        p_date = st.date_input("Date", value=date.today())
        metric = st.text_input("Key metric (e.g. sprint time, match rating)")
        value = st.text_input("Value")
        notes = st.text_area("Notes")

        submitted = st.form_submit_button("Add Performance Data")

        if submitted and metric:
            st.session_state.performance.append({
                "date": str(p_date),
                "metric": metric,
                "value": value,
                "notes": notes
            })
            st.success("Performance data added!")

    st.divider()
    st.subheader("📋 Performance History")

    for p in reversed(st.session_state.performance):
        st.write(f"📅 {p['date']} — {p['metric']}: {p['value']}")
        if p["notes"]:
            st.caption(p["notes"])
        st.markdown("---")

# -----------------------------
# GLOBAL RESET
# -----------------------------
st.divider()
if st.button("🧹 Reset All Data"):
    st.session_state.training = []
    st.session_state.sleep = []
    st.session_state.nutrition = []
    st.session_state.performance = []
    st.success("All data cleared!")
