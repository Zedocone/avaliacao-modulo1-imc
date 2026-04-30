import streamlit as st

st.title("calculadora IMC 📱")
st.subheader("feito com streamlit betinha mogado 🤣")

altura = st.number_input("digite a sua altura", min_value=0.0)
peso = st.number_input("digite o seu peso",min_value=0.0)

if st.button("calcular"):
    imc = peso / altura ** 2
    if imc < 18.5:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwyMUegwx-DTXnZ-H2pl0tC3eW-SDfba_u9w&s", width=150)
        st.error("abaixo do peso")
    elif imc < 24.9:    
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3vir_HIlJ-I_NCY8rHwaIa_M002KG4Ofo1g&s", width=150)
        st.success("na media paizao")