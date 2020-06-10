import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

hotel_df = pd.read_csv("hotel_bookings.csv")
##Change categorical data----------------------------------
cleanup_nums = {"hotel": {"Resort Hotel": 0, "City Hotel": 1}}
hotel_df.replace(cleanup_nums, inplace=True)

cleanup_nums = {"meal": {"BB": 0, "SC": 1,"HB": 2,"Undefined":3,"FB": 4}}
hotel_df.replace(cleanup_nums, inplace=True)

cleanup_nums = {"market_segment": {"Online TA": 0, "Offline TA/TO": 1,"Groups": 2,"Direct": 3,"Corporate": 4,"Complementary": 5,"Aviation":6,"Undefined":7}}
hotel_df.replace(cleanup_nums, inplace=True)

cleanup_nums = {"distribution_channel": {"TA/TO": 0, "Direct": 1,"Corporate": 2,"GDS": 3,"Undefined": 4}}
hotel_df.replace(cleanup_nums, inplace=True)

cleanup_nums = {"reserved_room_type": {"A": 0, "B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G":6,"H":7,"L":8,"P":9}}
hotel_df.replace(cleanup_nums, inplace=True)

cleanup_nums = {"assigned_room_type": {"A": 0, "B": 1,"C": 2,"D": 3,"E": 4,"F": 5,"G":6,"H":7,"I":8,"K":9,"L":10,"P":11}}
hotel_df.replace(cleanup_nums, inplace=True)

cleanup_nums = {"customer_type": {"Transient": 0, "Transient-Party": 1,"Contract": 2,"Group": 3}}
hotel_df.replace(cleanup_nums, inplace=True)

cleanup_nums = {"reservation_status": {"Check-Out": 0, "Canceled": 1,"Contract": 2,"No-Show": 3}}
hotel_df.replace(cleanup_nums, inplace=True)

cleanup_nums = {"deposit_type":{"No Deposit": 0, "Non Refund":1,"Refundable": 2}}
hotel_df.replace(cleanup_nums, inplace = True)

hotel_df["agent"].fillna(0, inplace = True)
hotel_df['agent'][hotel_df['agent'] >= 1 ] = 1 

hotel_df["company"].fillna(0, inplace = True)
hotel_df['company'][hotel_df['company'] >= 1 ] = 1 

hotel_df["children"].fillna(0, inplace = True)

###
hotel_num_df=hotel_df[['hotel', 'is_canceled', 'lead_time', 'stays_in_weekend_nights',
       'stays_in_week_nights', 'adults', 'children', 'babies', 'meal', 'market_segment', 'distribution_channel',
       'is_repeated_guest', 'previous_cancellations',
       'previous_bookings_not_canceled', 'reserved_room_type',
       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',
       'company', 'days_in_waiting_list', 'customer_type', 'adr',
       'required_car_parking_spaces', 'total_of_special_requests',
       'reservation_status']]

sample_hotel_df = hotel_num_df.sample(n = 8763)

data=sample_hotel_df[['hotel', 'stays_in_weekend_nights',
       'stays_in_week_nights', 'adults', 'children', 'babies', 'meal', 'market_segment', 'distribution_channel',
       'is_repeated_guest', 'previous_cancellations',
       'previous_bookings_not_canceled', 'reserved_room_type',
       'assigned_room_type', 'booking_changes', 'deposit_type', 'agent',
       'company', 'customer_type',
       'required_car_parking_spaces', 'total_of_special_requests']]
target = sample_hotel_df['is_canceled']

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)

rf = RandomForestClassifier(n_estimators=250)
rf = rf.fit(X_train, y_train)

def predict(data):
	return rf.predict(data)

