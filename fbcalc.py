import streamlit as st
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Pro Meal Planner 🍽️", page_icon="🍌", layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
    <h1 style='text-align: center; color: orange;'>🍽️ Pro Meal Plan Calculator</h1>
    <p style='text-align: center;'>Smart budgeting for Flex Bucks & Meal Swipes</p>
""", unsafe_allow_html=True)

# ---------------- DATE LOGIC ----------------
today = datetime.datetime.now()
weekday = today.weekday()
days_until_friday = (4 - weekday) % 7

semester_end = st.date_input("Select Semester End Date", datetime.date(2026, 5, 30))
days_remaining = (semester_end - today.date()).days

if days_remaining <= 0:
    st.error("Semester already ended. Choose a valid date.")
    st.stop()

# ---------------- LAYOUT ----------------
col1, col2, col3 = st.columns(3)

# ---------------- FLEX BUCKS ----------------
with col1:
    st.subheader("💰 Flex Bucks Planner")
    flex = st.number_input("Enter Flex Bucks", min_value=0.0, step=1.0)

    if flex > 0:
        per_day = flex / days_remaining
        st.success(f"💡 Spend per day: ${per_day:.2f}")
        st.info(f"Days remaining: {days_remaining}")

# ---------------- MEAL SWIPES ----------------
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

# ---------------- CALORIE TRACKER ----------------
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

# ---------------- WEEKLY MEAL PLAN ----------------
st.markdown("---")
st.subheader("📅 Smart Weekly Meal Planner")

# Predefined meal suggestions
meal_suggestions = {
    "Lose Weight": [
        "Oats + Boiled Eggs + Salad",
        "Grilled Chicken + Veggies",
        "Fruit Bowl + Nuts",
        "Brown Rice + Dal + Sabzi",
        "Smoothie + Peanut Butter Toast",
        "Soup + Salad",
        "Paneer + Veggies"
    ],
    "Maintain": [
        "Oats + Milk + Fruits",
        "Rice + Chicken Curry",
        "Sandwich + Juice",
        "Chapati + Dal + Sabzi",
        "Pasta + Veggies",
        "Egg Bhurji + Toast",
        "Paneer + Rice"
    ],
    "Gain Weight": [
        "Oats + Milk + Peanut Butter",
        "Rice + Chicken + Eggs",
        "Banana Shake + Sandwich",
        "Chapati + Paneer + Dal",
        "Pasta + Cheese",
        "Egg Omelette + Bread + Milk",
        "Dry Fruits + Smoothie"
    ]
}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
meal_plan = {}

# Auto-suggestions based on goal
suggested_meals = meal_suggestions.get(goal, meal_suggestions["Maintain"])

st.info("💡 Auto-suggested meals based on your goal (you can edit them)")

for i, day in enumerate(days):
    default_meal = suggested_meals[i]
    meal_plan[day] = st.text_input(
        f"{day} Plan",
        value=default_meal
    )

if st.button("📋 Generate Summary"):
    st.markdown("### 📝 Your Weekly Plan")
    for d, meal in meal_plan.items():
        st.write(f"**{d}:** {meal}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
