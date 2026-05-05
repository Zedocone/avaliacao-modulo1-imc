import streamlit as st

st.title("calculadora IMC 📱")
st.subheader("feito com streamlit ✨")

altura = st.number_input("digite a sua altura", min_value=0.0)
peso = st.number_input("digite o seu peso",min_value=0.0)

if st.button("calcular"):
    imc = peso / altura ** 2
    if imc < 18.5:
        st.error("abaixo do peso")
    elif imc < 24.9:
        st.success("na media paizao")
    elif imc < 29.9:
        st.error("sobre peso")
    elif imc 34.9:
        st.error("obesidade grau 1")
    elif imc 39.9:
         st.error("obesidade grau 2")
    elif imc > 40.0:
         st.error("CUIDADO, risco de morte")
