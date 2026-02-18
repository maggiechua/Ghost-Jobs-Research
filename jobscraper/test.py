import csv
from jobspy import scrape_jobs
import pandas as pd

jobs = scrape_jobs(
    site_name=["indeed", "linkedin"], # "glassdoor", "bayt", "naukri", "bdjobs"
    search_term="software engineer",
    location="Boston, MA",
    results_wanted=100,
    hours_old=24,
    country_indeed='USA',
    
    linkedin_fetch_description=True, # gets more info such as description, direct job url (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
)
print(f"Found {len(jobs)} jobs")
jobs.to_csv("jobs.csv", quoting=csv.QUOTE_ALL, escapechar="\\", index=False) # to_excel
df = pd.read_csv("jobs.csv") # to_excel
print(df.columns.tolist())
print(df.shape)
print(df[['title', 'company', 'location', 'site', 'date_posted']].head(10))
