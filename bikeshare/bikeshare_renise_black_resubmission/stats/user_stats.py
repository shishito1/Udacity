import time

def get_user_stats(df, city):
    """Display bikeshare user statisticss."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Get total counts by user type.
    user_type_count = df['User Type'].value_counts().astype(int).apply('{:,d}'.format)
    print('Count by user type:')
    print(f'{user_type_count.to_string(header=False)}')

    # Get count by gender except Washington.
    print('\n')
    if city.title() != 'Washington':
        count_by_gender = df['Gender'].value_counts().astype(int).apply('{:,d}'.format)
        print('Count by gender:')
        print(f'{count_by_gender.to_string(header=False)}')
    
    # Get the earliest, latest and most common birth year except Washington.
    print('\n')
    if city.title() != 'Washington': 
        print('Earliest birth year: ', df['Birth Year'].min())
        print('Most recent birth year: ', df['Birth Year'].max())
        print('Most common birth year: ', df['Birth Year'].mode()[0])
        
        print('\n')
        number_under_thirty = len(df[df['Birth Year'] < 1994])
        print(f'Number of subscribers under 30: {number_under_thirty:,}')

        number_over_thirty = len(df[df['Birth Year'] >= 1994])
        print(f'Number of subscribers over 30: {number_over_thirty:,}')

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    