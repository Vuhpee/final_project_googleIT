#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet



def generate_report(attachment, title, body):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(body)

    report.build([report_title, report_body])
