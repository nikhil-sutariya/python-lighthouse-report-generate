import argparse
import json
import requests
import os
import time
from bs4 import BeautifulSoup

def get_reports(url):
    os.system("sudo rm -rf reports web_vitals")
    os.system("mkdir reports web_vitals")

    sitemap = requests.get(url)
    web_vitals = []

    soup = BeautifulSoup(sitemap.content, "xml")
    loc_tags = soup.find_all("loc")

    urls = [loc.text.strip() for loc in loc_tags]

    for url in urls:
        file_name = url.split("//")[1].replace('/', '-')
        if "http" in url:
            url = url.replace('http', 'https')
        command = f'lighthouse {url} --output json --output-path "/home/itaims/Desktop/projects/seo-tool/reports/{file_name}.json" --preset desktop --chrome-flags="--headless" --quiet --view'
        os.system(command)
        f = open(f'reports/{file_name}.json', encoding="utf-8")
        json_data = json.load(f)
        
        report_dict = {}

        try:
            report_dict['performance'] = json_data['categories']['performance']['score'] * 100
            report_dict['accessibility'] = json_data['categories']['accessibility']['score'] * 100
            report_dict['best_practices'] = json_data['categories']['best-practices']['score'] * 100
            report_dict['seo'] = json_data['categories']['seo']['score'] * 100
            report_dict['url'] = url
            # report_dict['pwa'] = json_data['categories']['pwa']['score'] * 100

        except Exception as e:
            report_dict['performance'] = 0.0
            report_dict['accessibility'] = 0.0
            report_dict['best_practices'] = 0.0
            report_dict['seo'] = 0.0
            report_dict['url'] = url
            # report_dict['pwa'] = 0.0
            report_dict['error'] = str(e)

        web_vitals.append(report_dict)

    with open(f"web_vitals/web_vitals.json", 'w') as outfile:
        json.dump(web_vitals, outfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True, help="URL for which to generate SEO reports")
    args = parser.parse_args()
    start_time = time.time()
    
    get_reports(args.url)
    end_time = time.time()
    execution_time = (end_time - start_time) / 60
    print(f"Execution completed in {execution_time:.2f} minutes.")
