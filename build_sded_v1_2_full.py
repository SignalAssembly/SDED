# build_sded_v1_2_full.py
# Generates the full SDED v1.2 multi-page PDF and Zenodo metadata JSON.
# Requires: pip install reportlab

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.units import inch
import json

# Initialize styles
styles = getSampleStyleSheet()

# Configure Normal style for body text - justified with proper spacing
styles["Normal"].fontName = "Helvetica"
styles["Normal"].fontSize = 10
styles["Normal"].leading = 12
styles["Normal"].alignment = TA_JUSTIFY
styles["Normal"].spaceAfter = 6

# Configure Title style
styles["Title"].fontName = "Helvetica-Bold"
styles["Title"].fontSize = 16
styles["Title"].alignment = TA_LEFT
styles["Title"].spaceAfter = 6
styles["Title"].leading = 20

# Configure Heading1 for numbered sections
heading1_style = ParagraphStyle(
    'CustomHeading1',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=12,
    spaceBefore=12,
    spaceAfter=6,
    keepWithNext=True
)

# Metadata style (left-aligned, bold labels)
metadata_style = ParagraphStyle(
    'Metadata',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    alignment=TA_LEFT,
    spaceAfter=0,
    leading=12
)

# Prefatory note style
prefatory_style = ParagraphStyle(
    'Prefatory',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceBefore=12,
    spaceAfter=12
)

# Domain header style
domain_style = ParagraphStyle(
    'Domain',
    fontName='Helvetica-Bold',
    fontSize=11,
    spaceBefore=12,
    spaceAfter=6,
    keepWithNext=True
)

# Bullet point style for entries
bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    alignment=TA_JUSTIFY,
    leftIndent=20,
    bulletIndent=10,
    spaceAfter=6,
    leading=12
)

pdf_filename = "SDED_v1_2_full.pdf"
json_filename = "v1.2_metadata.json"

# Configure document with margins matching the reference
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    leftMargin=72,
    rightMargin=72,
    topMargin=72,
    bottomMargin=72
)
story = []

# Title and metadata
story.append(Paragraph("<b>SDED v1.2: Specification and Approved Vocabulary Set 1</b>", styles["Title"]))
story.append(Paragraph("<b>Version:</b> 1.2", metadata_style))
story.append(Paragraph("<b>Author:</b> Brian Wijaya", metadata_style))
story.append(Paragraph("<b>Date:</b> October 23, 2025, 10:49 AM CST", metadata_style))
story.append(Paragraph("<b>License:</b> CC-BY 4.0 International", metadata_style))
story.append(Paragraph("<b>DOI:</b> (to be assigned)", metadata_style))
story.append(Spacer(1, 12))

# Prefatory Note
story.append(Paragraph(
    "<b>Prefatory Note:</b> SDED v1.2 introduces the first Approved Vocabulary Set (AV-1) to standardize terminology across multiple domains by using syntactic replacement of eponymous terms with clear, descriptive equivalents. The goal of this update is to eliminate naming ambiguity and honor the SDED v1.1 principles while expanding coverage. All eponymous terms have been systematically replaced with substantive descriptors that convey meaning, with the original name noted for historical context. This approach promotes clarity and consistency in technical communication across domains.",
    prefatory_style
))

# Section 1
story.append(Paragraph("<b>1. Scope and Proportioning of Coverage (v1.2)</b>", heading1_style))
story.append(Paragraph(
    "Version 1.2 broadens the scope of the Standard Descriptive Eponym Dictionary (SDED) to encompass a wider range of academic and technical domains. AV-1 spans core STEM fields (Mathematics, Physics, Chemistry, Computer Science, Engineering, Medicine) and select areas of the humanities (Linguistics and Philosophy), reflecting a balanced coverage. Each domain's inclusion in AV-1 is proportioned based on the prevalence of eponymous terminology in that field and the impact on cross-disciplinary communication. Emphasis is placed on high-frequency and foundational terms in each domain to maximize the protocol's utility. While STEM domains constitute the majority of entries (reflecting their heavy use of eponyms in laws, theorems, and units), v1.2 also allocates entries to humanities and social sciences to ensure broad applicability. The scope remains extensible: future revisions may incorporate additional domains or subdomains as needed, maintaining proportional representation to avoid any domain dominance. In summary, SDED v1.2 aims for comprehensive yet balanced coverage, ensuring that no field with significant eponym usage is overlooked, and each included domain is covered in proportion to its historical and pedagogical reliance on eponyms.",
    styles["Normal"]
))

# Section 2
story.append(Paragraph("<b>2. Syntactic Equivalence Principle (Addendum to v1.1)</b>", heading1_style))
story.append(Paragraph(
    "SDED v1.2 introduces the <b>Syntactic Equivalence Principle</b>, an addendum to the guidelines established in v1.1. This principle asserts that each eponymous term and its approved descriptive replacement are to be treated as syntactically interchangeable in any context. In practical terms, a sentence using an eponym can be rewritten using the approved descriptor without altering the grammatical structure or meaning. The descriptive term stands in for the eponym one-to-one, serving as a direct substitute rather than a mere explanation. This equivalence extends to plurality, possessive forms, and adjectives derived from the term, ensuring consistency in usage. By formalizing eponym-descriptor pairs as syntactic equals, v1.2 guarantees that adopting the approved vocabulary will not disrupt the flow of technical documents or discourse. This addendum complements v1.1's semantic focus (ensuring terms carry equivalent meaning) with a syntactic guarantee, thereby fully preserving both meaning and grammatical function when replacing eponyms with their descriptive alternatives.",
    styles["Normal"]
))

# Section 3
story.append(Paragraph("<b>3. Structural Rules for Glossary Generation</b>", heading1_style))
story.append(Paragraph(
    "All entries in the Approved Vocabulary adhere to a strict schema to maximize information density and clarity. The structural rules for generating the glossary entries are as follows:",
    styles["Normal"]
))

# Bullet points for section 3
structural_rules = [
    "<b>Descriptive Replacement:</b> For each eponymous term, create a concise descriptive term that captures the essence of the concept. Any informative noun from the original name (e.g., \"theorem\", \"law\", \"disease\", \"algorithm\") is retained in the new term to indicate the type of concept.",
    "<b>Original Name and Date:</b> After the descriptive term, the original eponym (in full, including any first names or acronyms expanded) is provided in parentheses, suffixed with the trademark symbol ™ to denote it as a historical name, followed by \"est.\" and the year of establishment or first publication. This preserves the historical attribution without using the name as the primary identifier.",
    "<b>Colon-Separated Hierarchy:</b> Each entry is formatted as a single line (or paragraph) containing multiple informational components separated by colons ( : ) where appropriate. The pattern generally is: <i>Descriptive Term: Category or field: Brief definition or explanation (Original Eponym™ est. Year)</i>. The use of two or more colons creates a hierarchy of information (e.g., classification, then definition) within one entry, allowing complex information to be conveyed succinctly.",
    "<b>Domain Grouping:</b> Entries are grouped by their broad domain. Each domain is labeled in all caps, followed by a bracketed list of representative subdomains separated by bullet points ( • ) on the same line. Within each domain section, related terms across its subdomains are listed. This grouping aids users in scanning for terms relevant to a particular field.",
    "<b>No Redundancy:</b> If a descriptive term inherently includes a categorization (for example, \"Law\", \"Theory\", \"Algorithm\"), additional category labels may be omitted to avoid redundancy. Conversely, if the term is generic, a category label (e.g., \"genetic disorder\", \"optics principle\") is included after the first colon to clarify the context.",
    "<b>Acronym Expansion:</b> All acronyms used as eponyms are expanded within the original name in parentheses. For instance, an entry for \"RSA\" will present the expanded form \"Rivest–Shamir–Adleman\" in the parentheses of the original name. This rule ensures that the historical names are fully transparent.",
    "<b>Consistent Syntax:</b> The grammar of each entry is constructed to read as a coherent statement. A reader should be able to interpret the descriptive term and its explanation as a definition or identification of the concept. Colons serve as separators but the entry as a whole forms a meaningful description.",
    "<b>Formatting:</b> Each entry ends with a period only if it forms a complete sentence; otherwise, punctuation is minimized to the internal commas and the final parenthetical historical note. The trademark symbol ™ is attached immediately after the historical name without a space, and the \"est.\" date is formatted as a four-digit year (or a c. for circa if approximate).",
    "<b>Verification:</b> Each descriptive term is verified to ensure it does not introduce ambiguity and that it can replace the eponym in typical usage. The glossary generation process includes peer review to catch any descriptive names that might overlap with other concepts or lack clarity."
]

for rule in structural_rules:
    story.append(Paragraph("• " + rule, bullet_style))

story.append(Paragraph(
    "By following these structural rules, SDED v1.2's glossary achieves a high density of information while maintaining readability and consistency, thus making the Approved Vocabulary easy to adopt and reference across different disciplines.",
    styles["Normal"]
))

# Section 4
story.append(Paragraph("<b>4. Subdomain Expansion Rule</b>", heading1_style))
story.append(Paragraph(
    "The <b>Subdomain Expansion Rule</b> governs how new subject areas are incorporated into the SDED vocabulary structure. As knowledge domains evolve, SDED must remain adaptable. The rule stipulates that subdomains can be added to a domain's bracketed list (or new domains introduced) when the volume or significance of new eponymous terms in that area warrants inclusion. The criteria are: - <b>Threshold of Inclusion:</b> A new subdomain should be introduced once there are a significant number of terms (e.g., five or more) from that area identified for approved naming, or if the subdomain represents an emerging field of high relevance (even with fewer terms). - <b>Maintaining Balance:</b> Any expansion should maintain the overall proportional coverage. When adding many terms in a new subdomain, consider adding or highlighting terms in other domains if needed to preserve a balanced cross-domain representation. - <b>Append-only Growth:</b> The structure of existing domains and subdomains is preserved for backward compatibility. New subdomains are appended to the domain's list, and new domain sections are appended to the document in alphabetical order (or logical order if a grouping is preferable). Existing entries are not shuffled between subdomains in a way that would change references from previous versions. - <b>Cross-Domain Entries:</b> If a term could belong to multiple domains or subdomains, it is placed under the domain where its usage is most dominant. Cross-references may be noted in future revisions, but duplication of entries is avoided to keep the vocabulary set streamlined. - <b>Versioning:</b> Any expansion of subdomains (or domains) triggers a version update. The version number (as in v1.2) reflects substantive additions. Minor additions or corrections within existing subdomains can be handled in patch versions (e.g., v1.2.1) but adding an entirely new subdomain would justify an increment to v1.3 or higher. - <b>Documentation:</b> New subdomains and their rationale for inclusion are to be documented in the Scope section of that version's specification, preserving a record of how the coverage of SDED evolves over time.",
    styles["Normal"]
))

story.append(Paragraph(
    "By enforcing the Subdomain Expansion Rule, SDED ensures that its growth is methodical and justified, preventing ad-hoc additions that could skew the focus or usability of the Approved Vocabulary. This rule helps maintain the integrity of the SDED structure as it expands, keeping it systematic and user-friendly.",
    styles["Normal"]
))

# Approved Vocabulary Set 1
story.append(Paragraph("<b>Approved Vocabulary Set 1 (AV-1)</b>", heading1_style))
story.append(Paragraph(
    "Below is the complete Approved Vocabulary Set 1, organized by domain. Each domain section lists the descriptive replacement terms followed by the original eponymous name and establishment date. All eponyms have been syntactically replaced according to the SDED v1.2 guidelines.",
    styles["Normal"]
))

# MATHEMATICS
story.append(Paragraph("<b>MATHEMATICS [Algebra • Geometry • Calculus • Number Theory • Statistics • Topology]</b>", domain_style))
math_entries = [
    "<b>Right-Angle Triangle Theorem:</b> geometry: relates the squares of the sides in a right triangle (Pythagorean Theorem™ est. ~520 BC).",
    "<b>Nontrivial Exponent Insolubility Theorem:</b> number theory: no positive integer solutions exist for x^n + y^n = z^n when n > 2 (Fermat's Last Theorem™ est. 1637).",
    "<b>Inverse Probability Theorem:</b> statistics: fundamental formula for updating probabilities with new evidence (Bayes' Theorem™ est. 1763).",
    "<b>Normal Distribution:</b> statistics: bell-curve probability distribution for random variables (Gaussian Distribution™ est. 1809).",
    "<b>Greatest Common Divisor Algorithm:</b> algebra: method to compute the largest common divisor of two integers (Euclidean Algorithm™ est. ~300 BC).",
    "<b>Recursive Two-Term Sequence:</b> algebra: sequence in which each term is the sum of the two preceding terms (Fibonacci Sequence™ est. 1202).",
    "<b>Infinitesimal Quotient Rule:</b> calculus: rule for evaluating limits of indeterminate ratios by differentiating numerator and denominator (L'Hôpital's Rule™ est. 1696).",
    "<b>Power Series Expansion:</b> calculus: infinite polynomial series that approximates functions near a point (Taylor Series™ est. 1715).",
    "<b>Rectangular Coordinate System:</b> geometry: two-dimensional coordinate system defined by perpendicular axes (Cartesian Coordinates™ est. 1637).",
    "<b>One-Sided Surface:</b> topology: surface with only one continuous side and one boundary component (Möbius Strip™ est. 1858)."
]
for entry in math_entries:
    story.append(Paragraph("• " + entry, bullet_style))

# PHYSICS
story.append(Paragraph("<b>PHYSICS [Classical Mechanics • Optics • Electromagnetism • Thermodynamics • Quantum Physics • Astrophysics]</b>", domain_style))
physics_entries = [
    "<b>Principle of Inertia:</b> classical mechanics: an object remains at rest or in uniform motion unless acted on by a force (Newton's First Law™ est. 1687).",
    "<b>Force–Mass–Acceleration Law:</b> classical mechanics: force on an object equals its mass times its acceleration (Newton's Second Law™ est. 1687).",
    "<b>Action–Reaction Law:</b> classical mechanics: for every action force there is an equal and opposite reaction force (Newton's Third Law™ est. 1687).",
    "<b>Inverse-Square Gravitation Law:</b> classical mechanics: gravitational force between two masses is proportional to 1/r^2 (Newton's Law of Universal Gravitation™ est. 1687).",
    "<b>Spring Force Proportionality Law:</b> mechanics: extension of a spring is proportional to the applied force (Hooke's Law™ est. 1660).",
    "<b>Refraction Sine Law:</b> optics: the ratio of sines of the angles of incidence and refraction is constant for a given medium interface (Snell's Law™ est. 1621).",
    "<b>Principle of Least Time:</b> optics: light follows the path that takes the least time between two points (Fermat's Principle™ est. 1662).",
    "<b>Fluid Pressure Transmission Law:</b> fluid mechanics: pressure applied to an enclosed fluid is transmitted undiminished throughout (Pascal's Law™ est. 1647).",
    "<b>Buoyant Force Principle:</b> fluid mechanics: an object submerged in fluid experiences an upward force equal to the weight of displaced fluid (Archimedes' Principle™ est. ~250 BC).",
    "<b>Voltage–Current Proportionality Law:</b> electromagnetism: voltage across a conductor is directly proportional to the current through it (Ohm's Law™ est. 1827).",
    "<b>Electromagnetic Field Equations:</b> electromagnetism: set of four equations governing electric and magnetic fields (Maxwell's Equations™ est. 1865).",
    "<b>Relativistic Transformation Equations:</b> relativity: formulas for converting space-time coordinates between inertial frames moving at constant velocity (Lorentz Transformations™ est. 1904).",
    "<b>Quantum of Action Constant:</b> quantum physics: fundamental constant relating energy and frequency of a photon (Planck's Constant™ est. 1900).",
    "<b>Uncertainty Principle:</b> quantum physics: it is impossible to simultaneously know a particle's exact position and momentum (Heisenberg's Uncertainty Principle™ est. 1927).",
    "<b>Cosmic Expansion Law:</b> astrophysics: galaxies recede from each other at speeds proportional to their distance apart (Hubble's Law™ est. 1929).",
    "<b>White Dwarf Mass Limit:</b> astrophysics: maximum mass above which a white dwarf star collapses (Chandrasekhar Limit™ est. 1931).",
    "<b>Ferromagnetic Critical Temperature:</b> solid-state physics: temperature above which a ferromagnetic material loses its magnetism (Curie Temperature™ est. 1895)."
]
for entry in physics_entries:
    story.append(Paragraph("• " + entry, bullet_style))

# CHEMISTRY
story.append(Paragraph("<b>CHEMISTRY [Physical Chemistry • Thermodynamics • Organic Chemistry • Analytical Chemistry]</b>", domain_style))
chemistry_entries = [
    "<b>Inverse Pressure–Volume Law:</b> gas laws: at constant temperature, the pressure of a gas is inversely proportional to its volume (Boyle's Law™ est. 1662).",
    "<b>Proportional Volume–Temperature Law:</b> gas laws: at constant pressure, the volume of a gas is directly proportional to its absolute temperature (Charles's Law™ est. 1787).",
    "<b>Mole Particle Constant:</b> physical chemistry: the number of elementary entities (atoms or molecules) in one mole, approximately 6.022×10^23 (Avogadro's Number™ est. 1811).",
    "<b>Equilibrium Shift Principle:</b> chemistry: a system at equilibrium adjusts to counteract imposed changes (Le Châtelier's Principle™ est. 1884).",
    "<b>Heat Summation Law:</b> thermochemistry: the total enthalpy change of a reaction is the same, regardless of the number of steps (Hess's Law™ est. 1840).",
    "<b>Absorbance Proportionality Law:</b> analytical chemistry: the absorbance of light by a solution is proportional to the concentration of the absorbing species and path length (Beer–Lambert Law™ est. 1852).",
    "<b>Temperature-Dependent Rate Equation:</b> kinetics: reaction rate constant varies with temperature according to an exponential relation (Arrhenius Equation™ est. 1889)."
]
for entry in chemistry_entries:
    story.append(Paragraph("• " + entry, bullet_style))

# COMPUTER SCIENCE
story.append(Paragraph("<b>COMPUTER SCIENCE [Algorithms • Cryptography • Computer Architecture • Software Engineering]</b>", domain_style))
cs_entries = [
    "<b>Public-Key Cryptosystem:</b> cryptographic algorithm: first widely used algorithm for secure asymmetric encryption (Rivest–Shamir–Adleman (RSA)™ est. 1977).",
    "<b>Machine Intelligence Imitation Test:</b> artificial intelligence: evaluates a machine's ability to exhibit human-like intelligence through conversation (Turing Test™ est. 1950).",
    "<b>Parallel Speedup Limit Law:</b> computing: theoretical limit on the speedup achievable by parallelizing a task, due to serial portions (Amdahl's Law™ est. 1967).",
    "<b>Transistor Density Doubling Trend:</b> electronics: observation that the number of transistors on integrated circuits doubles approximately every two years (Moore's Law™ est. 1965).",
    "<b>Network Value Square Law:</b> networking: the value of a network grows proportional to the square of the number of its users or nodes (Metcalfe's Law™ est. 1980).",
    "<b>Organization Mirroring Principle:</b> software engineering: the structure of a software system reflects the communication structure of the organization that built it (Conway's Law™ est. 1968).",
    "<b>Stored-Program Computer Architecture:</b> computer architecture: design where instructions and data share the same memory, forming the basis of most modern computers (von Neumann Architecture™ est. 1945).",
    "<b>Single-Source Shortest Path Algorithm:</b> graph theory: algorithm to find the shortest paths from a given source node to all other nodes in a weighted graph (Dijkstra's Algorithm™ est. 1959)."
]
for entry in cs_entries:
    story.append(Paragraph("• " + entry, bullet_style))

# ENGINEERING
story.append(Paragraph("<b>ENGINEERING [Mechanical • Electrical • Civil • Control Systems • Aerospace]</b>", domain_style))
eng_entries = [
    "<b>Linear Elasticity Equation:</b> mechanics: relation stating that deformation is directly proportional to applied stress within elastic limit (Hooke's Law™ est. 1660).",
    "<b>Fluid Flow Energy Equation:</b> fluid dynamics: conservation of energy in flowing fluids, relating pressure, velocity, and height (Bernoulli's Equation™ est. 1738).",
    "<b>Viscous Flow Field Equations:</b> fluid dynamics: partial differential equations governing the motion of viscous fluid substances (Navier–Stokes Equations™ est. 1845).",
    "<b>Inertial–Viscous Ratio (Re) Number:</b> fluid dynamics: dimensionless number expressing the ratio of inertial forces to viscous forces in fluid flow (Reynolds Number™ est. 1883).",
    "<b>Harmonic Analysis Transform:</b> signal processing: mathematical transform that decomposes functions into oscillatory components (Fourier Transform™ est. 1822).",
    "<b>Design-Failure Adage:</b> engineering maxim: \"anything that can go wrong will go wrong,\" emphasizing the importance of robust design (Murphy's Law™ est. 1949).",
    "<b>Optimal Estimation Algorithm:</b> control systems: recursive algorithm for estimating the state of a process in the presence of noise (Kalman Filter™ est. 1960)."
]
for entry in eng_entries:
    story.append(Paragraph("• " + entry, bullet_style))

# MEDICINE
story.append(Paragraph("<b>MEDICINE [Anatomy • Pathology • Genetics • Clinical Medicine]</b>", domain_style))
med_entries = [
    "<b>Primary Degenerative Dementia:</b> neurology: progressive cognitive decline and memory loss due to neurodegeneration (Alzheimer's Disease™ est. 1906).",
    "<b>Idiopathic Motor Neuron Disorder:</b> neurology: degenerative condition causing tremors, rigidity, and bradykinesia (Parkinson's Disease™ est. 1817).",
    "<b>Trisomy 21 Syndrome:</b> genetics: congenital condition caused by an extra chromosome 21, leading to developmental and intellectual delays (Down Syndrome™ est. 1866).",
    "<b>Malignant Lymphatic Neoplasm:</b> oncology: cancer of lymphatic tissue characterized by Reed–Sternberg cells (Hodgkin Lymphoma™ est. 1832).",
    "<b>Acute Immune Polyneuropathy:</b> neurology: rapid-onset autoimmune disorder causing muscle weakness and paralysis (Guillain–Barré Syndrome™ est. 1916).",
    "<b>Chronic Intestinal Inflammatory Disease:</b> gastroenterology: long-term inflammatory disorder of the gastrointestinal tract (Crohn's Disease™ est. 1932).",
    "<b>Neonatal Vitality Score:</b> neonatology: scoring method evaluating newborns on appearance, pulse, grimace, activity, and respiration (Apgar Score™ est. 1952).",
    "<b>Glomerular Capsule:</b> anatomy: cup-like sack at the beginning of the kidney tubule that performs the first step in filtering blood (Bowman's Capsule™ est. 1842).",
    "<b>Uterine Tubes:</b> anatomy: pair of tubes through which ova travel from the ovaries to the uterus (Fallopian Tubes™ est. 1564)."
]
for entry in med_entries:
    story.append(Paragraph("• " + entry, bullet_style))

# BIOLOGY
story.append(Paragraph("<b>BIOLOGY [Genetics • Physiology • Biochemistry • Evolution]</b>", domain_style))
bio_entries = [
    "<b>Laws of Heredity:</b> genetics: two foundational principles of inheritance (segregation and independent assortment) describing genetic trait transmission (Mendel's Laws™ est. 1865).",
    "<b>Citric Acid Cycle:</b> biochemistry: core metabolic pathway for energy production through oxidation of acetate into CO₂ (Krebs Cycle™ est. 1937).",
    "<b>Carbon Fixation Cycle:</b> plant physiology: set of biochemical reactions converting carbon dioxide into organic molecules during photosynthesis (Calvin Cycle™ est. 1950).",
    "<b>Adaptive Evolution Theory:</b> evolutionary biology: theory of species change over time by natural selection acting on heritable variation (Darwinian Evolution™ est. 1859)."
]
for entry in bio_entries:
    story.append(Paragraph("• " + entry, bullet_style))

# LINGUISTICS AND HUMANITIES
story.append(Paragraph("<b>LINGUISTICS AND HUMANITIES [Linguistics • Philosophy • Psychology • Economics]</b>", domain_style))
humanities_entries = [
    "<b>Linguistic Relativity Hypothesis:</b> linguistics: proposal that the structure of a language affects its speakers' cognition and world-view (Sapir–Whorf Hypothesis™ est. 1929).",
    "<b>Principle of Parsimony:</b> philosophy: problem-solving heuristic favoring the simplest explanation that fits the facts (Occam's Razor™ est. 1324).",
    "<b>Unconscious Speech Error:</b> psychology: an inadvertent mistake in speech thought to reveal an unconscious belief or thought (Freudian Slip™ est. 1901).",
    "<b>Needs Pyramid:</b> psychology: hierarchical model of human motivation depicted as a pyramid from basic needs to self-actualization (Maslow's Hierarchy of Needs™ est. 1943).",
    "<b>80/20 Distribution Principle:</b> economics: observation that roughly 80% of effects come from 20% of causes, applied in wealth, productivity, and other domains (Pareto Principle™ est. 1906).",
    "<b>Assumed Stupidity Principle:</b> adage: advises not to attribute to malice that which can be adequately explained by incompetence (Hanlon's Razor™ est. 1980).",
    "<b>No-Original-Discoverer Law:</b> sociology of science: states that no scientific discovery is ever named after its first discoverer (Stigler's Law of Eponymy™ est. 1980).",
    "<b>Imitation Game:</b> popular culture; a parlour game analogy used to describe the test for machine intelligence (Turing's Imitation Game™ est. 1950)."
]
for entry in humanities_entries:
    story.append(Paragraph("• " + entry, bullet_style))

# Build PDF
doc.build(story)

# Metadata JSON (separate file, not in PDF)
metadata = {
    "title": "SDED v1.2 Specification and Approved Vocabulary Set 1",
    "author": "Brian Wijaya",
    "license": "CC-BY 4.0 International",
    "publication_date": "2025-10-23",
    "doi": "[placeholder]",
    "description": "This document defines the SDED v1.2 protocol and introduces Approved Vocabulary Set 1 (AV-1). It outlines the goals of SDED (replacing eponymous terms with descriptive equivalents across domains for clarity and consistency), details the protocol's structure (scope, syntactic equivalence principle, glossary generation rules, and subdomain expansion policy), and presents the fully expanded AV-1 containing standardized descriptive terms for key concepts in Mathematics, Physics, Chemistry, Computer Science, Engineering, Medicine, and Humanities."
}
with open(json_filename, "w") as f:
    json.dump(metadata, f, indent=2)

print("Generated:", pdf_filename, "and", json_filename)
