import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Would you like to see data for Chicago, New York City, or Washington?')
    city=input()
    while city.lower()!='chicago'and city.lower()!='new york city' and city.lower()!='washington': 
       print('option unavailable, Would you like to see data for Chicago, New York, or Washington?')
       city=input()
    print('would you like to filter for month or day or neither?')
    choice=input().lower()
    if(choice=='month'):
        print('which month would you like to filter to (all, january, february, ... , june)\n')
        month=input()
        months=["january", "february", "march", "april",
  "may", "june","all"]
        while month.lower() not in months: 
            print('option unavailable, which month would you like to filter to (all, january, february, ... , june)')
            month=input()
        day='all'
    
    else:
        if(choice=='day'):
            days=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday","all"]
            print('which day would you like to filter to (all, monday, tuesday, ... sunday)')
            day=input()
            while day.lower() not in days: 
                print('option unavailable, which day would you like to filter to (all, monday, tuesday, ... sunday)')
                day=input()
            month='all'
        else:
            month='all'
            day='all'
    print('')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print(f"the most common month is:{df['month'].mode()[0]}")
    # TO DO: display the most common day of week
    print(f"the most common day of the week is:{df['day_of_week'].mode()[0]}")
    # TO DO: display the most common start hour
    print(f"the most common start hour:{df['hour'].mode()[0]}")
    print("\nThis took %s seconds." % ((time.time() - start_time).round()))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"the most commonly used start station is:{df['Start Station'].mode()[0]}")

    # TO DO: display most commonly used end station
    print(f"the most commonly used End station is:{df['End Station'].mode()[0]}")

    df['combination']=df['Start Station']+' to '+df['End Station']
    # TO DO: display most frequent combination of start station and end station trip
    print(f"the most commonly used combination of start station and end station is:{df['combination'].mode()[0]}")
    print("\nThis took %s seconds." % ((time.time() - start_time).round()))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print(f"the total travel time in minutes:{(df['Trip Duration'].sum()/60).round()}")
    print(f"the total travel time in hours:{(df['Trip Duration'].sum()/3600).round()}")
    # TO DO: display mean travel time
    print(f"the average travel time:{(df['Trip Duration'].mean()).round()}")
    print("\nThis took %s seconds." % ((time.time() - start_time).round()))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"count of user types:{df.groupby(['User Type'])['User Type'].count()}")

    # TO DO: Display counts of gender
    try:
        print(f"count of user genders:{df.groupby(['Gender'])['Gender'].count()}")
        print(f"the oldest user's year of birth:{df['Birth Year'].max()}")
        print(f"the youngest user's year of birth:{df['Birth Year'].min()}")
        print(f"the most common year of birth:{df['Birth Year'].mode()[0]}")
    except KeyError:
        print('gender and birth year data for Washington is unavailable')
    

    # TO DO: Display earliest, most recent, and most common year of birth



    print("\nThis took %s seconds." % ((time.time() - start_time).round()))
    print('-'*40)

def display_rawdata(df):
    print('would you like to see raw data?')
    count=0
    answer=input()
    while (answer=='yes'):
        print(df[count:count+5])
        count=count+5
        print('would you like to see more of the raw data?')
        answer=input()
    
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rawdata(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
