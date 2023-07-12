# fetch_and_save_contact_details
Simple **Python script to fetch and save contact details** (name, e-mail adresse and date) interacting with the WordPress application "WPForms" (https://wpforms.com/).

The script only works with contact forms created with WPForms. The contact form has to ask for name and e-mail adresse.

The script logs into an e-mail account, fetches the e-mails from the contact form and filters name, e-mail adresse and date.

There has to be a txt file in the same directory as the python script. The script saves the contact informations in that txt file in csv format like it can be seen in the file "example.txt". 

At last the script prints the new contact informations and the total number of entries in the txt file.
