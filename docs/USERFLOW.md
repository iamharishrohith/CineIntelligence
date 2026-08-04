# User Flow & Interaction Journey

## 🗺️ System Navigation Map
CineIntelligence™ provides a simple 3-page user architecture:
1. **`Home Landing Page` (`/`)**: High-impact hero section, feature showcase, metrics, and application CTA.
2. **`Prediction Engine Dashboard` (`/app`)**: Interactive film specification form, Pan-India star cast dropdowns, 52+ theme chips, test presets, and ML inference output cards.
3. **`About & Architecture Page` (`/about`)**: Detailed model benchmarks table, EDA dataset inspector, and system data flow architecture.

---

## 🔄 End-to-End User Flowchart

```mermaid
flowchart TD
    Start([User Arrives at Platform]) --> Choice{Select Page}
    
    Choice -->|Landing Page| Home[Explore Platform Overview & Features]
    Home --> LaunchCTA[Click 'Launch Application 🚀']
    
    Choice -->|About Page| About[View Model Benchmarks & EDA Inspector]
    
    Choice -->|Prediction Dashboard| Dashboard[Inference Form Input]
    LaunchCTA --> Dashboard
    
    Dashboard --> ModeChoice{Select Input Mode}
    ModeChoice -->|Instant Preset| PresetBtn[Click 'High Test', 'Medium Test', or 'Low Test']
    ModeChoice -->|Custom Input| ManualInput[Select Director, Cast, Budget, Themes & Currency]
    
    PresetBtn --> AutoFill[Form Instantly Pre-Filled]
    AutoFill --> Submit[Click 'Execute Inference & Strategy Generation']
    ManualInput --> Submit
    
    Submit --> APIReq[POST /api/predict]
    APIReq --> Loading[GSAP Button Spinner & Inference Execution]
    
    Loading --> Res{Inference Category Output}
    
    Res -->|High Quality ≥ 7.5| HighCard[Greenlight Acquisition Badge + Confetti Fireworks 🎆]
    Res -->|Medium Quality 5.5-7.4| MedCard[Conditional Acquisition / OTT Premiere Badge 🟡]
    Res -->|Low Quality < 5.5| LowCard[High Risk / Pass Acquisition Badge 🔴]
    
    HighCard --> ScrollAlign[Smooth Scroll Offset Below Fixed Navbar]
    MedCard --> ScrollAlign
    LowCard --> ScrollAlign
    
    ScrollAlign --> ViewMetrics[Inspect Probability Chart & Strategic Advice]
```

---

## 📱 Mobile UI Interaction Experience
1. **Header Alignment**: Compact sticky glass navbar with scaled $48\text{px}$ brand logo.
2. **Preset Buttons**: Touch-friendly top preset bar for rapid 1-tap testing.
3. **Form Fields**: $16\text{px}$ input fields to prevent iOS Safari auto-zoom.
4. **Result Card**: Smooth scroll alignment positioning the results card $90\text{px}$ below the top navbar for un-occluded viewing.
