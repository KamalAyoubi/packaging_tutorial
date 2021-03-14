import bike_3trauma

df = bike_3trauma.Load_db().save_as_df()
bike_3trauma.plot_location(bike_3trauma.get_accident(df))