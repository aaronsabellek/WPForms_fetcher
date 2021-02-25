##!/usr/bin/env/ python3

#simple python script to fetch and save contact details (name, e-mail adresse and time)
#using the WordPress-application WPForms (https://wpforms.com/)
#by Aaron Sabellek


from imap_tools import MailBox, AND
import csv


#create list for all new contact details
data_list = []


#login to e-mail account using imap
with MailBox("imap.gmx.com").login("example@gmx.de", "password") as mailbox:

    #fetch unseen e-mails from mailbox in for loop
    for msg in mailbox.fetch(AND(seen=False)):

        #filter e-mails with specific subject used by the contact form
        if msg.subject == "Neue Anmeldung":

            #create list for contact details
            email_data = []

            #filter html content
            html_mail = msg.html

            #split html content to get the name and append it to email_data
            raw_mail = html_mail.split('<td style="color:#555555;padding-top: 3px;padding-bottom: 20px;">')
            name = raw_mail[1].split("</td>")[0]
            email_data.append(name)

            #split raw mail to get the e-mail address and append it to email_data
            raw_address = raw_mail[2].split('href="mailto:')
            address = raw_address[1].split('">')[0]
            email_data.append(address)

            #split datetime to get the date and append it to email_data
            date_split = msg.date_str.split(" ")
            date_list = date_split[1], date_split[2], date_split[3]
            date = " ".join(date_list)
            email_data.append(date)

            #append email_data to data_list
            data_list.append(email_data)


#append data from data_list to text file in csv format
with open('example.txt', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for email_data in data_list:
        csv_writer.writerow([email_data[0], email_data[1], email_data[2]])


#print data from data_list if there is any
if data_list != []:
    counter = 1
    print('Appended data:')
    print('Name, E-Mail, Time')
    for email_data in data_list:
        print(str(counter) + '. ' + email_data[0], email_data[1], email_data[2], sep=', ')
        counter += 1
else:
    print('No new data')


#print total number of rows in text file
with open('example.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    counter = 0
    for row in csv_reader:
        counter += 1
    print('total number of entries:', str(counter - 1))

            
            

        

