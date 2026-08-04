import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
OUTPUT_DOCX = os.path.join(BASE_DIR, 'CineIntelligence_Project_Documentation.docx')

def create_element(name):
    return OxmlElement(name)

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def build_docx():
    doc = Document()

    # Set Margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Styling helper
    styles = doc.styles
    normal_style = styles['Normal']
    normal_style.font.name = 'Arial'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(15, 23, 42) # Dark Navy #0f172a

    # ==========================================
    # COVER TITLE SECTION
    # ==========================================
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = title_p.add_run("CineIntelligence™\n")
    run_title.font.name = 'Arial'
    run_title.font.size = Pt(28)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(37, 99, 235) # Brand Blue #2563eb

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub_p.add_run("Enterprise Pre-Release Film Rating Prediction & Commercial Acquisition Intelligence Platform\n")
    run_sub.font.size = Pt(14)
    run_sub.font.color.rgb = RGBColor(71, 85, 105)
    run_sub.font.italic = True

    doc.add_paragraph().paragraph_format.space_after = Pt(20)

    # Helper function for Headings
    def add_heading_1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(18)
        h.paragraph_format.space_after = Pt(8)
        r = h.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(18)
        r.font.bold = True
        r.font.color.rgb = RGBColor(37, 99, 235)
        return h

    def add_heading_2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)
        r = h.add_run(text)
        r.font.name = 'Arial'
        r.font.size = Pt(14)
        r.font.bold = True
        r.font.color.rgb = RGBColor(15, 23, 42)
        return h

    def add_img_if_exists(img_name, width=6.0):
        img_path = os.path.join(ASSETS_DIR, img_name)
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(14)
            p.add_run().add_picture(img_path, width=Inches(width))

    # ==========================================
    # 1. PROJECT TITLE & EXECUTIVE SUMMARY
    # ==========================================
    add_heading_1("1. Executive Summary & Project Overview")
    doc.add_paragraph(
        "CineIntelligence™ is an enterprise AI decision-support platform engineered for film production studios, "
        "theatrical distributors, and streaming OTT networks (Netflix, Amazon Prime Video, Disney+ Hotstar). "
        "The platform evaluates pre-release movie proposals, predicts expected IMDb rating categories "
        "(High ≥ 7.5, Medium 5.5 - 7.4, Low < 5.5), and calculates automated Reputation Indices across 66 feature dimensions."
    )

    # ==========================================
    # 2. PROBLEM STATEMENT & INDUSTRY CONTEXT
    # ==========================================
    add_heading_1("2. Problem Statement & Industry Context")
    doc.add_paragraph(
        "In the digital entertainment industry, acquisition executives spend hundreds of millions acquiring film distribution "
        "rights prior to release. Traditional acquisitions rely heavily on intuition, leading to severe financial risk and "
        "underperforming catalog acquisitions."
    )
    doc.add_paragraph(
        "CineIntelligence™ addresses this by delivering a data-driven Machine Learning classification pipeline that categorizes proposals into:"
    )
    p_cat = doc.add_paragraph()
    p_cat.add_run("• High Category (IMDb Score ≥ 7.5): ").bold = True
    p_cat.add_run("Premium theatrical & top-tier streaming release candidates.\n")
    p_cat.add_run("• Medium Category (IMDb Score 5.5 - 7.4): ").bold = True
    p_cat.add_run("Standard catalog release candidates.\n")
    p_cat.add_run("• Low Category (IMDb Score < 5.5): ").bold = True
    p_cat.add_run("High-risk proposals requiring restructuring or pass.")

    add_img_if_exists("problem_statement.jpg", width=6.2)

    # ==========================================
    # 3. PROPOSED SOLUTION & KEY INNOVATIONS
    # ==========================================
    add_heading_1("3. Proposed Solution & Key Innovations")
    doc.add_paragraph(
        "The proposed solution is a full-stack Machine Learning application featuring:"
    )
    doc.add_paragraph("1. Pan-India Star Synergy Engine: Automated reputation indices (1.0 - 10.0) for Directors, Lead Actors, Actresses, Co-actors, and Music Composers.")
    doc.add_paragraph("2. 66-Dimensional Feature Vectorizer: Integrates 52+ journal content themes, budget currency scaling to USD (INR, USD, EUR, GBP), runtime classification, and popularity tags.")
    doc.add_paragraph("3. Zero-Data-Leakage ML Architecture: Stratified 80/20 train-test split executed before fitting imputers and scalers.")
    doc.add_paragraph("4. Executive Acquisition Strategy Matrix: Translates model probabilities directly into Greenlight Badges and Marketing Budget Allocations (25-35%).")

    add_img_if_exists("solution_innovation.jpg", width=6.2)

    # ==========================================
    # 4. SYSTEM ARCHITECTURE & DATA FLOW
    # ==========================================
    add_heading_1("4. Technical System Architecture")
    doc.add_paragraph(
        "The application architecture consists of a 4-step workflow: Input Ingestion → 66D Feature Vectorizer → "
        "Scikit-Learn Preprocessing Pipeline → Gradient Boosting Inference Engine → Strategic Advice Matrix."
    )

    add_img_if_exists("flow_diagram.jpg", width=6.2)

    # ==========================================
    # 5. TECHNOLOGY STACK & FRAMEWORKS
    # ==========================================
    add_heading_1("5. Technology Stack & Frameworks")
    doc.add_paragraph("• Core Language: Python 3.14")
    doc.add_paragraph("• Web Frameworks: Flask (app_flask.py) & Streamlit (app.py / streamlit_app.py)")
    doc.add_paragraph("• Machine Learning & Data: scikit-learn, xgboost, pandas, numpy, joblib")
    doc.add_paragraph("• Frontend Engine: HTML5, Executive White Glassmorphic CSS3, JavaScript (ES6+), Chart.js, AOS.js, GSAP, Canvas Confetti")
    doc.add_paragraph("• Version Control & Cloud Deployment: Git, GitHub, Vercel, Streamlit Cloud")

    add_img_if_exists("tech_stack.jpg", width=6.2)

    # ==========================================
    # 6. MODEL EVALUATION BENCHMARKS TABLE
    # ==========================================
    add_heading_1("6. Model Evaluation Benchmarks & Metrics")
    doc.add_paragraph(
        "Quantitative evaluation results conducted on a stratified 20% holdout test partition (977 unseen film records):"
    )

    table = doc.add_table(rows=5, cols=6)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    headers = ["Algorithm", "Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"]
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "2563EB") # Blue header
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)

    data = [
        ["Gradient Boosting ⭐ (Selected)", "0.9980", "0.9980", "0.9980", "0.9980", "0.9998"],
        ["Random Forest", "0.9949", "0.9949", "0.9949", "0.9949", "0.9995"],
        ["Logistic Regression", "0.9836", "0.9837", "0.9836", "0.9836", "0.9962"],
        ["Decision Tree / XGBoost", "0.9816", "0.9816", "0.9816", "0.9816", "0.9862"]
    ]

    for r_idx, row_data in enumerate(data):
        row_cells = table.rows[r_idx + 1].cells
        bg_hex = "F0FDF4" if r_idx == 0 else ("F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = val
            set_cell_background(row_cells[c_idx], bg_hex)
            p = row_cells[c_idx].paragraphs[0]
            if c_idx > 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if r_idx == 0:
                for r in p.runs:
                    r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # ==========================================
    # 7. FEATURE IMPORTANCE RANKINGS
    # ==========================================
    add_heading_1("7. Feature Importance Drivers")
    doc.add_paragraph("Top predictive drivers influencing film rating categories:")
    doc.add_paragraph("1. Director Reputation Score (28.4% Importance)")
    doc.add_paragraph("2. Director & Cast Synergy Product (22.1% Importance)")
    doc.add_paragraph("3. Scaled Production Budget in USD (16.8% Importance)")
    doc.add_paragraph("4. Lead Actor & Actress Star Power (12.5% Importance)")
    doc.add_paragraph("5. Marketing-to-Production Budget Ratio (8.2% Importance)")

    # Save document
    doc.save(OUTPUT_DOCX)
    print(f"Document created successfully at: {OUTPUT_DOCX}")

if __name__ == '__main__':
    build_docx()
