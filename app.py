import streamlit as st
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Athlete Pro Tracker", page_icon="🏃‍♂️", layout="wide")

# -----------------------------
# CUSTOM STYLING (VIBRANT UI)
# -----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }
    h1, h2, h3 {
        color: #38bdf8;
    }
    .stButton button {
        background-color: #22c55e;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏃‍♂️ Athlete Pro Performance Dashboard")
st.caption("Track training, recovery, nutrition, and performance like a pro athlete")

# -----------------------------
# SESSION STATE INIT
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
# SIDEBAR NAVIGATION
# -----------------------------
menu = st.sidebar.radio(
    "📍 Navigation",
    ["🏠 Dashboard", "🏋️ Training", "😴 Sleep", "🍽️ Nutrition", "📈 Performance"]
)

# =============================
# DASHBOARD
# =============================
if menu == "🏠 Dashboard":
    st.header("📊 Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Training Sessions", len(st.session_state.training))
    col2.metric("Sleep Logs", len(st.session_state.sleep))
    col3.metric("Meals Logged", len(st.session_state.nutrition))
    col4.metric("Performance Entries", len(st.session_state.performance))

    st.divider()

    # -----------------------------
    # TRAINING CHART
    # -----------------------------
    if st.session_state.training:
        df = pd.DataFrame(st.session_state.training)
        df["duration"] = pd.to_numeric(df["duration"])

        st.subheader("🏋️ Training Volume")

        fig, ax = plt.subplots()
        df.groupby("date")["duration"].sum().plot(kind="line", ax=ax)
        ax.set_title("Training Duration Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Minutes")
        st.pyplot(fig)

    # -----------------------------
    # SLEEP CHART
    # -----------------------------
    if st.session_state.sleep:
        df2 = pd.DataFrame(st.session_state.sleep)
        df2["hours"] = pd.to_numeric(df2["hours"])

        st.subheader("😴 Sleep Trends")

        fig2, ax2 = plt.subplots()
        df2.groupby("date")["hours"].mean().plot(kind="line", ax=ax2)
        ax2.set_title("Sleep Hours Over Time")
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Hours")
        st.pyplot(fig2)

    # -----------------------------
    # INSIGHT
    # -----------------------------
    st.divider()
    st.subheader("🧠 Insight")

    if len(st.session_state.sleep) > 0:
        avg_sleep = sum([s["hours"] for s in st.session_state.sleep]) / len(st.session_state.sleep)

        if avg_sleep < 6:
            st.warning("⚠️ Low recovery detected. Consider increasing sleep for better performance.")
        elif avg_sleep < 7.5:
            st.info("🙂 Moderate recovery. Small improvements could boost performance.")
        else:
            st.success("🔥 Excellent recovery patterns. Keep it up!")

# =============================
# TRAINING
# =============================
elif menu == "🏋️ Training":
    st.header("🏋️ Log Training")

    with st.form("training_form"):
        d = st.date_input("Date", value=date.today())
        sport = st.text_input("Sport")
        duration = st.number_input("Duration (minutes)", 0)
        intensity = st.selectbox("Intensity", ["Low", "Medium", "High"])
        notes = st.text_area("Notes")

        if st.form_submit_button("Add Training"):
            st.session_state.training.append({
                "date": str(d),
                "sport": sport,
                "duration": duration,
                "intensity": intensity,
                "notes": notes
            })
            st.success("Training added!")

    st.divider()
    for t in reversed(st.session_state.training):
        st.write(f"🏃 {t['date']} | {t['sport']} | {t['duration']} min | {t['intensity']}")
        st.caption(t["notes"])
        st.markdown("---")

# =============================
# SLEEP
# =============================
elif menu == "😴 Sleep":
    st.header("😴 Sleep Tracking")

    with st.form("sleep_form"):
        d = st.date_input("Date", value=date.today())
        hours = st.slider("Hours", 0, 12, 7)
        quality = st.selectbox("Quality", ["Poor", "Average", "Good", "Excellent"])
        notes = st.text_area("Notes")

        if st.form_submit_button("Add Sleep"):
            st.session_state.sleep.append({
                "date": str(d),
                "hours": hours,
                "quality": quality,
                "notes": notes
            })
            st.success("Sleep logged!")

    st.divider()
    for s in reversed(st.session_state.sleep):
        st.write(f"😴 {s['date']} | {s['hours']}h | {s['quality']}")
        st.caption(s["notes"])
        st.markdown("---")

# =============================
# NUTRITION
# =============================
elif menu == "🍽️ Nutrition":
    st.header("🍽️ Nutrition Log")

    with st.form("nutrition_form"):
        d = st.date_input("Date", value=date.today())
        meal = st.text_input("Meal")
        food = st.text_area("Food")
        health = st.selectbox("Quality", ["Unhealthy", "Neutral", "Healthy"])

        if st.form_submit_button("Add Meal"):
            st.session_state.nutrition.append({
                "date": str(d),
                "meal": meal,
                "food": food,
                "health": health
            })
            st.success("Meal added!")

    st.divider()
    for n in reversed(st.session_state.nutrition):
        st.write(f"🍽️ {n['date']} | {n['meal']} | {n['health']}")
        st.caption(n["food"])
        st.markdown("---")

# =============================
# PERFORMANCE
# =============================
elif menu == "📈 Performance":
    st.header("📈 Performance Metrics")

    with st.form("perf_form"):
        d = st.date_input("Date", value=date.today())
        metric = st.text_input("Metric")
        value = st.text_input("Value")
        notes = st.text_area("Notes")

        if st.form_submit_button("Add"):
            st.session_state.performance.append({
                "date": str(d),
                "metric": metric,
                "value": value,
                "notes": notes
            })
            st.success("Performance logged!")

    st.divider()
    for p in reversed(st.session_state.performance):
        st.write(f"📊 {p['date']} | {p['metric']} = {p['value']}")
        st.caption(p["notes"])
        st.markdown("---")
