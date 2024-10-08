
# Instagram Likers API

This project is an API designed to interact with Instagram to retrieve data related to post likers. The goal is to provide a simple interface to fetch, process, and store information about users who liked specific posts on Instagram.

## Purpose

This project was developed as a means to study the Instagram API and to further enhance coding skills.

## Features

- **Fetch Likers**: Retrieve a list of users who liked a specific Instagram post.
- **Data Cleanup**: Scripts for cleaning and organizing retrieved data.
- **Output Storage**: Store the results in structured formats for further analysis.
- **Legacy Insights**: Previous versions of the script, trying to get as atomic as possible. General study of Instagram's API.
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

3. Configure your Instagram API credentials by filling the .env example

### How to Get Credentials

1. Open a new browser tab to reset all session data.
2. Navigate to your Instagram profile.
3. Open the browser developer console (usually by pressing `F12` or `Ctrl+Shift+I`).
4. Go to the "Network" tab in the developer console.
5. Return to your Instagram feed.
6. Scroll down the feed a bit to load more posts.
7. Click on the "Likes" link/button under one of the posts.
8. Look for a "query" item.
9. Your credentials should be both on "header" and "cookies". Make sure they match the description on .env.example

## Query Example

Here is an example of the query process:

![Query Process](./media/query.jpg) 

## Credentials Example

Here is an example of what's inside the Query Process and the data you need.

![Data](./media/data.png) 


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
