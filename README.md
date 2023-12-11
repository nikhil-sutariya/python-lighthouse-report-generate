
# Lighouse like tool

The python function for getting website's lighthouse report of all pages using terminal by providing sitemap url of your website.

It will generate json file which contains web vitals report for all urls mentioned in the sitemap.xml
## Installation
### 1. Linux

```bash
npm install -g lighthouse

# Create python virtual environment
python3 -m venv venv

# Activate the python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```


## Run Locally

### 1. Linux

```bash
python3 seo_report.py --url https://example.com/sitemap.xml
```
