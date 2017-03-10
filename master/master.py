import requests

from downloader import download

# Import and set logger
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

platform = 'A-AFFY-1'

# Files API endpoint for ArrayExpress
FILES_URL = "http://www.ebi.ac.uk/arrayexpress/json/v2/files"

parameters = {'raw': 'true', 'array': platform}

r = requests.get(FILES_URL, params=parameters)
response_dictionary = r.json()

try:
    experiments = response_dictionary['files']['experiment']
except KeyError: # If the platform does not exist or has no files...
    logger.info('No files were found with this platform accession code. ' +
                'Try another accession code.')

raw_file_urls = set([])

for experiment in experiments:
    data_files = experiment['file']

    # If there is only one file object in data_files, ArrayExpress does not
    # put it in a list of size 1 - This breaks the code if we attempt to
    # iterate over it like a list. The next section handles both cases.

    if (type(data_files) == list):
        for data_file in data_files:
            if (data_file['kind'] == 'raw'):
                url = data_file['url'].replace("\\", "")
                raw_file_urls.add(url)

    else:  # It is just one file object
        if (data_files['kind'] == 'raw'):
            url = data_files['url'].replace("\\", "")
            raw_file_urls.add(url)


for url in raw_file_urls:
    download.delay(url)
    break
