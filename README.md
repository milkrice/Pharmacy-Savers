# Pharmacy Savers
Gives you the lowest price for your medication. 

# Features
- Account system 
- Username and password validation 
- Brand and generic drug search 
- Filtering out drug strength  
- Outputs data for the drug at the lowest price 

# Video Demo 
[Pharmacy Savers Demo](https://youtu.be/dS19Le593vs?si=ZCMfzxE5wJe2wcaL)

# Files Used 
- popular_pricelist.xlsx 
- radiant_pricelist.xlsx
- square_pricelist.xlsx

All three files contain the drug data of three different pharmaceutical companies in Bangladesh, and are taken from the **Directorate General of Drug Administration (DGDA)**. 

The files make up the dataframe used in the project with information such as the generic and brand names of drugs, as well as their respective dosages and prices. 

Additional information can be found in the files, however they have been removed from the dataframe used in the project due to a lack of neccessity. 

# Requirements 
Download all the files for this project, then install *re* and *pandas* using the following commands
```
pip install -r requirements.txt

```

# Usage
Use the following command to run the project
```
python project.py
``` 
You will be asked to either sign up or login. When creating a new account, make sure that the username is between 4 to 12 characters and that the password is between 6 to 20 characters. The password must have at least 1 uppercase and lowercase letter, 1 number and 1 special character. 
For the drugs, you can put in either brand or generic drug names, it will not affect the output. However, names should be entered as 'Paracetamol' and not 'paracetamol'. Dosages should be entered as '500 mg' and not '500mg'.

# Libraries Used 
- *re* is used for password validation 
- *pandas* is used to make and search through dataframes 

# Exploring the Code 
Many decisions went into making this project so I have decided to add in a section explaining some of them. 

There are 4 functions in addition the main function. These include *users*, *passes*, *account*, and *medication*.

*Users, passes* and *account* functions work hand in hand. The *account* function is responsible for storing usernames and passwords from *users* and *passes* in a dictionary. This dictionary acts as the user database. Both *users* and *passes* functions validate input. *Account* ensures that the login information matches values in the user database, and that new accounts are stored in the user database. Whereas *users* and *passes* ensures that the usernames and passwords fit the set requirements. As mentioned before, password validation is done by using the *re* library. 
Originally, there were only 3 functions, however to meet the requirements set by *pytest*, I had to refactor my code. The original code can be found in the "unfactored_project.py" file.

The *medication* function was arguably the most difficult to deal with, since I had to figure out a source of data, and then sort and manipulate that data accordingly. As mentioned before, the **DGDA** allowed me to download drug data for 3 major pharmaceutical companies as excel sheets. By converting these sheets to dataframes and merging them together, I was able to create the main dataframe for the project. The dataframe contained both generic and brand names of drugs, and the user could input either one. Therefore I wrote 2 versions of code, one that checked for the generic name in the database, and one that checked for the brand name. However after inputting a brand name, the program would then have to find the generic name, so that all possible sources of this drug could be found, their prices compared, and the lowest price given to the user. As the course did not introduce *pandas* before, I was able to gain a lot of valuable knowledge regarding dataframes while working on the project. 