import requests
from bs4 import BeautifulSoup
import re
import math
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Connection": "keep-alive",
}

r = requests.get("https://www.50yc.com/shenzhen/ov1", headers=headers) 
print(r.text)