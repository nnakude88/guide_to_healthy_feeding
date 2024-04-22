import streamlit as st
from PIL import Image

st.title("Guild to healthy feeding")
st.sidebar.header("check if you are feeding right ?")

Age = st.number_input("Enter your age: ", step=1)
def Age_reading(Age):
    if Age >= 60:
        return "You're advanced in age and should eat;low-fat diary products, nuts,seeds,vegetables,drink plenty water, then spend time with family members at meal time"
    elif 19 <= Age < 60:
        return "You are an Adult and should eat; calcium rich food,egg,cereals,wholegrain,food rich in carbohydrates"
    elif 13 <= Age < 19:
        return "You are a teenager and should feed mostly on wholegrains,legume,nuts,vegetables,fish and lean meat"
    elif 0.5 <= Age < 12:
        return "You are a Child and should eat; vegetables,fruits,poutry products,fish and lean meat"
    else:
         return "You are an infant and should feed on breastmilk and infant fomula"
    
result = Age_reading(Age)
st.write(result)

img = Image.open("feedwell.jpg")
st.image(img)
img = Image.open("feedwell_2.jpg")
st.sidebar.image(img, caption="You're as healthy as the food you eat")
