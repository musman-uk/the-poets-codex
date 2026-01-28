# Design Notes

## Foundations

- Quiet, intentional design that prioritises reading  
- A manuscript‑like atmosphere rather than a modern interface  
- Minimal ornamentation and a focus on clarity  
- Typography and spacing chosen to support calm, uninterrupted reading  
- A respectful presentation that gives each poet room to breathe  

The foundations of the site are shaped by a desire for quiet clarity, creating a reading environment that feels steady and intentional.

## Navigation

- Minimal, serif typography to echo printed manuscripts  
- Sections are modular and expandable, allowing the site to grow without redesign  
- The homepage acts as a gateway rather than a summary – a simple point of entry  
- Navigation should remain predictable across all pages  
- No competing elements: one primary action per screen  
- Breadcrumb‑like cues may appear subtly, but never as visual noise  

Navigation should feel effortless, offering direction without ever drawing attention to itself.

## Visual Identity

- Neutral tones to keep attention on the text  
- Ample whitespace to create a sense of breath and stillness  
- Poetic restraint: nothing decorative unless it serves clarity  
- Typography should feel literary but not nostalgic or ornate  
- Layouts should scale gracefully on all devices without shifting the tone  
- Images, if used, should be minimal and contextual, never ornamental  

The visual identity aims to feel like a contemporary manuscript, quiet in presentation and respectful in tone.

## Structure & Layout

- Content pages follow a consistent rhythm: title → context → body  
- Side margins remain generous to maintain the manuscript feel  
- Line lengths stay readable, avoiding both cramped and overly wide text  
- Templates in `source/` enforce consistency across all poets and sections  
- The design should support long‑form reading without fatigue  

The structure is designed to encourage slow, attentive reading without visual strain.

## Interaction Principles

- No animations unless they serve clarity  
- Hover and focus states should be subtle but accessible  
- Links should be clearly identifiable without bright colours  
- The interface should never compete with the text for attention  
- Accessibility is a core requirement, not an afterthought  

Interactions should remain subtle and purposeful, supporting the reader without distraction.

## Growth & Maintainability

- New poets and sections should slot naturally into the existing structure  
- The design must remain stable as the site expands  
- The build process ensures consistent output regardless of content size  
- The `.github` workflow regenerates the site without manual intervention  

The site is intended to grow steadily while remaining coherent and easy to maintain.
