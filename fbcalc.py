import streamlit as st
import datetime

st.set_page_config(page_title="Pro Meal Planner 🍽️", page_icon="🍌", layout="wide")

# HEADER 
st.markdown("""
    <h1 style='text-align: center; color: orange;'>🍽️ Pro Meal Plan Calculator</h1>
    <p style='text-align: center;'>Smart budgeting for Flex Bucks & Meal Swipes</p>
""", unsafe_allow_html=True)

# DATE LOGIC 
today = datetime.datetime.now()
weekday = today.weekday()
days_until_friday = (4 - weekday) % 7

semester_end = st.date_input("Select Semester End Date", datetime.date(2026, 5, 30))
days_remaining = (semester_end - today.date()).days

if days_remaining <= 0:
    st.error("Semester already ended. Choose a valid date.")
    st.stop()

# LAYOUT
col1, col2, col3 = st.columns(3)

# FLEX BUCKS 
with col1:
    st.subheader("💰 Flex Bucks Planner")
    flex = st.number_input("Enter Flex Bucks", min_value=0.0, step=1.0)

    if flex > 0:
        per_day = flex / days_remaining
        st.success(f"💡 Spend per day: ${per_day:.2f}")
        st.info(f"Days remaining: {days_remaining}")

# MEAL SWIPES
with col2:
    st.subheader("🍱 Meal Swipes Planner")
    swipes = st.number_input("Enter Meal Swipes", min_value=0, step=1)

    if swipes > 0:
        if days_until_friday == 0:
            st.warning("Reset day is today!")
        else:
            per_day_swipe = swipes / days_until_friday
            st.success(f"Use per day: {per_day_swipe:.2f} swipes")
            st.info(f"Days until reset: {days_until_friday}")

# CALORIE TRACKER 
with col3:
    st.subheader("🔥 Daily Calorie Goal")

    weight = st.number_input("Your weight (kg)", min_value=30, max_value=150, value=75)
    goal = st.selectbox("Goal", ["Lose Weight", "Maintain", "Gain Weight"])

    if goal == "Lose Weight":
        calories = weight * 22
    elif goal == "Maintain":
        calories = weight * 28
    else:
        calories = weight * 32

    st.success(f"Recommended Calories: {int(calories)} kcal/day")

# MEAL PLANNER 
st.markdown("---")
st.subheader("🤖 AI Weekly Meal Planner")

diet_type = st.selectbox("Choose Diet Type", ["Veg", "Non-Veg"])

# Meal database
meal_db = {
    "Veg": {
        "breakfast": ["Oats + Fruits", "Poha", "Upma", "Smoothie", "Idli + Sambar"],
        "lunch": ["Rice + Dal + Sabzi", "Chapati + Paneer", "Veg Pulao", "Curd Rice"],
        "dinner": ["Soup + Salad", "Paneer + Veggies", "Khichdi", "Chapati + Sabzi"]
    },
    "Non-Veg": {
        "breakfast": ["Egg Omelette + Toast", "Boiled Eggs + Fruits", "Chicken Sandwich"],
        "lunch": ["Rice + Chicken Curry", "Chapati + Egg Curry", "Grilled Chicken + Rice"],
        "dinner": ["Chicken Soup", "Grilled Fish + Veggies", "Egg Bhurji + Chapati"]
    }
}

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
meal_plan = {}

st.info("⚡ AI-generated meals based on your goal, calories & diet")

for day in days:
    breakfast = random.choice(meal_db[diet_type]["breakfast"])
    lunch = random.choice(meal_db[diet_type]["lunch"])
    dinner = random.choice(meal_db[diet_type]["dinner"])

    default_meal = f"🍳 {breakfast} | 🍛 {lunch} | 🌙 {dinner}"

    meal_plan[day] = st.text_input(f"{day}", value=default_meal)

# SUMMARY 
if st.button("📋 Generate Full Plan"):
    st.markdown("### 📝 Weekly Meal Plan")
    for d, meal in meal_plan.items():
        st.write(f"**{d}:** {meal}")

# SHOPPING LIST 
if st.button("🛒 Generate Shopping List"):
    st.markdown("### 🛍️ Shopping List")

    items = set()

    for meal in meal_plan.values():
        for item in meal.split("|"):
            parts = item.replace("🍳", "").replace("🍛", "").replace("🌙", "")
            for word in parts.split("+"):
                items.add(word.strip())

    for item in sorted(items):
        st.write(f"✅ {item}")

# FOOTER 
st.caption("Made with ❤️ using Streamlit")
