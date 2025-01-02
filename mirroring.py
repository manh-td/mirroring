import logging
import os
import json
import subprocess

LOGS_DIR = "./logs"
DATA_PATH = "dataset/all_java_160924.json"
BASH_SCRIPT_PATH = "mirroring.sh"

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
log_file_path = os.path.join(LOGS_DIR, 'mirroring.log')
logging.basicConfig(
    force=True,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

def load_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        logging.error(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        logging.error(f"Error: Failed to decode JSON. {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    data = load_json(DATA_PATH)

    url_list = []
    for datapoint in data:
        url = datapoint.get("commit_URL").split("/")[:-2]
        url = "/".join(url)
        if url not in url_list:
            url_list.append(url)

    logging.info(f"Number of unique URLs: {len(url_list)}")

    # Loop through the URL list and execute the script
    for url in url_list:
        try:
            logging.info(f"Executing {BASH_SCRIPT_PATH} with URL: {url}")
            result = subprocess.run(["bash", BASH_SCRIPT_PATH, url], capture_output=True, text=True)
            logging.info(f"Output:\n{result.stdout}")
            if result.stderr:
                logging.info(f"Error:\n{result.stderr}")
        except Exception as e:
            logging.error(f"Failed to execute script for {url}: {e}")
        logging.info("--------------------")
