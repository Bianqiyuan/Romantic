import streamlit as st

st.title("✨浪漫小测试")
ans1 = st.radio("你是否喜欢我？回答：", ["是", "否"])
if ans1 == "是":
    st.write("我爱你")
    days_text = st.text_input("你喜欢我多久了，几天（回答数字）？")
    if days_text:
        try:
            days = int(days_text)
            if days > 0:
                st.success("我爱你一生一世")
            else:
                st.success("我们将从此刻开始相爱至永远")
        except ValueError:
            st.success("那我们就从现在开始相爱至永远")
else:
    st.write("今晚夜色真美，我们还有机缘")
