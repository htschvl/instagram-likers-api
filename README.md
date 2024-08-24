
# Instagram Likers API

This project is an API designed to interact with Instagram to retrieve data related to post likers. The goal is to provide a simple interface to fetch, process, and store information about users who liked specific posts on Instagram.

## Purpose

This project was developed as a means to study the Instagram API and to further enhance coding skills.

## Features

- **Fetch Likers**: Retrieve a list of users who liked a specific Instagram post.
- **Data Cleanup**: Scripts for cleaning and organizing retrieved data.
- **Output Storage**: Store the results in structured formats for further analysis.
- **Legacy Insights**: Documentation and scripts reflecting the evolution of the API and future considerations.

## Project Structure

```plaintext
instagram-likers-api/
├── .gitignore
├── cleanup.py
├── config/
├── legacy files and what was learnt studying this api plus future concerns/
├── output/
└── src/
```

- **`.gitignore`**: Lists files and directories that Git should ignore.
- **`cleanup.py`**: Python script for cleaning and processing data.
- **`config/`**: Placeholder for configuration files.
- **`legacy files and what was learnt studying this api plus future concerns/`**: Documentation and legacy code related to the API's development.
- **`output/`**: Directory where the API's output will be stored.
- **`src/`**: The main directory containing the API's source code.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)
- Instagram API access (ensure you have the necessary credentials)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/htschvl/instagram-likers-api.git
   cd instagram-likers-api
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Instagram API credentials by placing them in the `config/` directory.

### Usage

1. **Fetch Likers**:
   Run the main script to fetch likers of a specific Instagram post:
   ```bash
   python src/main.py --post-url <Instagram Post URL>
   ```

2. **Data Cleanup**:
   Use the `cleanup.py` script to clean and organize fetched data:
   ```bash
   python cleanup.py
   ```

### Output

Processed data will be stored in the `output/` directory. You can customize the output format as needed.

## License

This project is licensed under the AGPL-3.0 License. See the `LICENSE` file for details.
