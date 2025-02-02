import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Judul Dashboard
st.title('Dashboard Analisis Penyewaan Sepeda')

# Menambahkan logo di sidebar
st.sidebar.image("bike.png")

# Membaca data
day_df = pd.read_csv('day.csv')
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Pra-pemrosesan data untuk pertanyaan 2
day_df['is_weekend'] = day_df['weekday']
day_df['is_holiday'] = day_df['holiday']
day_df['day_type'] = day_df['is_weekend'].astype(str) + day_df['is_holiday'].astype(str)
day_df['day_type'] = day_df['day_type'].map({'00': 'Weekday', '01': 'Holiday', '10': 'Weekend', '11': 'Weekend and Holiday'})

# Filter di sidebar
st.sidebar.header('Filter')
start_date = st.sidebar.date_input("Tanggal Awal", day_df['dteday'].min())
end_date = st.sidebar.date_input("Tanggal Akhir", day_df['dteday'].max())

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

season_mapping = {1: 'Spring', 2:'Summer', 3: 'Fall', 4:'Winter'}
day_df['season'] = day_df['season'].map(season_mapping)

season_options = day_df['season'].unique()
selected_season = st.sidebar.multiselect("Pilih Musim", season_options, default=season_options)


# Memfilter data
filtered_df = day_df[(day_df['dteday'] >= start_date) & (day_df['dteday'] <= end_date)]
filtered_df = filtered_df[filtered_df['season'].isin(selected_season)]

# Pertanyaan 1: Pengaruh Cuaca Terhadap Penyewaan Sepeda
st.header('Pengaruh Cuaca Terhadap Penyewaan Sepeda')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=filtered_df, ax=ax1)
plt.title('Pengaruh Cuaca Terhadap Penyewaan Sepeda')
plt.xlabel('Cuaca')
plt.ylabel('Jumlah Penyewaan')
plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig1)

# Pertanyaan 2: Perbedaan Jumlah Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan
st.header('Perbedaan Jumlah Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='day_type', y='cnt', data=filtered_df, order=['Weekday', 'Weekend'], ax=ax2)
plt.title('Perbandingan Jumlah Penyewaan Sepeda pada Hari Biasa, Akhir Pekan')
plt.xlabel('Jenis Hari')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig2)