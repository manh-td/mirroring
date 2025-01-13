# URL Mirroring Application

This application processes a JSON file containing commit URLs, extracts unique repository URLs, and executes a bash script (mirroring.sh) for each URL. It uses Python for data processing and logging.

---

## Features

- Loads JSON data containing commit URLs.
- Extracts unique repository URLs from the JSON.
- Executes a bash script (mirroring.sh) for each URL.
- Logs all actions and errors to both a log file and the console.

---

## Prerequisites

1. **Python 3.7 or higher**  
   Ensure Python is installed on your system.  
   [Download Python](https://www.python.org/downloads/)
   > Tested on Python 3.12.2

2. **Bash**
    The application executes a bash script (`mirroring.sh`). Ensure bash is installed and accessible.

3. **JSON Data File**  
   JSON file with the following structure:
   ```json
    [
        {
            "commit_URL": "https://github.com/user/repo/commit/abc123",
            "other_field": "content"
        },
        {
            "commit_URL": "https://github.com/user/repo/commit/abc123",
            "other_field": "content"
        },
    ]
   ```

---

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/manhtdd/mirroring.git
   cd mirroring
   ```

3. **Run the Application**:
   ```bash
   python -m main
   ```

---

## Configuration

### Environment Variables
- `DATA_PATH`: Path to the JSON file containing commit URLs.
- `LOGS_DIR`: Directory where logs will be stored (default: `./logs`).
- `BASH_SCRIPT_PATH`: Path to the bash script to execute (default: `./mirroring.sh`).

### Logging
- Logs are stored in the `logs/mirroring.log` file.
- Logs include timestamp, log level, function name, line number, and messages.

---

## Bash Script (mirroring.sh)

Ensure the `mirroring.sh` script is executable:
```bash
chmod +x mirroring.sh
```

Replace `<github-token>` with your PAT & `<username>` with your username:
```bash
#!/bin/bash

NEW_REPO_URL="https://<username>:<github-token>@gitlab.com/<username>/$OLD_REPO_NAME.git" # Replace with your new repo URL
```

---

## Example JSON Data

Save the following JSON in a file (e.g., `data.json`):
```json
[
    {"commit_URL": "https://github.com/user/repo/commit/abc123"},
    {"commit_URL": "https://github.com/user/repo/commit/def456"},
    {"commit_URL": "https://github.com/another/repo/commit/ghi789"}
]
```

---