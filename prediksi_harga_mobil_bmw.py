import pickle
import streamlit as st

model = pickle.load(open('prediksi_hargamobil_bmw.sav', 'rb'))

st.title('Perkiraan Harga Mobil')

year = st.number_input('Masukan Tahun Mobil')
mileage = st.number_input('Masukan KM Mobil') 
tax = st.number_input('Masukan Pajak Mobil') 
mpg = st.number_input('Masukan Konsumsi BBM Mobil') 
engineSize = st.number_input('Masukan Ukuran Mesin Mobil')

predict = ''

if st.button('Prediksi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Perkiraan Harga Mobil dalam Ponds : ', predict)