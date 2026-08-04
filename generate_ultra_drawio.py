import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIAGRAMS_DIR = os.path.join(BASE_DIR, 'diagrams')
os.makedirs(DIAGRAMS_DIR, exist_ok=True)

# 1. ULTRA-DETAILED SYSTEM ARCHITECTURE DRAW.IO XML
sys_arch_xml = """<mxfile host="app.diagrams.net" modified="2026-08-04T12:18:00.000Z" agent="CineIntelligence" version="21.0.0" type="device">
  <diagram id="system-architecture-detailed" name="CineIntelligence System Architecture (Detailed)">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="950" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Main Title -->
        <mxCell id="title" value="CineIntelligence™ Full Technical System Architecture" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=24;fontStyle=1;fontColor=#2563EB;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="600" height="40" as="geometry" />
        </mxCell>

        <!-- Tier 1: Client Presentation Layer -->
        <mxCell id="t1_box" value="1. Client Presentation Layer (Executive Glassmorphism UI)" style="swimlane;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;fontSize=14;fontColor=#1E40AF;" vertex="1" parent="1">
          <mxGeometry x="40" y="90" width="300" height="460" as="geometry" />
        </mxCell>
        <mxCell id="t1_c1" value="Landing Hero View&#10;(Badge, CTA, GSAP Animations)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t1_box">
          <mxGeometry x="20" y="40" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t1_c2" value="Inference Form &amp; Star Cast Pickers&#10;(Pan-India Directors, Actors, Music)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t1_box">
          <mxGeometry x="20" y="110" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t1_c3" value="Multi-Currency Budget Controls&#10;(INR ₹, USD $, EUR €, GBP £)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t1_box">
          <mxGeometry x="20" y="180" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t1_c4" value="52+ Content Themes Checkbox Grid&#10;(Action, Sci-Fi, Cyberpunk, Drama)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t1_box">
          <mxGeometry x="20" y="250" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t1_c5" value="Instant Test Preset Loaders&#10;(🔥 High, ⚡ Medium, ⚠️ Low)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t1_box">
          <mxGeometry x="20" y="320" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t1_c6" value="Dynamic Results View&#10;(Doughnut Chart, Confetti, Advice Card)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t1_box">
          <mxGeometry x="20" y="390" width="260" height="50" as="geometry" />
        </mxCell>

        <!-- Tier 2: Web Server & API Layer -->
        <mxCell id="t2_box" value="2. Web Application &amp; REST API Layer" style="swimlane;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;fontSize=14;fontColor=#14532D;" vertex="1" parent="1">
          <mxGeometry x="390" y="90" width="310" height="460" as="geometry" />
        </mxCell>
        <mxCell id="t2_c1" value="Flask WSGI Application&#10;(app_flask.py - Port 5000 / Vercel)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t2_box">
          <mxGeometry x="25" y="40" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t2_c2" value="Streamlit Server Engine&#10;(app.py / streamlit_app.py - Port 8501)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t2_box">
          <mxGeometry x="25" y="110" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t2_c3" value="REST Router &amp; Payload Validator&#10;(POST /api/predict)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t2_box">
          <mxGeometry x="25" y="180" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t2_c4" value="Jinja2 Template Renderer&#10;(index.html, app.html, about.html)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t2_box">
          <mxGeometry x="25" y="250" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t2_c5" value="Static Asset Handler&#10;(style.css, main.js, logo.jpg)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t2_box">
          <mxGeometry x="25" y="320" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t2_c6" value="JSON Serializer &amp; Error Handler" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t2_box">
          <mxGeometry x="25" y="390" width="260" height="50" as="geometry" />
        </mxCell>

        <!-- Tier 3: Feature Engineering & Preprocessor Layer -->
        <mxCell id="t3_box" value="3. Feature Engineering &amp; Preprocessing Engine" style="swimlane;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;fontSize=14;fontColor=#78350F;" vertex="1" parent="1">
          <mxGeometry x="750" y="90" width="310" height="460" as="geometry" />
        </mxCell>
        <mxCell id="t3_c1" value="Pan-India Star Synergy Engine&#10;(Director, Actor, Music indices 1.0-10.0)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t3_box">
          <mxGeometry x="25" y="40" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t3_c2" value="Multi-Currency USD Scaling&#10;(FX rate conversion &amp; Log budget transform)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t3_box">
          <mxGeometry x="25" y="110" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t3_c3" value="52+ Journal Theme Vectorizer&#10;(One-Hot binary theme flags)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t3_box">
          <mxGeometry x="25" y="180" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t3_c4" value="Runtime Classification Flag&#10;(is_short_film &lt; 40 mins)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t3_box">
          <mxGeometry x="25" y="250" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t3_c5" value="66-Dimensional Feature Vector" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t3_box">
          <mxGeometry x="25" y="320" width="260" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t3_c6" value="Scikit-Learn Preprocessor Pipeline&#10;(MedianImputer + StandardScaler)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t3_box">
          <mxGeometry x="25" y="390" width="260" height="50" as="geometry" />
        </mxCell>

        <!-- Tier 4: ML Inference & Artifact Storage Layer -->
        <mxCell id="t4_box" value="4. ML Inference &amp; Storage Layer" style="swimlane;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;fontSize=14;fontColor=#1E40AF;" vertex="1" parent="1">
          <mxGeometry x="1110" y="90" width="250" height="460" as="geometry" />
        </mxCell>
        <mxCell id="t4_c1" value="Gradient Boosting Classifier&#10;(best_model.joblib)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t4_box">
          <mxGeometry x="15" y="40" width="220" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t4_c2" value="Probability Estimator&#10;[P(High), P(Medium), P(Low)]" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t4_box">
          <mxGeometry x="15" y="120" width="220" height="50" as="geometry" />
        </mxCell>
        <mxCell id="t4_c3" value="Strategic Advice Matrix&#10;(Action Badges &amp; Marketing %)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="t4_box">
          <mxGeometry x="15" y="200" width="220" height="50" as="geometry" />
        </mxCell>

        <!-- Connector Arrows -->
        <mxCell id="ca1" value="HTTP POST /api/predict" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#2563EB;strokeWidth=2;fontStyle=1;fontSize=11;" edge="1" parent="1" source="t1_box" target="t2_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="ca2" value="Raw Input Payload" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#16A34A;strokeWidth=2;fontStyle=1;fontSize=11;" edge="1" parent="1" source="t2_box" target="t3_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="ca3" value="Transformed Vector" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#D97706;strokeWidth=2;fontStyle=1;fontSize=11;" edge="1" parent="1" source="t3_box" target="t4_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

# 2. ULTRA-DETAILED USER FLOW DRAW.IO XML
user_flow_xml = """<mxfile host="app.diagrams.net" modified="2026-08-04T12:18:00.000Z" agent="CineIntelligence" version="21.0.0" type="device">
  <diagram id="user-flow-detailed" name="CineIntelligence User Journey Flow (Detailed)">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="950" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <mxCell id="u_title" value="CineIntelligence™ Comprehensive User Interaction Flowchart" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=22;fontStyle=1;fontColor=#2563EB;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="600" height="40" as="geometry" />
        </mxCell>

        <mxCell id="u1" value="1. User Visits Platform&#10;(http://localhost:5000 / Vercel)" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="100" width="220" height="70" as="geometry" />
        </mxCell>

        <mxCell id="u2" value="Page Choice?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="340" y="85" width="160" height="100" as="geometry" />
        </mxCell>

        <mxCell id="u3_home" value="Explore Landing Page&#10;(Hero, Feature Cards, Counters)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="320" y="240" width="200" height="50" as="geometry" />
        </mxCell>

        <mxCell id="u3_about" value="Explore About Page&#10;(Benchmarks Table, EDA Inspector)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="320" y="320" width="200" height="50" as="geometry" />
        </mxCell>

        <mxCell id="u3_app" value="Prediction Engine Dashboard&#10;(/app)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="105" width="220" height="60" as="geometry" />
        </mxCell>

        <mxCell id="u4_preset" value="Input Mode Choice?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="850" y="85" width="170" height="100" as="geometry" />
        </mxCell>

        <mxCell id="u5_p1" value="Click '🔥 High Test' Preset&#10;(Vikram 2: ₹180 Cr Action Thriller)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1080" y="40" width="250" height="50" as="geometry" />
        </mxCell>
        <mxCell id="u5_p2" value="Click '⚡ Medium Test' Preset&#10;(Chai &amp; Conversations: ₹12 Cr Drama)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1080" y="110" width="250" height="50" as="geometry" />
        </mxCell>
        <mxCell id="u5_p3" value="Click '⚠️ Low Test' Preset&#10;(B-Grade Horror: ₹35 Lakhs)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FEF2F2;strokeColor=#EF4444;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1080" y="180" width="250" height="50" as="geometry" />
        </mxCell>

        <mxCell id="u6_submit" value="Click 'Execute Inference &amp; Strategy Generation'" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#2563EB;strokeColor=#1E40AF;fontStyle=1;fontColor=#FFFFFF;" vertex="1" parent="1">
          <mxGeometry x="810" y="270" width="250" height="60" as="geometry" />
        </mxCell>

        <mxCell id="u7_exec" value="GSAP Loading Pulse &amp; POST /api/predict Request" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="810" y="370" width="250" height="50" as="geometry" />
        </mxCell>

        <mxCell id="u8_decision" value="Predicted Category Output?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="830" y="460" width="210" height="100" as="geometry" />
        </mxCell>

        <mxCell id="u9_high" value="High Quality (≥ 7.5)&#10;Confetti Fireworks 🎆 + Greenlight Badge" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="540" y="600" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="u9_med" value="Medium Quality (5.5 - 7.4)&#10;Yellow Warning Badge + SVOD Catalog" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="815" y="600" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="u9_low" value="Low Quality (&lt; 5.5)&#10;Red Risk Badge + Pass Status" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FEF2F2;strokeColor=#EF4444;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1090" y="600" width="240" height="60" as="geometry" />
        </mxCell>

        <mxCell id="u10_scroll" value="Smooth Scroll Offset 90px Below Fixed Navbar &amp; Chart Render" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="780" y="710" width="310" height="70" as="geometry" />
        </mxCell>

        <!-- Arrows -->
        <mxCell id="ar1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="u1" target="u2" />
        <mxCell id="ar2" value="Home" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#64748B;" edge="1" parent="1" source="u2" target="u3_home" />
        <mxCell id="ar3" value="About" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#64748B;" edge="1" parent="1" source="u2" target="u3_about" />
        <mxCell id="ar4" value="App" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="u2" target="u3_app" />
        <mxCell id="ar5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="u3_app" target="u4_preset" />
        <mxCell id="ar6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="u4_preset" target="u5_p1" />
        <mxCell id="ar7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#D97706;" edge="1" parent="1" source="u4_preset" target="u5_p2" />
        <mxCell id="ar8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#EF4444;" edge="1" parent="1" source="u4_preset" target="u5_p3" />
        <mxCell id="ar9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="u5_p1" target="u6_submit" />
        <mxCell id="ar10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="u6_submit" target="u7_exec" />
        <mxCell id="ar11" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="u7_exec" target="u8_decision" />
        <mxCell id="ar12" value="High" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="u8_decision" target="u9_high" />
        <mxCell id="ar13" value="Medium" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#D97706;" edge="1" parent="1" source="u8_decision" target="u9_med" />
        <mxCell id="ar14" value="Low" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#EF4444;" edge="1" parent="1" source="u8_decision" target="u9_low" />
        <mxCell id="ar15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="u9_high" target="u10_scroll" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

# 3. ULTRA-DETAILED DATA FLOW DRAW.IO XML
data_flow_xml = """<mxfile host="app.diagrams.net" modified="2026-08-04T12:18:00.000Z" agent="CineIntelligence" version="21.0.0" type="device">
  <diagram id="data-flow-detailed" name="CineIntelligence Data Flow (Detailed)">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="950" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <mxCell id="d_title" value="CineIntelligence™ Complete Data Flow &amp; Feature Vectorization Matrix" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=22;fontStyle=1;fontColor=#2563EB;" vertex="1" parent="1">
          <mxGeometry x="350" y="20" width="700" height="40" as="geometry" />
        </mxCell>

        <mxCell id="d1" value="Client Form Payload (JSON)&#10;title, director_name, lead_actor, currency, budget_val, content_themes" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="100" width="280" height="70" as="geometry" />
        </mxCell>

        <mxCell id="d2" value="Pan-India Star Synergy Engine&#10;Lookup S_director, S_actor, S_actress, S_music, S_banner&#10;Compute Synergy = S_director x S_cast" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="95" width="260" height="80" as="geometry" />
        </mxCell>

        <mxCell id="d3" value="Multi-Currency USD Normalizer&#10;Convert (INR ₹, USD $, EUR €, GBP £) &#10;Compute log_budget = ln(budget_usd + 1)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="660" y="95" width="260" height="80" as="geometry" />
        </mxCell>

        <mxCell id="d4" value="52+ Journal Theme Vectorizer&#10;One-Hot binary encoding [1, 0, 0, 1, ...]" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="960" y="95" width="240" height="80" as="geometry" />
        </mxCell>

        <mxCell id="d5" value="66-Dimensional Feature Vector Array (X)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="360" y="240" width="560" height="60" as="geometry" />
        </mxCell>

        <mxCell id="d6" value="Scikit-Learn Preprocessor Pipeline&#10;(Median SimpleImputer + StandardScaler)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="340" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="d7" value="Gradient Boosting Classifier&#10;(best_model.joblib)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="660" y="340" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="d8" value="Probability Distribution Map&#10;{ High: p1, Medium: p2, Low: p3 }" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="440" width="260" height="60" as="geometry" />
        </mxCell>

        <mxCell id="d9" value="Commercial Strategic Advice Engine&#10;{ Action Badge, Marketing Spend %, Platform Placement }" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="650" y="440" width="310" height="60" as="geometry" />
        </mxCell>

        <mxCell id="d10" value="REST JSON Response Payload &amp; DOM Render&#10;(Chart.js Doughnut Chart + Confetti + Strategic Cards)" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="460" y="540" width="360" height="80" as="geometry" />
        </mxCell>

        <!-- Connections -->
        <mxCell id="dc1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="d1" target="d2" />
        <mxCell id="dc2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#D97706;" edge="1" parent="1" source="d2" target="d3" />
        <mxCell id="dc3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#D97706;" edge="1" parent="1" source="d3" target="d4" />
        <mxCell id="dc4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="d4" target="d5" />
        <mxCell id="dc5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="d5" target="d6" />
        <mxCell id="dc6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="d6" target="d7" />
        <mxCell id="dc7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="d7" target="d8" />
        <mxCell id="dc8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="d7" target="d9" />
        <mxCell id="dc9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="d8" target="d10" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

with open(os.path.join(DIAGRAMS_DIR, 'system_architecture.drawio'), 'w', encoding='utf-8') as f:
    f.write(sys_arch_xml)

with open(os.path.join(DIAGRAMS_DIR, 'user_flow.drawio'), 'w', encoding='utf-8') as f:
    f.write(user_flow_xml)

with open(os.path.join(DIAGRAMS_DIR, 'data_flow.drawio'), 'w', encoding='utf-8') as f:
    f.write(data_flow_xml)

print("Saved all 3 ultra-detailed Draw.io files in diagrams/ folder!")
