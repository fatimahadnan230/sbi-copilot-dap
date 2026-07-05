# SBI Co-Pilot: Agentic Digital Adoption Platform (DAP)

### 🚀 State Bank of India (SBI) GFF Hackathon Submission
**Theme:** Agentic AI & Emerging Tech  
**Focus Pillar:** Digital Adoption  

---

## 📌 Project Overview
SBI Co-Pilot is an autonomous multi-agent Digital Adoption Platform designed to sit natively as an overlay layer across SBI's digital ecosystem (YONO, YONO Business, NetBanking). By replacing traditional, massive instruction text documents with dynamic, context-aware "Ghost-Guiding" walkthroughs, it lowers application friction and bridges the digital literacy divide for rural and senior demographics.

## 🌟 Key Differentiators (USPs)
* **Self-Healing UI Guidance:** Dynamically senses application code variations and shifts tooltips on the screen automatically without breaking.
* **Vernacular Voice-to-Action:** Converts casual regional voice input directly into backend financial transaction journeys using Bhashini API mapping.
* **Friction-Predictive Intervention:** Deploys interactive user coaching dynamically when real-time scroll hesitation or telemetry input timeouts are recorded.

---

## ⚙️ Core Technical Architecture

```text
[User Telemetry Stream] ──> [Friction Agent] ──> [Supervisor Orchestrator]
                                                          │
                  ┌───────────────────────────────────────┴───────────────────────────────────────┐
                  ▼                                       ▼                                       ▼
        [Navigation Agent]                        [Document OCR Agent]                 [Compliance/Explainer Agent]
    (Dynamic Tooltip Overlays)                 (Real-time Upload Validation)            (Vernacular Context Summary)
