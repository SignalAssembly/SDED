# build_sded_v1_2_RevisionB_full.py
# Generates the full SDED v1.2 Revision B multi-page PDF and Zenodo metadata JSON.
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
    alignment=TA_LEFT,
    spaceBefore=12,
    spaceAfter=12
)

# Domain header style (for 'DOMAIN NAME' Approved Library)
domain_style = ParagraphStyle(
    'Domain',
    fontName='Helvetica-Bold',
    fontSize=11,
    spaceBefore=12,
    spaceAfter=6,
    keepWithNext=True
)

# Subdomain header style (for [SUBDOMAIN]: Keywords.)
subdomain_style = ParagraphStyle(
    'Subdomain',
    fontName='Helvetica',
    fontSize=10,
    alignment=TA_LEFT,
    leftIndent=20,
    bulletIndent=10,
    spaceAfter=3,
    spaceBefore=6,
    leading=12
)

# Library entry style (for inline term listings)
library_entry_style = ParagraphStyle(
    'LibraryEntry',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    alignment=TA_LEFT,
    leftIndent=20,
    spaceAfter=6,
    leading=12
)

# Bullet point style (for structural rules section)
bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    alignment=TA_LEFT,
    leftIndent=20,
    bulletIndent=10,
    spaceAfter=6,
    leading=12
)

pdf_filename = "SDED_Protocol_Specification_v1.2.pdf"
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
story.append(Paragraph("<b>SDED v1.2 Revision B: Specification and Approved Vocabulary</b>", styles["Title"]))
story.append(Paragraph("<b>Version:</b> 1.2 Revision B", metadata_style))
story.append(Paragraph("<b>Author:</b> Brian Wijaya", metadata_style))
story.append(Paragraph("<b>Date:</b> October 23, 2025, 10:49 AM CST", metadata_style))
story.append(Paragraph("<b>License:</b> CC-BY 4.0 International", metadata_style))
story.append(Paragraph("<b>DOI:</b> (to be assigned)", metadata_style))
story.append(Spacer(1, 12))

# Prefatory Note with pronunciation line
story.append(Paragraph(
    "<b>Prefatory Note:</b> SDED v1.2 Revision B introduces domain-specific Approved Vocabulary to standardize terminology across multiple fields by using syntactic replacement of eponymous terms with clear, descriptive equivalents. The goal of this update is to eliminate naming ambiguity and honor the SDED v1.1 principles while expanding coverage. All eponymous terms have been systematically replaced with substantive descriptors that convey meaning, with the original name noted for historical context. The vocabulary is organized by subdomain with thematic keyword groupings for efficient reference. This approach promotes clarity and consistency in technical communication across domains.<br/><br/><b>Scope Focus:</b> This version specifically addresses <b>surname-based eponyms</b>—terms named after people. Non-surname-based eponyms (such as purely descriptive acronyms or technical naming conventions) will be addressed in future versions after surname eponyms have been sufficiently covered. This focused approach ensures systematic and thorough treatment of person-based attributions in scientific and technical nomenclature.<br/><br/><b>Pronunciation:</b> SDED is read \"ess-ded,\" or informally \"S Dead,\" reflecting the protocol's goal of replacing dead-end eponyms with living descriptive clarity.",
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
    "<b>Minimal Intervention Principle:</b> SDED replacements preserve all existing substantive terminology from the original eponym and only replace the surname syllables. If an eponym already contains descriptive terms (e.g., \"Fourier <i>Transform</i>\", \"Bohr-Sommerfeld <i>Quantization</i>\"), those substantive words are retained unchanged in the replacement (e.g., \"Frequency-Decomposition <i>Transform</i>\", \"Orbital <i>Quantization</i>\"). Do not arbitrarily change parts of speech (noun to adjective, verb to noun, etc.) or rewrite good terminology. The goal is syntactic equivalence: we replace wasted commemorative syllables with descriptive ones, creating a drop-in substitute. SDED is not about rewriting science—it is about replacing surnames with substance while preserving the conceptual structure of the original term.",
    "<b>Sufficiently Substantive Descriptor Principle:</b> When multiple distinct concepts share a category (e.g., multiple fixed-point theorems, multiple mean-value theorems, multiple separation axioms), the replacement term must include descriptive adjectives that expose the distinguishing taxonomical, ontological, or epistemic quality of that specific concept. For example, \"Brouwer Fixed-Point Theorem™\" cannot be replaced with merely \"Fixed-Point Theorem\" because other fixed-point theorems exist (Banach, Kakutani, Schauder, etc.). The replacement must specify: \"Continuous-Map Fixed-Point Theorem\" to expose that Brouwer's theorem applies specifically to continuous functions on compact convex sets. Similarly, \"Hausdorff Space™\" requires distinction from other separation axioms, becoming \"Point-Separation-by-Neighborhoods Space\" to describe the T2 property. The goal is not simplification but exposition of underlying concepts through maximally informative descriptors that facilitate advancement from intermediate to advanced understanding.",
    "<b>Intermediate-Level Abbreviations:</b> Standard scientific abbreviations understood at the intermediate level (DNA, RNA, ATP, CoA, ATPase, PCR, CRISPR, etc.) are acceptable in replacement terms. Abbreviations that represent advanced abstractions or obscure the underlying concept should be spelled out or replaced with descriptive terms. The goal is to remove surname-based abstractions that obstruct the transition from intermediate to advanced understanding.",
    "<b>Descriptive Replacement:</b> For each eponymous term, create a concise descriptive term that captures the essence of the concept. Any informative noun from the original name (e.g., \"theorem\", \"law\", \"disease\", \"algorithm\") is retained in the new term to indicate the type of concept.",
    "<b>Original Name and Date:</b> After the descriptive term, the original eponym (in full, including any first names or acronyms expanded) is provided in parentheses, suffixed with the trademark symbol ™ to denote it as a historical name, followed by \\\"est.\\\" and the year of establishment or first publication. This preserves the historical attribution without using the name as the primary identifier.<br/><br/>Using \\\"Fourier Transform™\\\" as a joke or critique of scientific naming conventions is legally safe because trademark law only applies to commercial source identifiers, not to expressive commentary.<br/><br/>Adding \\\"™\\\" in that context is an act of parody, not commerce. Parody is protected because it mimics form to make its point; courts consistently recognize that imitating a mark's appearance is lawful when used for humor, criticism, or commentary and not likely to cause confusion.<br/><br/>By writing \\\"Fourier Transform™,\\\" one is not claiming ownership but highlighting the absurdity of privatizing scientific concepts. The act is expressive, non-commercial, and protected under U.S. free-speech doctrine.<br/><br/>This is not mean-spirited; it parallels the linguistic reclamation of descriptive terms such as \\\"tissue\\\" regaining primacy over the brand \\\"Kleenex.\\\" Such reclamation returns language to the commons.",
    "<b>Library Format:</b> Each domain's Approved Library uses a compact, reference-style format. Subdomains are introduced with bracketed headers (e.g., [ANALYSIS]) followed by thematic keyword descriptors (e.g., Functions. Series. Continuity.). Term entries are listed inline in a single paragraph. Unrelated terms are separated by period-space ('. '). Hierarchical eponym branches use colon (':') to introduce child terms, comma (',') to separate children within the branch, and period ('.') to end the branch. Example: Entry-One (Eponym™, est. Year). Broad-Framework (Parent Eponym™, est. Year): Child-One (Parent's First™, est. Year), Child-Two (Parent's Second™, est. Year). Next-Entry (Different Eponym™, est. Year).",
    "<b>Derivative Subdomain Rule:</b> If the number of distinct topical descriptors following a subdomain exceeds the available line length, the subdomain must be split into two or more derivative subdomains. Each new subdomain inherits the base label but is prepended with a substantively descriptive adjective that clarifies its conceptual focus. For example: [ALGORITHMS] may split into [HEURISTIC ALGORITHMS] and [DETERMINISTIC ALGORITHMS].",
    "<b>Domain Grouping:</b> Entries are grouped by their broad domain. Each domain is labeled with single quotes (e.g., 'MATHEMATICS' Approved Library). Within each domain section, related terms across its subdomains are listed using the compact library format.",
    "<b>No Redundancy:</b> Thematic keywords and term entries avoid redundancy. The keyword list provides conceptual orientation while the term entries provide specific replacements for eponyms.",
    "<b>Acronym Expansion:</b> All acronyms used as eponyms must be expanded within the historical name parentheses, with the abbreviation shown in square brackets. Format: Descriptive-Term (Expanded Form [ACRONYM]™, est. Year). For instance, an entry for \"RSA\" must be formatted as: Public-Key Cryptosystem (Rivest-Shamir-Adleman [RSA]™, est. 1977). Similarly, \"BFS\" becomes: Breadth-First Search (Breadth-First Search [BFS]™, est. 1959). This rule ensures that both the full meaning and the common abbreviation are transparent.",
    "<b>Consistent Syntax:</b> The grammar of each entry is constructed to provide clear attribution. Each term entry shows the descriptive replacement followed by the historical eponym and establishment date in a consistent format.",
    "<b>Hierarchical Notation:</b> Punctuation conveys semantic relationships. Period-space ('. ') separates unrelated entries. Colon (':') introduces hierarchical branches where a parent eponym spawned multiple child eponyms (e.g., Newtonian Framework begot Newton's First Law, Newton's Second Law, etc.). Within such branches, commas (',') separate child entries, and a period ('.') terminates the branch. This notation applies when multiple eponyms share a common parent term. The trademark symbol ™ is attached immediately after the historical name without a space, and the \"est.\" date is formatted as a four-digit year (or a c. for circa if approximate).",
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

# Approved Vocabulary
story.append(Paragraph("<b>Approved Vocabulary</b>", heading1_style))
story.append(Paragraph(
    "Below is the complete Approved Vocabulary, organized by domain. Each domain contains thematically grouped terms with their descriptive replacements and original eponymous names.",
    styles["Normal"]
))

# MATHEMATICS
story.append(Paragraph("<b>'MATHEMATICS' Approved Vocabulary</b>", domain_style))

story.append(Paragraph("• <b>[ANALYSIS]:</b> Functions. Series. Continuity. Transformations. Spectra.", subdomain_style))
story.append(Paragraph("Frequency-Decomposition Transform (Fourier Transform™, est. 1822). Curvature-Based Geometry (Riemannian Geometry™, est. 1854). Integral-Summation Series (Bernoulli Series™, est. 1713). Topological-Completeness Space (Hilbert Space™, est. 1902). Complete-Normed Space (Banach Space™, est. 1922). Least-Squares Polynomial (Legendre Polynomials™, est. 1782). Probabilist's-Weight Orthogonal Polynomials (Hermite Polynomials™, est. 1864). Discrete-Time Transform (Z-Transform™, est. 1950). Continuous-Probability Transform (Laplace Transform™, est. 1782). Compactness-Convergence Theorem (Arzelà-Ascoli Theorem™, est. 1895).", library_entry_style))

story.append(Paragraph("• <b>[FUNCTIONAL ANALYSIS]:</b> Operators. Distributions. Weak Convergence. Spectral Theory.", subdomain_style))
story.append(Paragraph("Generalized-Function Distribution (Schwartz Distribution™, est. 1950). Compact-Operator Theory (Fredholm Theory™, est. 1903). Self-Adjoint Extension (von Neumann Extension™, est. 1930). Spectral-Decomposition Theorem (Spectral Theorem™, est. 1930). Dual-Space Representation Theorem (Riesz Representation Theorem™, est. 1907). Weak-Star-Topology Compactness Theorem (Banach-Alaoglu Theorem™, est. 1940).", library_entry_style))

story.append(Paragraph("• <b>[ALGEBRA]:</b> Structures. Relations. Symmetry. Groups. Rings. Fields.", subdomain_style))
story.append(Paragraph("Field-Extension Theory (Galois Theory™, est. 1831). Invariant-Transformation Group (Lie Group™, est. 1873). Ring-Homomorphism Theorem (Noether Isomorphism Theorem™, est. 1921). Curvature-Defined Smooth Geometry (Riemannian Geometry™, est. 1854). Prime-Power-Subgroup Theorems (Sylow Theorems™, est. 1872). Matrix-Canonical Form (Jordan Normal Form™, est. 1870). Cofactor-Determinant Expansion (Laplace Expansion™, est. 1772). Unique-Factorization Domain (Dedekind Domain™, est. 1871). Fundamental-Homomorphism Theorems (Isomorphism Theorems™, est. 1927).", library_entry_style))

story.append(Paragraph("• <b>[LINEAR ALGEBRA]:</b> Matrices. Eigenvalues. Decompositions. Orthogonality.", subdomain_style))
story.append(Paragraph("Generalized-Matrix Inverse (Moore-Penrose Inverse™, est. 1955). Orthogonalization Process (Gram-Schmidt Process™, est. 1883). Dominant-Eigenvalue Iteration (Power Iteration™, est. 1929). QR-Matrix Factorization (QR Decomposition™, est. 1958). Positive-Definite Factorization (Cholesky Decomposition™, est. 1910).", library_entry_style))

story.append(Paragraph("• <b>[GEOMETRY]:</b> Shapes. Curvature. Manifolds. Projective Structures.", subdomain_style))
story.append(Paragraph("Right-Angle Relation (Pythagorean Theorem™, est. c. 500 BC). Conic-Section Classification (Apollonius Theorem™, est. c. 200 BC). Circle-Power Relation (Ptolemy Theorem™, est. c. 150). Angle-Bisector Ratio (Stewart's Theorem™, est. 1746). Triangle-Center Concurrency (Ceva's Theorem™, est. 1678). Parallel-Intercept Proportion (Thales' Theorem™, est. c. 600 BC). Rectangular Coordinates (Rectangular Coordinates™, est. 1637). Polar Coordinates (Polar Coordinates™, est. 1691). Curvature-Torsion Relations (Frenet-Serret Formulas™, est. 1847). Projective-Transformation Geometry (Projective Geometry™, est. 1639).", library_entry_style))

story.append(Paragraph("• <b>[DIFFERENTIAL GEOMETRY]:</b> Curvature. Geodesics. Connections. Bundles.", subdomain_style))
story.append(Paragraph("Intrinsic-Curvature Theorem (Gauss-Bonnet Theorem™, est. 1848). Parallel-Transport Connection (Levi-Civita Connection™, est. 1917). Geodesic-Deviation Field (Jacobi Field™, est. 1866). Curvature Tensor (Riemann Curvature Tensor™, est. 1854). Sectional-Curvature Theorem (Schur's Theorem™, est. 1886). Isometric-Manifold Embedding Theorem (Nash Embedding Theorem™, est. 1956).", library_entry_style))

story.append(Paragraph("• <b>[TOPOLOGY]:</b> Continuity. Compactness. Connectivity. Homotopy.", subdomain_style))
story.append(Paragraph("One-Sided Strip (Möbius Strip™, est. 1858). Non-Orientable Bottle (Klein Bottle™, est. 1882). Topological Characteristic (Euler Characteristic™, est. 1752). Continuous-Map Fixed-Point Theorem (Brouwer Fixed-Point Theorem™, est. 1911). Compact-Closed Theorem (Heine-Borel Theorem™, est. 1895). Fundamental Group (Poincaré Fundamental Group™, est. 1895). Homology Numbers (Betti Numbers™, est. 1871). Point-Separation-by-Neighborhoods Space (Hausdorff Space™, est. 1914). Topological-Dimension-Invariance Theorem (Brouwer Invariance of Domain™, est. 1912).", library_entry_style))

story.append(Paragraph("• <b>[NUMBER THEORY]:</b> Primes. Divisibility. Congruences. Distribution. Diophantine Equations.", subdomain_style))
story.append(Paragraph("Nontrivial-Exponent Insolubility (Fermat's Last Theorem™, est. 1637). Prime-Counting Asymptotic (Prime Number Theorem™, est. 1896). Small-Exponent Congruence (Fermat's Little Theorem™, est. 1640). Simultaneous-Congruence Solution (Chinese Remainder Theorem™, est. c. 300). Quadratic-Reciprocity Law (Gauss Reciprocity™, est. 1796). Repeated-Division Greatest-Common-Divisor Algorithm (Euclidean Algorithm™, est. c. 300 BC). Rational-Approximation Theorem (Dirichlet Approximation™, est. 1842). Critical-Line Hypothesis (Riemann Hypothesis™, est. 1859). Arithmetic-Progression Primes (Dirichlet's Theorem™, est. 1837). Sieve-Bound Method (Brun's Theorem™, est. 1919).", library_entry_style))

story.append(Paragraph("• <b>[CALCULUS]:</b> Limits. Derivatives. Integrals. Series. Sequences.", subdomain_style))
story.append(Paragraph("Indeterminate-Limit Rule (L'Hôpital's Rule™, est. 1696). Power-Series Expansion (Taylor Series™, est. 1715). Zero-Centered Series (Maclaurin Series™, est. 1742). Fundamental-Integration Theorem (Newton-Leibniz Theorem™, est. 1684). Product-Rule Integration Formula (Integration by Parts™, est. 1715). Chain-Rule Integration (Chain Rule Integration™, est. 1686). Derivative-Mean-Value Theorem (Lagrange Mean-Value Theorem™, est. 1797). Extreme-Value Existence (Weierstrass Extreme Value™, est. 1860). Implicit-Function Theorem (Implicit Differentiation™, est. 1878). Dominated-Convergence Theorem (Lebesgue Dominated Convergence™, est. 1904).", library_entry_style))

story.append(Paragraph("• <b>[MULTIVARIABLE CALCULUS]:</b> Gradients. Divergence. Curl. Line Integrals. Surface Integrals.", subdomain_style))
story.append(Paragraph("Line-Integral Theorem (Green's Theorem™, est. 1828). Volume-Flux Theorem (Gauss Divergence Theorem™, est. 1813). Surface-Circulation Theorem (Stokes' Theorem™, est. 1854). Variable Transformation (Jacobian Transformation™, est. 1841). Constrained-Optimization Method (Lagrange Multipliers™, est. 1788). Level-Set Implicit-Function Theorem (Implicit Function Theorem™, est. 1878).", library_entry_style))

story.append(Paragraph("• <b>[PROBABILITY & STATISTICS]:</b> Distributions. Inference. Estimation. Hypothesis Testing.", subdomain_style))
story.append(Paragraph("Conditional-Probability Theorem (Bayes' Theorem™, est. 1763). Normal Distribution (Gaussian Distribution™, est. 1809). Convergence-To-Normal Theorem (Central Limit Theorem™, est. 1922). Sample-Mean-Convergence Law (Law of Large Numbers™, est. 1713). Minimum-Variance Bound (Cramér-Rao Bound™, est. 1946). Maximum-Likelihood Estimation (Fisher's Maximum Likelihood Estimation [MLE]™, est. 1922). Optimal-Test Lemma (Neyman-Pearson Lemma™, est. 1933). Rank-Based Test (Wilcoxon Test™, est. 1945). Goodness-of-Fit Test (Chi-Square Test™, est. 1900). Linear-Correlation Measure (Pearson Correlation™, est. 1895). Rank-Correlation Measure (Spearman Rank™, est. 1904). Likelihood-Curvature Information (Fisher Information™, est. 1925).", library_entry_style))

story.append(Paragraph("• <b>[STOCHASTIC PROCESSES]:</b> Random Walks. Markov Chains. Diffusion. Martingales.", subdomain_style))
story.append(Paragraph("Memoryless-Transition Process (Markov Chain™, est. 1906). Continuous-Random-Walk Process (Wiener Process™, est. 1923). Discrete-Event Process (Poisson Process™, est. 1837). Stochastic-Integration Calculus (Itô Calculus™, est. 1944). Martingale-Convergence Theorem (Doob Martingale Convergence Theorem™, est. 1953). Optional-Stopping Equation (Wald's Equation™, est. 1945). Stationary-Distribution Theorem (Perron-Frobenius Theorem™, est. 1912).", library_entry_style))

story.append(Paragraph("• <b>[LOGIC & SET THEORY]:</b> Axioms. Cardinals. Ordinals. Model Theory.", subdomain_style))
story.append(Paragraph("Set-Theory Axioms (Zermelo-Fraenkel Axioms™, est. 1908). Formal-System Incompleteness Theorems (Gödel's Incompleteness Theorems™, est. 1931). Continuum-Cardinality Hypothesis (Continuum Hypothesis™, est. 1878). Choice-Principle Axiom (Axiom of Choice™, est. 1904). Well-Ordering Theorem (Zermelo's Theorem™, est. 1904). Uncountability Diagonal Argument (Cantor's Diagonal Argument™, est. 1891). Two-Valued Algebra (Boolean Algebra™, est. 1854). Syntactic-Semantic Completeness Theorem (Gödel Completeness Theorem™, est. 1929). Compactness-Logic Theorem (Compactness Theorem™, est. 1930).", library_entry_style))

# PHYSICS
story.append(Paragraph("<b>'PHYSICS' Approved Vocabulary</b>", domain_style))

story.append(Paragraph("• <b>[CLASSICAL MECHANICS]:</b> Motion. Force. Energy. Momentum. Angular Motion.", subdomain_style))
story.append(Paragraph("Classical Mechanics (Newtonian Mechanics™, est. 1687): Inertial-Rest Law (Newton's First Law™, est. 1687), Force-Acceleration Law (Newton's Second Law™, est. 1687), Action-Reaction Law (Newton's Third Law™, est. 1687), Inverse-Square Gravitation (Newton's Law of Gravitation™, est. 1687). Spring-Force Law (Hooke's Law™, est. 1660). Energy-Conservation Mechanics (Lagrangian Mechanics™, est. 1788). Stationary-Action Principle (Hamilton's Principle™, est. 1834). Symmetry-Conservation Theorem (Noether's Theorem™, est. 1915). Planetary-Motion Laws (Kepler's Laws™, est. 1609). Rotating-Frame Force (Coriolis Force™, est. 1835). Fictitious-Outward Force (Centrifugal Force™, est. 1659).", library_entry_style))

story.append(Paragraph("• <b>[FLUID DYNAMICS]:</b> Flow. Pressure. Viscosity. Turbulence. Boundary Layers.", subdomain_style))
story.append(Paragraph("Pressure-Energy Conservation (Bernoulli's Equation™, est. 1738). Viscous-Flow Equations (Navier-Stokes Equations™, est. 1845). Buoyant-Force Principle (Archimedes' Principle™, est. c. 250 BC). Pressure-Transmission Law (Pascal's Law™, est. 1647). Flow-Regime Number (Reynolds Number™, est. 1883). Boundary-Layer Theory (Prandtl Layer™, est. 1904). Vorticity-Transport Equation (Helmholtz Vorticity™, est. 1858). Drag-Coefficient Law (Stokes Drag Law™, est. 1851).", library_entry_style))

story.append(Paragraph("• <b>[THERMODYNAMICS]:</b> Temperature. Entropy. Equilibrium. Heat. Phase Transitions.", subdomain_style))
story.append(Paragraph("Absolute-Temperature Scale (Kelvin™, est. 1848). Entropy-Increase Law (Second Law of Thermodynamics™, est. 1850). Heat-Engine Cycle (Carnot Cycle™, est. 1824). Enthalpy-Additivity Law (Hess's Law™, est. 1840). Throttling-Expansion Effect (Joule-Thomson Effect™, est. 1852). Free Energy (Gibbs Free Energy™, est. 1875). Free Energy (Helmholtz Free Energy™, est. 1882). Real-Gas Equation (Van der Waals Equation™, est. 1873). Magnetic-Transition Temperature (Curie Temperature™, est. 1895). Thermal-Radiation Law (Stefan-Boltzmann Law™, est. 1879). Blackbody-Spectrum Law (Planck's Law™, est. 1900). Peak-Wavelength-Displacement Law (Wien's Displacement Law™, est. 1893).", library_entry_style))

story.append(Paragraph("• <b>[STATISTICAL MECHANICS]:</b> Ensembles. Partition Functions. Phase Space. Ergodicity.", subdomain_style))
story.append(Paragraph("Energy Distribution (Boltzmann Distribution™, est. 1868). Velocity Distribution (Maxwell-Boltzmann Distribution™, est. 1860). Fermion Statistics (Fermi-Dirac Statistics™, est. 1926). Boson Statistics (Bose-Einstein Statistics™, est. 1924). Entropy-Microstate Relation (Boltzmann Entropy™, est. 1877). Energy-Equipartition Theorem (Equipartition Theorem™, est. 1859). Canonical Ensemble (Gibbs Ensemble™, est. 1902).", library_entry_style))

story.append(Paragraph("• <b>[ELECTROMAGNETISM]:</b> Charge. Field. Potential. Induction. Waves.", subdomain_style))
story.append(Paragraph("Field-Evolution Equations (Maxwell's Equations™, est. 1865). Electric-Current Unit (Ampere™, est. 1820). Electric-Potential Unit (Volt™, est. 1860). Magnetic-Flux Unit (Weber™, est. 1852). Magnetic-Density Unit (Tesla™, est. 1880). Resistance Unit (Ohm™, est. 1827). Capacitance Unit (Farad™, est. 1873). Inductance Unit (Henry™, est. 1832). Current-Voltage Law (Ohm's Law™, est. 1827). Electromagnetic-Induction Law (Faraday's Law™, est. 1831). Magnetic Force (Lorentz Force™, est. 1895). Electrostatic-Force Law (Coulomb's Law™, est. 1785). Magnetic-Field Law (Ampère's Law™, est. 1826). Electric-Flux Law (Gauss's Law™, est. 1835). Poynting-Energy Flux (Poynting Vector™, est. 1884).", library_entry_style))

story.append(Paragraph("• <b>[OPTICS]:</b> Reflection. Refraction. Diffraction. Interference. Polarization.", subdomain_style))
story.append(Paragraph("Refraction-Angle Law (Snell's Law™, est. 1621). Least-Time Principle (Fermat's Principle™, est. 1662). Thin-Lens Equation (Lensmaker's Equation™, est. 1693). Double-Slit Interference (Young's Interference™, est. 1801). Diffraction-Limit Criterion (Rayleigh Criterion™, est. 1879). Polarization-Angle Law (Brewster's Law™, est. 1815). Light Scattering (Rayleigh Scattering™, est. 1871). Frequency-Shift Effect (Doppler Effect™, est. 1842). Fresnel Zones (Fresnel Zones™, est. 1818). Double Refraction (Double Refraction™, est. 1669).", library_entry_style))

story.append(Paragraph("• <b>[QUANTUM MECHANICS]:</b> Wavefunctions. Operators. Uncertainty. Entanglement. Measurement.", subdomain_style))
story.append(Paragraph("Quantum-Action Constant (Planck's Constant™, est. 1900). Position-Momentum Uncertainty (Heisenberg Uncertainty™, est. 1927). Wavefunction-Evolution Equation (Schrödinger Equation™, est. 1926). Exclusion Principle (Pauli Exclusion Principle™, est. 1925). Quantized-Orbital Model (Bohr Model™, est. 1913). Orbital Quantization (Bohr-Sommerfeld Quantization™, est. 1916). Matter-Wave Relation (de Broglie Wavelength™, est. 1924). Probabilistic-Interpretation Rule (Born Rule™, est. 1926). Matrix-Formulation Mechanics (Heisenberg Matrix Mechanics™, est. 1925). Time-Independent Perturbation Theory (Rayleigh-Schrödinger Perturbation Theory™, est. 1926). Magnetic-Field Splitting (Zeeman Effect™, est. 1896). Quantum-Electrodynamic Shift (Lamb Shift™, est. 1947). Spin-Orbit Coupling (Fine Structure™, est. 1916). Hyperfine-Structure Splitting (Hyperfine Splitting™, est. 1924).", library_entry_style))

story.append(Paragraph("• <b>[QUANTUM FIELD THEORY]:</b> Fields. Particles. Interactions. Renormalization. Symmetries.", subdomain_style))
story.append(Paragraph("Relativistic-Spin Equation (Dirac Equation™, est. 1928). Field-Quantized Electrodynamics (Quantum Electrodynamics™, est. 1948). Vacuum-Energy Effect (Casimir Effect™, est. 1948). Mass-Generation Mechanism (Higgs Mechanism™, est. 1964). Color-Charge Dynamics (Quantum Chromodynamics™, est. 1973). Electroweak-Unification Model (Weinberg-Salam Theory™, est. 1967). Gauge-Symmetry Theory (Yang-Mills Theory™, est. 1954). Renormalization-Group Flow (Callan-Symanzik Equation™, est. 1970).", library_entry_style))

story.append(Paragraph("• <b>[RELATIVITY]:</b> Spacetime. Curvature. Invariance. Geodesics. Black Holes.", subdomain_style))
story.append(Paragraph("Frame-Transformation Formula (Lorentz Transformation™, est. 1904). Mass-Energy Equivalence (E=mc²™, est. 1905). Time-Dilation Effect (Einstein Time Dilation™, est. 1905). Length-Contraction Effect (Lorentz Contraction™, est. 1889). Velocity-Addition Formula (Einstein Velocity Addition™, est. 1905). Spacetime-Curvature Equations (Einstein Field Equations™, est. 1915). Spherical-Solution Metric (Schwarzschild Metric™, est. 1916). Event-Horizon Radius (Schwarzschild Radius™, est. 1916). Cosmological-Expansion Model (Friedmann Equations™, est. 1922). Gravitational-Wave Solution (Gravitational Waves™, est. 1916). Equivalence-Principle Statement (Einstein Equivalence™, est. 1907). Rotating-Black-Hole Solution (Kerr Metric™, est. 1963).", library_entry_style))

story.append(Paragraph("• <b>[ASTROPHYSICS & COSMOLOGY]:</b> Expansion. Stellar Evolution. Galactic Dynamics. Dark Matter.", subdomain_style))
story.append(Paragraph("Cosmic-Expansion Law (Hubble's Law™, est. 1929). White-Dwarf Mass-Limit (Chandrasekhar Limit™, est. 1931). Neutron-Star Mass-Limit (Tolman-Oppenheimer-Volkoff Limit™, est. 1939). Stellar-Classification Diagram (Hertzsprung-Russell Diagram™, est. 1911). Main-Sequence Duration (Schönberg-Chandrasekhar Limit™, est. 1942). Standard-Candle Supernova (Type Ia Supernova™, est. 1941). Dark-Energy Constant (Cosmological Constant™, est. 1917). Microwave-Background Discovery (Penzias-Wilson CMB™, est. 1965). Rotation-Curve Anomaly (Dark Matter Problem™, est. 1933).", library_entry_style))

story.append(Paragraph("• <b>[PARTICLE PHYSICS]:</b> Quarks. Leptons. Bosons. Symmetries. Standard Model.", subdomain_style))
story.append(Paragraph("Neutron-Discovery Particle (Chadwick Neutron™, est. 1932). Positron-Discovery Antiparticle (Anderson Positron™, est. 1932). Muon-Discovery Lepton (Anderson Muon™, est. 1936). Parity-Violation Experiment (Wu Experiment™, est. 1956). Quark Model (Gell-Mann Quark Model™, est. 1964). CP-Violation Experiment (Cronin-Fitch Experiment™, est. 1964). Weak-Force Bosons (W and Z Bosons™, est. 1983). Higgs-Boson Discovery (ATLAS-CMS Discovery™, est. 2012). Neutrino Oscillations (Neutrino Oscillations™, est. 1998). CKM-Mixing Matrix (Cabibbo-Kobayashi-Maskawa Matrix™, est. 1973).", library_entry_style))

story.append(Paragraph("• <b>[CONDENSED MATTER]:</b> Crystals. Superconductivity. Magnetism. Phase Transitions. Topological States.", subdomain_style))
story.append(Paragraph("Crystal-Diffraction Law (Bragg's Law™, est. 1913). Zero-Resistance State (Superconductivity™, est. 1911). Josephson-Tunneling Effect (Josephson Effect™, est. 1962). Flux Quantum (Flux Quantum™, est. 1961). Integer-Hall Effect (Quantum Hall Effect™, est. 1980). Fractional-Hall Wavefunction (Laughlin Wavefunction™, est. 1983). BCS-Pairing Theory (BCS Theory™, est. 1957). Crystal-Momentum Theorem (Bloch Theorem™, est. 1928). Interacting-Fermion Quasiparticle Liquid (Landau Fermi Liquid™, est. 1956). Spin Glass (Spin Glass™, est. 1972). Topological Insulators (Topological Insulators™, est. 2007).", library_entry_style))

# COMPUTER SCIENCE
story.append(Paragraph("<b>'COMPUTER SCIENCE' Approved Vocabulary</b>", domain_style))

story.append(Paragraph("• <b>[GRAPH ALGORITHMS]:</b> Shortest Paths. Spanning Trees. Network Flow. Traversal.", subdomain_style))
story.append(Paragraph("Shortest-Path Algorithm (Dijkstra's Algorithm™, est. 1956). Shortest-Path With-Negative-Weights (Bellman-Ford Algorithm™, est. 1958). All-Pairs Shortest-Path (Floyd-Warshall Algorithm™, est. 1962). Minimum-Spanning Tree (Kruskal's Algorithm™, est. 1956). Minimum-Spanning-Tree Algorithm (Prim's Algorithm™, est. 1957). Maximum-Flow Algorithm (Ford-Fulkerson Algorithm™, est. 1956). Min-Cut Max-Flow (Max-Flow Min-Cut Theorem™, est. 1956).", library_entry_style))

story.append(Paragraph("• <b>[SORTING & SEARCHING ALGORITHMS]:</b> Comparison. Divide-Conquer. Hashing.", subdomain_style))
story.append(Paragraph("Divide-Merge Sort (Merge Sort™, est. 1945). Partition-Based Sort (Quick Sort™, est. 1960). Heap-Based Sort (Heap Sort™, est. 1964). Binary-Search Algorithm (Binary Search™, est. 1946). Hash-Table Structure (Hash Table™, est. 1953). Balanced-Tree Structure (AVL Tree™, est. 1962).", library_entry_style))

story.append(Paragraph("• <b>[COMPUTATIONAL COMPLEXITY]:</b> Time. Space. Reductions. Completeness.", subdomain_style))
story.append(Paragraph("NP-Completeness Theory (Cook-Levin Theorem™, est. 1971). Polynomial-Time Reduction (Karp Reduction™, est. 1972). Space-Hierarchy Theorem (Savitch's Theorem™, est. 1970).", library_entry_style))

story.append(Paragraph("• <b>[INFORMATION THEORY]:</b> Entropy. Coding. Compression. Channel Capacity.", subdomain_style))
story.append(Paragraph("Information Entropy (Shannon Entropy™, est. 1948). Channel-Capacity Theorem (Shannon-Hartley Theorem™, est. 1948). Source-Coding Theorem (Shannon's Source Coding™, est. 1948). Error-Correcting Code (Hamming Code™, est. 1950). Optimal-Prefix Coding (Huffman Coding™, est. 1952). Sliding-Window Dictionary Compression (Lempel-Ziv 77 [LZ77]™, est. 1977). Arithmetic Coding (Arithmetic Coding™, est. 1976).", library_entry_style))

story.append(Paragraph("• <b>[CRYPTOGRAPHY]:</b> Public-Key. Symmetric. Hashing. Digital Signatures.", subdomain_style))
story.append(Paragraph("Public-Key Cryptosystem (Rivest-Shamir-Adleman [RSA]™, est. 1977). Asymmetric Key-Exchange (Diffie-Hellman™, est. 1976). Binary-Hash-Tree Structure (Merkle Tree™, est. 1979).", library_entry_style))

story.append(Paragraph("• <b>[MACHINE LEARNING & AI]:</b> Learning. Classification. Neural Networks. Optimization.", subdomain_style))
story.append(Paragraph("Machine-Intelligence Test (Turing Test™, est. 1950). Perceptron-Learning Algorithm (Perceptron™, est. 1958). Backpropagation Algorithm (Backpropagation™, est. 1986). Random-Forest Ensemble (Random Forest™, est. 2001). K-Means Clustering (K-Means™, est. 1957). Naive-Bayes Classifier (Naive Bayes™, est. 1960). Decision-Tree Learning (Decision Trees™, est. 1986). PageRank-Link Analysis (PageRank™, est. 1996).", library_entry_style))

story.append(Paragraph("• <b>[COMPUTER ARCHITECTURE]:</b> Instruction Sets. Pipelines. Memory Hierarchy. Parallelism.", subdomain_style))
story.append(Paragraph("Stored-Program Architecture (von Neumann Architecture™, est. 1945). Separate-Memory Architecture (Harvard Architecture™, est. 1944). Pipeline-Hazard Detection (Hazard Detection™, est. 1964). Dynamic-Instruction Scheduling (Tomasulo Algorithm™, est. 1967). Parallel-Speedup Law (Amdahl's Law™, est. 1967).", library_entry_style))

story.append(Paragraph("• <b>[PROGRAMMING LANGUAGES & COMPILERS]:</b> Parsing. Type Systems. Optimization.", subdomain_style))
story.append(Paragraph("Binary-Production Normal Form (Chomsky Normal Form™, est. 1959). Context-Free-Grammar Metalanguage Notation (Backus-Naur Form [BNF]™, est. 1960). Parametric Type-System (Hindley-Milner™, est. 1978). Untyped Lambda Calculus (Church Lambda Calculus™, est. 1932). Fixed-Point Combinator (Y Combinator™, est. 1930).", library_entry_style))

story.append(Paragraph("• <b>[DATABASES & DATA STRUCTURES]:</b> Relational. Transactions. Indexing. Concurrency.", subdomain_style))
story.append(Paragraph("Relational-Database Model (Codd Relational Model™, est. 1970). Normal-Form Decomposition (Boyce-Codd Normal Form™, est. 1974).", library_entry_style))

story.append(Paragraph("• <b>[OPERATING SYSTEMS]:</b> Scheduling. Memory Management. Synchronization. File Systems.", subdomain_style))
story.append(Paragraph("Banker's-Algorithm Deadlock (Banker's Algorithm™, est. 1965). Semaphore-Synchronization Primitive (Dijkstra Semaphore™, est. 1965). Monitor-Synchronization Construct (Hoare Monitor™, est. 1974).", library_entry_style))

# ENGINEERING
story.append(Paragraph("<b>'ENGINEERING' Approved Vocabulary</b>", domain_style))

story.append(Paragraph("• <b>[CONTROL SYSTEMS]:</b> Feedback. Stability. Control Theory. Response Analysis.", subdomain_style))
story.append(Paragraph("Frequency-Response Analysis (Bode Plot™, est. 1938). Root-Locus Method (Evans Root Locus™, est. 1948). Stability-Criterion Analysis (Nyquist Stability™, est. 1932). Optimal-State-Estimation Filter (Kalman Filter™, est. 1960). Optimal-Control Maximum Principle (Pontryagin Maximum Principle™, est. 1956). Energy-Function Stability (Lyapunov Stability™, est. 1892).", library_entry_style))

story.append(Paragraph("• <b>[SIGNAL PROCESSING]:</b> Sampling. Filtering. Transforms. Analysis.", subdomain_style))
story.append(Paragraph("Sampling-Rate Criterion (Nyquist-Shannon Theorem™, est. 1928). Discrete-Fourier Transform (Discrete Fourier Transform [DFT]™, est. 1965). Fast-Fourier Transform (Fast Fourier Transform [FFT]™, est. 1965). Wavelet-Transform Analysis (Morlet Wavelet™, est. 1984). Adaptive-Filter Algorithm (Wiener Filter™, est. 1949). Cepstral-Analysis Method (Cepstrum™, est. 1963). Hilbert-Transform Analysis (Hilbert Transform™, est. 1905).", library_entry_style))

story.append(Paragraph("• <b>[ELECTRICAL CIRCUITS]:</b> Networks. Analysis. Theorems. Impedance.", subdomain_style))
story.append(Paragraph("Circuit-Analysis Theorem (Kirchhoff's Laws™, est. 1845). Network-Equivalence Theorem (Thévenin's Theorem™, est. 1883). Norton-Equivalent Circuit (Norton's Theorem™, est. 1926). Maximum-Power Transfer (Maximum Power Theorem™, est. 1880). Superposition-Principle Analysis (Superposition Theorem™, est. 1845). Mesh-Current Method (Mesh Analysis™, est. 1847). Nodal-Voltage Method (Nodal Analysis™, est. 1847).", library_entry_style))

story.append(Paragraph("• <b>[STRUCTURAL MECHANICS]:</b> Stress. Strain. Elasticity. Failure Criteria.", subdomain_style))
story.append(Paragraph("Elastic-Deformation Law (Hooke's Law™, est. 1678). Structural-Failure Criterion (Mohr-Coulomb Theory™, est. 1773). Beam-Deflection Theory (Euler-Bernoulli Beam™, est. 1750). Column-Buckling Analysis (Euler Buckling™, est. 1757). Stress-Concentration Factor (Peterson's Factor™, est. 1974). Yield-Criterion Theory (Von Mises Yield™, est. 1913). Plasticity-Flow Theory (Prandtl-Reuss Flow™, est. 1924). Fracture-Mechanics Parameter (Griffith Criterion™, est. 1921).", library_entry_style))

story.append(Paragraph("• <b>[MATERIALS SCIENCE]:</b> Properties. Structures. Phase Diagrams. Characterization.", subdomain_style))
story.append(Paragraph("Crystal-Structure Diffraction (Bragg's Law™, est. 1912). Dislocation Vector (Burgers Vector™, est. 1939). Hardness-Testing Scale (Mohs Hardness™, est. 1822). Indentation-Depth Hardness Scale (Rockwell Hardness Scale™, est. 1914). Pyramidal-Indentation Hardness Test (Vickers Hardness Test™, est. 1921). Phase-Transformation Rule (Gibbs Phase Rule™, est. 1876). Hall-Petch Strengthening (Hall-Petch Relation™, est. 1951).", library_entry_style))

story.append(Paragraph("• <b>[FLUID MECHANICS]:</b> Flow. Viscosity. Turbulence. Hydraulics.", subdomain_style))
story.append(Paragraph("Viscous-Flow Equation (Navier-Stokes Equations™, est. 1822). Inviscid-Flow Theory (Euler Equations™, est. 1757). Boundary-Layer Theory (Prandtl Boundary Layer™, est. 1904). Pipe-Flow Friction (Darcy-Weisbach Equation™, est. 1845). Reynolds-Number Similarity (Reynolds Number™, est. 1883). Bernoulli-Energy Conservation (Bernoulli's Principle™, est. 1738). Venturi-Effect Flow (Venturi Effect™, est. 1797). Pitot-Tube Measurement (Pitot Tube™, est. 1732).", library_entry_style))

story.append(Paragraph("• <b>[THERMODYNAMICS]:</b> Heat Transfer. Energy. Efficiency. Cycles.", subdomain_style))
story.append(Paragraph("Ideal-Gas Law (Boyle-Charles Law™, est. 1662). Carnot-Efficiency Cycle (Carnot Cycle™, est. 1824). Rankine-Power Cycle (Rankine Cycle™, est. 1859). Brayton-Gas Cycle (Brayton Cycle™, est. 1872). Stirling-Engine Cycle (Stirling Cycle™, est. 1816). Otto-Combustion Cycle (Otto Cycle™, est. 1876). Diesel-Compression Cycle (Diesel Cycle™, est. 1892). Joule-Thomson Effect (Joule-Thomson Expansion™, est. 1852).", library_entry_style))

# MEDICINE
story.append(Paragraph("<b>'MEDICINE' Approved Vocabulary</b>", domain_style))

story.append(Paragraph("• <b>[NEURODEGENERATIVE CONDITIONS]:</b> Cognitive Decline. Motor Disorders. Dementia. Progressive Decline.", subdomain_style))
story.append(Paragraph("Neural-Degenerative Dementia (Alzheimer's Disease™, est. 1906). Dopaminergic-Motor Disorder (Parkinson's Disease™, est. 1817). Motor-Neuron Degeneration (Lou Gehrig's Disease™, est. 1869). Progressive-Chorea Disorder (Huntington's Disease™, est. 1872). Frontotemporal-Dementia Syndrome (Pick's Disease™, est. 1892). Prion-Encephalopathy Condition (Creutzfeldt-Jakob Disease™, est. 1920). Lewy-Body Dementia (Lewy Body Disease™, est. 1912).", library_entry_style))

story.append(Paragraph("• <b>[AUTOIMMUNE CONDITIONS]:</b> Inflammatory. Systemic. Tissue-Specific. Immune Dysfunction.", subdomain_style))
story.append(Paragraph("Autoimmune-Inflammatory Bowel (Crohn's Disease™, est. 1932). Thyroid-Autoimmune Condition (Graves' Disease™, est. 1835). Hypothyroid-Autoimmune Disorder (Hashimoto's Thyroiditis™, est. 1912). Adrenal-Insufficiency Syndrome (Addison's Disease™, est. 1855). Connective-Tissue Disorder (Sjögren's Syndrome™, est. 1933). Vasculitis-Inflammatory Condition (Kawasaki Disease™, est. 1967). Myasthenic-Neuromuscular Disorder (Myasthenia Gravis™, est. 1877).", library_entry_style))

story.append(Paragraph("• <b>[HEMATOLOGIC CONDITIONS]:</b> Blood Disorders. Clotting. Anemia. Malignancies.", subdomain_style))
story.append(Paragraph("Lymphatic-Malignancy Condition (Hodgkin Lymphoma™, est. 1832). Non-Hodgkin Lymphoma (Burkitt Lymphoma™, est. 1958). Clotting-Factor Deficiency (Hemophilia™, est. 1803). Von-Willebrand Coagulopathy (Von Willebrand Disease™, est. 1926). Sickle-Cell Hemoglobinopathy (Sickle Cell Disease™, est. 1910). Aplastic-Anemia Syndrome (Fanconi Anemia™, est. 1927). Christmas-Factor Deficiency (Christmas Disease™, est. 1952).", library_entry_style))

story.append(Paragraph("• <b>[GENETIC SYNDROMES]:</b> Chromosomal. Metabolic. Developmental. Hereditary.", subdomain_style))
story.append(Paragraph("Trisomy-21 Syndrome (Down Syndrome™, est. 1866). Turner-Monosomy Syndrome (Turner Syndrome™, est. 1938). Klinefelter-Aneuploidy Condition (Klinefelter Syndrome™, est. 1942). Fragile-X Syndrome (Martin-Bell Syndrome™, est. 1943). Marfan-Connective Disorder (Marfan Syndrome™, est. 1896). Cystic-Fibrosis CFTR-Mutation (Cystic Fibrosis™, est. 1938). Tay-Sachs Lysosomal Storage (Tay-Sachs Disease™, est. 1881).", library_entry_style))

story.append(Paragraph("• <b>[CARDIOVASCULAR CONDITIONS]:</b> Cardiac. Vascular. Congenital. Acquired.", subdomain_style))
story.append(Paragraph("Tetralogy-Congenital Defect (Tetralogy of Fallot™, est. 1888). Aortic-Stenosis Syndrome (Wolff-Parkinson-White Syndrome™, est. 1930). Long-QT Arrhythmia (Romano-Ward Syndrome™, est. 1963). Brugada-Arrhythmia Syndrome (Brugada Syndrome™, est. 1992). Takayasu-Arteritis Vasculitis (Takayasu Arteritis™, est. 1908). Kawasaki-Vasculitis Disease (Kawasaki Disease™, est. 1967).", library_entry_style))

story.append(Paragraph("• <b>[INFECTIOUS DISEASES]:</b> Bacterial. Viral. Parasitic. Opportunistic.", subdomain_style))
story.append(Paragraph("Bubonic-Plague Bacterium (Yersinia Pestis™, est. 1894). Tuberculosis-Mycobacterium (Koch's Bacillus™, est. 1882). Lyme-Disease Spirochete (Borrelia Burgdorferi™, est. 1982). Epstein-Barr Herpesvirus (Epstein-Barr Virus [EBV]™, est. 1964). Legionnaires-Disease Bacterium (Legionella™, est. 1976). Mycobacterial-Skin Disease (Hansen's Disease™, est. 1873). Chagas-Disease Trypanosomiasis (Chagas Disease™, est. 1909).", library_entry_style))

story.append(Paragraph("• <b>[ENDOCRINE CONDITIONS]:</b> Hormone Disorders. Metabolic. Glandular. Regulation.", subdomain_style))
story.append(Paragraph("Hyperthyroid-Metabolic State (Graves' Disease™, est. 1835). Cushing-Hypercortisolism Syndrome (Cushing's Syndrome™, est. 1912). Acromegaly-Growth Excess (Acromegaly™, est. 1886). Diabetes-Insipidus ADH-Deficiency (Diabetes Insipidus™, est. 1794). Conn-Aldosterone Excess (Conn's Syndrome™, est. 1955). Sheehan-Postpartum Hypopituitarism (Sheehan's Syndrome™, est. 1937).", library_entry_style))

# BIOLOGY
story.append(Paragraph("<b>'BIOLOGY' Approved Vocabulary</b>", domain_style))

story.append(Paragraph("• <b>[CELLULAR BIOLOGY]:</b> Cell Cycle. Organelles. Membranes. Transport.", subdomain_style))
story.append(Paragraph("Endoplasmic-Reticulum Network (ER™, est. 1945). Secretory-Vesicle Body (Golgi Body™, est. 1898). Citric-Acid Cycle (Krebs Cycle™, est. 1937). Acetyl-CoA Pathway (Acetyl Coenzyme-A™, est. 1951). Sodium-Potassium Pump (Na-K-ATPase™, est. 1957). Immortal Cells (HeLa Cells™, est. 1951). Replication-Senescence Limit (Hayflick Limit™, est. 1961).", library_entry_style))

story.append(Paragraph("• <b>[MOLECULAR GENETICS]:</b> DNA. RNA. Gene Expression. Regulation.", subdomain_style))
story.append(Paragraph("DNA-Polymerase Enzyme (DNA Pol™, est. 1956). Sanger-Sequencing Method (Sanger Method™, est. 1977). PCR-Amplification Technique (Polymerase Chain Reaction™, est. 1983). CRISPR-Gene Editing (CRISPR-Cas9™, est. 2012). Western-Blot Immunoassay (Western Blot™, est. 1979). Southern-Blot Hybridization (Southern Blot™, est. 1975). Northern-Blot RNA-Detection (Northern Blot™, est. 1977). Maxam-Gilbert Sequencing (Maxam-Gilbert Method™, est. 1977).", library_entry_style))

story.append(Paragraph("• <b>[EVOLUTIONARY BIOLOGY]:</b> Selection. Adaptation. Speciation. Population Dynamics.", subdomain_style))
story.append(Paragraph("Natural-Selection Theory (Darwin's Theory™, est. 1859). Inheritance Laws (Mendel's Laws™, est. 1866). Hardy-Weinberg Equilibrium (Hardy-Weinberg Principle™, est. 1908). Runaway-Sexual Selection (Fisherian Runaway™, est. 1930). Hybrid-Incompatibility Model (Dobzhansky-Muller Model™, est. 1936). Island-Population Model (Wright's Island Model™, est. 1931). Neutral-Evolution Theory (Neutral Theory™, est. 1968).", library_entry_style))

story.append(Paragraph("• <b>[ECOLOGY]:</b> Populations. Communities. Ecosystems. Interactions.", subdomain_style))
story.append(Paragraph("Predator-Prey Equations (Predator-Prey Model™, est. 1925). Ecological-Niche Concept (Hutchinson's Niche™, est. 1957). Competitive-Exclusion Law (Gause's Law™, est. 1934). Island-Biogeography Theory (MacArthur-Wilson Theory™, est. 1967). Tolerance Law (Shelford's Law™, est. 1913). Limiting-Factor Law (Liebig's Law™, est. 1840).", library_entry_style))

story.append(Paragraph("• <b>[BIOCHEMISTRY]:</b> Enzymes. Metabolic Pathways. Proteins. Signaling.", subdomain_style))
story.append(Paragraph("Enzyme-Kinetics Model (Michaelis-Menten Equation™, est. 1913). Double-Reciprocal Plot (Lineweaver-Burk™, est. 1934). Protein-Dihedral Plot (Ramachandran Plot™, est. 1963). pH-Buffer Equation (Henderson-Hasselbalch™, est. 1908). Cooperativity-Binding Coefficient (Hill Equation™, est. 1910). Aerobic-Glycolysis Effect (Warburg Effect™, est. 1924). Lactate-Recycling Cycle (Cori Cycle™, est. 1929).", library_entry_style))

# LINGUISTICS AND HUMANITIES
story.append(Paragraph("<b>'LINGUISTICS AND HUMANITIES' Approved Vocabulary</b>", domain_style))

story.append(Paragraph("• <b>[LINGUISTIC THEORY]:</b> Syntax. Semantics. Phonology. Grammar.", subdomain_style))
story.append(Paragraph("Transformational-Generative Linguistics (Chomskyan Linguistics™, est. 1957). Sign-Structure Linguistics (Saussurean Linguistics™, est. 1916). Universal-Grammar Hypothesis (Universal Grammar™, est. 1965). Linguistic-Relativity Hypothesis (Linguistic Relativity™, est. 1940). Conversational-Maxims Pragmatics (Grice's Maxims™, est. 1975). Communication-Functions Model (Jakobson Model™, est. 1960).", library_entry_style))

story.append(Paragraph("• <b>[PHILOSOPHY]:</b> Ethics. Epistemology. Logic. Metaphysics.", subdomain_style))
story.append(Paragraph("Categorical-Imperative Ethics (Kantian Ethics™, est. 1785). Hedonic-Calculus Utilitarianism (Benthamite Utilitarianism™, est. 1789). Substance-Mind-Body Dualism (Cartesian Dualism™, est. 1641). Transcendent-Form Idealism (Platonic Forms™, est. 380 BCE). Categorical-Term Logic (Aristotelian Logic™, est. 350 BCE). Thesis-Antithesis-Synthesis Dialectic (Hegelian Dialectic™, est. 1807). Will-To-Power Perspectivism (Nietzschean Philosophy™, est. 1886).", library_entry_style))

story.append(Paragraph("• <b>[ECONOMIC THEORY]:</b> Markets. Production. Policy. Distribution.", subdomain_style))
story.append(Paragraph("Demand-Side Economics (Keynesian Economics™, est. 1936). Labor-Value Theory (Marxist Economics™, est. 1867). Invisible-Hand Market Economics (Smithian Economics™, est. 1776). Comparative-Advantage Principle (Ricardian Comparative Advantage™, est. 1817). Population-Growth Theory (Malthusian Trap™, est. 1798). Noncooperative-Equilibrium Game-Theory (Nash Equilibrium™, est. 1950). Allocation-Efficiency Criterion (Pareto Optimality™, est. 1906).", library_entry_style))

story.append(Paragraph("• <b>[PSYCHOLOGY]:</b> Cognition. Development. Behavioral Theory. Clinical.", subdomain_style))
story.append(Paragraph("Unconscious-Psychosexual Psychology (Freudian Psychology™, est. 1900). Classical-Conditioning Model (Pavlovian Conditioning™, est. 1897). Radical Behaviorism (Skinnerian Behaviorism™, est. 1938). Cognitive-Development Stages (Piagetian Theory™, est. 1936). Needs-Hierarchy Model (Maslow's Hierarchy™, est. 1943). Psychosocial-Development Stages (Erikson's Stages™, est. 1950). Collective-Unconscious Archetype Psychology (Jungian Psychology™, est. 1912).", library_entry_style))

# Build PDF
doc.build(story)

# Metadata JSON (separate file, not in PDF)
metadata = {
    "title": "SDED v1.2 Revision B Specification and Approved Vocabulary Set 1",
    "version": "1.2 Revision B",
    "author": "Brian Wijaya",
    "license": "CC-BY 4.0 International",
    "publication_date": "2025-10-23T10:49:00-06:00",
    "doi": "[placeholder]",
    "description": "This document defines the SDED v1.2 Revision B protocol and introduces Approved Vocabulary Set 1 (AV-1) organized by domain. It outlines the goals of SDED (replacing eponymous terms with descriptive equivalents across domains for clarity and consistency), details the protocol's structure (scope, syntactic equivalence principle, glossary generation rules, and subdomain expansion policy with derivative subdomain naming rules), and presents thematically grouped Approved Vocabulary for Mathematics, Physics, Computer Science, Engineering, Medicine, Biology, and Linguistics and Humanities. Revision B adds pronunciation guidance and legal commentary on the use of trademark symbols in parody and linguistic reclamation."
}
with open(json_filename, "w") as f:
    json.dump(metadata, f, indent=2)

print("Generated:", pdf_filename, "and", json_filename)
