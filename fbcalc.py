import datetime
import requests
import streamlit as st
# from streamlit_lottie import st_lottie

flexBucksAmmount = 0

today = datetime.datetime.now().weekday()
days_until_friday = (4 - today) % 7

lastDaySpring = datetime.datetime.strptime("2023-05-02", "%Y-%m-%d")
today = datetime.datetime.strptime(
    str(datetime.datetime.now().date()), "%Y-%m-%d")
daysOnCampus = today-lastDaySpring
numstring = str(daysOnCampus)
numstring = numstring[1:3]


def isNumber(string):
    try:
        float(string)
        return True
    except:
        return False


def wholeNumber(string):
    try:
        int(string)
        return True
    except:
        return False


st.set_page_config(page_title="Meal Plan/er🍌", page_icon="🍌")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# foodAni = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ysas4vcp.json")

# swipeAni = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tchv1irg.json")

with st.container():
    st.markdown("<h1 style='text-align: center; font-size: 70px; color: orange;'> Meal Plan Calculator. </h1>",
                unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'> Calculate how much flex bucks you can spend per day or meal swipes </h1>", unsafe_allow_html=True)


with st.container():
    leftCol, rightCol=st.columns(2)
    with leftCol:
        # st_lottie(foodAni, height=100, key="food")
        flexBucks=st.text_input(
            "Enter amount of flex bucks you currently have: ")
        if flexBucks != "":
            if isNumber(flexBucks):
                flexBucksAmmount=float(flexBucks)/float(numstring)
                st.write(
                    "You can only spend this amount per day this semester for your flexbucks to last: $", round(flexBucksAmmount, 2))
                st.write("Days until end of semester: ", int(numstring))
            else:
                st.write(
                    "Please enter a number with no special characters/letters :)")
    with rightCol:
        # st_lottie(swipeAni, height=100, key="swipes")
        mealSwipes = st.text_input("Enter amount of meal swipes you currently have: ")

if mealSwipes != "":
    if wholeNumber(mealSwipes):
        if days_until_friday > 0:
            per_day = float(mealSwipes) / float(days_until_friday)
            st.write(
                "You can only use this amount of swipes per day to last until friday:",
                round(per_day, 2)
            )
            st.write("Days until friday (reset day): ", days_until_friday)
        else:
            st.write("Error: Days until Friday cannot be 0")
    else:
        st.write("Please enter a whole number :)")