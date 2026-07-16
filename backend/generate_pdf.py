import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Define color palette
PRIMARY_COLOR = colors.HexColor("#1E3A8A")   # Dark Navy
SECONDARY_COLOR = colors.HexColor("#0D9488") # Teal
TEXT_COLOR = colors.HexColor("#334155")      # Slate-700
BG_CODE_COLOR = colors.HexColor("#F8FAFC")   # Slate-50
BORDER_COLOR = colors.HexColor("#E2E8F0")    # Slate-200
TITLE_COLOR = colors.HexColor("#0F172A")     # Slate-900

# File Paths for the Design Patterns
PATTERNS = [
    {
        "name": "Singleton Pattern",
        "file": "core/singleton.py",
        "description": "The Singleton pattern ensures a class has only one instance and provides a global point of access to it. In DevFlow, this is used for the database connection (MongoConnection) to ensure we don't open duplicate connections to MongoDB.",
        "code_path": "core/singleton.py",
        "usage": None
    },
    {
        "name": "Strategy Pattern",
        "file": "tasks/strategy.py",
        "description": "The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Here, it encapsulates different task priority execution strategies (Low, Medium, High Priority) and runs them dynamically based on context.",
        "code_path": "tasks/strategy.py",
        "usage": None
    },
    {
        "name": "State Pattern",
        "file": "tasks/state.py",
        "description": "The State pattern allows an object to alter its behavior when its internal state changes. In DevFlow, task status transitions (Todo -> InProgress -> Testing -> Done) are governed by state objects, making state transitions clean and preventing invalid transitions.",
        "code_path": "tasks/state.py",
        "usage": {
            "title": "State Pattern Usage in tasks/views.py (ChangeTaskStatusView)",
            "file": "tasks/views.py",
            "lines": (77, 89)
        }
    },
    {
        "name": "Builder Pattern",
        "file": "reports/builder.py",
        "description": "The Builder pattern separates the construction of a complex object from its representation. In DevFlow, ReportBuilder builds a report document step-by-step by accumulating counts for projects, sprints, tasks, and bugs, and then returning the final report.",
        "code_path": "reports/builder.py",
        "usage": {
            "title": "Builder Pattern Usage in reports/services.py (ReportService)",
            "file": "reports/services.py",
            "lines": (11, 34)
        }
    },
    {
        "name": "Observer Pattern (Core)",
        "file": "core/observers.py",
        "description": "The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified automatically. In DevFlow, the Subject class manages observers like EmailObserver and NotificationObserver and broadcasts messages to them.",
        "code_path": "core/observers.py",
        "usage": None
    },
    {
        "name": "Observer Pattern (Notifications)",
        "file": "notifications/subject.py & observer.py",
        "description": "A domain-specific implementation of the Observer pattern for the notification system. The NotificationSubject tracks observers and notifies them, print-formatting notification events when triggered.",
        "code_path": "notifications/subject.py",
        "additional_code_path": "notifications/observer.py",
        "usage": None
    },
    {
        "name": "Chain of Responsibility Pattern",
        "file": "core/approval_chain.py",
        "description": "The Chain of Responsibility pattern passes a request along a chain of handlers. Each handler decides either to process the request or to pass it to the next handler in the chain. In DevFlow, project approval requests pass from PMApproval to AdminApproval.",
        "code_path": "core/approval_chain.py",
        "usage": None
    },
    {
        "name": "Command Pattern",
        "file": "core/commands.py",
        "description": "The Command pattern encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations. DevFlow uses it to encapsulate task actions (CreateTaskCommand, DeleteTaskCommand).",
        "code_path": "core/commands.py",
        "usage": None
    },
    {
        "name": "Factory Pattern",
        "file": "core/factories.py",
        "description": "The Factory pattern provides an interface for creating objects in a superclass, but allows subclasses or specific factory logic to alter the type of objects that will be created. In DevFlow, UserFactory creates and saves User instances with specific roles.",
        "code_path": "core/factories.py",
        "usage": None
    }
]

def format_code_to_html(code_text):
    html = code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    lines = html.split('\n')
    formatted_lines = []
    for line in lines:
        stripped = line.lstrip(' ')
        num_spaces = len(line) - len(stripped)
        formatted_line = '&nbsp;' * num_spaces + stripped
        formatted_lines.append(formatted_line)
    return '<br/>'.join(formatted_lines)

def get_file_content(relative_path, start_line=1, end_line=None):
    abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)
    if not os.path.exists(abs_path):
        return f"# File not found: {relative_path}"
    with open(abs_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if end_line is None:
        selected_lines = lines[start_line - 1:]
    else:
        selected_lines = lines[start_line - 1:end_line]
    
    # Strip carriage returns and join
    return "".join(selected_lines)

def draw_decorations(canvas, doc):
    if doc.page == 1:
        # Draw a beautiful cover page background
        canvas.saveState()
        canvas.setFillColor(PRIMARY_COLOR)
        canvas.rect(0, 0, 612, 12, fill=True, stroke=False)
        canvas.setFillColor(SECONDARY_COLOR)
        canvas.rect(0, 12, 612, 6, fill=True, stroke=False)
        canvas.restoreState()
        return

    # Draw header and footer on subsequent pages
    canvas.saveState()
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(PRIMARY_COLOR)
    canvas.drawString(54, 755, "DEVFLOW DESIGN PATTERNS DOCUMENTATION")
    
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawRightString(558, 755, "BACKEND ARCHITECTURE REPORT")
    
    canvas.setStrokeColor(BORDER_COLOR)
    canvas.setLineWidth(0.5)
    canvas.line(54, 747, 558, 747)
    
    # Footer
    page_num = canvas.getPageNumber()
    canvas.drawString(54, 36, "Confidential - Internal Developer Reference")
    canvas.drawRightString(558, 36, f"Page {page_num}")
    canvas.line(54, 48, 558, 48)
    canvas.restoreState()

def build_pdf():
    pdf_filename = "Design_Patterns_Report.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=72,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=32,
        leading=38,
        textColor=PRIMARY_COLOR,
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=14,
        leading=18,
        textColor=SECONDARY_COLOR,
        spaceAfter=40
    )
    
    meta_style = ParagraphStyle(
        'CoverMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=TEXT_COLOR,
        spaceAfter=5
    )
    
    heading1_style = ParagraphStyle(
        'Heading1Style',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=PRIMARY_COLOR,
        spaceBefore=15,
        spaceAfter=10,
        keepWithNext=True
    )
    
    heading2_style = ParagraphStyle(
        'Heading2Style',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=SECONDARY_COLOR,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=TEXT_COLOR,
        spaceAfter=8
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        textColor=TITLE_COLOR
    )
    
    story = []
    
    # --- COVER PAGE ---
    story.append(Spacer(1, 100))
    story.append(Paragraph("DEVFLOW CODEBASE", subtitle_style))
    story.append(Paragraph("Design Patterns<br/>Architecture Report", title_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("A comprehensive documentation of structural, creational, and behavioral design patterns implemented within the DevFlow backend application.", body_style))
    story.append(Spacer(1, 150))
    
    import datetime
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    
    story.append(Paragraph(f"<b>Generated On:</b> {current_date}", meta_style))
    story.append(Paragraph("<b>Target System:</b> DevFlow Backend (Python/Django & MongoEngine)", meta_style))
    story.append(Paragraph("<b>Format:</b> Developer Technical Reference Document (PDF)", meta_style))
    story.append(PageBreak())
    
    # --- TABLE OF CONTENTS / SUMMARY ---
    story.append(Paragraph("Executive Summary & Patterns Index", heading1_style))
    summary_text = (
        "This document details the architectural design patterns implemented across the DevFlow backend codebase. "
        "Design patterns improve system maintainability, readability, and scalability. The DevFlow backend adheres to "
        "established enterprise software engineering patterns, facilitating structured state flows, dynamic prioritize handling, "
        "and clean notification propagation. Below is the list of documented patterns:"
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 15))
    
    # Create Table of Patterns
    table_data = [
        [Paragraph("<b>Pattern Name</b>", body_style), Paragraph("<b>Implementation File</b>", body_style), Paragraph("<b>Type</b>", body_style)]
    ]
    
    pattern_types = {
        "Singleton Pattern": "Creational",
        "Factory Pattern": "Creational",
        "Builder Pattern": "Creational",
        "Strategy Pattern": "Behavioral",
        "State Pattern": "Behavioral",
        "Observer Pattern (Core)": "Behavioral",
        "Observer Pattern (Notifications)": "Behavioral",
        "Chain of Responsibility Pattern": "Behavioral",
        "Command Pattern": "Behavioral"
    }
    
    for pat in PATTERNS:
        ptype = pattern_types.get(pat["name"], "Behavioral")
        table_data.append([
            Paragraph(f"<b>{pat['name']}</b>", body_style),
            Paragraph(f"<code>{pat['file']}</code>", body_style),
            Paragraph(ptype, body_style)
        ])
        
    t = Table(table_data, colWidths=[160, 240, 100])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BORDER_COLOR),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, BG_CODE_COLOR]),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,1), (-1,-1), 5),
        ('TOPPADDING', (0,1), (-1,-1), 5),
    ]))
    story.append(t)
    story.append(PageBreak())
    
    # --- DESIGN PATTERNS SECTIONS ---
    for pat in PATTERNS:
        elements = []
        elements.append(Paragraph(pat["name"], heading1_style))
        elements.append(Paragraph(f"<b>File Reference:</b> <code>{pat['file']}</code>", body_style))
        elements.append(Spacer(1, 5))
        elements.append(Paragraph(pat["description"], body_style))
        elements.append(Spacer(1, 10))
        
        # Primary Code Block
        elements.append(Paragraph("<b>Implementation Code:</b>", heading2_style))
        code_content = get_file_content(pat["code_path"])
        formatted_code = format_code_to_html(code_content)
        code_p = Paragraph(formatted_code, code_style)
        
        # Place code inside a single cell table with background color for a nice box effect
        code_table = Table([[code_p]], colWidths=[504])
        code_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), BG_CODE_COLOR),
            ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('LEFTPADDING', (0,0), (-1,-1), 12),
            ('RIGHTPADDING', (0,0), (-1,-1), 12),
            ('TOPPADDING', (0,0), (-1,-1), 10),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ]))
        elements.append(code_table)
        
        # Additional Code Path (e.g. for notifications/observer.py)
        if "additional_code_path" in pat:
            elements.append(Spacer(1, 10))
            elements.append(Paragraph(f"<b>Observer Implementation Code:</b> <code>{pat['additional_code_path']}</code>", heading2_style))
            add_code_content = get_file_content(pat["additional_code_path"])
            add_formatted_code = format_code_to_html(add_code_content)
            add_code_p = Paragraph(add_formatted_code, code_style)
            
            add_code_table = Table([[add_code_p]], colWidths=[504])
            add_code_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), BG_CODE_COLOR),
                ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
                ('LEFTPADDING', (0,0), (-1,-1), 12),
                ('RIGHTPADDING', (0,0), (-1,-1), 12),
                ('TOPPADDING', (0,0), (-1,-1), 10),
                ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ]))
            elements.append(add_code_table)
            
        # Usage Code Block
        if pat["usage"]:
            elements.append(Spacer(1, 10))
            elements.append(Paragraph(f"<b>Usage Context:</b> {pat['usage']['title']}", heading2_style))
            start, end = pat["usage"]["lines"]
            usage_code = get_file_content(pat["usage"]["file"], start, end)
            formatted_usage = format_code_to_html(usage_code)
            usage_p = Paragraph(formatted_usage, code_style)
            
            usage_table = Table([[usage_p]], colWidths=[504])
            usage_table.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")), # Slate-100 for usage distinction
                ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
                ('LEFTPADDING', (0,0), (-1,-1), 12),
                ('RIGHTPADDING', (0,0), (-1,-1), 12),
                ('TOPPADDING', (0,0), (-1,-1), 10),
                ('BOTTOMPADDING', (0,0), (-1,-1), 10),
            ]))
            elements.append(usage_table)
            
        # Use KeepTogether so a single pattern's details are kept on the same page if possible,
        # or we append elements and a PageBreak
        story.append(KeepTogether(elements))
        story.append(Spacer(1, 20))
        story.append(PageBreak())
        
    # Remove the last PageBreak if we don't want an empty page
    if story and isinstance(story[-1], PageBreak):
        story.pop()
        
    doc.build(story, onFirstPage=draw_decorations, onLaterPages=draw_decorations)
    print("PDF Generated successfully: Design_Patterns_Report.pdf")

if __name__ == "__main__":
    build_pdf()
