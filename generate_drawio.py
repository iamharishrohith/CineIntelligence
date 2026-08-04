import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIAGRAMS_DIR = os.path.join(BASE_DIR, 'diagrams')
os.makedirs(DIAGRAMS_DIR, exist_ok=True)

# 1. System Architecture Draw.io XML
sys_arch_xml = """<mxfile host="app.diagrams.net" modified="2026-08-04T12:15:00.000Z" agent="CineIntelligence" version="21.0.0" type="device">
  <diagram id="system-architecture" name="CineIntelligence System Architecture">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <mxCell id="title" value="CineIntelligence™ System Architecture" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=22;fontStyle=1;fontColor=#2563EB;" vertex="1" parent="1">
          <mxGeometry x="300" y="20" width="500" height="40" as="geometry" />
        </mxCell>
        
        <mxCell id="client_box" value="Client Presentation Layer (Executive Glassmorphism UI)" style="swimlane;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;fontSize=14;fontColor=#1E40AF;" vertex="1" parent="1">
          <mxGeometry x="40" y="90" width="260" height="240" as="geometry" />
        </mxCell>
        <mxCell id="client_u1" value="Landing Hero &amp; Feature Showcase" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="client_box">
          <mxGeometry x="20" y="40" width="220" height="40" as="geometry" />
        </mxCell>
        <mxCell id="client_u2" value="Inference Form &amp; Test Presets" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="client_box">
          <mxGeometry x="20" y="100" width="220" height="40" as="geometry" />
        </mxCell>
        <mxCell id="client_u3" value="Doughnut Chart &amp; Strategic Matrix" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="client_box">
          <mxGeometry x="20" y="160" width="220" height="40" as="geometry" />
        </mxCell>

        <mxCell id="api_box" value="API &amp; Backend Controller (Flask / Streamlit)" style="swimlane;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;fontSize=14;fontColor=#14532D;" vertex="1" parent="1">
          <mxGeometry x="370" y="90" width="260" height="240" as="geometry" />
        </mxCell>
        <mxCell id="api_u1" value="Flask REST Controller (app_flask.py)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="api_box">
          <mxGeometry x="20" y="40" width="220" height="40" as="geometry" />
        </mxCell>
        <mxCell id="api_u2" value="Streamlit Engine (app.py)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="api_box">
          <mxGeometry x="20" y="100" width="220" height="40" as="geometry" />
        </mxCell>

        <mxCell id="ml_box" value="Feature Engineering &amp; ML Inference Engine" style="swimlane;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;fontSize=14;fontColor=#78350F;" vertex="1" parent="1">
          <mxGeometry x="700" y="90" width="280" height="240" as="geometry" />
        </mxCell>
        <mxCell id="ml_u1" value="Star Synergy &amp; Currency Scaling (66D)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="ml_box">
          <mxGeometry x="20" y="40" width="240" height="40" as="geometry" />
        </mxCell>
        <mxCell id="ml_u2" value="Gradient Boosting Model (best_model.joblib)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#CBD5E1;fontStyle=1;" vertex="1" parent="ml_box">
          <mxGeometry x="20" y="100" width="240" height="40" as="geometry" />
        </mxCell>

        <mxCell id="conn1" value="POST /api/predict" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#2563EB;strokeWidth=2;fontStyle=1;fontSize=11;" edge="1" parent="1" source="client_box" target="api_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="conn2" value="Execute Predictor Engine" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#16A34A;strokeWidth=2;fontStyle=1;fontSize=11;" edge="1" parent="1" source="api_box" target="ml_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

# 2. User Flow Draw.io XML
user_flow_xml = """<mxfile host="app.diagrams.net" modified="2026-08-04T12:15:00.000Z" agent="CineIntelligence" version="21.0.0" type="device">
  <diagram id="user-flow" name="CineIntelligence User Journey Flow">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <mxCell id="uf_title" value="CineIntelligence™ User Journey Flowchart" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontStyle=1;fontColor=#2563EB;" vertex="1" parent="1">
          <mxGeometry x="300" y="20" width="500" height="40" as="geometry" />
        </mxCell>

        <mxCell id="u_s1" value="1. User Arrives at Platform" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="80" y="100" width="180" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="u_s2" value="2. Select Mode (Preset vs Custom)" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="320" y="80" width="200" height="100" as="geometry" />
        </mxCell>

        <mxCell id="u_s3" value="3. Form Pre-Filled / Submitted" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="570" y="100" width="200" height="60" as="geometry" />
        </mxCell>

        <mxCell id="u_s4" value="4. Model Inference &amp; Probability Chart Rendered" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="820" y="100" width="240" height="60" as="geometry" />
        </mxCell>

        <mxCell id="uc1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="u_s1" target="u_s2" />
        <mxCell id="uc2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#D97706;" edge="1" parent="1" source="u_s2" target="u_s3" />
        <mxCell id="uc3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="u_s3" target="u_s4" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

# 3. Data Flow Draw.io XML
data_flow_xml = """<mxfile host="app.diagrams.net" modified="2026-08-04T12:15:00.000Z" agent="CineIntelligence" version="21.0.0" type="device">
  <diagram id="data-flow" name="CineIntelligence Data Flow">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="850" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <mxCell id="df_title" value="CineIntelligence™ Data Pipeline Flowchart" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=20;fontStyle=1;fontColor=#2563EB;" vertex="1" parent="1">
          <mxGeometry x="300" y="20" width="500" height="40" as="geometry" />
        </mxCell>

        <mxCell id="d_s1" value="Raw JSON Payload" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="100" width="160" height="60" as="geometry" />
        </mxCell>

        <mxCell id="d_s2" value="Star Synergy &amp; Currency Engine" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="270" y="100" width="200" height="60" as="geometry" />
        </mxCell>

        <mxCell id="d_s3" value="66D Feature Vector" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FDF4;strokeColor=#16A34A;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="520" y="100" width="160" height="60" as="geometry" />
        </mxCell>

        <mxCell id="d_s4" value="Scikit-Learn Gradient Boosting" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#2563EB;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="730" y="100" width="200" height="60" as="geometry" />
        </mxCell>

        <mxCell id="dc1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#2563EB;" edge="1" parent="1" source="d_s1" target="d_s2" />
        <mxCell id="dc2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#D97706;" edge="1" parent="1" source="d_s2" target="d_s3" />
        <mxCell id="dc3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;strokeColor=#16A34A;" edge="1" parent="1" source="d_s3" target="d_s4" />
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

print("Saved all 3 Draw.io files in diagrams/ folder!")
