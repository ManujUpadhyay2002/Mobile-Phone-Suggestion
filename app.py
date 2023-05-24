import streamlit as st
import pandas as pd

df = pd.read_csv('./Data/mobile_price_data.csv')

st.title('Mobile Phone Suggestion')

price = st.selectbox(
    'Select Price Range : ',
    ('₹6000-₹10000', '₹10000-₹15000', '₹15000-₹20000', '₹20000-₹30000', '₹30000-₹40000', '₹40000-₹50000', '₹50000-₹60000'))

mn, mx = [eval(i) for i in price.replace('₹', '').split('-')]
df.iloc[:, 1] = df.iloc[:, 1].apply(
    lambda x: int(x.replace('₹', '').replace(',', '')))

# Filtering
ff = df[df['mobile_price'] >=
        mn][df[df['mobile_price'] >= mn]['mobile_price'] <= mx]
a = ff['int_memory'].unique()

memory = st.selectbox(
    'Select Memory : ',
    (a)
)

ff = ff[ff['int_memory'] == memory]
a = ff['ram'].unique()

ram = st.selectbox(
    'Select Ram : ',
    (a)
)
ff = ff[ff['ram'] == ram]
a = ff['battery_power'].unique()

battery = st.selectbox(
    'Select Battery : ',
    (a)
)

ff = ff[ff['battery_power'] == battery]
a = ff['p_cam'].unique()

b_cam = st.selectbox(
    'Select Back Camera : ',
    (a)
)

ff = ff[ff['p_cam'] == b_cam]
a = ff['f_cam'].unique()

f_cam = st.selectbox(
    'Select Front Camera : ',
    (a)
)

ff = ff[ff['f_cam'] == f_cam]
ff['mobile_name'] = ff['mobile_name'].apply(lambda x: x.split('(')[0].strip())

if st.button('Get Mobiles'):
    for i in ff['mobile_name'].unique():
        name = i
        colors = pd.DataFrame(ff.groupby('mobile_name'))[
            1][0]['mobile_color'].values
        detail = pd.DataFrame(ff.groupby('mobile_name'))[1][0][['dual_sim', 'disp_size', 'resolution', 'os', 'num_cores', 'mp_speed', 'int_memory',
                                                                'ram', 'p_cam', 'f_cam', 'network', 'battery_power', 'mob_width', 'mob_height', 'mob_depth', 'mob_weight']].drop_duplicates()
        detail.rename(columns={'dual_sim': 'Sim Type', 'disp_size': 'Display Size', 'resolution': 'Resolution', 'os': 'Operating System', 'num_cores': 'Cores', 'mp_speed': 'Processor Speed', 'int_memory': 'ROM', 'ram': 'RAM', 'p_cam': 'Back Camera',
                      'f_cam': 'Front Camera', 'network': 'Network', 'battery_power': 'Battery Power', 'mob_width': 'Mobile Width', 'mob_height': 'Mobile Height', 'mob_depth': 'Mobile Depth', 'mob_weight': 'Mobile Weight'}, inplace=True)
        st.write('Mobile : ', name)
        st.write('Colors : ', colors[0])
        for j, k in detail.items():
            st.write(j, " : ", k.values[0])
