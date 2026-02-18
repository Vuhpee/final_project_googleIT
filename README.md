# Automated Catalog Update & Reporting Pipeline

Google IT Automation with Python final project implementing an end-to-end automation workflow for maintaining an online product catalog. The solution standardizes supplier images, uploads media assets, posts structured catalog data to a web endpoint, generates a PDF summary report, emails the report automatically, and monitors system health with alerting.

---

## Project Scope

- **Image processing:** Convert supplier images from TIFF to standardized JPEG format (600×400).
- **Media upload:** Upload processed images to a web service.
- **Catalog updates:** Parse product description files and POST structured JSON records to a catalog API endpoint.
- **Reporting:** Generate a PDF report summarizing catalog items.
- **Email automation:** Send the report via email as an attachment.
- **Monitoring:** Check system health (CPU, memory, disk, hostname resolution) and email alerts when thresholds are exceeded.

---

## Tech Stack

- Python
- Pillow (image processing)
- Requests (HTTP client)
- ReportLab (PDF generation)
- SMTP email automation
- psutil (system monitoring)

---

## Repository Contents

- `changeImage.py`  
  Converts `.tiff` images to `.jpeg`, resizes to **600×400**, and standardizes output format.

- `supplier_image_upload.py`  
  Uploads processed `.jpeg` files to the server upload endpoint via HTTP requests.

- `run.py`  
  Reads product description files, extracts product attributes (including weight parsing), and POSTs JSON payloads to the catalog endpoint.

- `reports.py`  
  Builds a PDF report (ReportLab) summarizing items for the daily/periodic report.

- `report_email.py`  
  Generates the PDF report and sends it via email as an attachment.

- `emails.py`  
  Shared email helper utilities for composing and sending messages.

- `health_check.py`  
  Performs system health checks using threshold logic (CPU, disk, memory, DNS/hostname) and sends alert emails when issues are detected.

---

## Key Skills Demonstrated

- Python automation and scripting
- REST API interactions (POST, file upload)
- Image processing pipelines:
- Structured data extraction and transformation
- Automated reporting (PDF generation)

## Highlights / Impact

- Designed an end-to-end automation pipeline integrating image processing, API communication, reporting, and monitoring into a single workflow.
- Reduced manual catalog maintenance by automating data ingestion, media handling, and structured JSON submissions.
- Improved operational reliability by implementing proactive system health checks with automated email alerts.
- Demonstrated practical DevOps-oriented automation skills including file transformation, REST integration, and monitoring logic.
- Email automation (SMTP)
- Basic monitoring/alerting and reliability checks
