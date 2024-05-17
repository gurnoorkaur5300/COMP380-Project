# Hotel Reservation System

**Team Code Titans**: Gregory Calderon, Martin Gallegos Cordero, Gurnoor Kaur, Arameh Baghdasarian

## Overview

This project was developed for COMP 380: Introduction to Software Engineering at California State University, Northridge. It provides an automated system for managing hotel reservations.

### Prerequisites

Ensure that Python and SQLite are installed on your system for database management.

### Dependencies

Install the necessary Python packages using pip:

```bash
pip install pillow tk sqlite3
```

If you are on Windows, add `tkmacosx` for specific UI elements:

```bash
pip install tkmacosx
```

### Clone the Repository

```bash
git clone https://github.com/gurnoorkaur5300/COMP380-Project.git
cd COMP380-Project
```

## Usage

Run the system using:

```bash
python controller.py
```

This command launches the homepage where users can browse hotels, create accounts, or log in.

## System Requirements

- **Operating System**: Compatible with Mac OS and Windows.
- **Python**: Version 3.8 or newer.
- **Hardware**: Performance dependent on machine.

## Features

- Browse hotels and make reservations.
- Manage user accounts (both customer and admin).
- Secure password handling with SHA256 hashing.
