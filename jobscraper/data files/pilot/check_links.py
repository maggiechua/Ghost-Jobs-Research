from playwright.sync_api import sync_playwright
from seleniumbase import sb_cdp
import pandas as pd
import datetime
import random
import time
import re
import os

sb = sb_cdp.Chrome(locale="en")
endpoint_url = sb.get_endpoint_url()

# File Paths
current_dir = os.getcwd()
data_path = f"{current_dir}/data files/pilot/sample data"
ma_path = f"{data_path}/MA"
ny_path = f"{data_path}/NY"

# Data Structures
sectors = ["HSA", "PST", "RT", "IN", "FI"]
platforms = {"G": "glassdoor", "I": "indeed"}

occupations = {
    # Finance & Insurance (FI)
    # "SCFS": {"sector_id": "FI", "role": "Securities, Commodities, and Financial Services"},
    # "FM": {"sector_id": "FI",  "role": "Financial Manager"},
    # "FIA": {"sector_id": "FI",  "role": "Finance and Investment Analyst"},
    # "PFA": {"sector_id": "FI",  "role": "Personal Financial Advisor"},
    # "CSR-FI": {"sector_id": "FI",  "role": "Customer Service Representative"},

    # Healthcare and Social Assistance (HSA)
    # "PCA": {"sector_id": "HSA", "role": "Home, Health, and Personal Care Aides"},
    "RN": {"sector_id": "HSA", "role": "Registered Nurse"},
    "CNA": {"sector_id": "HSA", "role": "Nursing Assistant"},
    "MSA": {"sector_id": "HSA", "role": "Medical Secretaries and Administrative Assistants"},
    # "MAS": {"sector_id": "HSA", "role": "Medical Assistant"},

    # Professional Scientific Technical Services (PST)
    "AAA": {"sector_id": "PST", "role":  "Accountants and Auditors"},
    "SWE": {"sector_id": "PST", "role":  "Software Developer"},
    "MGA": {"sector_id": "PST", "role":  "Management Analyst"},
    "GOM-PST": {"sector_id": "PST", "role":  "General and Operations Manager"},
    "LAW": {"sector_id": "PST", "role":  "Lawyers"},

    # Retail Trade (RT)
    "RSP": {"sector_id": "RT", "role": "Retail Salesperson"},
    "CAH": {"sector_id": "RT", "role": "Cashier"},
    "STO": {"sector_id": "RT", "role": "Stockers and Order Fillers"},
    "CSR-RT": {"sector_id": "RT", "role": "Customer Service Representative"},
    "GOM-RT": {"sector_id": "RT", "role": "General and Operations Manager"},

    # Information (IN)
    "SRS": {"sector_id": "IN", "role": "Sales Representatives of Services"},
    "CIS": {"sector_id": "IN", "role": "Computer and Information Systems Manager"},
    "MRS": {"sector_id": "IN", "role": "Market Research Analysts and Marketing Specialists"},
    "PAD": {"sector_id": "IN", "role": "Producers and Directors"},
    "ED": {"sector_id": "IN", "role": "Editor"},
}

# resuable function to visit job posting and check if active
def check_link(url, platform):
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(endpoint_url)
        context = browser.contexts[0]
        page = context.pages[0]
        try:
            page.goto(url)
            sb.sleep(3)
            sb.solve_captcha()
            sb.sleep(1.5)

             # call platform-specific function to handle survival analysis check
            match platform: 
                case "glassdoor":
                    return glassdoor(page)
                case "linkedin":
                    return linkedin(page)
                case "indeed":
                    return indeed(page)
        except:
            return "blocked"

# handling glassdoor links
def glassdoor(page):
    pause = random.randint(30,90)
    expired = page.get_by_role("dialog", name="Job expired").all_inner_texts()
    sb.sleep(3)
    removed = page.get_by_text("Job is OOO").is_visible()
    sb.sleep(pause)

    if expired:
        return "expired"
    elif removed:
        return "removed"
    else:
        return "active"

# handling linkedin links - does not work
def linkedin(page):
    page.get_by_role("button", name="Dismiss").click()
    sb.sleep(3)
    save_button = page.get_by_role("button", name="Save the job").click()
    available = page.get_by_text("Join or sign in to find your next job").is_visible()
    sb.sleep(1.5)
    expired = page.get_by_text("No longer accepting applications").is_visible()

    if available:
        print(available)
        return "active"
    else:
        return "expired"

# handling indeed links
def indeed(page):
    expired = page.get_by_text("This job has expired on Indeed").is_visible()
    sb.sleep(3)
    removed = page.get_by_text("Return home").is_visible()
    pause = random.randint(30,90)
    time.sleep(pause)

    if expired:
        return "expired"
    elif removed:
        return "removed"
    else:
        return "active"

today = datetime.datetime.now().strftime("%Y-%m-%d")
today_date_obj = datetime.datetime.strptime(today, "%Y-%m-%d")

# BUG - data structure discontinuity in the loop
counter = 0
filepath = f"{current_dir}/data files/pilot/sample data/FI/FI_I_SCFS_sample.csv"        
links_df = pd.read_csv(filepath)
for i in range(len(links_df)):
    site = links_df.at[i, 'site']
    url = links_df.at[i, 'job_url']
    
    status = check_link(url, site)
    print(i, site, url, status)

    links_df.at[i, 'status'] = status
    links_df.at[i, 'last_checked_date'] = today

    date_posted = datetime.datetime.strptime(links_df.at[i, 'date_posted'], "%Y-%m-%d")
    listing_age = today_date_obj - date_posted
    days_old = str(listing_age).split(" ")[0]
    links_df.at[i, 'listing_age_days'] = int(days_old)

    weeks_old = int(days_old) // 7
    links_df.at[i, 'listing_age'] = weeks_old
    links_df.to_csv(filepath, index=False)
    pause = random.randint(30,90)
    time.sleep(pause)