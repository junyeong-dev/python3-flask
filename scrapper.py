import requests
from bs4 import BeautifulSoup

# 마지막 페이지를 가져옴
def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pager = soup.find("div", {"class": "s-pagination"}).find_all("a")
    # print(pager)
    last_page = pager[-2].get_text(strip=True)
    return int(last_page)

def extract_job(html):
    title = html.find("h2").find("a")["title"]
    company, location = html.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip("\r").strip("\n")
    job_id = html['data-jobid']
    return {
        'title': title,
        'company': company,
        'location': location,
        'apply_link': f"https://stackoverflow.com/jobs/{job_id}"
    }

def extract_jobs(last_page, url):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Page: {page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(keyword):
    url = f"https://stackoverflow.com/jobs?q={keyword}&pg=1"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page, url)
    return jobs