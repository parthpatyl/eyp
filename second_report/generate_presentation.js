const path = require("path");
const pptxgen = require("pptxgenjs");
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
slide1.addShape(pres.ShapeType.rect, { x: 0, y: 5.15, w: "100%", h: 0.08, fill: { color: COLORS.accentLight } });
slide1.addText("HIGH ALTITUDE LONG ENDURANCE (HALE) UNMANNED AERIAL VEHICLES", {
  x: 0.5, y: 1.8, w: 9, h: 1, fontSize: 26, fontFace: "Calibri", color: COLORS.accentLight, bold: true, align: "center", valign: "middle"
});
slide1.addText("Sustained Flight Through Renewable Energy", {
  x: 0.5, y: 2.7, w: 9, h: 0.6, fontSize: 20, fontFace: "Calibri", color: COLORS.textLight, align: "center", valign: "middle"
});
slide1.addText("Parth Patil (22BTRAS031)", {
  x: 0.5, y: 3.8, w: 9, h: 0.4, fontSize: 18, fontFace: "Calibri", color: COLORS.textLight, align: "center"
});
slide1.addText("Under the guidance of Dr Amalesh Barai", {
  x: 0.5, y: 4.2, w: 9, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accentLight, align: "center"
});
slide1.addText("Department of Aerospace Engineering, JAIN (Deemed-to-be University)", {
  x: 0.5, y: 4.55, w: 9, h: 0.3, fontSize: 12, fontFace: "Calibri", color: COLORS.accentLight, align: "center"
});
slide1.addText("2025-2026", { x: 0.5, y: 4.9, w: 9, h: 0.25, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight, align: "center" });

// SLIDE 2: Agenda
let slide2 = pres.addSlide();
slide2.background = { color: COLORS.lightBg };
slide2.addText("Presentation Agenda", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide2.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const agendaItems = ["Project Motivation & Aims", "Literature Review — Existing HALE UAVs", "Design Requirements & Constraints", "Conceptual Design Overview", "Aerodynamic, Propulsion & Structural Design", "Performance Analysis & Results", "Stability, Trade-offs & Validation", "Conclusions & Future Work"];
agendaItems.forEach((item, idx) => {
  slide2.addText((idx + 1).toString(), { x: 0.4, y: 1.3 + idx * 0.5, w: 0.4, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
  slide2.addText(item, { x: 0.9, y: 1.3 + idx * 0.5, w: 8, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.textDark });
});

// SLIDE 3: Motivation
let slide3 = pres.addSlide();
slide3.background = { color: COLORS.lightBg };
slide3.addText("Project Motivation & Aims", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide3.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide3.addText("Why HALE UAV?", { x: 0.4, y: 1.2, w: 4.5, h: 0.4, fontSize: 18, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide3.addText("• Bridge gap between conventional aircraft and satellites\n• Operate at altitudes above 18 km for days/weeks\n• Enable persistent surveillance & communication relay\n• Reduce reliance on expensive satellite infrastructure", {
  x: 0.4, y: 1.6, w: 4.5, h: 1.8, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide3.addText("Project Aim", { x: 5.2, y: 1.2, w: 4.5, h: 0.4, fontSize: 18, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide3.addText("Conceive, analyse, and assess a theoretically sound solar-powered HALE UAV achieving multi-week endurance with payload versatility and operational reliability.", {
  x: 5.2, y: 1.6, w: 4.3, h: 1.4, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide3.addShape(pres.ShapeType.rect, { x: 0.4, y: 3.7, w: 9.2, h: 1.2, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
slide3.addText("Target: Continuous flight above 18 km for minimum 24 hours, with ambition for several days", {
  x: 0.6, y: 3.9, w: 8.8, h: 0.8, fontSize: 16, fontFace: "Calibri", color: COLORS.textLight, align: "center", valign: "middle"
});

// SLIDE 4: Objectives
let slide4 = pres.addSlide();
slide4.background = { color: COLORS.lightBg };
slide4.addText("Project Objectives", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide4.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const objectives = [
  { title: "Primary", desc: "Develop comprehensive conceptual design satisfying mission endurance, payload, and safety requirements" },
  { title: "Literature Survey", desc: "Review existing solar UAVs: aerodynamic configs, materials, energy storage" },
  { title: "Design Limitations", desc: "Assess energy-storage limits, low-Re aerodynamics, structural/fatigue constraints" },
  { title: "Performance Evaluation", desc: "Predict endurance, energy budgets, and mission reliability via simulation" },
  { title: "Design Improvements", desc: "Recommend modifications: propulsion optimisation, aeroelastic analysis" },
  { title: "Energy Integration", desc: "Quantify renewable energy impact on endurance and reliability" }
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
  ["Platform", "Mass (kg)", "Wingspan (m)", "AR", "Endurance"],
  ["Zephyr S", "53", "25", "24", "25+ days"],
  ["Helios", "730", "75", "30", "14+ hours"],
  ["EAV-3 (KARI)", "53", "19.5", "17.4", "Stratospheric test"],
  ["AtlantikSolar", "6.9", "—", "—", "81 hours (world record)"],
  ["Present Design", "~114", "32", "~30", "Target: 24+ hours"]
];
slide5.addTable(tableData, {
  x: 0.4, y: 1.0, w: 9.2, h: 2.8, colWidths: [2.8, 1.6, 1.6, 1.2, 2],
  fontFace: "Calibri", fontSize: 12, color: COLORS.textDark,
  border: { type: "solid", pt: 0.5, color: "CCCCCC" },
  rowH: [0.45, 0.45, 0.45, 0.45, 0.45, 0.45],
  fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", COLORS.accentLight]
});
slide5.addText("Key Insights:", { x: 0.4, y: 4.0, w: 9, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide5.addText("• High-aspect-ratio monoplane configurations dominate (AR 17.4 to 30+)", { x: 0.4, y: 4.35, w: 9, h: 0.3, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark });
slide5.addText("• Triple-junction GaAs cells achieve 25–30% efficiency — practical upper bound", { x: 0.4, y: 4.65, w: 9, h: 0.3, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark });

// SLIDE 6: Requirements
let slide6 = pres.addSlide();
slide6.background = { color: COLORS.lightBg };
slide6.addText("Design Requirements & Constraints", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide6.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide6.addText("Mission Requirements", { x: 0.4, y: 1.2, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide6.addText("• Altitude: 18–22 km (stratospheric)\n• Endurance: Minimum 24 hours (target: multi-day)\n• Cruise speed: ~80 km/h\n• Payload: 5-10 kg for instruments & comms", {
  x: 0.4, y: 1.6, w: 4.5, h: 1.5, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide6.addText("Technical Constraints", { x: 5.2, y: 1.2, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide6.addText("• Low Reynolds number flows (10⁵–10⁶)\n• Structural stiffness for flutter avoidance\n• Energy storage for night-time operation\n• Environmental: cloud, wind shear, temperature", {
  x: 5.2, y: 1.6, w: 4.3, h: 1.5, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide6.addText("Performance Targets", { x: 0.4, y: 3.4, w: 9, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
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
slide7.addText("Top-Level Design Approach", { x: 0.4, y: 1.1, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide7.addText("• High-aspect-ratio monoplane configuration\n• Solar cells on wing & fuselage surfaces\n• Hybrid energy: solar + batteries + fuel cell\n• CFRP composite ultra-lightweight structure\n• Distributed propulsion system", {
  x: 0.4, y: 1.5, w: 4.5, h: 1.8, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide7.addText("Configuration Choice", { x: 5.2, y: 1.1, w: 4.5, h: 0.4, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide7.addText("Monoplane with high aspect ratio selected over biplane, BWB, and joined-wing based on:\n\n• Manufacturing simplicity\n• Proven technology readiness\n• Structural reliability\n• Ground handling practicality", {
  x: 5.2, y: 1.5, w: 4.3, h: 1.8, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide7.addShape(pres.ShapeType.rect, { x: 0.4, y: 3.6, w: 9.2, h: 1.3, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
slide7.addText("Selected Design Parameters", { x: 0.6, y: 3.7, w: 8.8, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accentLight, bold: true });
slide7.addText("Wingspan: 32 m  |  Aspect Ratio: ~30  |  Empty Weight: ~114 kg  |  Payload: 5-10 kg", {
  x: 0.6, y: 4.1, w: 8.8, h: 0.7, fontSize: 16, fontFace: "Calibri", color: COLORS.textLight, align: "center", valign: "middle"
});

// SLIDE 8: Aerodynamic Design
let slide8 = pres.addSlide();
slide8.background = { color: COLORS.lightBg };
slide8.addText("Aerodynamic Design", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide8.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide8.addText("Wing Geometry", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide8.addText("• Wingspan: 32 m\n• Aspect Ratio: ~30\n• Low-Reynolds-number airfoil selection\n• High-lift, low-drag optimization", {
  x: 0.4, y: 1.45, w: 4.5, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide8.addText("Key Considerations", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide8.addText("• Low Re flows (10⁵–10⁶): viscous effects dominate\n• Target L/D: 25-30\n• Minimise induced drag with high AR\n• CFD + analytical methods for validation", {
  x: 5.2, y: 1.45, w: 4.3, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide8.addText("Configuration Comparison", { x: 0.4, y: 2.9, w: 4.5, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true });
const aeroTable = [
  ["Configuration", "Pros", "Cons"],
  ["Monoplane", "Simple, proven", "Standard AR"],
  ["Biplane", "High payload", "Interference drag"],
  ["BWB", "Higher L/D", "Complexity"],
  ["Joined-wing", "AR ~40 possible", "Structural complexity"]
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
slide8.addText("Aspect Ratio", { x: 5.2, y: 4.0, w: 4.3, h: 0.3, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight, align: "center" });

// SLIDE 9: Propulsion System
let slide9 = pres.addSlide();
slide9.background = { color: COLORS.lightBg };
slide9.addText("Propulsion System", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide9.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide9.addText("Hybrid Energy Architecture", { x: 0.4, y: 1.1, w: 9, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
const powerSrcs = [
  { title: "Solar (Day)", val: "~9 kW", desc: "Triple-junction GaAs cells\n25-30% efficiency" },
  { title: "Storage (Night)", val: "~24 kWh", desc: "Hybrid battery + fuel cell" },
  { title: "Cruise Power", val: "~2 kW", desc: "Electrical power demand" }
];
powerSrcs.forEach((src, idx) => {
  let xPos = 0.4 + idx * 3.1;
  slide9.addShape(pres.ShapeType.rect, { x: xPos, y: 1.5, w: 2.9, h: 1.4, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
  slide9.addText(src.title, { x: xPos, y: 1.55, w: 2.9, h: 0.3, fontSize: 11, fontFace: "Calibri", color: COLORS.accentLight, align: "center" });
  slide9.addText(src.val, { x: xPos, y: 1.85, w: 2.9, h: 0.55, fontSize: 24, fontFace: "Calibri", color: COLORS.highlight, bold: true, align: "center" });
  slide9.addText(src.desc, { x: xPos + 0.1, y: 2.4, w: 2.7, h: 0.5, fontSize: 10, fontFace: "Calibri", color: COLORS.textLight, align: "center" });
});
slide9.addText("Energy System Reasoning", { x: 0.4, y: 3.2, w: 9, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide9.addText("• Fuel cells outperform batteries above 2.8 kWh demand [10]\n• Night-time requirement (~23.9 kWh) makes pure batteries infeasible (~95 kg)\n• Hydrogen fuel cell solution: ~1.44 kg H2 + ~3 kg system = ~4.3 kg total\n• Propulsion optimisation (Dantsker et al.) could reduce power demand by 19%", {
  x: 0.4, y: 3.55, w: 9, h: 1.3, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark
});

// SLIDE 10: Structural Design
let slide10 = pres.addSlide();
slide10.background = { color: COLORS.lightBg };
slide10.addText("Structural Design", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide10.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide10.addText("Material Selection: CFRP Composites", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide10.addText("• Carbon-fibre reinforced polymers\n• High stiffness-to-weight ratio\n• Anisotropic tailoring for load paths\n• Out-of-plane reinforcement for damage tolerance", {
  x: 0.4, y: 1.45, w: 4.5, h: 1.4, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide10.addText("Structural Analysis", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide10.addText("• ANSYS Workbench for FEA\n• Static deflection analysis\n• Modal frequency analysis\n• Flutter margin prediction", {
  x: 5.2, y: 1.45, w: 4.3, h: 1.2, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide10.addText("Estimated Weight Breakdown", { x: 0.4, y: 3.0, w: 9, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.accent, bold: true });
const weightTable = [
  ["Component", "Mass (kg)", "Notes"],
  ["Airframe (structure)", "~22", "CFRP primary"],
  ["Solar panels", "~15", "GaAs on wing/fuselage"],
  ["Energy storage", "~5", "Fuel cell + H2"],
  ["Avionics & systems", "~5", "Sensors, comms, etc."],
  ["Payload", "5-10", "Mission equipment"],
  ["Total Empty", "~52", "Without payload"],
  ["Max Takeoff", "~62", "With max payload"]
];
slide10.addTable(weightTable, {
  x: 0.4, y: 3.35, w: 9.2, h: 2.0, colWidths: [3.5, 1.5, 4.2],
  fontFace: "Calibri", fontSize: 11, color: COLORS.textDark,
  border: { type: "solid", pt: 0.5, color: "CCCCCC" },
  rowH: [0.35, 0.28, 0.28, 0.28, 0.28, 0.28, 0.28],
  fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF"]
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
slide11.addText("Key Analysis Results", { x: 0.4, y: 2.7, w: 9, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide11.addText("• Cruise power: ~2 kW electrical\n• Solar power available: ~9 kW (triple-junction GaAs at 1,360 W/m2)\n• Night-time energy storage: ~23.9 kWh for 12-hour dark period\n• Altitude power penalty: ~3.5% power increase per km altitude gain\n• Propulsion optimisation potential: 19% efficiency improvement", {
  x: 0.4, y: 3.05, w: 9, h: 1.6, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});

// SLIDE 12: Stability & Control
let slide12 = pres.addSlide();
slide12.background = { color: COLORS.lightBg };
slide12.addText("Stability & Control", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide12.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide12.addText("Stability Analysis", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide12.addText("• Longitudinal & directional stability\n• Static margin: minimum 5% MAC\n• Reference (EAV-3): 28.4% SM at 31% MAC\n• CG remains stable during flight", {
  x: 0.4, y: 1.45, w: 4.5, h: 1.4, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide12.addText("Control Surfaces", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide12.addText("• Conventional tail arrangement\n• Ailerons for roll control\n• Elevator for pitch\n• Rudder for yaw\n• Larger deflections at low density", {
  x: 5.2, y: 1.45, w: 4.3, h: 1.4, fontSize: 13, fontFace: "Calibri", color: COLORS.textDark
});
slide12.addText("Flutter Analysis", { x: 0.4, y: 3.0, w: 9, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide12.addText("High-aspect-ratio very flexible wings introduce significant aeroelastic coupling. Using Murua et al. [44] methodology: geometrically exact beam finite elements + Unsteady Vortex Lattice Method (UVLM) provides accurate flutter boundary prediction including wing-tail wake interference effects.", {
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
  ["Aspect Ratio 30", "Manufacturing vs performance", "Practical compromise for ground handling"],
  ["Fuel cell over battery", "Complexity vs mass", "95 kg battery vs 4.3 kg fuel cell system"],
  ["Monoplane config", "AR limit vs simplicity", "Proven technology, lower risk"],
  ["Solar cell type", "Efficiency vs weight", "GaAs 25-30% for optimal power"]
];
slide13.addTable(tradeoffs, {
  x: 0.4, y: 1.1, w: 9.2, h: 2.0, colWidths: [3, 3, 3.2],
  fontFace: "Calibri", fontSize: 12, color: COLORS.textDark,
  border: { type: "solid", pt: 0.5, color: "CCCCCC" },
  rowH: [0.4, 0.38, 0.38, 0.38, 0.38],
  fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF"]
});
slide13.addShape(pres.ShapeType.rect, { x: 0.4, y: 3.4, w: 9.2, h: 1.3, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
slide13.addText("Critical Trade-off: Battery vs Fuel Cell", {
  x: 0.6, y: 3.5, w: 8.8, h: 0.35, fontSize: 14, fontFace: "Calibri", color: COLORS.highlight, bold: true
});
slide13.addText("Night-time storage of ~23.9 kWh makes pure lithium-ion solution infeasible:\n• Battery mass: ~95.7 kg at 250 Wh/kg\n• Hydrogen system: ~4.3 kg total (1.44 kg H2 + tankage + BOP)\n→ Fuel cell selected for multi-day endurance", {
  x: 0.6, y: 3.9, w: 8.8, h: 0.75, fontSize: 12, fontFace: "Calibri", color: COLORS.textLight
});

// SLIDE 14: Results Summary
let slide14 = pres.addSlide();
slide14.background = { color: COLORS.lightBg };
slide14.addText("Results Summary", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide14.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
const resultsTable = [
  ["Parameter", "Value", "Status"],
  ["Wingspan", "32 m", "Design target met"],
  ["Aspect Ratio", "~30", "Within literature range"],
  ["Empty Weight", "~52 kg", "Competitive with Zephyr S"],
  ["Max Takeoff", "~62 kg", "With max payload"],
  ["Endurance", ">24 hours", "Target achieved"],
  ["Altitude", "18-22 km", "Stratospheric"],
  ["L/D Ratio", "25-30", "Target achieved"],
  ["Cruise Power", "~2 kW", "Feasible"],
  ["Solar Power", "~9 kW", "Available at altitude"],
  ["Night Storage", "~23.9 kWh", "Fuel cell solution"]
];
slide14.addTable(resultsTable, {
  x: 0.4, y: 1.1, w: 9.2, h: 3.2, colWidths: [3.5, 2.2, 3.5],
  fontFace: "Calibri", fontSize: 12, color: COLORS.textDark,
  border: { type: "solid", pt: 0.5, color: "CCCCCC" },
  rowH: [0.38, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
  fill: [COLORS.accentLight, "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF", "FFFFFF"]
});

// SLIDE 15: Validation
let slide15 = pres.addSlide();
slide15.background = { color: COLORS.lightBg };
slide15.addText("Validation & Limitations", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.darkBg, bold: true
});
slide15.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide15.addText("Validated Conceptually", { x: 0.4, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide15.addText("✓ Energy balance closure verified\n✓ Power requirements realistic (~2 kW)\n✓ Solar power adequate (~9 kW available)\n✓ Fuel cell mass savings confirmed\n✓ L/D targets achievable per EAV-3", {
  x: 0.4, y: 1.45, w: 4.5, h: 1.6, fontSize: 13, fontFace: "Calibri", color: "1B7D3E"
});
slide15.addText("Limitations & Future Validation Needed", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide15.addText("⚠ No wind tunnel testing performed\n⚠ No CFD high-fidelity validation\n⚠ No flight testing\n⚠ Aeroelastic effects modeled conceptually\n⚠ Manufacturing defects not quantified", {
  x: 5.2, y: 1.45, w: 4.3, h: 1.6, fontSize: 13, fontFace: "Calibri", color: COLORS.highlight
});
slide15.addShape(pres.ShapeType.rect, { x: 0.4, y: 3.4, w: 9.2, h: 1.0, fill: { color: COLORS.darkBg }, shadow: makeShadow() });
slide15.addText("This is a CONCEPTUAL DESIGN study. Detailed computational modeling, prototype fabrication, and flight testing are recommended for validation.", {
  x: 0.6, y: 3.6, w: 8.8, h: 0.6, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight, align: "center", valign: "middle"
});

// SLIDE 16: Conclusions
let slide16 = pres.addSlide();
slide16.background = { color: COLORS.darkBg };
slide16.addText("Conclusions", {
  x: 0.5, y: 0.4, w: 8, h: 0.6, fontSize: 28, fontFace: "Calibri", color: COLORS.textLight, bold: true
});
slide16.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: 0.08, h: "100%", fill: { color: COLORS.accent } });
slide16.addText("Objectives Achieved", { x: 0.4, y: 1.1, w: 9, h: 0.35, fontSize: 18, fontFace: "Calibri", color: COLORS.accentLight, bold: true });
slide16.addText("✓ Comprehensive conceptual design developed\n✓ Literature review expanded with recent developments\n✓ Energy system feasibility confirmed\n✓ Design parameters aligned with literature benchmarks\n✓ Trade-offs analyzed and justified", {
  x: 0.4, y: 1.45, w: 9, h: 1.6, fontSize: 14, fontFace: "Calibri", color: COLORS.textLight
});
slide16.addText("Key Findings", { x: 0.4, y: 3.2, w: 9, h: 0.35, fontSize: 18, fontFace: "Calibri", color: COLORS.accentLight, bold: true });
slide16.addText("• Solar-powered HALE UAV is technically feasible for multi-day endurance\n• Hybrid energy storage (fuel cell) essential over pure batteries for night-time power\n• Propulsion optimisation can reduce power demand by up to 19%\n• High-aspect-ratio wings require careful aeroelastic analysis", {
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
slide17.addText("• Detailed CFD and wind tunnel validation\n• Composite wing segment testing\n• Flutter boundary testing\n• Energy management algorithm development", {
  x: 0.4, y: 1.45, w: 4.5, h: 1.4, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark
});
slide17.addText("Long-Term (Development)", { x: 5.2, y: 1.1, w: 4.5, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide17.addText("• Scaled demonstrator fabrication\n• Flight testing validation\n• Technology maturation\n• Mission system integration", {
  x: 5.2, y: 1.45, w: 4.3, h: 1.4, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark
});
slide17.addText("Emerging Technologies to Monitor", { x: 0.4, y: 3.0, w: 9, h: 0.35, fontSize: 16, fontFace: "Calibri", color: COLORS.accent, bold: true });
slide17.addText("• Morphing wings for adaptive aerodynamics\n• Solid-state batteries for improved energy density\n• Ultra-light flexible solar arrays\n• Supercapacitor hybrid storage (eliminating battery degradation)", {
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
  "[2] Goraj, Z. (2004). HALE UAV of a new generation. Bull. Polish Academy",
  "[3] Romeo et al. (2004). HELIPLAT: Design & analysis. Journal of Aircraft",
  "[4] Najafi, Y. (2011). Design of HALE Solar Powered UAV. SJSU MS Thesis",
  "[10] Boukoberine et al. (2019). Energy storage for UAVs. J. Power Sources",
  "[39] Oettershagen et al. (2017). AtlantikSolar UAV. J. Field Robotics",
  "[40] Hwang et al. (2016). KARI EAV-3 aerodynamic design. Journal of Aircraft",
  "[44] Murua et al. (2011). Stability of very flexible aircraft. AIAA"
];
slide18.addText(refs.join("\n\n"), { x: 0.4, y: 1.1, w: 9.2, h: 4.2, fontSize: 12, fontFace: "Calibri", color: COLORS.textDark });

// SLIDE 19: Thank You
let slide19 = pres.addSlide();
slide19.background = { color: COLORS.darkBg };
slide19.addShape(pres.ShapeType.rect, { x: 0, y: 0, w: "100%", h: 0.08, fill: { color: COLORS.accentLight } });
slide19.addText("Questions & Discussion", {
  x: 0.5, y: 1.8, w: 9, h: 0.8, fontSize: 36, fontFace: "Calibri", color: COLORS.textLight, bold: true, align: "center"
});
slide19.addText("Thank You", { x: 0.5, y: 2.8, w: 9, h: 0.6, fontSize: 24, fontFace: "Calibri", color: COLORS.accentLight, align: "center" });
slide19.addText("Parth Patil | 22BTRAS031\nDr Amalesh Barai (Advisor)\nJAIN (Deemed-to-be University), Department of Aerospace Engineering", {
  x: 0.5, y: 3.8, w: 9, h: 1.0, fontSize: 14, fontFace: "Calibri", color: COLORS.accentLight, align: "center"
});

pres.writeFile({ fileName: path.join(__dirname, "HALE_UAV_Presentation.pptx") })
  .then(() => console.log(`Presentation saved to ${path.join(__dirname, "HALE_UAV_Presentation.pptx")}`))
  .catch(err => console.error("Error saving presentation:", err));