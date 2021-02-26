# fetch_and_save_contact_details
Simple **Python script to fetch and save contact details** (name, e-mail adresse and time) interacting with the **WordPress application WPForms** (https://wpforms.com/).

The script logs into your e-mail account, fetches the e-mails from your contact form and filters name, e-mail adresse and time if the contact form asks for that information.
There has to be a txt file in the same directory as the python script. The script saves the contact informations in that txt file in csv format like it can be seen in the file "example.txt". 
At last the script prints the new contact informations and the total number of entries in the txt file.
