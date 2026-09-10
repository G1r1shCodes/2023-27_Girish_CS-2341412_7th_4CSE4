import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image as RLImage
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        if self._pageNumber == 1:
            return  # Suppress page number on cover page
        self.saveState()
        self.setFont("Times-Roman", 10)
        self.setFillColor(colors.HexColor("#333333"))
        page_text = f"{self._pageNumber}"
        self.drawCentredString(A4[0] / 2, 36, page_text)
        self.restoreState()

def build_pdf(filename="Internship Report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=1.5*inch,
        rightMargin=1.0*inch,
        topMargin=0.75*inch,
        bottomMargin=1.0*inch
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=20,
        leading=24,
        alignment=1,
        textColor=colors.black
    )

    subtitle_style = ParagraphStyle(
        'CoverSubTitle',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=14,
        leading=18,
        alignment=1,
        textColor=colors.black
    )

    body_center = ParagraphStyle(
        'CoverCenter',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=16,
        alignment=1,
        textColor=colors.black
    )

    chap_style = ParagraphStyle(
        'ChapHeader',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=14,
        leading=18,
        alignment=1,
        spaceBefore=15,
        spaceAfter=15,
        textColor=colors.black,
        keepWithNext=True
    )
    
    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=15,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.black,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Normal'],
        fontName='Times-BoldItalic',
        fontSize=12,
        leading=15,
        spaceBefore=10,
        spaceAfter=4,
        textColor=colors.black,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=16,
        spaceAfter=8,
        textColor=colors.black
    )

    story = []

    # ================= COVER PAGE =================
    story.append(Spacer(1, 15))
    story.append(Paragraph("Report", title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("of", body_center))
    story.append(Spacer(1, 10))
    story.append(Paragraph("AI & AUTOMATION SYSTEMS FOR CABLE<br/>MANUFACTURING & OPERATIONS", title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("KDI Power Business Automation & AI Platform", subtitle_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Submitted To", body_center))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Department of Computer Science and Engineering</b><br/>School of Computer Science and Engineering<br/>IILM University, Greater Noida, U.P.", body_center))
    story.append(Spacer(1, 15))
    story.append(Paragraph("In partial fulfilment of the requirement of degree of", body_center))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>B.Tech CSE</b>", subtitle_style))
    story.append(Spacer(1, 15))
    
    if os.path.exists("logo.png"):
        story.append(RLImage("logo.png", width=1.8*inch, height=1.8*inch))
        story.append(Spacer(1, 15))
        
    story.append(Paragraph("<b>By</b>", body_center))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Roll Number of Student: <b>CS-2341412</b><br/>Name of Student: <b>GIRISH KUMAR YADAV</b><br/>Batch: <b>2023–27 (Section 4CSE4)</b>", body_center))
    story.append(Spacer(1, 30))
    story.append(Paragraph("31 August 2026", body_center))
    story.append(PageBreak())

    # ================= CANDIDATE DECLARATION =================
    story.append(Paragraph("Candidate's Declaration", chap_style))
    decl_text = (
        "I, <b>GIRISH KUMAR YADAV</b> do hereby declare that the internship report titled "
        "<b>\"AI & AUTOMATION SYSTEMS FOR CABLE MANUFACTURING & OPERATIONS --- KDI Power Business Automation & AI Platform\"</b> "
        "has been completed by me to fulfil the requirement for the award of the degree of Bachelor of Technology in CSE. "
        "All the references have been quoted and I have not taken as such any material from any other source. "
        "I affirm to you that this report is my own and has not been submitted to any other institute for any degree/diploma requirement "
        "and further I shall be solely responsible for any kind of copyright violation in this regard."
    )
    story.append(Paragraph(decl_text, body_style))
    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>Signature:</b> ___________________________", body_style))
    story.append(Paragraph("<b>Student Name:</b> GIRISH KUMAR YADAV", body_style))
    story.append(Paragraph("<b>Roll No.:</b> CS-2341412", body_style))
    story.append(Paragraph("<b>Date:</b> 31 August 2026", body_style))
    story.append(PageBreak())

    # ================= ACKNOWLEDGEMENT =================
    story.append(Paragraph("Acknowledgement", chap_style))
    ack_text = (
        "I am using this opportunity to express my gratitude to everyone who supported me throughout the Internship Program. "
        "I am thankful for their aspiring guidance, invaluably constructive criticism and friendly advice during this work. "
        "I am sincerely grateful to them for sharing their truthful and illuminating views on a number of issues related to this work.<br/><br/>"
        "I would like to express my deepest appreciation to <b>Mr. Vijay Gautam</b>, Administrative Manager, KDI Power Private Limited, New Delhi, "
        "for providing me with the opportunity to intern at the organization and for his mentorship throughout the internship period.<br/><br/>"
        "I am profoundly grateful to the entire <b>Engineering & Operations Team</b> at KDI Power for their continuous support and technical insights.<br/><br/>"
        "I extend my sincere thanks to <b>IILM University, Greater Noida</b>, and the <b>School of Computer Science and Engineering</b> for facilitating "
        "this internship opportunity."
    )
    story.append(Paragraph(ack_text, body_style))
    story.append(Spacer(1, 30))
    story.append(Paragraph("<b>Signature:</b> ___________________________", body_style))
    story.append(Paragraph("<b>Student Name:</b> GIRISH KUMAR YADAV", body_style))
    story.append(Paragraph("<b>Roll No.:</b> CS-2341412", body_style))
    story.append(Paragraph("<b>Date:</b> 31 August 2026", body_style))
    story.append(PageBreak())

    # ================= INTERNSHIP CERTIFICATE =================
    story.append(Paragraph("Internship Completion Certificate", chap_style))
    story.append(Spacer(1, 15))
    cert_box_data = [
        [Paragraph("<b>KDI POWER PRIVATE LIMITED</b><br/>"
                   "<i>ISO 9001:2015, ISO 14001:2015, ISO 45001:2018 Certified Manufacturer</i><br/>New Delhi, India<br/><br/>"
                   "<b>CERTIFICATE OF INTERNSHIP COMPLETION</b><br/>"
                   "<b>Certificate No.: KDIP/INT/2026/AI-014</b> | <b>Date of Issue: 2nd September 2026</b><br/><br/>"
                   "This is to certify that <b>Mr. GIRISH KUMAR YADAV</b> (Roll No. CS-2341412) has successfully completed a two-month internship "
                   "in <b>Artificial Intelligence & Automation</b> with <b>KDI Power Private Limited</b>, from <b>29 June 2026 to 31 August 2026</b>. "
                   "During this period, he demonstrated strong technical aptitude, initiative, and commitment, and independently designed, developed, "
                   "and deployed the KDI Power WhatsApp Business Messaging System, PDF Editor, and LinkedIn Lead Generator.<br/><br/>"
                   "<b>Authorized Signatory:</b> VIJAY GAUTAM, Administrative Manager, KDI Power Pvt. Ltd.", body_style)]
    ]
    t_box = Table(cert_box_data, colWidths=[5.5*inch])
    t_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8F9FA")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#A0AEC0")),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ]))
    story.append(t_box)
    story.append(PageBreak())

    # ================= CHAPTER 1 =================
    story.append(Paragraph("Chapter 1: Project Description", chap_style))
    
    story.append(Paragraph("1.1 Introduction", h1_style))
    story.append(Paragraph(
        "The global industrial manufacturing vertical, particularly electrical wire and cable manufacturing, operates in a high-demand environment "
        "where operations, sales, and field teams must manage trade inquiries, technical datasheets, competitive tenders, and employee tasks efficiently.<br/><br/>"
        "<b>KDI Power Private Limited</b> commissioned the development of an integrated suite of Artificial Intelligence and Automation systems. "
        "During my industrial internship from <b>29 June 2026 to 31 August 2026</b>, I designed, built, and deployed five core software systems: "
        "(1) WhatsApp AI Assistant & Sales Dashboard; (2) KDI Lead Intelligence Engine; (3) LinkedIn Tender & Scheme Tracker; "
        "(4) AI PDF Reconstructor & Editor; and (5) Google Sheets Task Automation Bot.", body_style
    ))

    story.append(Paragraph("1.2 Organization Profile", h1_style))
    story.append(Paragraph(
        "<b>KDI Power Private Limited</b> is an ISO 9001, ISO 14001, and ISO 45001 certified manufacturer of electrical wires and cables headquartered in New Delhi. "
        "Its core product portfolio includes Low Voltage (LT) Power Cables, XLPE Cables, Aerial Bunched Cables (ABC), Control Cables, House Wires, and Rubber Cables.", body_style
    ))

    story.append(Paragraph("1.3 Problem Statement", h1_style))
    story.append(Paragraph(
        "1. Delayed Sales Turnaround on WhatsApp during off-hours.<br/>"
        "2. High Cost of International B2B Lead Discovery for export markets.<br/>"
        "3. Manual Competitor & Tender Tracking across news and social channels.<br/>"
        "4. Uneditable Technical Datasheet Scans needing layout/formula extraction.<br/>"
        "5. Operational Task Tracking Overhead with manual phone follow-ups.", body_style
    ))

    story.append(Paragraph("1.4 Project Objectives", h1_style))
    story.append(Paragraph(
        "• Build automated WhatsApp Bot with Meta Cloud API and Supabase pgvector RAG.<br/>"
        "• Create a 3-tier lead discovery pipeline with Google Maps Playwright scraping and Groq scoring.<br/>"
        "• Implement LinkedIn CDP scraper and Mistral AI post summarizer.<br/>"
        "• Construct hybrid React/FastAPI PDF Editor using MinerU and NVIDIA NIM VLM.<br/>"
        "• Deploy Google Sheets API webhook on Render with GitHub Actions cron runners.", body_style
    ))

    story.append(Paragraph("1.5 Technologies and Tools Used", h1_style))
    
    tech_data = [
        [Paragraph("<b>Category</b>", body_style), Paragraph("<b>Technology / Tool</b>", body_style), Paragraph("<b>Purpose</b>", body_style)],
        [Paragraph("Backend", body_style), Paragraph("Python 3.10+, FastAPI, Flask, Streamlit", body_style), Paragraph("Microservices, APIs, Scrapers", body_style)],
        [Paragraph("Frontend", body_style), Paragraph("React 18, Vite, Chart.js, Glassmorphic CSS", body_style), Paragraph("Editor canvas, Sales dashboard UI", body_style)],
        [Paragraph("Databases", body_style), Paragraph("Supabase PostgreSQL, pgvector, SQLite", body_style), Paragraph("Relational storage, RAG embeddings", body_style)],
        [Paragraph("AI / LLMs", body_style), Paragraph("Groq (Llama 3.3), Mistral AI, NVIDIA NIM", body_style), Paragraph("Conversations, summaries, VLM OCR", body_style)],
        [Paragraph("Automation", body_style), Paragraph("Playwright (Chromium/CDP), MinerU", body_style), Paragraph("Google Maps, LinkedIn CDP, PDF OCR", body_style)],
    ]
    t_tech = Table(tech_data, colWidths=[1.1*inch, 2.3*inch, 2.1*inch])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_tech)
    story.append(Spacer(1, 10))

    story.append(Paragraph("1.6 System Architecture Diagrams", h1_style))
    if os.path.exists("architecture_diagram.png"):
        story.append(RLImage("architecture_diagram.png", width=5.5*inch, height=2.8*inch))
        story.append(Paragraph("<font size=9>Figure 1.1: System Architecture Diagram of KDI Power Platform</font>", body_center))
        story.append(Spacer(1, 10))

    if os.path.exists("image.png"):
        story.append(RLImage("image.png", width=5.5*inch, height=2.8*inch))
        story.append(Paragraph("<font size=9>Figure 1.2: End-to-End B2B Lead Intelligence Pipeline Workflow</font>", body_center))
        story.append(Spacer(1, 10))

    if os.path.exists("dashboard.png"):
        story.append(RLImage("dashboard.png", width=5.5*inch, height=2.8*inch))
        story.append(Paragraph("<font size=9>Figure 1.3: Glassmorphic Sales Analytics Dashboard UI</font>", body_center))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # ================= CHAPTER 2 =================
    story.append(Paragraph("Chapter 2: Bibliography / References", chap_style))
    bib_text = (
        "1. Meta Platforms Inc. (2026). <i>WhatsApp Cloud API Documentation</i>.<br/>"
        "2. FastAPI. (2026). <i>FastAPI Framework Documentation</i>.<br/>"
        "3. Supabase. (2026). <i>Supabase PostgreSQL and pgvector Guide</i>.<br/>"
        "4. Groq Inc. (2026). <i>Groq Llama 3.3 API Documentation</i>.<br/>"
        "5. Microsoft Playwright. (2026). <i>Playwright for Python Documentation</i>.<br/>"
        "6. Mistral AI. (2026). <i>Mistral Developer Platform Documentation</i>.<br/>"
        "7. Google Cloud. (2026). <i>Google Sheets API v4 Guide</i>.<br/>"
        "8. NVIDIA NIM. (2026). <i>Llama 3.2 90B Vision LLM Documentation</i>.<br/>"
        "9. React. (2026). <i>React 18 Documentation</i>.<br/>"
        "10. MinerU Authors. (2026). <i>MinerU PDF Layout Detection Engine</i>."
    )
    story.append(Paragraph(bib_text, body_style))
    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>Report Prepared By:</b><br/><b>GIRISH KUMAR YADAV</b><br/>AI & Automation Engineering Intern<br/>KDI Power Private Limited, New Delhi<br/><b>Date:</b> 31 August 2026", body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated '{filename}'")

if __name__ == "__main__":
    build_pdf()
