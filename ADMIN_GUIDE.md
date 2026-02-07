# Flex-Check Pro - Admin User Guide

This guide is designed to help administrators effectively manage student rosters, track class attendance, and handle data using Flex-Check Pro.

## 1. Getting Started

### Install App Icon (Add to Home Screen)
For quick access, you can add Flex-Check Pro to your device's home screen like a native app.

**iPhone / iPad (Safari):**
1. Open the app link in **Safari**.
2. Tap the **Share** icon (square with arrow up) at the bottom or top.
3. Scroll down and tap **Add to Home Screen**.
4. Tap **Add**.

**Android (Chrome):**
1. Open the app link in **Chrome**.
2. Tap the **Menu** icon (three dots) at the top right.
3. Tap **Install app** or **Add to Home Screen**.
4. Follow the prompt to install.

### Initial Setup
When you first launch the application, you must set up the admin account to secure the Roster data.
1.  Click on the **ROSTER** tab.
2.  You will see the **Setup Admin** screen.
3.  **Create Password**: Enter a secure password and confirm it.
4.  **Security Question**: Select a question and provide an answer.
    *   *Important*: This is the **only** way to reset your password if you forget it without losing data.
5.  Click **CREATE ACCOUNT**.

### Logging In
1.  Click on the **ROSTER** tab.
2.  Enter your password and click **UNLOCK**.

---

## 2. Student Management

### Adding Students (Bulk Import)
1.  In the **ROSTER** tab, click the **+ BULK IMPORT** button.
2.  In the text box, enter student names, one per line.
    *   Format: `First Last` (e.g., `John Smith`) or `Last, First` (e.g., `Smith, John`).
3.  Click **IMPORT LIST**.
4.  **Duplicate Handling**:
    *   If a name already exists, the system will pause and ask:
        *   **OK**: Import the new student with a number suffix (e.g., "John Smith 2").
        *   **Cancel**: Skip this student (useful if they are already in the system).
5.  A summary will appear showing how many students were added or skipped.

### Editing Student Details
1.  In the **ROSTER** list, click on a student's name to open their profile.
2.  **Edit Name**: Click directly on the First Name or Last Name text at the top to type a new name.
    *   *Note*: If you try to change a name to one that already exists, the system will alert you and revert the change to prevent duplicates.
3.  **Contact Info**: Update **Parent Email** or **Parent Phone**. The system saves automatically when you click away.

### Deactivating vs. Deleting
*   **Deactivate (Recommended)**:
    *   Toggle the **Active/Inactive** button in the student profile.
    *   Inactive students are **hidden** from the Check-In search but their history and balance are preserved.
    *   Useful for students taking a break.
*   **Delete (Permanent)**:
    *   Click **DELETE STUDENT ACCOUNT** at the bottom of the profile.
    *   **Warning**: This permanently removes the student and **all their class history**. This cannot be undone unless you have a backup.

---

## 3. Class Management

### Adding Classes (Refill)
When a parent pays for a new package of classes:
1.  Open the student's profile in **ROSTER**.
2.  Locate the **Add Classes** section.
3.  Select the type (e.g., "Refill" or "Adjustment").
4.  Enter the number of classes (e.g., `10` or `20`).
5.  Click **ADD**.
6.  The **Classes Left** balance will update immediately.

### Fixing Mistakes (Adjustments)
If you added too many classes or need to correct a balance:
1.  Use the **Add Classes** section.
2.  Enter a **negative number** (e.g., `-1`) to deduct classes manually.
3.  Select "Adjustment" as the description.

### Viewing History
*   Scroll to the bottom of the student profile to see **Class History**.
*   This shows a chronological list of every Check-In (-1) and Deposit (+X), along with the date and time.

---

## 4. Daily Operations

### The Check-In Process
1.  Go to the **CHECK-IN** tab.
2.  Type the student's name in the search bar.
3.  Click the black **CHECK IN** button next to their name.
4.  **Result**:
    *   The system deducts **1 Class**.
    *   The student card turns gray, shows "Checked In", and moves to the bottom of the list.

### Daily Reports
1.  Go to the **ROSTER** tab and log in.
2.  The **Daily Report** section is at the top.
3.  **Date Selection**: Use the date picker to view history for past days.
4.  **Summary**:
    *   The title shows the total count (e.g., **Daily Report 15**).
    *   The list shows every student who checked in that day, their check-in time, and their current remaining classes.

---

## 5. Data & Export

### Excel Export
Useful for end-of-month reporting or external analysis.
1.  In **ROSTER**, scroll to the **Data Management** section at the bottom.
2.  Click the green **EXPORT TO EXCEL** button.
3.  A file named `FlexCheck_Export_YYYY-MM-DD.xlsx` will download.
    *   **Students Tab**: Lists all students, active status, contact info, and current balance.
    *   **Transactions Tab**: Lists every single transaction history record.

### Backup & Restore
**Crucial for data safety.** Since this app lives in your browser, clearing your browser cache will delete the data.
1.  **Backup**: Click **DOWNLOAD BACKUP** regularly (e.g., weekly). Save the `.json` file to a secure location (Google Drive, USB, etc.).
2.  **Restore**:
    *   Click **RESTORE BACKUP**.
    *   Select your `.json` file.
    *   **Warning**: This merges the backup data with your current data.

---

## 6. Troubleshooting

### I forgot my Admin Password
1.  On the login screen, click **Forgot Password?**.
2.  Answer the Security Question you set up.
3.  If correct, you can create a new password immediately.

### I cleared my browser cache / "App Reset"
If you cleared your browser data, the app will look like it's brand new.
1.  If you have a **Backup (.json)** file:
    *   Complete the "Setup Admin" process with a temporary password.
    *   Go to **Data Management** and use **RESTORE BACKUP** to reload your data.
2.  If you do **not** have a backup, the data is lost permanently. **Please backup regularly.**
