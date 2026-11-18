
Job Application Tracker

A web-based job application tracking system built using **Python, Flask and SQLite**. The application allows users to record job applications, view submitted applications and update their application status through a simple interface.

Features

- Add job applications with company name, job role and application date.
- View and manage saved job applications.
- Update application status across four stages: Applied, Interview, Rejected and Offered.
- Store application records in an SQLite database.
- Run the application inside a Docker container.
- GitHub Actions workflow for automated application checks.

Application Architecture

The application follows a simple Flask-based architecture with SQLite for data persistence.

```mermaid
flowchart TD
    A["User / Web Browser"] --> B["Flask Application - app.py"]

    B --> C["GET / - View Applications"]
    B --> D["GET /add - Display Form"]
    B --> E["POST /add - Save Application"]
    B --> F["POST /update/id - Update Status"]

    C --> G[("SQLite Database - jobs.db")]
    E --> G
    F --> G

    B --> H["Jinja Templates"]
    H --> I["index.html"]
    H --> J["add.html"]

    I --> A
    J --> A

    K["Static CSS"] --> A
```

Technology Stack

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![GitHub_Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)