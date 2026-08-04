import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
OUTPUT_DOCX = os.path.join(BASE_DIR, 'CineIntelligence_Complete_Documentation.docx')
OUTPUT_DOCX_ALT = os.path.join(BASE_DIR, 'CineIntelligence_Project_Documentation.docx')

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def build_ultra_detailed_docx():
    doc = Document()

    # Set Margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base Font Setup
    styles = doc.styles
    normal_style = styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(15, 23, 42)

    # Helper Functions
    def add_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(26)
        r.font.bold = True
        r.font.color.rgb = RGBColor(37, 99, 235)
        return p

    def add_subtitle(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(13)
        r.font.italic = True
        r.font.color.rgb = RGBColor(71, 85, 105)
        return p

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(20)
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(17)
        r.font.bold = True
        r.font.color.rgb = RGBColor(37, 99, 235)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = RGBColor(15, 23, 42)
        return p

    def add_bullet(title, body):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(4)
        r_t = p.add_run(title + ": ")
        r_t.bold = True
        r_t.font.color.rgb = RGBColor(15, 23, 42)
        r_b = p.add_run(body)
        r_b.font.color.rgb = RGBColor(71, 85, 105)
        return p

    def add_img(img_name, width=6.2):
        path = os.path.join(ASSETS_DIR, img_name)
        if os.path.exists(path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(14)
            p.add_run().add_picture(path, width=Inches(width))

    def add_flowchart_box(title, steps):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(12)
        
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.rows[0].cells[0]
        set_cell_background(cell, "EFF6FF")
        
        cp = cell.paragraphs[0]
        r_head = cp.add_run(f"📌 {title}\n")
        r_head.bold = True
        r_head.font.size = Pt(11)
        r_head.font.color.rgb = RGBColor(37, 99, 235)
        
        for idx, step in enumerate(steps):
            arrow = " ➔ " if idx < len(steps) - 1 else ""
            r_step = cp.add_run(f"[{step}]" + arrow)
            r_step.font.size = Pt(10)
            r_step.font.color.rgb = RGBColor(15, 23, 42)

    # TITLE & METADATA
    add_title("CineIntelligence™\n")
    add_subtitle("Enterprise Pre-Release Film Rating Prediction & Commercial Acquisition Intelligence Platform\nDetailed Technical, Architectural & Flowchart Specification Report\n")
    
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ["Project Author / Lead", "Harish Rohith (iamharishrohith@gmail.com)"],
        ["Platform Architecture", "Flask (REST API + Glassmorphic UI) & Streamlit"],
        ["Machine Learning Engine", "Scikit-Learn Gradient Boosting Classifier (0.9980 F1)"],
        ["GitHub Repository", "https://github.com/iamharishrohith/CineIntelligence"]
    ]
    for idx, (k, v) in enumerate(meta_data):
        r_cells = meta_table.rows[idx].cells
        r_cells[0].text = k
        r_cells[1].text = v
        set_cell_background(r_cells[0], "EFF6FF")
        set_cell_background(r_cells[1], "F8FAFC")
        r_cells[0].paragraphs[0].runs[0].font.bold = True
    
    doc.add_paragraph().paragraph_format.space_after = Pt(18)

    # 1. EXECUTIVE SUMMARY
    add_h1("1. Executive Summary & Vision")
    doc.add_paragraph(
        "CineIntelligence™ is a state-of-the-art enterprise AI decision-support platform engineered specifically "
        "for theatrical film distributors, OTT streaming networks (Netflix, Amazon Prime Video, Disney+ Hotstar), "
        "and independent film production studios. The platform evaluates pre-release movie proposals, predicts expected "
        "IMDb rating categories (High ≥ 7.5, Medium 5.5 - 7.4, Low < 5.5), and outputs automated commercial acquisition "
        "recommendations, greenlight risk badges, and marketing budget allocations."
    )

    # 2. PROBLEM STATEMENT
    add_h1("2. Problem Statement & Financial Risk Analysis")
    doc.add_paragraph(
        "In the global entertainment and film distribution industry, content acquisition executives spend millions "
        "acquiring theatrical and streaming distribution rights long before a film is completed or released to audiences. "
        "Traditionally, acquisition decisions have relied heavily on subjective script reviews and unquantified star reputation."
    )
    add_img("problem_statement.jpg", width=6.2)

    # 3. USER FLOWCHART & INTERACTION DIAGRAM
    add_h1("3. User Interaction & Journey Flowchart")
    doc.add_paragraph(
        "The user flow defines how acquisition executives, studio heads, and producers navigate the system from initial landing to final recommendation rendering:"
    )

    add_flowchart_box(
        "User Journey Flowchart",
        [
            "User Arrives at Platform",
            "Select Page (Home / App / About)",
            "Select Input Mode (Instant Preset vs Manual Input)",
            "Form Pre-filled / Submitted",
            "POST /api/predict Execution",
            "Category Output (High / Medium / Low)",
            "Doughnut Chart & Strategic Acquisition Advice Rendered"
        ]
    )

    # 4. PROPOSED SOLUTION & INNOVATIONS
    add_h1("4. Proposed Solution & Key Innovations")
    add_img("solution_innovation.jpg", width=6.2)
    add_bullet("1. Pan-India Star Synergy Engine", "Computes dynamic reputation indices (1.0 - 10.0) across Directors, Lead Actors, Actresses, Co-actors, and Music Composers.")
    add_bullet("2. Multi-Currency Global Budget Converter", "Supports budget inputs across 4 currencies (INR ₹, USD $, EUR €, GBP £) and 4 units (Crores, Lakhs, Millions, Thousands).")
    add_bullet("3. 52+ Journal Content Theme Vectorizer", "Vectorizes 52 multi-select journal content themes and popularity driver tags.")

    # 5. DATA FLOWCHART & PIPELINE ARCHITECTURE
    add_h1("5. End-to-End Data Flowchart & Pipeline Architecture")
    doc.add_paragraph(
        "The data flow defines the movement and transformation of data from client form inputs to 66-dimensional feature vectors, preprocessing, ML inference, and strategic output:"
    )

    add_flowchart_box(
        "Data Flowchart Architecture",
        [
            "Form Inputs JSON Payload",
            "Star Synergy Index Lookup",
            "Multi-Currency USD Scaling",
            "52+ Theme Vectorizer",
            "66D Feature Vector",
            "Scikit-Learn Preprocessor",
            "Gradient Boosting Inference",
            "Category Probabilities",
            "Strategic Advice Matrix Response"
        ]
    )

    add_img("flow_diagram.jpg", width=6.2)

    # 6. MACHINE LEARNING WORKFLOW FLOWCHART
    add_h1("6. Machine Learning Model Training Workflow Flowchart")
    doc.add_paragraph(
        "The machine learning lifecycle flow ensures rigorous model benchmarking and zero data leakage:"
    )

    add_flowchart_box(
        "Machine Learning Workflow Flowchart",
        [
            "Data Ingestion (4,883 Records)",
            "Data Cleaning & Imputation",
            "Domain Feature Engineering (66D)",
            "Stratified 80/20 Train-Test Split",
            "Fit Imputer + OneHot + Scaler on Train Set ONLY",
            "Multi-Model Benchmarking (GB, RF, LR, XGB)",
            "Metric Evaluation (Accuracy: 0.9980, F1: 0.9980)",
            "Artifact Serialization (best_model.joblib)"
        ]
    )

    # 7. TECH STACK
    add_h1("7. Technology Stack & Frameworks")
    add_img("tech_stack.jpg", width=6.2)

    # 8. MODEL EVALUATION BENCHMARKS TABLE
    add_h1("8. Model Evaluation Benchmarks & Metrics")
    bench_table = doc.add_table(rows=5, cols=6)
    bench_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    b_headers = ["Algorithm", "Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"]
    for i, title in enumerate(b_headers):
        cell = bench_table.rows[0].cells[i]
        cell.text = title
        set_cell_background(cell, "2563EB")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    b_data = [
        ["Gradient Boosting ⭐ (Selected)", "0.9980", "0.9980", "0.9980", "0.9980", "0.9998"],
        ["Random Forest", "0.9949", "0.9949", "0.9949", "0.9949", "0.9995"],
        ["Logistic Regression", "0.9836", "0.9837", "0.9836", "0.9836", "0.9962"],
        ["Decision Tree / XGBoost", "0.9816", "0.9816", "0.9816", "0.9816", "0.9862"]
    ]

    for r_idx, row in enumerate(b_data):
        row_cells = bench_table.rows[r_idx + 1].cells
        bg_hex = "F0FDF4" if r_idx == 0 else ("F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = val
            set_cell_background(row_cells[c_idx], bg_hex)
            p = row_cells[c_idx].paragraphs[0]
            if c_idx > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if r_idx == 0:
                for r in p.runs:
                    r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # 9. COMMERCIAL ACQUISITION STRATEGY MATRIX
    add_h1("9. Commercial Acquisition Strategy Matrix")
    strat_table = doc.add_table(rows=4, cols=4)
    strat_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    s_headers = ["Predicted Category", "Action Badge", "Marketing Spend %", "Platform Placement"]
    for i, title in enumerate(s_headers):
        cell = strat_table.rows[0].cells[i]
        cell.text = title
        set_cell_background(cell, "2563EB")
        p = cell.paragraphs[0]
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    s_data = [
        ["High Quality (≥ 7.5)", "Greenlight / Instant Acquisition", "25% - 35% of Budget", "Prime-Time Digital Premiere & Global Theatrical"],
        ["Medium Quality (5.5 - 7.4)", "Conditional Acquisition", "10% - 20% of Budget", "SVOD Standard Catalog & Regional Theatrical"],
        ["Low Quality (< 5.5)", "Pass / High Risk Acquisition", "Minimal (< 5%)", "Ad-Supported AVOD / Licensing Fee Discount"]
    ]

    for r_idx, row in enumerate(s_data):
        row_cells = strat_table.rows[r_idx + 1].cells
        bg_hex = "F0FDF4" if r_idx == 0 else ("FFFBEB" if r_idx == 1 else "FEF2F2")
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = val
            set_cell_background(row_cells[c_idx], bg_hex)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # Save safely
    try:
        doc.save(OUTPUT_DOCX)
        print(f"Document saved at: {OUTPUT_DOCX}")
    except Exception as e:
        print(f"Locked output, saving to alternate path: {e}")
        doc.save(OUTPUT_DOCX_ALT)
        print(f"Document saved at alternate: {OUTPUT_DOCX_ALT}")

if __name__ == '__main__':
    build_ultra_detailed_docx()
