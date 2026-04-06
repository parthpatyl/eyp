const path = require("path");
const pptxgen = require("pptxgenjs");

const IMAGES = {
    title: "/home/prth/.gemini/antigravity/brain/8524501f-0042-4846-81e9-59983921b241/hale_uav_title_1771364812240.png",
    blueprint: "/home/prth/.gemini/antigravity/brain/8524501f-0042-4846-81e9-59983921b241/hale_uav_blueprint_1771364831661.png",
    cutaway: "/home/prth/.gemini/antigravity/brain/8524501f-0042-4846-81e9-59983921b241/hale_uav_cutaway_1771364847905.png"
};

let pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.title = "HALE UAV Final Year Project";

const makeShadow = () => ({ type: "outer", blur: 8, offset: 3, angle: 135, color: "000000", opacity: 0.12 });

const COLORS = {
    darkBg: "1B2A4A",
    lightBg: "F4F6FA",
    accent: "2E86AB",
    accentLight: "A8DADC",
    textDark: "1B2A4A",
    textLight: "FFFFFF",
    highlight: "E63946"
};

// SLIDE 1: Title
let slide1 = pres.addSlide();
slide1.background = { color: COLORS.darkBg };
// Add background image with overlay
slide1.addImage({ path: IMAGES.title, x: 0, y: 0, w: "100%", h: "100%", transparency: 60 });
slide1.addShape(pres.ShapeType.rect, { x: 0, y: 5.15, w: "100%", h: 0.08, fill: { color: COLORS.accentLight } });
slide1.addText("HIGH ALTITUDE LONG ENDURANCE (HALE) UNMANNED AERIAL VEHICLES", {
    x: 0.5, y: 1.8, w: 9, h: 1, fontSize: 26, fontFace: "Calibri", color: COLORS.accentLight, bold: true, align: "center", valign: "middle", shadow: makeShadow()
});
slide1.addText("Sustained Flight Through Renewable Energy", {
    x: 0.5, y: 2.7, w: 9, h: 0.6, fontSize: 20, fontFace: "Calibri", color: COLORS.textLight, align: "center", valign: "middle", shadow: makeShadow()
});
slide1.addText("Parth Patil (22BTRAS031)", {
    x: 0.5, y: 3.8, w: 9, h: 0.4, fontSize: 18, fontFace: "Calibri", color: COLORS.textLight, align: "center", shadow: makeShadow()
});
slide1.addText("Advisor: Dr Amalesh Barai", {
    x: 0.5, y: 4.2, w: 9, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accentLight, align: "center", shadow: makeShadow()
});
slide1.addText("Department of Aerospace Engineering, JAIN (Deemed-to-be University)", {
    x: 0.5, y: 4.55, w: 9, h: 0.3, fontSize: 12, fontFace: "Calibri", color: COLORS.accentLight, align: "center", shadow: makeShadow()
});
slide1.addText("2025-2026", { x: 0.5, y: 4.9, w: 9, h: 0.25, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight, align: "center", shadow: makeShadow() });

// SLIDE 2: Agenda
let slide2 = pres.addSlide();
slide2.background = { color: COLORS.lightBg };
slide2.addText("Presentation Agenda", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide2.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const agendaItems = [
    "Project Motivation & Aims", 
    "Literature Review — Existing HALE UAVs", 
    "Design Requirements & Constraints", 
    "Conceptual Design Overview", 
    "Aerodynamic, Propulsion & Structural Design", 
    "Performance Analysis & Results", 
    "Stability, Trade-offs & Validation", 
    "Conclusions & Future Work"
];
agendaItems.forEach((item, idx) => {
    slide2.addText((idx + 1).toString(), { x: 0.8, y: 1.3 + idx * 0.5, w: 0.4, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
    slide2.addText(item, { x: 1.3, y: 1.3 + idx * 0.5, w: 7, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.textDark });
});

// SLIDE 3: Motivation
let slide3 = pres.addSlide();
slide3.background = { color: COLORS.lightBg };
slide3.addText("Project Motivation & Aims", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide3.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide3.addText("Why HALE UAV? [1][2]", { x: 0.4, y: 1.2, w: 4.5, h: 0.4, fontSize: 18, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide3.addText("• Bridge gap between conventional aircraft and satellites\n• Operate at altitudes above 18 km for days/weeks\n• Enable persistent surveillance & communication relay\n• Reduce reliance on expensive satellite infrastructure", {
    x: 0.4, y: 1.6, w: 4.5, h: 1.8, fontSize: 14, fontFace: "Calibri", color: COLORS.textDark
});
slide3.addText("Project Aim [1-4]", { x: 5.2, y: 1.2, w: 4.5, h: 0.4, fontSize: 18, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide3.addText("Conceive, analyse, and assess a theoretically sound solar-powered HALE UAV achieving multi-week endurance with payload versatility and operational reliability.", {
    x: 5.2, y: 1.6, w: 4.3, h: 1.4, fontSize: 14, fontFace: "Calibri", color: COLORS.textDark
});
slide3.addShape(pres.ShapeType.rect, { x: 0.4, y: 3.7, w: 9.2, h: 1.2, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
slide3.addText("Target: Continuous flight above 18 km for minimum 24 hours, with ambition for several days [1][2]", {
    x: 0.6, y: 3.9, w: 8.8, h: 0.8, fontSize: 18, fontFace: "Calibri", color: COLORS.textLight, align: "center", valign: "middle"
});

// SLIDE 4: Objectives
let slide4 = pres.addSlide();
slide4.background = { color: COLORS.lightBg };
slide4.addText("Project Objectives", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide4.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const objectives = [
    { title: "Primary", desc: "Develop comprehensive conceptual design satisfying mission endurance, payload, and safety requirements [1-4]" },
    { title: "Literature Survey", desc: "Review existing solar UAVs: aerodynamic configs, materials, energy storage [1-4][39-44]" },
    { title: "Design Limitations", desc: "Assess energy-storage limits, low-Re aerodynamics, structural/fatigue constraints [8-15]" },
    { title: "Performance Evaluation", desc: "Predict endurance, energy budgets, and mission reliability via simulation [5-7]" },
    { title: "Design Improvements", desc: "Recommend modifications: propulsion optimisation, aeroelastic analysis [42][44]" },
    { title: "Energy Integration", desc: "Quantify renewable energy impact on endurance and reliability [39][43][45]" }
];
objectives.forEach((obj, idx) => {
    let yPos = 1.2 + idx * 0.7;
    slide4.addShape(pres.ShapeType.rect, { x: 0.4, y: yPos, w: 0.12, h: 0.55, fill: { color: COLORS.accent } });
    slide4.addText(obj.title, { x: 0.7, y: yPos, w: 2, h: 0.55, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true, valign: "middle" });
    slide4.addText(obj.desc, { x: 2.8, y: yPos, w: 6.8, h: 0.55, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark, valign: "middle" });
});

// SLIDE 5: Literature Review
let slide5 = pres.addSlide();
slide5.background = { color: COLORS.lightBg };
slide5.addText("Literature Review — Key Existing HALE UAVs", {
    x: 0.5, y: 0.3, w: 9, h: 0.5, fontSize: 24, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide5.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const tableData = [
    ["Platform", "Mass (kg)", "Wingspan (m)", "AR", "Endurance", "Ref"],
    ["Zephyr S", "53", "25", "24", "25+ days", "[3][4]"],
    ["Helios", "730", "75", "30", "14+ hours", "[3][4]"],
    ["EAV-3 (KARI)", "53", "19.5", "17.4", "Stratospheric test", "[40]"],
    ["AtlantikSolar", "6.9", "—", "—", "81 hours", "[39]"],
    ["Present Design", "~114*", "32", "~30", "Target: 24+ hours", "—"]
];
slide5.addTable(tableData, {
    x: 0.4, y: 1.0, w: 9.2, h: 2.8, colWidths: [2.8, 1.4, 1.4, 0.8, 2, 0.8],
    fontFace: "Calibri", fontSize: 12, color: COLORS.textDark,
    border: { type: "solid", pt: 0.5, color: "CCCCCC" },
    rowH: [0.45, 0.45, 0.45, 0.45, 0.45, 0.45],
    fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", COLORS.accentLight]
});
slide5.addText("*Structural estimate derived from energy feasibility analysis. Not MTOW.", { x: 0.4, y: 3.85, w: 9, h: 0.3, fontSize: 10, fontFace: "Calibri", color: COLORS.textDark, italic: true });
slide5.addText("Key Insights [1-3][14][39]:", { x: 0.4, y: 4.1, w: 9, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide5.addText("• High-aspect-ratio monoplane configurations dominate (AR 17.4 to 30+)", { x: 0.4, y: 4.4, w: 9, h: 0.3, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark });
slide5.addText("• Triple-junction GaAs cells achieve 25–30% efficiency — practical upper bound", { x: 0.4, y: 4.7, w: 9, h: 0.3, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark });

// SLIDE 6: Requirements
let slide6 = pres.addSlide();
slide6.background = { color: COLORS.lightBg };
slide6.addText("Design Requirements & Constraints", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide6.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide6.addText("Mission Requirements [1][2]", { x: 0.4, y: 1.2, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide6.addText("• Altitude: 18–22 km (stratospheric)\n• Endurance: Minimum 24 hours (target: multi-day)\n• Cruise speed: ~80 km/h\n• Payload: 5-10 kg for instruments & comms", {
    x: 0.4, y: 1.6, w: 4.5, h: 1.5, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide6.addText("Technical Constraints [6-29]", { x: 5.2, y: 1.2, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide6.addText("• Low Reynolds number flows (10⁵–10⁶)\n• Structural stiffness for flutter avoidance\n• Energy storage for night-time operation\n• Environmental: cloud, wind shear, temperature", {
    x: 5.2, y: 1.6, w: 4.3, h: 1.5, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
const targets = [{ val: "25-30", unit: "L/D", label: "Lift-to-Drag Ratio" }, { val: ">18 km", unit: "", label: "Service Ceiling" }, { val: ">24 hrs", unit: "", label: "Endurance" }];
targets.forEach((t, idx) => {
    let xPos = 0.4 + idx * 3.1;
    slide6.addShape(pres.ShapeType.rect, { x: xPos, y: 3.85, w: 2.9, h: 1.1, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
    slide6.addText(t.val, { x: xPos, y: 3.9, w: 2.9, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.highlight, bold: true, align: "center" });
    slide6.addText(t.label, { x: xPos, y: 4.5, w: 2.9, h: 0.35, fontSize: 11, fontFace: "Calibri", color: COLORS.accentLight, align: "center" });
});

// SLIDE 7: Conceptual Design
let slide7 = pres.addSlide();
slide7.background = { color: COLORS.lightBg };
slide7.addText("Conceptual Design Overview", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide7.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
// Add Blueprint Image
slide7.addImage({ path: IMAGES.blueprint, x: 5.2, y: 1.5, w: 4.3, h: 2.0 });

slide7.addText("Top-Level Design Approach [1-4]", { x: 0.4, y: 1.1, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide7.addText("• High-aspect-ratio monoplane configuration\n• Solar cells on wing & fuselage surfaces\n• Hybrid energy: solar + batteries + fuel cell\n• CFRP composite ultra-lightweight structure\n• Distributed propulsion system", {
    x: 0.4, y: 1.5, w: 4.5, h: 1.8, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide7.addText("Configuration Choice [1][18-20]", { x: 5.2, y: 1.1, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide7.addText("Monoplane with high aspect ratio selected over biplane, BWB, and joined-wing based on manufacturing simplicity and proven technology readiness.", {
    x: 5.2, y: 3.6, w: 4.3, h: 1.0, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark
});
slide7.addShape(pres.ShapeType.rect, { x: 0.4, y: 3.6, w: 4.5, h: 1.3, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
slide7.addText("Selected Design Parameters", { x: 0.5, y: 3.7, w: 4.3, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accentLight, bold: true });
slide7.addText("Wingspan: 32 m\nAspect Ratio: ~30\nStructure Est: ~114 kg\nPayload: 5-10 kg", {
    x: 0.5, y: 4.1, w: 4.3, h: 0.7, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight, align: "center", valign: "middle"
});


// SLIDE 8: Aerodynamic Design
let slide8 = pres.addSlide();
slide8.background = { color: COLORS.lightBg };
slide8.addText("Aerodynamic Design", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide8.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide8.addText("Wing Geometry [6][7][40]", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide8.addText("• Wingspan: 32 m\n• Aspect Ratio: ~30\n• Low-Reynolds-number airfoil selection\n• High-lift, low-drag optimization", {
    x: 0.4, y: 1.45, w: 4.5, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide8.addText("Key Considerations [5-7]", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide8.addText("• Low Re flows (10⁵–10⁶): viscous effects\n• Target L/D: 25-30\n• Minimise induced drag with high AR\n• CFD + analytical methods for validation", {
    x: 5.2, y: 1.45, w: 4.3, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide8.addText("Configuration Comparison [1][18-20]", { x: 0.4, y: 2.9, w: 4.5, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true });
const aeroTable = [
    ["Configuration", "Pros", "Cons"],
    ["Monoplane", "Simple, proven", "Tip deflection"],
    ["Biplane", "High payload", "Interference drag"],
    ["BWB", "Higher L/D", "Complexity"],
    ["Joined-wing", "Span eff 1.4-1.5", "Struct. complexity"]
];
slide8.addTable(aeroTable, {
    x: 0.4, y: 3.25, w: 4.5, h: 1.5, colWidths: [1.4, 1.55, 1.55],
    fontFace: "Calibri", fontSize: 10, color: COLORS.textDark,
    border: { type: "solid", pt: 0.5, color: "CCCCCC" },
    rowH: [0.35, 0.28, 0.28, 0.28, 0.28],
    fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF"]
});
slide8.addShape(pres.ShapeType.rect, { x: 5.2, y: 3.2, w: 4.3, h: 1.2, fill: { color: COLORS.highlight }, shadow: makeShadow() });
slide8.addText("30", { x: 5.2, y: 3.3, w: 4.3, h: 0.7, fontSize: 48, fontFace: "Calibri", color: COLORS.textLight, bold: true, align: "center" });
slide8.addText("Aspect Ratio [40]", { x: 5.2, y: 4.0, w: 4.3, h: 0.3, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight, align: "center" });

// SLIDE 9: Propulsion System
let slide9 = pres.addSlide();
slide9.background = { color: COLORS.lightBg };
slide9.addText("Propulsion & Energy Architecture", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide9.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
// Add Cutaway Image
slide9.addImage({ path: IMAGES.cutaway, x: 5.2, y: 1.1, w: 4.3, h: 2.5 });

slide9.addText("Hybrid Energy Architecture [10][14]", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
const powerSrcs = [
    { title: "Solar (Day)", val: "~9 kW", desc: "Triple-junction GaAs\n25-30% efficiency" },
    { title: "Storage (Night)", val: "~24 kWh", desc: "Li-Ion + Fuel Cell" },
    { title: "Cruise Power", val: "~2 kW", desc: "Electrical demand" }
];
powerSrcs.forEach((src, idx) => {
    let yPos = 1.5 + idx * 1.1;
    slide9.addShape(pres.ShapeType.rect, { x: 0.4, y: yPos, w: 4.5, h: 1.0, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
    slide9.addText(src.title, { x: 0.5, y: yPos + 0.1, w: 3.0, h: 0.3, fontSize: 12, fontFace: "Calibri", color: COLORS.accentLight });
    slide9.addText(src.val, { x: 3.2, y: yPos + 0.1, w: 1.5, h: 0.4, fontSize: 20, fontFace: "Calibri", color: COLORS.highlight, bold: true, align: "right" });
    slide9.addText(src.desc, { x: 0.5, y: yPos + 0.5, w: 4.0, h: 0.3, fontSize: 10, fontFace: "Calibri", color: COLORS.textLight });
});

slide9.addText("Reasoning for Hydrogen Fuel Cell [10][39]:", { x: 5.2, y: 3.8, w: 4.3, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide9.addText("• Night requirement (~24 kWh) requires ~95kg of batteries.\n• H2 System: ~1.44kg H2 + Tank + BOP ≈ 4.3kg.\n• Massive weight saving enables multi-day endurance.", {
    x: 5.2, y: 4.15, w: 4.3, h: 1.0, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark
});

// SLIDE 10: Structural Design
let slide10 = pres.addSlide();
slide10.background = { color: COLORS.lightBg };
slide10.addText("Structural Design", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide10.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide10.addText("Material Selection: CFRP Composites [8][9]", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide10.addText("• Carbon-fibre reinforced polymers (T-800/T-300)\n• High stiffness-to-weight ratio (5x Al)\n• Anisotropic tailoring for load paths (bending/torsion)", {
    x: 0.4, y: 1.45, w: 4.5, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide10.addText("Structural Analysis [5][22][44]", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide10.addText("• ANSYS Workbench for FEA (large-displacement)\n• Static deflection: tip deflection 10-15% of semi-span\n• Aeroelastic coupling analysis (Murua et al.)", {
    x: 5.2, y: 1.45, w: 4.3, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide10.addText("Weight Breakdown (Component Level) [40]", { x: 0.4, y: 3.0, w: 9, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true });
const weightTable = [
    ["Component", "Mass (kg)", "Notes"],
    ["Airframe", "~22", "CFRP primary structure"],
    ["Solar panels", "~15", "GaAs arrays"],
    ["Energy storage", "~5", "Fuel cell system"],
    ["Avionics/Payld", "~10-15", "Combined"],
    ["Total (MTOW)", "~62", "Estim. w/ Payload"]
];
slide10.addTable(weightTable, {
    x: 0.4, y: 3.35, w: 9.2, h: 1.8, colWidths: [3.5, 1.5, 4.2],
    fontFace: "Calibri", fontSize: 11, color: COLORS.textDark,
    border: { type: "solid", pt: 0.5, color: "CCCCCC" },
    rowH: [0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF"]
});

// SLIDE 11: Performance Analysis
let slide11 = pres.addSlide();
slide11.background = { color: COLORS.lightBg };
slide11.addText("Performance Analysis", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide11.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const perfMetrics = [
    { val: ">24 hrs", label: "Endurance", color: COLORS.highlight },
    { val: "18-22 km", label: "Altitude", color: COLORS.accent },
    { val: "25-30", label: "L/D Ratio", color: COLORS.darkBg },
    { val: "~80 km/h", label: "Cruise Speed", color: COLORS.accent }
];
perfMetrics.forEach((m, idx) => {
    let xPos = 0.4 + idx * 2.35;
    slide11.addShape(pres.ShapeType.rect, { x: xPos, y: 1.1, w: 2.2, h: 1.3, fill: { color: m.color }, shadow: makeShadow() });
    slide11.addText(m.val, { x: xPos, y: 1.2, w: 2.2, h: 0.7, fontSize: 28, fontFace: "Calibri", color: COLORS.textLight, bold: true, align: "center" });
    slide11.addText(m.label, { x: xPos, y: 1.9, w: 2.2, h: 0.4, fontSize: 12, fontFace: "Calibri", color: COLORS.textLight, align: "center" });
});
slide11.addText("Key Analysis Results [10][15][42]", { x: 0.4, y: 2.7, w: 9, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide11.addText("• Cruise power: ~2 kW electrical\n• Solar power available: ~9 kW (stratospheric irradiance 1360 W/m²)\n• Night-time energy storage: ~23.9 kWh for 12-hr dark period\n• Altitude power penalty: ~3.5% per km\n• Propulsion optimisation potential: 19% efficiency improvement", {
    x: 0.4, y: 3.05, w: 9, h: 1.6, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});

// SLIDE 12: Stability & Control
let slide12 = pres.addSlide();
slide12.background = { color: COLORS.lightBg };
slide12.addText("Stability & Control", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide12.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide12.addText("Stability Analysis [12][13][40]", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide12.addText("• Longitudinal & directional stability\n• Static margin: min 5% MAC (EAV-3 ref: 28.4%)\n• CG remains stable (no fuel burn shift)", {
    x: 0.4, y: 1.45, w: 4.5, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide12.addText("Control Surfaces [27]", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide12.addText("• Conventional tail (elevator, rudder)\n• Ailerons for roll control\n• Larger deflections required at low air density\n• Redundant actuator architecture", {
    x: 5.2, y: 1.45, w: 4.3, h: 1.4, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide12.addText("Flutter Analysis [22][44]", { x: 0.4, y: 3.0, w: 9, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide12.addText("High-aspect-ratio flexible wings introduce aeroelastic coupling. Conventional doublet-lattice methods insufficient. Used Murua et al. methodology: geometrically exact beam FE + Unsteady Vortex Lattice Method (UVLM) for accurate flutter boundary prediction.", {
    x: 0.4, y: 3.35, w: 9, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});

// SLIDE 13: Trade-offs
let slide13 = pres.addSlide();
slide13.background = { color: COLORS.lightBg };
slide13.addText("Design Trade-offs & Decisions", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide13.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const tradeoffs = [
    ["Decision", "Trade-off", "Resolution"],
    ["Aspect Ratio 30", "Mfg vs performance", "Practical compromise"],
    ["Fuel cell > Battery", "Complexity vs mass", "95kg vs 4.3kg"],
    ["Monoplane config", "Simplicity", "Proven technology"],
    ["GaAs cells", "Cost vs Efficiency", "Optimum power"]
];
slide13.addTable(tradeoffs, {
    x: 0.4, y: 1.1, w: 9.2, h: 2.0, colWidths: [3, 3, 3.2],
    fontFace: "Calibri", fontSize: 12, color: COLORS.textDark,
    border: { type: "solid", pt: 0.5, color: "CCCCCC" },
    rowH: [0.4, 0.38, 0.38, 0.38, 0.38],
    fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF"]
});
slide13.addShape(pres.ShapeType.rect, { x: 0.4, y: 3.4, w: 9.2, h: 1.3, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
slide13.addText("Critical Trade-off: Battery vs Fuel Cell [10][39]", {
    x: 0.6, y: 3.5, w: 8.8, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.highlight, bold: true
});
slide13.addText("Night-time storage of ~23.9 kWh makes pure lithium-ion solution infeasible:\n• Battery mass: ~95.7 kg\n• Hydrogen system: ~4.3 kg total\n→ Fuel cell selected for multi-day endurance", {
    x: 0.6, y: 3.9, w: 8.8, h: 0.75, fontSize: 12, fontFace: "Calibri", color: COLORS.textLight
});

// SLIDE 14: Results Summary (NEW)
let slide14 = pres.addSlide();
slide14.background = { color: COLORS.lightBg };
slide14.addText("Results Summary", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide14.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const resultsTable = [
    ["Parameter", "Value", "Status"],
    ["Wingspan", "32 m", "Target met"],
    ["Aspect Ratio", "~30", "Within range [40]"],
    ["MTOW (Comp.)", "~57-62 kg", "Estimated"],
    ["Endurance", ">24 hrs", "Achievable [39]"],
    ["Altitude", "18-22 km", "Stratospheric"],
    ["L/D Ratio", "25-30", "Target met [40]"],
    ["Night Storage", "~23.9 kWh", "Fuel Cell Used [10]"],
    ["Fuel Cell Mass", "~4.3 kg", "vs 95kg Battery"]
];
slide14.addTable(resultsTable, {
    x: 0.4, y: 1.1, w: 9.2, h: 3.0, colWidths: [3, 2.5, 3.7],
    fontFace: "Calibri", fontSize: 12, color: COLORS.textDark,
    border: { type: "solid", pt: 0.5, color: "CCCCCC" },
    fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF"]
});
slide14.addText("Note: ~114 kg energy feasibility mass includes margin for battery trade-study. Component build-up (~62kg) reflects operational weight.", { 
    x: 0.4, y: 4.3, w: 9, h: 0.6, fontSize: 11, fontFace: "Calibri", color: COLORS.textDark, italic: true 
});

// SLIDE 15: Validation & Limitations (NEW)
let slide15 = pres.addSlide();
slide15.background = { color: COLORS.lightBg };
slide15.addText("Validation & Limitations", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide15.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide15.addText("Validated Conceptually (Green)", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: "1B5E20", bold: true }); // Dark Green
slide15.addText("✓ Energy balance closure verified [39]\n✓ Power realistic (~2 kW) [10]\n✓ Solar power adequate (~9 kW) [14]\n✓ Fuel cell mass savings confirmed [10]\n✓ L/D targets achievable [40]", {
    x: 0.4, y: 1.45, w: 4.5, h: 1.5, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide15.addText("Limitations (Red)", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: "B71C1C", bold: true }); // Dark Red
slide15.addText("⚠ No wind tunnel/flight testing\n⚠ No high-fidelity CFD validation [5]\n⚠ Aeroelastic effects conceptual [44]\n⚠ PV integration losses est. [43]\n⚠ Mass budget reconciliation required", {
    x: 5.2, y: 1.45, w: 4.3, h: 1.5, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide15.addShape(pres.ShapeType.rect, { x: 0.4, y: 3.5, w: 9.2, h: 1.0, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
slide15.addText("This is a CONCEPTUAL DESIGN study. Detailed computational modelling, prototype fabrication, and experimental flight testing are recommended for full validation.", {
    x: 0.6, y: 3.6, w: 8.8, h: 0.8, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight, align: "center", valign: "middle"
});

// SLIDE 16: Conclusions
let slide16 = pres.addSlide();
slide16.background = { color: COLORS.darkBg };
slide16.addText("Conclusions", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.textLight, bold: true
});
slide16.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide16.addText("Objectives Achieved", { x: 0.4, y: 1.1, w: 9, h: 0.35, fontSize: 18, fontFace: "Calibri", color: COLORS.accentLight, bold: true });
slide16.addText("✓ Comprehensive conceptual design developed\n✓ Literature review expanded\n✓ Energy system feasibility confirmed (Fuel Cell)\n✓ Design parameters aligned with benchmarks\n✓ Trade-offs analyzed", {
    x: 0.4, y: 1.45, w: 9, h: 1.6, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight
});
slide16.addText("Key Findings", { x: 0.4, y: 3.2, w: 9, h: 0.35, fontSize: 18, fontFace: "Calibri", color: COLORS.accentLight, bold: true });
slide16.addText("• Solar-powered HALE UAV technical feasibility confirmed for multi-day endurance\n• Hybrid energy storage essential for night operations\n• Propulsion optimisation reduces power demand significantly\n• High-AR wings require advanced aeroelastic analysis", {
    x: 0.4, y: 3.55, w: 9, h: 1.4, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight
});

// SLIDE 17: Future Work
let slide17 = pres.addSlide();
slide17.background = { color: COLORS.lightBg };
slide17.addText("Future Work & Recommendations", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide17.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide17.addText("Near-Term (Research)", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide17.addText("• Detailed CFD and wind tunnel validation\n• Composite wing segment testing [44]\n• Energy mgmt algorithm [39]", {
    x: 0.4, y: 1.45, w: 4.5, h: 1.0, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark
});
slide17.addText("Long-Term (Development)", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide17.addText("• Scaled demonstrator fabrication\n• Flight testing\n• Mission system integration", {
    x: 5.2, y: 1.45, w: 4.3, h: 1.0, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark
});
slide17.addText("Emerging Technologies [45]", { x: 0.4, y: 3.0, w: 9, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide17.addText("• Morphing wings\n• Solid-state batteries\n• Ultra-light flexible solar arrays\n• Supercapacitor hybrid storage", {
    x: 0.4, y: 3.35, w: 9, h: 1.3, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark
});

// SLIDE 18: References
let slide18 = pres.addSlide();
slide18.background = { color: COLORS.lightBg };
slide18.addText("Key References", {
    x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide18.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const refs = [
    "[1] Goraj et al. (1999). Design concept of a HALE UAV. Aircraft Design",
    "[2] Goraj, Z. (2004). HALE UAV of a new generation.",
    "[3] Romeo et al. (2004). HELIPLAT: Design & analysis.",
    "[10] Boukoberine et al. (2019). Energy storage for UAVs.",
    "[39] Oettershagen et al. (2017). AtlantikSolar UAV.",
    "[40] Hwang et al. (2016). KARI EAV-3 aerodynamic design.",
    "[42] Dantsker et al. (2020). Propulsion optimisation.",
    "[43] Lopusiewicz & Ksiazek (2024). PV integration.",
    "[44] Murua et al. (2011). Stability of very flexible aircraft.",
    "[45] Liller et al. (2025). Battery-free solar UAV."
];
slide18.addText(refs.join("\n"), { x: 0.4, y: 1.1, w: 9.2, h: 4.0, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark });

// SLIDE 19: Thank You
let slide19 = pres.addSlide();
slide19.background = { color: COLORS.darkBg };
slide19.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: "100%", h: 0.08, fill: { color: COLORS.accentLight } });
slide19.addText("Questions & Discussion", {
    x: 0.5, y: 1.8, w: 9, h: 0.8, fontSize: 36, fontFace: "Calibri", color: COLORS.textLight, bold: true, align: "center"
});
slide19.addText("Thank You", { x: 0.5, y: 2.8, w: 9, h: 0.6, fontSize: 24, fontFace: "Calibri", color: COLORS.accentLight, align: "center" });
slide19.addText("Parth Patil | 22BTRAS031\nDr Amalesh Barai (Advisor)", {
    x: 0.5, y: 3.8, w: 9, h: 1.0, fontSize: 14, fontFace: "Calibri", color: COLORS.accentLight, align: "center"
});

pres.writeFile({ fileName: path.join(__dirname, "HALE_UAV_Presentation_v2.pptx") })
    .then(() => console.log(`Presentation saved to ${path.join(__dirname, "HALE_UAV_Presentation_v2.pptx")}`))
    .catch(err => console.error("Error saving presentation:", err));
