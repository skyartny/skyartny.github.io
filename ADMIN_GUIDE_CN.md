# Flex-Check Pro - Admin User Guide (中文版)

本指南旨在帮助管理员使用 Flex-Check Pro 高效管理学生花名册、追踪出勤情况以及处理数据。

## 1. 开始使用 (Getting Started)

### 安装应用图标 (添加到主屏幕)
为了方便快速访问，您可以将 Flex-Check Pro 添加到设备的主屏幕，就像原生应用一样。

**应用网址:** [https://flexcheck.framedghosts.com/](https://flexcheck.framedghosts.com/)

**iPhone / iPad (Safari):**
1. 在 **Safari** 浏览器中打开上述应用链接。
2. 点击底部或顶部的 **分享** 图标 (带有向上箭头的方框)。
3. 向下滚动并点击 **添加到主屏幕** (Add to Home Screen)。
4. 点击 **添加** (Add)。

<img src="ios_install.png" width="300" alt="iOS 安装指南">

**Android (Chrome):**
1. 在 **Chrome** 浏览器中打开上述应用链接。
2. 点击右上角的 **菜单** 图标 (三个点)。
3. 点击 **安装应用** (Install app) 或 **添加到主屏幕** (Add to Home Screen)。
4. 按照提示完成安装。

<img src="android_install.png" width="300" alt="Android 安装指南">

### 初始设置
首次启动应用程序时，您必须设置管理员账户以保护花名册数据。
1.  点击 **ROSTER** (花名册) 标签页。
2.  您将看到 **Setup Admin** (设置管理员) 屏幕。
3.  **Create Password**: 输入并确认一个安全的密码。
4.  **Security Question**: 选择一个问题并提供答案。
    *   *重要提示*: 如果您忘记密码，这是找回账户且不丢失数据的 **唯一** 方法。
5.  点击 **CREATE ACCOUNT** (创建账户)。

### 登录
1.  点击 **ROSTER** 标签页。
2.  输入密码并点击 **UNLOCK** (解锁)。

---

## 2. 学生管理

### 批量添加学生 (Adding Students)
1.  在 **ROSTER** 标签页，点击 **+ BULK IMPORT** (批量导入) 按钮。
2.  在文本框中输入学生姓名，每行一个。
    *   格式: `First Last` (例如 `John Smith`) 或 `Last, First` (例如 `Smith, John`)。
3.  点击 **IMPORT LIST** (导入列表)。
4.  **处理重复**:
    *   如果姓名已存在，系统会暂停并询问：
        *   **OK**: 使用带编号的名称导入（例如 "John Smith 2"）。
        *   **Cancel**: 跳过此学生（如果他们已经在系统中）。
5.  系统会显示一个摘要，说明添加或跳过了多少学生。

### 编辑学生信息
1.  在 **ROSTER** 列表中，点击学生姓名以打开其个人资料。
2.  **编辑姓名**: 直接点击顶部的名字或姓氏文本即可输入新名称。
    *   *注意*: 如果您尝试更改为已存在的姓名，系统会提示并撤销更改，以防止重复。
3.  **联系信息**: 更新 **Parent Email** (家长邮箱) 或 **Parent Phone** (家长电话)。点击其他地方时系统会自动保存。

### 停用与删除 (Deactivating vs. Deleting)
*   **停用 (Active/Inactive - 推荐)**:
    *   在学生个人资料中切换 **Active/Inactive** 按钮。
    *   Inactive (停用) 的学生将从 Check-In 搜索中 **隐藏**，但其历史记录和余额将被保留。
    *   适用于暂时休学的学生。
*   **删除 (Permanent - 永久)**:
    *   点击个人资料底部的 **DELETE STUDENT ACCOUNT** (删除学生账户)。
    *   **警告**: 此操作将永久删除学生及其 **所有课时历史记录**。除非您有备份，否则无法撤销。

---

## 3. 课时管理

### 增加课时 (Adding Classes/Refill)
当家长支付新课包费用时：
1.  在 **ROSTER** 中打开学生个人资料。
2.  找到 **Add Classes** (增加课时) 部分。
3.  选择类型（例如 "Refill" 充值或 "Adjustment" 调整）。
4.  输入课时数（例如 `10` 或 `20`）。
5.  点击 **ADD** (增加)。
6.  **Classes Left** (剩余课时) 余额将立即更新。

### 修正错误 (Adjustments)
如果您添加了太多课时或需要手动更正余额：
1.  使用 **Add Classes** 部分。
2.  输入 **负数**（例如 `-1`）以手动扣除课时。
3.  选择 "Adjustment" 作为描述。

### 查看历史记录
*   滚动到学生个人资料底部以查看 **Class History** (课时历史)。
*   这显示了按时间顺序排列的每笔 Check-In (-1) 和 Deposit (+X)，以及日期和时间。

---

## 4. 日常操作

### 签到流程 (The Check-In Process)
1.  进入 **CHECK-IN** 标签页。
2.  在搜索栏中输入学生姓名。
3.  点击其姓名旁边的黑色 **CHECK IN** 按钮。
4.  **结果**:
    *   系统扣除 **1 课时**。
    *   学生卡变为灰色，显示 "Checked In"，并移至列表底部。

### 每日报告 (Daily Reports)
1.  进入 **ROSTER** 标签页并登录。
2.  **Daily Report** (每日报告) 部分位于顶部。
3.  **日期选择**: 使用日期选择器查看过去日期的记录。
4.  **摘要**:
    *   标题显示当天的总人数 (例如 **Daily Report 15**)。
    *   列表显示当天签到的每位学生、签到时间及其当前剩余课时。

---

## 5. 数据与导出

### Excel 导出 (Excel Export)
用于月底报告或外部数据分析。
1.  在 **ROSTER** 中，滚动到底部的 **Data Management** (数据管理) 部分。
2.  点击绿色的 **EXPORT TO EXCEL** 按钮。
3.  将下载名为 `FlexCheck_Export_YYYY-MM-DD.xlsx` 的文件。
    *   **Students 标签页**: 列出所有学生、活跃状态、联系信息及当前余额。
    *   **Transactions 标签页**: 列出每一笔历史交易记录。

### 备份与恢复 (Backup & Restore)
**这对数据安全至关重要。** 由于此应用驻留在您的浏览器中，清除浏览器缓存将删除数据。
1.  **备份**: 定期点击 **DOWNLOAD BACKUP** (下载备份)（例如每周）。将 `.json` 文件保存到安全位置（Google Drive、U盘等）。
2.  **恢复**:
    *   点击 **RESTORE BACKUP** (恢复备份)。
    *   选择您的 `.json` 文件。
    *   **警告**: 这会将备份数据与您当前的数据合并。

---

## 6. 故障排除

### 我忘记了管理员密码
1.  在登录屏幕上，点击 **Forgot Password?** (忘记密码？)。
2.  回答您设置的安全问题。
3.  如果正确，您可以立即创建一个新密码。

### 我清除了浏览器缓存 / "App 重置"
如果您清除了浏览器数据，应用看起来就像是全新的。
1.  如果您有 **备份 (.json)** 文件：
    *   使用临时密码完成 "Setup Admin" (设置管理员) 流程。
    *   进入 **Data Management** 并使用 **RESTORE BACKUP** 重新加载您的数据。
2.  如果您 **没有** 备份，数据将永久丢失。**请务必定期备份。**
