import numpy as np
import pandas as pd

swd_sheet = pd.read_csv(r"C:\Users\Vedant Dutta\Downloads\PHoEnix GB Merch Deductions.csv")
roll_nos = swd_sheet.loc[:,'ID']

final_ids = []
gen_emails = []

def split_id(roll_no):
    temp_arr = []
    for char in (roll_no):
        temp_arr.append(char)
    return temp_arr

# this function returns an array with the split up form of each row of the roll nos

def initial_roll_no_arr():
    initial_id = []
    for i in range(752):
        if (i == 0):
            continue
        initial_id.append(swd_sheet.loc[i,'ID'])

    first_arr = np.array(initial_id)
    first_arr.reshape(-1)
    return first_arr

# this function is being used to create a (752,1) dimension array of all the roll nos
def list2string(s):
    str1 = ''
    for char in s:
        str(char)
        str1 += char
    return str1

# this function is used to convert a certain list into a string
def main():
    batch_1 = [[], [], [], [], [], [], [], []]
    batch_2 = [[], [], [], [], [], [], [], []]
    temp_carr = np.empty([751,1], dtype=object)
    my_ids = initial_roll_no_arr()
    for i in range(751):
        if (split_id(my_ids[i]))[4] == 'B':
            batch_1[0] = '2'
            batch_1[1] = str((split_id(my_ids[i]))[1])
            batch_1[2] = str((split_id(my_ids[i]))[2])
            batch_1[3] = str((split_id(my_ids[i]))[3])
            batch_1[4] = str((split_id(my_ids[i]))[8])
            batch_1[5] = str((split_id(my_ids[i]))[9])
            batch_1[6] = str((split_id(my_ids[i]))[10])
            batch_1[7] = str((split_id(my_ids[i]))[11])
            final_ids.append(batch_1.copy())

        if (split_id(my_ids[i]))[4] == 'A':
            batch_2[0] = '2'
            batch_2[1] = str((split_id(my_ids[i]))[1])
            batch_2[2] = str((split_id(my_ids[i]))[2])
            batch_2[3] = str((split_id(my_ids[i]))[3])
            batch_2[4] = str((split_id(my_ids[i]))[8])
            batch_2[5] = str((split_id(my_ids[i]))[9])
            batch_2[6] = str((split_id(my_ids[i]))[10])
            batch_2[7] = str((split_id(my_ids[i]))[11])
            final_ids.append(batch_2.copy())

    for j in range(650):
        temp_carr[j] = list2string(final_ids[j])
        temp_carr[j] = "f" + list2string(final_ids[j]) + "@hyderabad.bits-pilani.ac.in"

    df = pd.DataFrame(temp_carr)
    df.to_csv(r"C:\Users\Vedant Dutta\email_ids.csv", header=False, index=False)

    # this part of the code is for generating proper sequence of all the email ids
main()