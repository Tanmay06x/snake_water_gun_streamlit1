
import streamlit as st
import random

st.title("🐍 Snake - Water - Gun Game")
st.markdown("Play against the computer!")

youstr = st.radio("Choose your move:", ["Snake", "Water", "Gun"])
youDict = {"Snake": 1, "Water": -1, "Gun": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if st.button("Play"):
    computer = random.choice([-1, 0, 1])
    you = youDict[youstr]

    st.write(f"**You chose:** {youstr}")
    st.write(f"**Computer chose:** {reverseDict[computer]}")

    if computer == you:
        st.success("It's a Draw!")
    else:
        if computer == 1 and you == -1:
            st.error("You Lose!")
        elif computer == 1 and you == 0:
            st.success("You Win!")
        elif computer == 0 and you == -1:
            st.success("You Win!")
        elif computer == 0 and you == 1:
            st.error("You Lose!")
        elif computer == -1 and you == 1:
            st.success("You Win!")
        elif computer == -1 and you == 0:
            st.error("You Lose!")
        else:
            st.warning("Something went wrong!")
