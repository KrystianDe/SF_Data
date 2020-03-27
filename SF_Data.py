from simple_salesforce import Salesforce
from pandas import DataFrame
from pprint import pprint as pp

class SF_Data:

    def __init__(self):
        self.sf = Salesforce(username='username', password='password', security_token='security_Token', sandbox=True)

    def get_contacts(self):
        
        sf_contacts = self.sf.bulk.Contact.query("SELECT name, External_ID__c FROM Contact")

        data_frame = DataFrame(sf_contacts).iloc[:,  lambda df: [1, 2]]
        list_of_contacts = []

        list_of_names = data_frame['Name'].values
        list_of_ids = data_frame['External_ID__c'].values

        self.assign_Id_to_Contact(list_of_contacts, list_of_names, list_of_ids)

        return list_of_contacts


    def get_projects(self):
        sf_projects = self.sf.bulk.Main_Project__c.query("SELECT Name FROM Main_Project__c")

        data_frame = DataFrame(sf_projects).iloc[:,  lambda df: [1]]
        
        list_of_projects = data_frame['Name'].values
       
        return list_of_projects.tolist()

    def assign_Id_to_Contact(self, list_of_contacts, names, ids):

        for i in range(0, len(names)):
            contact = (names[i], ids[i])
            list_of_contacts.append(contact)


