import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago':'chicago.csv',
             'new york city':'new_york_city.csv',
             'washington':'washington.csv'}

def get_filters():

    # get input from user for city names:

    city_list = ['chicago','new york city','washington']
    month_list = ['all','january','february','march','april','may','june']
    day_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    city = input("Enter the name of the city from the given list whose data you would like to explore \n -> chicago \n -> new york city \n -> washington \n")

    while city.lower() not in city_list:
        print ('Ooops You entered a wrong input')

        city = input("Enter the name of the city from the given list whose data you would like to explore \n 1.chicago \n 2. new york city \n 3. washington \n")

    # get input from user for months:

    month = input("Enter the month from the given list \n -> january \n -> february \n -> march \n -> april \n -> may \n -> june \n -> all \n")

    while month.lower() not in month_list:

        print ("Ooops You entered a wrong input")

        month = input("Enter the month from the given list \n 1.january \n 2.february \n 3.march \n 4.april \n 5.may \n 6.june \n 7.all \n")
    # get input from user for days:
    day = input("Enter any day \n -> monday \n -> tuesday \n -> wednesday \n -> thursday \n -> friday \n -> saturday \n -> sunday \n -> all \n ")

    while day.lower() not in day_list:

        print ("Ooops You entered a wrong input")

        day = input("Enter any day \n 1.monday \n 2.tuesday \n 3.wednesday \n 4.thursday \n 5.friday \n 6.saturday \n 7.sunday \n 8.all \n")


    print ("-"*70)

    return city.lower(), month.lower(), day.lower()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable

    Args:
         (str) city - name of the city to analyze
         (str) month - name of the month to filter by , or "all" to apply no month filter
         (str) day - name of the day of week to filter by, or "all" to apply no day filter

     returns:
         df - pandas dataframe containing city data filtered by month and day
    """



    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day of week'] = df['Start Time'].dt.weekday_name

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':

        df = df[df['day of week'] == day.title()]

    return df

def time_stats(df):

    """ Displays Statistics regarding most frequent times of travel"""

    print ("\n Calculating The Most Frequent Times of Travel ...... \n")

    start_time = time.time()

    # Display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    most_common_month = df['month'].mode()[0]

    print ("The most common month is :",most_common_month)

    print ("\n")

    # display the most common day

    df['day of week'] = df['Start Time'].dt.weekday_name

    most_common_day_here = df['day of week'].mode()[0]

    print ("Most common day of week is :",most_common_day_here)

    # Display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    most_common_start_hour = df['hour'].mode()[0]

    print ("Most common start hour is :",most_common_start_hour)

    print ("\n This took %s seconds. " %(time.time() - start_time))

    print ("-"*70)


def station_stats(df):
    """ Display statistics regarding the most popular stations and trips """

    print ("\n Calculating the most common stations and trips .......\n")

    start_time = time.time()
    # Display the most commonly used start station

    common_start_station = df['Start Station'].mode()[0]

    print ("The most commonly used start station is :",common_start_station)
    # Display the most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print ("The most commonly used end station is :",common_end_station)

    print ("\n")

    # Display the most frequent combination of start and end station

    df['Combi'] = df['Start Station'] + "   " + df['End Station']

    most_popular_combi = df['Combi'].value_counts().idxmax(axis = 1)

    print ("The most frequent combination of start and end stations are :",most_popular_combi)

    print ("\n")

    print ("\n This took %s seconds " % (time.time() - start_time))

    print ("-"*70)

def trip_duration_stats(df):

    """ Display statistics on the total and average trip duration """

    print ("\n Calculating trip duration ......\n")

    start_time = time.time()

    # Display total travel time

    total_travel_time = df['Trip Duration'].sum()

    print ("The total time travelled is {} seconds ".format(total_travel_time))

    print ("\n")

    # Display mean travel time

    mean_travel_time = df['Trip Duration'].mean()

    print ("The mean travelled time is {} seconds".format(mean_travel_time))

    print ("-"*70)

def user_stats(df):
    """ Display statistics on bikeshare users """

    print ("\n Calculating User Stats ......\n")

    start_time = time.time()

    # Display counts of user types

    user_types_in = df['User Type'].value_counts()

    print (user_types_in)

    # Display counts of gender types

    try:
        gender_types_in = df['Gender'].value_counts()

        print (gender_types_in)

    except KeyError:
        print("This dataframe does not exist")

    # Display earliest , most recent and most common year of birth

    try:
        df.sort_values(by = ['Birth Year'],ascending = [0])

        print ("The earliest year of birth is :",int(df['Birth Year'].min()))

        print ("\n")

        print ("The most recent year of birth is ",int(df['Birth Year'].max()))

        print ("\n")

        common_year_of_birth = df['Birth Year'].mode()[0]

        print ("Most common birth year",int(common_year_of_birth))

    except:
        print ("This dataframe does not exist")

    print ("This took %s seconds. " %(time.time() - start_time))

    print ("-"*70)


def raw_data(city):

    df = pd.read_csv(CITY_DATA[city])

    N = int(input("Enter the number of rows u want to see from the raw data frame \n"))

    print (df.head(N))


def main():

    confirm = input("Looks like you are interested in exploring some US bikeshare data. Enter YES to proceed or enter any other key to quit\n")

    while confirm.lower() == 'yes':

        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        raw = input("do u want to see raw data frame ? enter YES to proceed . else enter any other key to quit. \n")


        if raw.lower() == 'yes':
            raw_data(city)


        restart = input("\n Would you like to restart . Enter YES or NO \n ")

        if restart.lower() != 'yes':

            break

if __name__ == "__main__":
    main()
