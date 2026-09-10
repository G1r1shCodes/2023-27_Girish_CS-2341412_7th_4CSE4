#  Industrial Internship Portfolio & Project Documentation

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.3-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![Meta WhatsApp API](https://img.shields.io/badge/Meta-WhatsApp%20Cloud%20API-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://developers.facebook.com/docs/whatsapp/cloud-api)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL%20%2F%20pgvector-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![Groq AI](https://img.shields.io/badge/AI-Groq%20%2F%20Llama%203.3-f34f29?style=for-the-badge)](https://groq.com/)
[![Mistral AI](https://img.shields.io/badge/AI-Mistral%20AI-orange?style=for-the-badge&logo=mistral&logoColor=white)](https://mistral.ai/)
[![Playwright](https://img.shields.io/badge/Automation-Playwright-2E8B57?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![Google Sheets API](https://img.shields.io/badge/Google-Sheets%20API%20v4-34A853?style=for-the-badge&logo=googlesheets&logoColor=white)](https://developers.google.com/sheets/api)

---

## 📌 Academic & Internship Metadata

| Parameter | Details |
| :--- | :--- |
| **Student Name** | **Girish Kumar Yadav** |
| **Roll Number** | **CS-2341412** |
| **Session** | **2023–2027** |
| **Year / Semester** | **4th Year / 7th Semester** |
| **Section** | **4CSE4** |
| **Repository Name** | `2023-27_Girish_CS-2341412_7th_4CSE4` |
| **GitHub Repository** | [https://github.com/G1r1shCodes/2023-27_Girish_CS-2341412_7th_4CSE4.git](https://github.com/G1r1shCodes/2023-27_Girish_CS-2341412_7th_4CSE4.git) |
| **Host Organization** | **KDI Power Private Limited** *(Manufacturer of Wires & Cables)* |
| **Internship Domain** | **Artificial Intelligence & Automation** |
| **Internship Tenure** | **29 June 2026 – 31 August 2026** (2 Months) |
| **Certificate Number** | `KDIP/INT/2026/AI-014` |
| **Authorized Signatory**| Vijay Gautam (Administrative Manager, KDI Power Pvt Ltd) |

---

## 📁 Repository Structure & Deliverables

```text
2023-27_Girish_CS-2341412_7th_4CSE4/
├── Internship Certificate.pdf         # Official Internship Certificate (KDI Power Pvt Ltd)
├── Internship Report.pdf              # Comprehensive Internship Project & Architecture Report
├── Internship Presentation.pptx       # Internship Overview & Project Demo Presentation (PPT)
├── README.md                          # Master Repository Documentation & Collective Project Index
│
├── Whatsapp-Bot-/                     # Project 1: AI WhatsApp Business Bot & Sales Dashboard
├── kdi-lead-intelligence/             # Project 2: B2B Lead Intelligence & Scraping Pipeline
├── KDI-LinkedIn-Schema-Tracker/       # Project 3: LinkedIn Tender & Government Scheme Tracker
├── PDF-Editor/                        # Project 4: AI PDF Reconstructor & OCR/VLM Editor
└── Task-project/                      # Project 5: Google Sheets & WhatsApp Task Reminder Engine
```

---

## 📄 Key Internship Artifacts

### 1.  Internship Certificate (`Internship Certificate.pdf`)
* **Certificate ID:** `KDIP/INT/2026/AI-014`
* **Issued Date:** 2nd September 2026
* **Key Achievements Recognized:** Successfully designed, developed, and deployed the KDI Power WhatsApp Business Messaging System, PDF Editor, and LinkedIn Lead Generator with high evaluation marks across all technical and professional parameters.

### 2.  Internship Report (`Internship Report.pdf`)
* Exhaustive technical report documenting the problem statement, system architecture, database design (Supabase pgvector), LLM prompts, scraping mechanics, automated testing, and production deployment on cloud services (Render, Vercel/Vite, Google Cloud API).

### 3.  Internship Presentation (`Internship Presentation.pptx`)
* Visual slide deck outlining the company profile (KDI Power Pvt Ltd), technology stack evolution, live system screenshots, code walkthroughs, ROI/productivity metrics achieved, and future scope.

---

##  Projects Overview Matrix

| # | Project Name | Tech Stack | Key Functionality | Deployment / Status |
|---|---|---|---|---|
| **1** | **[KDI Power AI WhatsApp Assistant & Sales Dashboard](file:///d:/Whatsapp-Bot-)** | Python, FastAPI, Meta Cloud API, Groq AI, Supabase PostgreSQL, Chart.js | Conversational AI sales bot, product catalog Q&A, Lead capture, real-time glassmorphic analytics dashboard | Deployed on Render + Supabase |
| **2** | **[KDI Lead Intelligence Engine](file:///d:/kdi-lead-intelligence)** | Python, Streamlit, Playwright, Groq/OpenAI, SQLite, openpyxl | 3-tier B2B lead discovery for cable distributors & utilities, Google Maps scraping with proxy rotation, LLM scoring | Local Streamlit + Cron Task Scheduler |
| **3** | **[LinkedIn Tender & Scheme Tracker](file:///d:/KDI-LinkedIn-Schema-Tracker)** | Python, Playwright CDP, Mistral AI, openpyxl, Windows Batch | Scraping competitor LinkedIn posts (Polycab, KEI, Finolex, etc.), filtering RDSS/DDUGJY schemes & tenders, AI bullet summaries | Standalone Executable / Desktop Batch |
| **4** | **[AI-Powered PDF Editor & OCR Engine](file:///d:/PDF-Editor)** | React 18, Vite, FastAPI, MinerU, NVIDIA NIM VLM, MathJax, Playwright | Scanned PDF layout detection, VLM extraction of LaTeX math & tables, browser click-to-edit canvas, true SVG/PDF export | Docker / Vite + FastAPI Desktop Portable |
| **5** | **[Google Sheets Task Automation Bot](file:///d:/Task-project)** | Python, FastAPI, Meta WhatsApp Cloud API, Google Sheets API v4 | Automated task reminders to employees, webhook status listener (Pending/Done), IST timestamping & time tracking | Deployed on Render + GitHub Actions |

---

##  Detailed Project Breakdown

### Project 1: KDI Power AI WhatsApp Assistant & Sales Dashboard
* **Directory:** [`Whatsapp-Bot-`](file:///d:/Whatsapp-Bot-)
* **Primary Role:** Lead Automation & Customer Service Bot
* **Key Technical Contributions:**
  - Integrated **Meta WhatsApp Cloud API** using webhooks to handle real-time inbound customer queries regarding electrical wire and cable catalog products (Aerial Bunched Cables, XLPE Cables, Control Cables).
  - Utilized **Groq AI** (`llama-3.3-70b-versatile` & `compound-mini`) with RAG embeddings in **Supabase (pgvector)** to intelligently extract structured lead info (Name, Company, Cable Type, Quantity, Location).
  - Designed and built a **Glassmorphic Sales Dashboard** using Vanilla JS and Chart.js for real-time lead tracking, status filtering, and live catalog price/stock updating.

### Project 2: KDI Lead Intelligence & B2B Lead Finder
* **Directory:** [`kdi-lead-intelligence`](file:///d:/kdi-lead-intelligence)
* **Primary Role:** Automated B2B Lead Acquisition & Qualification Engine
* **Key Technical Contributions:**
  - Engineered a **3-tier lead pipeline**: Discovery (Google Maps scraping via Playwright Chromium) $\rightarrow$ Intelligence (Website content extraction & email validation) $\rightarrow$ Persistence (SQLite DB + Formatted Excel report).
  - Built an automated **KDI Cable Scoring Engine** that scores lead suitability ($0-100$) based on sector match (cable distributor, EPC contractor, DISCOM/utility), location bonus (South Africa & India), and LLM classification.
  - Implemented **Proxy Rotation** support and automated weekly execution via Windows Task Scheduler & cron.

### Project 3: KDI LinkedIn Tender & Scheme Tracker
* **Directory:** [`KDI-LinkedIn-Schema-Tracker`](file:///d:/KDI-LinkedIn-Schema-Tracker)
* **Primary Role:** Competitor Benchmarking & Government Scheme Intelligence
* **Key Technical Contributions:**
  - Developed an automated scraper using **Playwright CDP** attached to a dedicated Chrome profile (`chrome-data`) to scrape top 10 cable competitors (Polycab, KEI, Finolex, RR Global, Havells, V-Guard).
  - Integrated **Mistral AI** (`mistral-small-latest`) to generate concise 3–5 bullet point executive summaries of posts mentioning tenders, power grid electrification, and government schemes (RDSS, DDUGJY).
  - Automatically appends extracted intelligence into a lock-safe Excel spreadsheet (`Master_Tracker.xlsx`).

### Project 4: AI-Powered PDF Reconstructor & Editor (`PDFEdit`)
* **Directory:** [`PDF-Editor`](file:///d:/PDF-Editor)
* **Primary Role:** Smart Document Layout Parsing & LaTeX/Math OCR Editor
* **Key Technical Contributions:**
  - Built a hybrid processing pipeline using **MinerU** for document layout detection on CPU and offloading complex tables & math formulas to **NVIDIA NIM (Llama 3.2 90B Vision)**.
  - Created a full-featured **React 18 + Vite** UI with interactive canvas block editing, font customization, and undo/redo state history.
  - Implemented headless **Chromium & MathJax SVG rendering** via Playwright to reconstruct editable documents back into pixel-perfect downloadable PDFs.

### Project 5: Google Sheets & WhatsApp Task Automation Engine
* **Directory:** [`Task-project`](file:///d:/Task-project)
* **Primary Role:** Field Worker & Internal Task Monitoring Automation
* **Key Technical Contributions:**
  - Linked **Google Sheets API v4** service accounts to act as a real-time cloud task manager database.
  - Built a **FastAPI Webhook service** hosted on Render that pings staff members on WhatsApp with personalized task deadlines.
  - Automated message parsing: when staff reply `ok` or `done`, the webhook updates **Status**, **Received On**, **Completed On**, and calculates total **Time Taken** in Indian Standard Time (IST).
  - Configured **GitHub Actions (`send_reminders.yml` & `keep_alive.yml`)** for periodic cron triggers and server uptime maintenance.

---

##  Global Technology Stack & Tools

* **Programming Languages:** Python 3.10+, JavaScript (ES6+), HTML5, CSS3, SQL
* **Frontend Frameworks & Libraries:** React 18, Vite, Chart.js, Vanilla Glassmorphism CSS
* **Backend Frameworks:** FastAPI, Uvicorn, Flask, Node.js
* **Databases & Cloud Storage:** Supabase (PostgreSQL, PostgREST, pgvector), SQLite, Google Sheets API
* **AI & LLM Services:** Groq AI (Llama 3.3 70B), Mistral AI API, NVIDIA NIM (Llama 3.2 Vision), Meta Cloud API
* **Browser Automation & Scraping:** Playwright (Chromium / CDP), BeautifulSoup4, Requests
* **DevOps & Continuous Deployment:** Render, GitHub Actions, Docker, Windows Batch Scripting

---

##  Installation & Running Guidelines

To inspect or execute any of the individual internship projects locally, navigate to their respective subfolders and follow the setup instructions in their local `README.md`:

```bash
# 1. Clone the master repository
git clone https://github.com/G1r1shCodes/2023-27_Girish_CS-2341412_7th_4CSE4.git
cd 2023-27_Girish_CS-2341412_7th_4CSE4

# 2. Run Project 1: WhatsApp Bot & Dashboard
cd Whatsapp-Bot-
pip install -r requirements.txt
uvicorn app:app --reload

# 3. Run Project 2: Lead Intelligence Pipeline
cd ../kdi-lead-intelligence
pip install -r requirements.txt
python app.py

# 4. Run Project 3: LinkedIn Scheme Tracker
cd ../KDI-LinkedIn-Schema-Tracker
RunTracker.bat

# 5. Run Project 4: AI PDF Editor
cd ../PDF-Editor
npm install
pip install -r requirements.txt
python main.py

# 6. Run Project 5: Google Sheets Task Reminder Bot
cd ../Task-project
python send_reminders.py
```

---

##  Conclusion & Industry Impact

During the 2-month internship tenure at **KDI Power Private Limited**, the developed software solutions successfully automated:
1. Customer inbound sales query responses and lead capture via WhatsApp.
2. Cross-border B2B cable buyer discovery across India and South Africa.
3. Market competitive analysis and government tender tracking on LinkedIn.
4. Technical document digitization, PDF editing, and formula extraction.
5. Operational task tracking and field staff reminder notifications.

---
*Created as part of the 7th Semester B.Tech Computer Science & Engineering (4CSE4) Internship Submission.*
