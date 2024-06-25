# Command Execution WebApp

Welcome to the **Command Execution WebApp**! This project allows users to run commands on the server and view the output in real-time through a web interface. The web application is built using HTML, CSS, JavaScript, and Python CGI scripts.

![Demo](screenshots/demo.png)

## Features

- Execute server commands from a web interface
- Real-time output display
- Animated gradient background
- Modern and clean design

## Technologies Used

- **HTML5**: For the web page structure
- **CSS3**: For styling and animations
- **JavaScript**: For client-side logic and AJAX requests
- **Python**: For server-side command execution using CGI

## Getting Started

### Prerequisites

- A web server (e.g., Apache)
- Python 3
- Basic knowledge of HTML, CSS, JavaScript, and Python

### Installation

1. **Clone the Repository**:

    ```sh
    git clone git@github.com:dilip8700/command-execution-webapp.git
    cd command-execution-webapp
    ```

2. **Setup the Web Server**:
   - Ensure your web server is configured to run CGI scripts.
   - Update your Apache configuration to allow CGI execution.

    ```apache
    ScriptAlias /cgi-bin/ /path/to/your/repository/cgi-bin/
    <Directory "/path/to/your/repository/cgi-bin">
        AllowOverride None
        Options +ExecCGI
        AddHandler cgi-script .cgi .py
        Require all granted
    </Directory>
    ```

3. **Deploy the Files**:
   - Copy the HTML, CSS, and JavaScript files to your web server’s document root (e.g., `/var/www/html/`).
   - Copy the Python CGI script to the `cgi-bin` directory within your repository.

    ```sh
    cp html/index.html /var/www/html/
    cp html/style.css /var/www/html/
    cp html/script.js /var/www/html/
    cp cgi-bin/command_exec.py /path/to/your/repository/cgi-bin/
    chmod +x /path/to/your/repository/cgi-bin/command_exec.py
    ```

4. **Restart the Web Server**:

    ```sh
    sudo systemctl restart apache2
    ```

### Usage

1. Open your web browser and navigate to `http://your_server_ip/index.html`.
2. Enter a command in the input field and click "Run".
3. View the command output displayed on the page.

## Directory Structure

```plaintext
command-execution-webapp/
├── html/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── cgi-bin/
    └── command_exec.py


