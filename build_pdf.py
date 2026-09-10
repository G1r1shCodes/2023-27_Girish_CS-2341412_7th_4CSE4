import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
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
        self.setFont("Helvetica", 10)
        self.setFillColor(colors.HexColor("#333333"))
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(A4[0] - 54, 36, page_text)
        self.drawString(54, 36, "KDI Power Pvt. Ltd. — Industrial Internship Report")
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 50, A4[0] - 54, 50)
        self.restoreState()

def build_pdf(filename="Internship Report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=64
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        alignment=1,
        textColor=colors.HexColor("#1A365D")
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        alignment=1,
        textColor=colors.HexColor("#2B6CB0")
    )

    body_center = ParagraphStyle(
        'CoverCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        alignment=1,
        textColor=colors.HexColor("#2D3748")
    )
    
    h1_style = ParagraphStyle(
        'Header1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        spaceBefore=14,
        spaceAfter=8,
        textColor=colors.HexColor("#1A365D"),
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Header2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.HexColor("#2B6CB0"),
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        spaceAfter=8,
        textColor=colors.HexColor("#2D3748")
    )

    bullet_style = ParagraphStyle(
        'BulletDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        leftIndent=15,
        spaceAfter=4,
        textColor=colors.HexColor("#2D3748")
    )

    story = []

    # ================= COVER PAGE =================
    story.append(Spacer(1, 20))
    story.append(Paragraph("INDUSTRIAL INTERNSHIP REPORT", title_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("on", body_center))
    story.append(Spacer(1, 10))
    story.append(Paragraph("AI & Automation Systems for Cable<br/>Manufacturing & Operations", subtitle_style))
    story.append(Spacer(1, 25))
    story.append(Paragraph("<b>Submitted To</b><br/>Department of Computer Science & Engineering<br/>School of Engineering & Technology", body_center))
    story.append(Spacer(1, 20))
    story.append(Paragraph("<i>In partial fulfilment of the requirements for the degree of</i><br/><b>Bachelor of Technology in Computer Science & Engineering</b>", body_center))
    story.append(Spacer(1, 30))
    
    meta_table_data = [
        [Paragraph("<b>Student Name:</b>", body_style), Paragraph("Girish Kumar Yadav", body_style)],
        [Paragraph("<b>Roll Number:</b>", body_style), Paragraph("CS-2341412", body_style)],
        [Paragraph("<b>Batch / Session:</b>", body_style), Paragraph("2023–2027 (4th Year / 7th Semester)", body_style)],
        [Paragraph("<b>Section:</b>", body_style), Paragraph("4CSE4", body_style)],
        [Paragraph("<b>Host Organization:</b>", body_style), Paragraph("KDI Power Private Limited, Delhi", body_style)],
        [Paragraph("<b>Internship Duration:</b>", body_style), Paragraph("29 June 2026 – 31 August 2026 (2 Months)", body_style)],
        [Paragraph("<b>Certificate No.:</b>", body_style), Paragraph("KDIP/INT/2026/AI-014", body_style)],
    ]
    t = Table(meta_table_data, colWidths=[2.2*inch, 4.2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t)
    story.append(PageBreak())

    # ================= CANDIDATE DECLARATION =================
    story.append(Paragraph("Candidate's Declaration", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1A365D"), spaceAfter=15))
    decl_text = (
        "I, <b>Girish Kumar Yadav</b>, Roll No. <b>CS-2341412</b>, student of B.Tech 7th Semester, Section <b>4CSE4</b> "
        "(Session <b>2023–27</b>), Department of Computer Science and Engineering, hereby declare that the internship report "
        "titled <b>\"AI & Automation Systems for Cable Manufacturing & Operations\"</b> is an authentic record of my own work "
        "carried out during my two-month industrial internship from <b>29 June 2026 to 31 August 2026</b> at <b>KDI Power Private Limited</b>, "
        "New Delhi, under Certificate No. <b>KDIP/INT/2026/AI-014</b>.<br/><br/>"
        "All references and resources used in this report have been duly acknowledged. I affirm that this report has not been submitted "
        "elsewhere for the award of any other degree or diploma."
    )
    story.append(Paragraph(decl_text, body_style))
    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>Signature:</b> ___________________________", body_style))
    story.append(Paragraph("<b>Student Name:</b> Girish Kumar Yadav", body_style))
    story.append(Paragraph("<b>Roll Number:</b> CS-2341412", body_style))
    story.append(Paragraph("<b>Batch:</b> 2023–27 (4CSE4)", body_style))
    story.append(Spacer(1, 20))
    story.append(PageBreak())

    # ================= ACKNOWLEDGEMENT =================
    story.append(Paragraph("Acknowledgement", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1A365D"), spaceAfter=15))
    ack_text = (
        "I express my deepest gratitude to the management of <b>KDI Power Private Limited</b>, New Delhi, for granting me the "
        "opportunity to undergo a two-month industrial internship in Artificial Intelligence & Automation. I am particularly indebted to "
        "<b>Mr. Vijay Gautam</b>, Administrative Manager, for his continuous guidance, encouragement, and invaluable domain insights "
        "throughout the project lifecycle.<br/><br/>"
        "I also extend my sincere appreciation to the faculty members of the Department of Computer Science and Engineering for their "
        "constant support and academic foundation. Finally, I thank my family and peers for their unceasing motivation."
    )
    story.append(Paragraph(ack_text, body_style))
    story.append(Spacer(1, 40))
    story.append(Paragraph("<b>Signature:</b> ___________________________", body_style))
    story.append(Paragraph("<b>Student Name:</b> Girish Kumar Yadav", body_style))
    story.append(Paragraph("<b>Roll Number:</b> CS-2341412", body_style))
    story.append(Spacer(1, 20))
    story.append(PageBreak())

    # ================= EXECUTIVE SUMMARY & PROJECT BREAKDOWN =================
    story.append(Paragraph("1. Executive Summary & Company Profile", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1A365D"), spaceAfter=12))
    
    summary_text = (
        "<b>KDI Power Private Limited</b> is an ISO 9001, ISO 14001, and ISO 45001 certified manufacturer of electrical wires and cables "
        "headquartered in New Delhi, India. The company manufactures Low Voltage (LT) Power Cables, Aerial Bunched Cables (ABC), XLPE Power Cables, "
        "Control Cables, House Wires, and Rubber Cables for DISCOM utilities, EPC contractors, and global distributors.<br/><br/>"
        "During the 2-month industrial internship (June 29 – Aug 31, 2026), I worked as an <b>AI & Automation Engineer</b> and developed "
        "five major production applications to automate sales, lead generation, tender tracking, document processing, and task management."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("2. Technical Projects Portfolio", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1A365D"), spaceAfter=12))

    projects = [
        ("Project 1: KDI Power AI WhatsApp Assistant & Sales Dashboard",
         "Built an automated WhatsApp bot using FastAPI, Meta WhatsApp Cloud API, Groq AI (Llama 3.3 70B), Supabase PostgreSQL (pgvector RAG), "
         "and a real-time glassmorphic single-page sales dashboard for analytics and price editing."),
        ("Project 2: KDI Lead Intelligence & B2B Lead Discovery Engine",
         "Engineered a 3-tier lead discovery pipeline with Google Maps Playwright scraping, proxy rotation, Groq LLM scoring engine (0-100 scale), "
         "and automated formatted Excel exports (.xlsx) targeting cable distributors in India and South Africa."),
        ("Project 3: LinkedIn Tender & Government Scheme Tracker",
         "Developed an automated scraper using Playwright CDP attached to Chrome profiles and Mistral AI summarization to track competitor updates "
         "(Polycab, KEI, Finolex, Havells) and government electrification orders (RDSS, DDUGJY)."),
        ("Project 4: AI-Powered PDF Reconstructor & OCR Editor",
         "Constructed a hybrid web editor with React 18 / Vite and FastAPI using MinerU layout detection, NVIDIA NIM VLM (Llama 3.2 90B Vision) "
         "for table/math formula extraction, and Playwright headless Chromium for true PDF reconstruction."),
        ("Project 5: Google Sheets & WhatsApp Task Automation Engine",
         "Deployed a FastAPI webhook on Render connected to Google Sheets API v4 service accounts and WhatsApp Meta API for automated employee "
         "task reminders and real-time IST completion timestamping.")
    ]

    for title, desc in projects:
        story.append(Paragraph(title, h2_style))
        story.append(Paragraph(desc, body_style))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 10))
    story.append(Paragraph("3. Summary Matrix of Internship Deliverables", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1A365D"), spaceAfter=12))

    matrix_data = [
        [Paragraph("<b>#</b>", body_style), Paragraph("<b>Project</b>", body_style), Paragraph("<b>Tech Stack</b>", body_style), Paragraph("<b>Status</b>", body_style)],
        [Paragraph("1", body_style), Paragraph("WhatsApp Sales Bot", body_style), Paragraph("FastAPI, Meta API, Groq, Supabase", body_style), Paragraph("Deployed", body_style)],
        [Paragraph("2", body_style), Paragraph("Lead Intelligence", body_style), Paragraph("Playwright, Groq, SQLite, Excel", body_style), Paragraph("Deployed", body_style)],
        [Paragraph("3", body_style), Paragraph("LinkedIn Tender Tracker", body_style), Paragraph("Playwright CDP, Mistral AI, Excel", body_style), Paragraph("Deployed", body_style)],
        [Paragraph("4", body_style), Paragraph("AI PDF Editor", body_style), Paragraph("React 18, Vite, FastAPI, MinerU, NIM", body_style), Paragraph("Deployed", body_style)],
        [Paragraph("5", body_style), Paragraph("Task Reminder Bot", body_style), Paragraph("FastAPI, Google Sheets API, Render", body_style), Paragraph("Deployed", body_style)],
    ]
    
    t_matrix = Table(matrix_data, colWidths=[0.4*inch, 1.8*inch, 2.8*inch, 1.4*inch])
    t_matrix.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_matrix)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated '{filename}'")

if __name__ == "__main__":
    build_pdf()
