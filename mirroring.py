import logging
import os
import subprocess

LOGS_DIR = "./logs"
URLS_FILE_PATH = "./sample-input.txt"  # Load URLs from this text file
BASH_SCRIPT_PATH = "./mirroring.sh"

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

def load_urls(file_path):
    """Loads a list of unique URLs from a text file."""
    try:
        with open(file_path, 'r') as file:
            urls = {line.strip() for line in file if line.strip()}  # Use a set to remove duplicates
        return list(urls)
    except FileNotFoundError:
        logging.error(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    url_list = load_urls(URLS_FILE_PATH)
    
    logging.info(url_list)
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
