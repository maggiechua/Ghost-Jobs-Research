import numpy as np
import datetime
import time
import csv
import os

from jobspy import scrape_jobs

# Variables for Platforms + Labor Markets
platforms = {
    # "L": "linkedin",
    "G": "glassdoor",
    # "I": "indeed"
}
markets = {
    "NY": "New York, NY" ,
    "MA": "Boston, MA",
}

# Creating data structures for sectors, occupations, and job titles
sectors = {
    "FI": "Finance & Insurance",
    "PST": "Professional, Scientific, and Technical Services",
    "IN": "Information",
    "RT": "Retail Trade",
    "HSA": "Healthcare & Social Assistance"
}

occupations = {
    # Finance & Insurance (FI)
    "SCFS": {"sector_id": "FI", "role": "Securities, Commodities, and Financial Services"},
    "ISA": {"sector_id": "FI", "role": "Insurance Sales Agent"},
    "FM": {"sector_id": "FI",  "role": "Financial Manager"},
    "FIA": {"sector_id": "FI",  "role": "Finance and Investment Analyst"},
    "PFA": {"sector_id": "FI",  "role": "Personal Financial Advisor"},
    "CSR-FI": {"sector_id": "FI",  "role": "Customer Service Representative"},

    # Professional Scientific Technical Services (PST)
    "AAA": {"sector_id": "PST", "role":  "Accountants and Auditors"},
    "SWE": {"sector_id": "PST", "role":  "Software Developer"},
    "MGA": {"sector_id": "PST", "role":  "Management Analyst"},
    "GOM-PST": {"sector_id": "PST", "role":  "General and Operations Manager"},
    "LAW": {"sector_id": "PST", "role":  "Lawyers"},
    "PLA": {"sector_id": "PST", "role":  "Paralegal and Legal Assistant"},

    # Retail Trade (RT)
    "RSP": {"sector_id": "RT", "role": "Retail Salesperson"},
    "CAH": {"sector_id": "RT", "role": "Cashier"},
    "STO": {"sector_id": "RT", "role": "Stockers and Order Fillers"},
    "SUP": {"sector_id": "RT", "role": "First-Line Supervisors of Retail Sales Workers"},
    "CSR-RT": {"sector_id": "RT", "role": "Customer Service Representative"},
    "GOM-RT": {"sector_id": "RT", "role": "General and Operations Manager"},

    # Healthcare and Social Assistance (HSA)
    "PCA": {"sector_id": "HSA", "role": "Home, Health, and Personal Care Aides"},
    "RN": {"sector_id": "HSA", "role": "Registered Nurse"},
    "NA": {"sector_id": "HSA", "role": "Nursing Assistant"},
    "MSA": {"sector_id": "HSA", "role": "Medical Secretaries and Administrative Assistants"},
    "MHC": {"sector_id": "HSA", "role": "Substance Abuse, Behavioral Disorder, and Mental Health Counselors"},
    "RIC": {"sector_id": "HSA", "role": "Receptionists and Information Clerks"},
    "MAS": {"sector_id": "HSA", "role": "Medical Assistant"},

    # Information (IN)
    "SRS": {"sector_id": "IN", "role": "Sales Representatives of Services"},
    "CIS": {"sector_id": "IN", "role": "Computer and Information Systems Manager"},
    "MRS": {"sector_id": "IN", "role": "Market Research Analysts and Marketing Specialists"},
    "CSA": {"sector_id": "IN", "role": "Computer System Analyst"},
    "SM": {"sector_id": "IN", "role": "Sales Manager"},
    "PAD": {"sector_id": "IN", "role": "Producers and Directors"},
    "ED": {"sector_id": "IN", "role": "Editor"},
}

job_titles = np.array([
    # Finance & Insurance
    {"jt_id": "ST", "occ_id": "SCFS", "title": "Securities Trader"},
    {"jt_id": "IB", "occ_id": "SCFS", "title": "Investment Banker"},
    {"jt_id": "ISA","occ_id": "ISA", "title": "Insurance Sales Agent"},
    {"jt_id": "FM", "occ_id": "FM", "title": "Financial Manager"},
    {"jt_id": "IA", "occ_id": "FIA", "title": "Investment Analyst"},
    {"jt_id": "FA", "occ_id": "FIA", "title": "Financial Analyst"},
    {"jt_id": "PFA","occ_id": "PFA", "title": "Personal Financial Advisor"},
    {"jt_id": "CSR","occ_id": "CSR-FI", "title": "Customer Service Representative"}, 

    # Professional Scientific Technical Services 
    {"jt_id": "ACT","occ_id": "AAA", "title": "Accountant"},
    {"jt_id": "AUD","occ_id": "AAA", "title": "Auditor"},
    {"jt_id": "SWE","occ_id": "SWE", "title": "Software Developer"},
    {"jt_id": "MC", "occ_id": "MGA", "title": "Management Consultant"},
    {"jt_id": "BA", "occ_id": "MGA", "title": "Business Analyst"},
    {"jt_id": "BC", "occ_id": "MGA", "title": "Business Consultant"},
    {"jt_id": "LAW", "occ_id": "LAW", "title": "Lawyer"},
    {"jt_id": "PLA", "occ_id": "PLA", "title": "Paralegal"},
    {"jt_id": "GM", "occ_id": "GOM-PST", "title": "General Manager"},
    {"jt_id": "OM", "occ_id": "GOM-PST", "title": "Operations Manager"},

    # Retail Trade
    {"jt_id": "RSP", "occ_id": "RSP", "title": "Retail Salesperson"},
    {"jt_id": "CAH", "occ_id": "CAH", "title": "Cashier"},
    {"jt_id": "SK", "occ_id": "STO", "title": "Stocker"},
    {"jt_id": "OF", "occ_id": "STO", "title": "Order Filler"},
    {"jt_id": "SUP", "occ_id": "GOM-RT", "title": "Supervisor"},
    {"jt_id": "DM", "occ_id": "GOM-RT", "title": "Department Manager"},
    {"jt_id": "CSR","occ_id": "CSR-RT", "title": "Customer Service Representative"},

    # Healthcare and Social Assistance
    {"jt_id": "PCA", "occ_id": "PCA", "title": "Personal Care Aide"},
    {"jt_id": "RN", "occ_id": "RN", "title": "Registered Nurse"},
    {"jt_id": "NA", "occ_id": "NA", "title": "Nursing Assistant"},
    {"jt_id": "MSC", "occ_id": "MSA", "title": "Medical Secretary"},
    {"jt_id": "AA", "occ_id": "MSA", "title": "Administrative Assistant"},
    {"jt_id": "MAS", "occ_id": "MAS", "title": "Medical Assistant"},
    {"jt_id": "MHC", "occ_id": "MHC", "title": "Mental Health Counselor"},
    {"jt_id": "SAC", "occ_id": "MHC", "title": "Substance Abuse Counselor"},
    {"jt_id": "REC", "occ_id": "RIC", "title": "Receptionist"},
    {"jt_id": "INC", "occ_id": "RIC", "title": "Information Clerk"},

    # Information Sector
    {"jt_id": "SRS", "occ_id": "SRS", "title": "Sales Representative"},
    {"jt_id": "CSM", "occ_id": "CIS", "title": "Computer Systems Manager"},
    {"jt_id": "ISM", "occ_id": "CIS", "title": "Information Systems Manager"},
    {"jt_id": "MRA", "occ_id": "MRS", "title": "Marketing Research Analyst"},
    {"jt_id": "MS", "occ_id": "MRS", "title": "Marketing Specialist"},
    {"jt_id": "CSA", "occ_id": "CSA", "title": "Computer System Analyst"},
    {"jt_id": "SM", "occ_id": "SM", "title": "Sales Manager"},
    {"jt_id": "PD", "occ_id": "PAD", "title": "Producer"},
    {"jt_id": "DI", "occ_id": "PAD", "title": "Director"},
    {"jt_id": "ED", "occ_id": "ED", "title": "Editor"},
])

current_dir = os.path.dirname(os.path.abspath(__file__))
date = datetime.datetime.now().strftime("%Y-%m-%d")

# function to scrape jobs across all labor markets and platforms
for m in markets:
    for j in job_titles:
        time.sleep(30) # delay for 30 seconds 
        for p in platforms:
            occ = j['occ_id']
            title = j['jt_id']
            sector = occupations[occ]['sector_id']

            # folder paths to place created file in correct local repository location
            folder_path = f"{current_dir}/raw data/{m}/{sector}/{j['occ_id']}"
            file_name = f"{m}-{sector}-{occ}-{title}-{p}-{date}.csv"
            full_path = os.path.join(folder_path, file_name)
            
            # web-scraping
            try:
                if p == "G":
                    if m == "NY":
                        msa = markets[m].split(",")[0].replace(" ", "-").lower()
                    else: 
                        msa = markets[m].split(",")[0]
                    
                    jobs = scrape_jobs(
                        site_name=[platforms[p]], 
                        search_term=j['title'],
                        location=msa,
                        results_wanted=168,
                        hours_old=52,
                        country_indeed='USA',
                        linkedin_fetch_description=True, # gets more info such as description, direct job url (slower)
                    )
                else:
                    if p == "L":
                        time.sleep(60)
                    msa = markets[m]
                    jobs = scrape_jobs(
                        site_name=[platforms[p]],
                        search_term=j['title'],
                        location=msa,
                        results_wanted=168,
                        hours_old=52,
                        country_indeed='USA',
                        linkedin_fetch_description=True, # gets more info such as description, direct job url (slower)
                    )
                
                # if folder does not exist in local directory, create folder
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # write scraped data to csv file
                if not jobs.empty:
                    jobs.to_csv(full_path, quoting=csv.QUOTE_ALL, escapechar="\\", index=False) # to_excel\

                # print status message
                print(f"Market: {m} Platform: {platforms[p]}  Jobs: {len(jobs)} Sector: {sector} Job Occ/Title: {occ}-{title}")
            except:
                print("Error faced when web scraping")
