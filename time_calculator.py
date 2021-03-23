def add_time(start, duration,week_day = ""):


    simplified = start.replace(':', ' ').split()  # separates every element -> ['11', '06', 'PM']
    s_forward = duration.replace(':', ' ').split()  # separates every element -> ['2','02']

    hours = int(simplified[0]) # initial hours
    current = simplified[2]  # either 'AM' or 'PM'
    counter = 0
    is_day = int(s_forward[0])%24 == 0 # to check if multiple days
    number_days = int(s_forward[0])//24


    if (0 < int(simplified[0]) < 13 and 0 <= int(s_forward[0]) and
            0 <= int(simplified[1]) < 60 and 0 <= int(s_forward[1]) < 60):

        minutes = int(s_forward[1]) + int(simplified[1])  # gets total of minutes
        hours_sum = hours + int(s_forward[0])

        #check if minutes are more than 60 and if so consequently will add 1 hour
        if minutes >=60:

           hours+=1
           minutes = minutes % 60


           if hours >=12 and hours_sum>=12:
               hours = (hours + int(s_forward[0]))%12

               if current == 'AM':
                   current = 'PM'
               else:
                   # if PM and hours exceed turns to am which adds 1 day
                   counter = 1 + number_days
                   current = 'AM'

           elif hours >=12:
               hours = (hours + int(s_forward[0])) % 12

               if current == 'AM':
                   current = 'PM'
               else:
                   # if PM and hours exceed turns to am which adds 1 day
                   counter = 1 + + number_days # every time pm goes to am adds 1 day
                   hours = (hours + int(s_forward[0])) % 12
                   current = 'AM'

        elif hours_sum>=12:

            hours = hours % 12

            if current == 'AM' and is_day:
                current ='AM'
                counter = number_days

            elif current == 'PM' and is_day:
                current = 'PM'
                counter = number_days

            elif current == 'AM':
                current = 'PM'

            else: #if PM and hours exceed turns to am which adds 1 day
                counter=1 + number_days # every time pm goes to am adds 1 day
                hours = (hours + int(s_forward[0])) % 12
                current = 'AM'

        else:

            hours = hours_sum

        # checking how many days forward

        if counter == 1:
            next_day = ' (next day)'
            current = current + next_day
        elif counter > 1:
            n_days = f" ({counter} days later)"
            current = current + n_days

        if hours == 0:
            hours = 12


        new_time = f"{hours}:{minutes:0>2d} {current}"
        print(new_time)
        return new_time

    else:
        print("Please insert times in the correct format")





add_time("11:00 PM", "49:00")
#add_time("3:30 PM", "2:12", "Monday")