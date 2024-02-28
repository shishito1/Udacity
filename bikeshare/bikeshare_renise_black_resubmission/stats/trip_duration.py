import time

def get_trip_duration_stats(df):
    """Display trip duration statistics."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Get the total, average and longest travel times.
    print('Total travel time: ', df['Trip Duration'].sum())
    print('\nAverage travel time: ', df['Trip Duration'].mean())
    print('\nLongest travel time: ', df['Trip Duration'].max())    

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    