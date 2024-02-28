import pandas as pd
import stats.time_stats as time_stats
import stats.station_stats as station_stats
import stats.trip_duration as trip_duration
import stats.user_stats as user_stats
import dt_time.filter_by_date as filter_by_date

CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv' 
    }
    
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def view_more_lines_decision(df):
    """Display table data by city."""
    starting_number_of_lines = 5
    print(df.head(starting_number_of_lines))
    view_more_lines = input("\n Would you like to view more lines? Enter yes or no: \n")

    # Show table data in increments of 5.
    while view_more_lines.lower() == 'yes':
        starting_number_of_lines += 5

        if starting_number_of_lines >= len(df):
            break

        print(df.head(starting_number_of_lines))
        view_more_lines = input("\n Would you like to view more lines? Enter yes or no: \n")

    print('-'*40)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        city: name of the city to analyze
        month: name of the month to filter by, or "all" to apply no month filter
        day: name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get a valid city name.
    city = input("Enter a city (chicago, new york city or washington): ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Input not valid. City must be chicago, new york city or washington: ').lower()

    # Get a valid month of the year.
    month = input("Enter a month (all, january, february, ...): ").lower()
    while month not in months and month != 'all':
        month = input("Enter a valid month of the year between january and june: ")

    # Get a valid day of the week.
    day = input ("Enter day of the week (all, monday, tuesday, ..., sunday): ").lower()
    while day not in days and day != 'all':
        day = input("Enter a valid day of the week like all, monday, tuesday, ..., sunday: ")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        city: city to analyze
        month: month to filter by, or "all" to apply no month filter
        day: day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # Convert the birth year to int for all cities but Washington.
    if city != 'washington':
        df['Birth Year'] = df['Birth Year'].astype('Int64')

    filter_by_date.filter_by_month(df, month, months)
    filter_by_date.filter_by_day(df, day)

    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        view_more_lines_decision(df)

        print('-'*40)
        time_stats.get_time_stats(df)
        station_stats.get_station_stats(df)
        trip_duration.get_trip_duration_stats(df)
        user_stats.get_user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
