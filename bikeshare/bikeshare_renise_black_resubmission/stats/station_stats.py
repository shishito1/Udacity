import time

def get_station_stats(df):
    """Display statistics on the most popular stations."""  
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Most common start station: ', df['Start Station'].mode()[0])
    print('Most commonly used end station: ', df['End Station'].mode()[0])

    # Find most common start and end station combination.
    print('\n')
    frequent_start_end_station = df[['Start Station', 'End Station']].mode(axis=0)
    print('Most frequest start and end station combination:')
    for station in frequent_start_end_station:
        print(f"{station}: {frequent_start_end_station[station].to_string(index=False)}")

    print("\n\nThis took {} seconds.".format(time.time() - start_time))
    print('-'*40)
    