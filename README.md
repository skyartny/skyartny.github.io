# Flex-Check Pro

Flex-Check Pro is a lightweight, offline-capable student check-in and roster management web application. It is designed to streamline the process of tracking student attendance, managing account balances, and keeping parents informed.

Built with a local-first architecture, it stores data instantly in your browser (IndexedDB).

## ✨ Key Features

### 📋 Check-In System
*   **Fast Search**: Instantly find students by name.
*   **One-Tap Check-In**: Checks students in and automatically deducts a configurable session fee (default $30).
*   **Visual Status**: Clear indicators for students who have already checked in or have a low balance.

### 🛡️ Admin Dashboard
*   **Secure Access**: Password-protected admin area with SHA-256 hashing.
*   **Easy Setup**: Simple first-time setup flow to create an admin password and security question.
*   **Password Recovery**:
    *   **Offline**: Reset password using your pre-set Security Question.
*   **Student Management**:
    *   View/Edit details (Name, Parent Email, Phone).
    *   **Active/Inactive Status**: Toggle student status to hide them from the check-in list without deleting data.
    *   **Transaction History**: Full ledger of check-ins and deposits with running balance.
    *   **Funds Management**: Deposit funds or make adjustments (supports negative values).
*   **Daily Reports**: View a chronological list of check-ins for any selected date, including parent contact info.
*   **Bulk Import**: Quickly add multiple students using a simple text format.

### ⚙️ Configuration & Data
*   **Custom Check-In Fee**: Set the default amount deducted per check-in directly from the admin panel.
*   **Local-First**: Works offline using Dexie.js (IndexedDB).
*   **Manual Backup/Restore**: Download a JSON backup of your data or restore from a file at any time.

## 🛠️ Tech Stack

*   **HTML5**
*   **Tailwind CSS** (via CDN for styling)
*   **Alpine.js** (via CDN for reactivity and state management)
*   **Dexie.js** (Wrapper for IndexedDB)

## 🚀 Setup & Installation

Since this is a static web application, it does not require a backend server.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/haijuncuny/haijuncuny.github.io.git
    cd haijuncuny.github.io
    ```

2.  **Run Locally:**
    You can use any static file server. For example, with Python:
    ```bash
    python3 -m http.server 8000
    ```
    Then open `http://localhost:8000` in your browser.

## 📖 Usage Guide

### 1. Initial Setup
*   When you first access the **ROSTER** tab, you will be asked to **Setup Admin**.
*   Create a secure password and answer a **Security Question** (required for offline recovery).

### 2. Adding Students
*   Go to **ROSTER** (enter your admin password).
*   Click **+ BULK IMPORT**.
*   Enter names (e.g., `John Doe` or `Doe, John`), one per line.
*   Click **IMPORT LIST**.

### 3. Managing Funds & Fees
*   **Set Check-In Fee**: Scroll to the bottom of the Roster tab ("Data Management"). Enter the desired amount (e.g., 25) and click **Save**.
*   **Add Funds**: Click on a student's name. Under **Deposit Funds**, select "Refill" or "Adjustment", enter amount, and click **ADD**.

### 4. Daily Check-In
*   Go to the **CHECK-IN** tab.
*   Type the student's name.
*   Click the black **CHECK IN** button.
*   The system will deduct the configured fee.

## 🔒 Security

*   **Admin Password**: Stored as a SHA-256 hash in the local database. It is **never** sent to the server in plain text.
*   **Data Privacy**: All data resides in your browser's local storage. No external database is used.

### ⚠️ How to Reset if Password is Lost (Clean IndexedDB)

If you forget your Admin Password and cannot recover it via the Security Question, you can **reset the application**. This will delete all local data, so only do this if you have a backup or are okay starting fresh.

#### Option 1: Using Chrome DevTools (Recommended)
1.  Open the application in your browser.
2.  Press **F12** (or `Cmd+Option+I` on Mac) to open Developer Tools.
3.  Go to the **Application** tab.
4.  In the left sidebar, under **Storage**:
    *   Click **Clear site data**.
    *   Click the **Clear site data** button.
5.  Reload the page. You will be prompted to setup a new Admin account.

#### Option 2: Programmatically (Console)
1.  Open the browser console (`F12` -> Console).
2.  Run the following command:
    ```javascript
    indexedDB.deleteDatabase("FlexCheck_V4").onsuccess = function() {
        localStorage.clear();
        location.reload();
    };
    ```
3.  The page will reload, and you can start fresh.

## 📄 License

This project is open-source and available under the MIT License.
