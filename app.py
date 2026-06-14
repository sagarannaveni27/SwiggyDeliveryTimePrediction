import streamlit as st
import pandas as pd
import pickle

st.title('Swiggy Delivery Time Prediction')
st.image(r'https://miro.medium.com/v2/resize:fit:1400/1*fE3JkGyzhWXlXApVnShDtw.gif')

with open(r'model.pkl', 'rb') as file:
    Model = pickle.load(file)

df = pd.read_csv(r'swiggy cleaned_data.csv')

#input
Age = st.number_input('Enter age', min_value=18, max_value=50)
Ratings = st.slider('Enter the rating', 1.0, 5.0, 4.0, 0.1)
Weather = st.selectbox('Enter weather type', df['weather'].unique())
Traffic = st.selectbox('Enter the traffic', df['traffic'].unique())
Vehicle_condition = st.selectbox('Enter the Vehicle_condition', df['vehicle_condition'].unique())
Type_of_order = st.selectbox('Enter the type of orde', df['type_of_order'].unique())
Multiple_drivers = st.selectbox('Enter the No.of drivers', df['multiple_deliveries'].unique())
City = st.selectbox('Enter City Name', df['city_name'].unique())
Day_of_week = st.selectbox('Enter the Day of week (lowercase)', ['saturday', 'friday', 'tuesday', 'monday', 'sunday', 'wednesday','thursday'])
Pickup_time = st.number_input('Enter Pickup time', min_value=1, max_value=20)
order_time_hour = st.number_input('Enter the order time', min_value=0, max_value=23)
order_time_of_day = st.selectbox('Enter the order time of day', df['order_time_of_day'].unique())
distance = st.number_input('Enter the distance', min_value=0, max_value=25)
type_of_vehicle = st.selectbox('Enter the type of vehicle', df['type_of_vehicle'].unique())
city_type = st.selectbox('Enter the city type', df['city_type'].unique())
Festival = st.radio('Enter Festival', df['festival'].unique(), horizontal= True)


input_data = pd.DataFrame({'age':[Age], 'ratings':[Ratings], 'weather':[Weather], 'traffic':[Traffic], 'vehicle_condition':[Vehicle_condition],
            'type_of_order':[Type_of_order], 'type_of_vehicle':[type_of_vehicle], 'multiple_deliveries':[Multiple_drivers], 'festival':[Festival],
            'city_type':[city_type], 'city_name':[City], 'order_day_of_week':[Day_of_week],
            'pickup_time_minutes':[Pickup_time], 'order_time_hour':[order_time_hour], 'order_time_of_day':[order_time_of_day],
            'distance':[distance]})


if st.button('Predict'):
    st.success(f' #### Time Taken in min { Model.predict(input_data)}')