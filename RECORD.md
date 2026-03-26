# RECORD

## 1. Design Style

### Reading Environment
- Manuscript‑inspired layout prioritising long‑form readability  
- Neutral palette; whitespace used as a structural element  
- Serif typography with stable line‑height and controlled measure  
- No decorative elements unless they improve clarity or hierarchy  

### Interaction & Accessibility
- Minimal interaction surface; no animations unless functional  
- Predictable navigation across all templates  
- Clear focus states and accessible contrast ratios  
- Links identifiable without relying on saturated colours  

### Layout System
- Consistent page rhythm: title → metadata/context → body  
- Generous side margins to maintain manuscript feel  
- Templates enforce structural consistency across all poet pages  
- Responsive scaling preserves tone and spacing across breakpoints  

---

## 2. Development Process

### Content Model
- Markdown files stored under `source/pages/`  
- Front‑matter metadata defines title, date, palette, and layout parameters  
- Build script parses metadata and injects into Jinja‑like templates  

### Template System
- Base template defines global typography, spacing, and navigation  
- Page‑level templates extend base and apply manuscript layout rules  
- Poets index generated dynamically from parsed metadata  

### Build Pipeline
- Python build script compiles Markdown → HTML  
- Output written to `docs/` for GitHub Pages deployment  
- `.github/workflows/` automates regeneration on push  
- Pipeline must remain deterministic regardless of content volume  

---

## 3. Milestones

### Repository Setup
- Initial folder structure defined  
- Base templates and placeholder pages added  
- Early metadata schema drafted for poet entries  

### Build & Workflow
- Markdown → template mapping established  
- Static generation pipeline implemented  
- GitHub workflow configured for automated builds  

### Content Structure
- First poet folio drafted to validate metadata and layout  
- Navigation and page rhythm stabilised  
- README updated to reflect current architecture  

---

## 4. Version History

### Unreleased
- Added foundational templates and layout system  
- Drafted Home, About, and Poets pages  
- Implemented early build pipeline  
- Introduced design constraints and structural principles  

(Versioning begins at first full release.)

---

## 5. Roadmap

### v1.0.0 — First Release
- Populate Poets section with initial entries  
- Finalise metadata schema (`metadata.json`)  
- Add cross‑links between related poets/themes  
- Ensure stable static generation across all content  
- Prepare structure for incremental expansion  

