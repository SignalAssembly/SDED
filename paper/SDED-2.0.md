# SDED 2.0: Self-Documenting Terminology for the Arts and Humanities

## Naming as an Engineered Knowledge Interface

Brian Wijaya | September 8, 2026 | Version 2.0 publication candidate

Conceptual framework, protocol specification, and research agenda. CC BY 4.0.

## Abstract

Terminology is an interface through which people retrieve, distinguish, construct, and transmit knowledge. Its quality cannot be evaluated by brevity or historical familiarity alone. This paper extends Substantive-Description Eponym Deprecation (SDED) from surname-based naming reform to a broader analysis of opaque labels, hidden defaults, category migration, structural asymmetry, and misleading compression in the arts and humanities. It proposes an audience-relative protocol that separates concept identity, descriptive name, conventional alias, compact symbol, contextual function, and provenance. Music supplies the principal case study: seventh-chord nomenclature, suspensions, inversions, modes, meter, and instrument classifications expose failures that are not reducible to eponymy. Philosophy supplies a second test, where descriptions can clarify arguments but can also prejudge contested conclusions or erase historically specific positions. A wider humanities survey identifies cases for retention, supplementation, disambiguation, and replacement. Controlled verbosity is treated as a testable design hypothesis: explicit components may improve reconstruction and error detection, while increasing reading and coordination costs. The framework incorporates cultural authority, backward compatibility, and multilingual scope rather than imposing universal renaming. It provides an intervention taxonomy, an auditable evaluation profile, and experiments comparing conventional, descriptive, and layered terminology. Its contribution is a method for evaluating naming systems and governing changes; it does not claim that proposed labels have already demonstrated learning benefits.

## 1. The problem: names as interfaces

A learner encounters a name and must do something with it: recognize a sound, construct a chord, identify a claim, find a source, distinguish a school, or describe an artifact. The relevant question is whether the name supplies the information required for that task. A label can be efficient for retrieval and poor for construction. It can be structurally uninformative while being historically indispensable. It can be a good symbol and a bad pedagogical expansion.

SDED 2.0 evaluates these differences explicitly. The proposal is neither a purified vocabulary without history nor a rule that every name must contain its definition. It is a protocol for making dependencies visible and choosing appropriate naming layers. The strongest case for change occurs when a label conceals a small, stable, useful structure that its intended readers could readily understand if it were expressed.

The central unit of analysis is a **term-in-use within a conceptual family**, not an isolated word. A family may be a product of dimensions, a branching classification, a historically connected collection, or a set of competing positions. Those are different structures. One should not impose the grammar of a product on a historical tradition or mistake a list of related words for a taxonomy.

In this paper, *self-documenting* means that an intended reader can recover specified distinguishing information from the name using an explicitly stated prerequisite vocabulary. It does not mean comprehensible to a reader who knows no language or domain concepts. A name such as *major triad with minor seventh above its root* presupposes triad, major, minor, interval, seventh, and root. It replaces a special-purpose lookup with reusable knowledge; it does not eliminate prerequisites.

The music examples primarily concern Western staff notation, common-practice tonal analysis, and selected jazz and popular-music conventions. This scope is stated rather than smuggled in as universal music theory. Cultural traditions require their own accounts of what distinctions matter.

## 2. What the original SDED project established

### 2.1 Publication, development, and recovery

The registered v1.1 paper is **SDED™ Protocol Specification: Substantive-Description Eponym Deprecation — A Community Standard for Non-Arbitrary Naming in Knowledge Bases**, issued October 22, 2025. Its version DOI is [10.5281/zenodo.17418489](https://doi.org/10.5281/zenodo.17418489); the series DOI is [10.5281/zenodo.17418488](https://doi.org/10.5281/zenodo.17418488). DataCite identifies it as v1.1 and describes a community protocol for descriptive-first naming, epistemic transparency, educational materials, databases, and ontologies. [Publication registration](https://api.datacite.org/dois/10.5281/zenodo.17418489).

The present reconstruction also uses the subsequent v1.2 PDFs and builders in [SignalAssembly/SDED](https://github.com/SignalAssembly/SDED), especially revision `9023bf4`, and an author-retained October 2025 conversation excerpt. These are development sources, not interchangeable copies of the deposited v1.1 paper. Zenodo's public record API confirmed that the deposit includes both v1.0 and v1.1 PDFs. The file downloads and login page timed out, so the deposited PDF text could not be inspected. The registration confirms publication identity and stated aims, but it does not establish every clause of the full paper. The historical report accompanying this manuscript records that limitation.

The v1.2 implementation is more specific than the registration abstract. Its strongest principles are:

1. **Minimal Intervention:** retain meaningful parts of an existing term. Replacing an opaque modifier does not license changing *theorem* into *framework*, *forms* into *philosophy*, or a property into a method.
2. **Sufficiently Substantive Descriptor:** distinguish the intended concept from its nearest alternatives. Removing a surname while leaving only *fixed-point theorem* discards the very information the name must recover.
3. **Syntactic Equivalence:** aim for a usable name that can occupy the original expression's grammatical role, rather than appending an explanation that cannot be used in discourse.
4. **Preserved Attribution:** move historical naming information into an explicit accompanying layer.
5. **Audience-Relative Abbreviation:** abbreviations familiar at an intermediate level need not be mechanically expanded; the target was obstruction between intermediate and advanced understanding.
6. **Systematic Extension:** organize related terms and make new vocabulary follow a rule rather than accumulate exceptions.

These principles are recoverable from the later specification and author corrections. They should not be confused with every generated replacement in the vocabulary. The implementation often fell short of the principle it asserted.

### 2.2 Evolution visible in the conversations

The recovered timestamped October 22, 2025 conversation establishes the original formulation directly. The author first requested a copyright-style mark on the descriptive name, then explicitly moved to a trademark-style mark on the historical name. At 12:19 he supplied the expansion *Substantive-Description Eponym Deprecation*, the community-oriented purpose, and the descriptor-first historical-name/date syntax. Later that day he requested v1.1 to accept ASCII `(TM)` and added low-friction reference/propagation guidance. The typographic difficulty remembered in the present request is documented in repeated PDF-generation attempts. These are primary records of the drafting discussion, not byte verification of the deposited PDFs.

An October 15 naming discussion already defends verbose category words in filenames because they expose category/instance structure. The October 23 *Vector as 1D array* transcript then connects mathematical naming opacity to the published DOI, directly confirms the author's identity, and develops the v1.2 approved-vocabulary plan. It records a preference for conceptual organization over chronological order and for PDF plus self-contained HTML. The original pronunciation is *ess-ded* or *S Dead*, with an “it's dead” wordplay; it is retained as history, not a requirement to abandon every inherited name.

The October excerpt shows repeated refinement. The author first demands real descriptive replacements rather than dictionary definitions. He clarifies that punctuation distinguishes unrelated entries from historical branches. He narrows the immediate version to surname-based terms while anticipating broader work later. He then insists that informative head nouns and parts of speech survive the operation. Next he rejects generic substitutes that fail to distinguish neighbors. Finally he allows substantial length and qualifies acronym expansion by the reader's knowledge.

That is a progression toward **discriminative naming**, not merely toward deleting personal names. Some assistant proposals violated it: *Power Series* was offered for a particular named series; a stability property was described through an energy-function proof technique; broad classes were used as substitutes for specific algorithms. Such proposals are evidence of failure modes in the drafting process, not endorsed scientific conclusions.

A February 9, 2026 local session note applies SDED to operational tool names, including changes from *know* to *recall* and *simulate* to *input*. That note is a secondary session summary, not direct evidence of every author decision; its alternate acronym expansion is not adopted as an official rename. It nevertheless documents an operational naming strand before the September music discussion.

The September 8, 2026 *Shell Chord Formulas* discussion supplies the musical calibration for this paper. The author's question about dominant seventh becomes a question about the axes being named. He identifies the mismatch between quality and function, then the unequal treatment of structurally parallel combinations, then the usefulness of names that directly support construction. His request for greater verbosity is tied to reconstruction and robustness. This is a documented extension of the earlier distinguishing-descriptor principle beyond eponyms.

The same conversation also contains overstatements that this paper does not adopt. A historically derived word can acquire a legitimate structural sense; users of that sense are not necessarily making a logical error. Also, structural symmetry does not establish equal frequency, perceptual similarity, or equivalent harmonic behavior. Those distinctions matter to a defensible critique.

### 2.3 What must change

The universal promise of syntactic interchangeability is too strong. Substitution can fail in quotations, histories, adjectival constructions, and contested arguments. The new requirement is a documented substitution test for a specified use, not equivalence in every possible sentence.

The v1.2 surname-only working boundary is too narrow for the current investigation. The initial October 22 draft had already distinguished historical, artistic, and cultural references whose naming is itself the content. The present cultural safeguards therefore refine an early distinction; they are not invented from nothing in 2.0. *Dominant seventh*, *simple meter*, and *woodwind* demonstrate problems without surnames. Conversely, a surname may be the most precise locator for a particular historical argument. Deprecation is therefore one intervention among several.

The earlier derivative-subdomain rule also needs correction. It split a domain when its descriptors exceeded available line length. Page width is a presentation property, not an ontological criterion. Its example of heuristic versus deterministic algorithms does not form a clean partition: a heuristic can be deterministic. SDED 2.0 separates conceptual relations from display layout and checks whether purported sibling categories overlap.

The term *Approved Vocabulary* also needs an evidence status. Editorial acceptance is not proof of semantic equivalence, community endorsement, or pedagogical effectiveness. A proposal can be publishable as a proposal while its learning claims remain untested.

## 3. Formal definition and naming architecture

### 3.1 Definition

**SDED 2.0 is an audience-relative protocol for evaluating and maintaining terminology as a knowledge interface. It exposes task-relevant conceptual distinctions in a descriptive layer, preserves independently valuable conventional and historical labels, and requires evidence for both semantic adequacy and claimed user benefits.**

SDED retains its original project name for continuity. The acronym is not silently assigned a new expansion. The new subtitle describes its broader scope.

Represent an entry as:

`E = (identity, concept, domain, audience, task, prerequisites, labels, structure, function, provenance, relations, evidence, status)`.

The **concept** field states the intended sense and its boundaries. **Identity** is a stable identifier whose value does not change merely because a display name changes. **Structure** records relevant properties or construction rules. **Function** belongs to a use or occurrence and may be unknown or disputed. **Labels** are typed: descriptive, conventional, spoken shorthand, symbolic, historical, or community-preferred. **Relations** distinguish equivalence, broader/narrower, part/whole, historical derivation, and association. Shared provenance never by itself proves conceptual subsumption.

The principle is related to existing knowledge-organization practice, not an invention of concept/label separation. SKOS distinguishes concepts, preferred labels, alternative labels, notation, and notes; its preferred-label constraint operates by language. SDED adds an explicit task-relative review of what a name lets a reader infer. Register-specific preferences require an application policy or richer label representation rather than assigning multiple English preferred labels contrary to a chosen SKOS model. [W3C SKOS Primer](https://www.w3.org/TR/skos-primer).

### 3.2 A concrete layered entry

| Layer | Example |
|---|---|
| Stable identity | A registry identifier for the chord quality, independent of the name |
| Canonical structural name in a teaching profile | Major triad with minor seventh above its root |
| Compact descriptive shorthand | Major-minor seventh chord |
| Conventional alias | Dominant seventh chord, quality sense |
| Symbol template | Root name followed by 7; for example C7 |
| Structural specification | Root-relative intervals 1, 3, 5, flat 7 |
| Instance | C-E-G-B-flat |
| Contextual function | Unspecified until a musical context and analysis are supplied |
| Historical relation | Quality associated with the seventh chord on tonal scale degree 5 |

The quality record must not have *dominant function* as an unconditional property. C7 can act as V7 of F; in a C blues it can be a tonic sonority. The same structural name must survive that change. The token **7** alone is not a complete chord identity: it is a suffix whose interpretation requires a root and a notation convention.

### 3.3 A name is not a complete record

The name should expose the smallest useful set of distinctions, not serialize the entire ontology. A record can carry a scope note, formula, demonstration, counterexample, translation, and historical source without forcing every field into speech.

This distinction prevents two opposite errors: calling an opaque name adequate because an external definition exists, and forcing every contextual property into an impossibly long name. The descriptive name must do useful inferential work; the record handles what cannot responsibly fit.

## 4. Evaluation method

### 4.1 Audit a family before proposing replacements

1. Specify the reader and task. Distinguish first exposure, intermediate construction, expert rehearsal, historical research, and catalog retrieval.
2. Identify the concept independently of its label using examples, exclusions, and accepted domain sources.
3. List the family and its relevant dimensions. Test whether it is a product, hierarchy, continuum, contested grouping, or historical association.
4. Parse each current name. Mark which components express structure, function, provenance, metaphor, convention, person, place, or school.
5. State what cannot be inferred and what a reader must look up. Record prerequisites separately from term-specific conventions.
6. Test family consistency and category migration. Change the context while holding the structure fixed; change one structural coordinate while holding the others fixed.
7. Propose retain, supplement, split, or rename interventions. Test their extensional adequacy against nearby concepts and exceptions.
8. Assess history, self-identification, translation, search, and switching costs. Require relevant community participation for community names.
9. Publish the rationale, evidence status, and reversible mapping. Test claimed benefits before representing them as established.

Applied without an eponym detector, steps 3-6 identify the seventh-chord case: the underlying construction has two coordinates while the labels use more than one rule. The same procedure identifies *suspension* as both a time-dependent event and a static chord-symbol category. These are independent calibration targets.

### 4.2 Evaluation profile, not a universal score

Rate each dimension from 0 to 4 for a specified audience and task: 0 means the needed information is absent or misleading; 1 requires substantial term-specific lookup; 2 supports partial inference; 3 supports most relevant distinctions with declared prerequisites; 4 supports reliable reconstruction and discrimination in the tested task. Use **not assessed**, not zero, for missing evidence. Historical and cultural value use separate documentary judgments rather than this inferential scale.

| Dimension | Operational question or measurement |
|---|---|
| Structural transparency | Can readers recover the defining construction or position? |
| Compositionality | Do known components generate the correct family member? |
| Semantic locality | How much task-relevant information is in the name and its declared primitives? |
| Memorization burden | How many term-specific mappings are needed beyond shared prerequisites? |
| Ambiguity and misparse risk | Which wrong interpretations remain plausible? |
| Category consistency | Is structure kept separate from role, history, and evidence type? |
| Symmetry | Do genuinely parallel coordinates receive parallel treatment? |
| Extensibility | Can new members be named without an exception rule? |
| Pedagogical usefulness | Accuracy, transfer, delayed performance, and calibration |
| Expert efficiency | Time, errors, coordination burden, and speech interference |
| Machine parsability | Can a declared grammar recover fields without guessing? |
| Multilingual portability | Are distinctions preserved through independent translations? |
| Backward compatibility | Can legacy searches and documents resolve the intended sense? |
| Historical information value | Does the name identify an argument, lineage, source, or event that matters? |
| Cultural identity value | Who uses and authorizes the designation, and what would replacement erase? |
| Brevity | Characters, syllables, reading time, and utterance time, reported separately |

No weighted total should overrule semantic correctness or cultural authority. A descriptive term that changes the concept fails even if it is easy to read. A high transparency score does not confer authority to rename a community.

For a local comparison one may model expected cost as `J = task errors + lookup cost + reading/speaking cost + transition cost`, with explicit task-specific weights and separately reported cultural and historical constraints. Such weights are a decision aid, not measured facts. Report sensitivity: an expert rehearsal profile may prefer a symbol where an intermediate construction profile prefers the expansion.

### 4.3 Controlled verbosity and recoverability

Longer names can carry distinguishable components, repeated category cues, and explicit reference frames. This creates opportunities to detect an inconsistency: a record called *major triad with minor seventh* paired with 1-flat 3-5-flat 7 visibly disagrees with itself to a reader who knows the primitives. An opaque token alone offers no comparable internal check.

However, this is an analogy to redundancy, not a demonstrated error-correcting code. If the name and formula are generated from the same mistaken rule, their agreement provides no independent assurance. More characters do not automatically carry more useful information. Repeated synonyms can add length without improving discriminability. A full definition may introduce more unfamiliar primitives than it removes.

Let `C` be the intended concept, `N` a name, and `K` the reader's declared prerequisite knowledge. The design objective is to reduce uncertainty about task-relevant features of `C` given `N` and `K`, while controlling communication and maintenance costs. Conditional uncertainty is a useful model; it is not a measurement until concepts, tasks, reader populations, and error distributions have been operationalized.

Graceful degradation means that forgetting one convention does not destroy every route to the concept. A descriptor, legacy alias, formula, and example can provide complementary retrieval routes. Complete recoverability after institutional loss remains an aspiration requiring preserved primitives, formats, and context; prose alone cannot guarantee it.

## 5. Taxonomy of naming failure modes

Failure is relative to a use, not an accusation against a word's existence.

| Failure mode | Diagnostic test | Typical treatment |
|---|---|---|
| Eponym opacity | Removing knowledge of the person removes all discriminating information | Add or prefer a distinguishing descriptor; retain attribution |
| Geographic opacity | A place word supplies no construction rule | Separate location/provenance from structure |
| Historical fossilization | A formerly descriptive association no longer predicts current use | Scope the old sense and document migration |
| Metaphor used as taxonomy | Literal or figurative interpretation predicts false membership | Qualify the sense; retain useful mnemonic |
| Structure/function mixing | Same object changes role, but the type name implies a fixed role | Separate quality/type from contextual function |
| False asymmetry | Parallel coordinates receive unequal grammatical treatment | Name the coordinates consistently |
| Inconsistent composition | A modifier affects different fields in different siblings | Declare grammar; expand hidden fields |
| Hidden defaults | Missing marks silently choose quality, orientation, or reference | Publish the default and offer explicit expansion |
| Overloading | One string denotes concepts with different tests of identity | Split sense records; qualify use |
| Category migration | A historical locator becomes a type, genre, or evaluative term | Keep a dated sense history and typed aliases |
| Arbitrary abbreviation | Expansion still requires a special lookup | Add expansion or descriptor; retain efficient symbol |
| Notation leaking into names | A symbol's abbreviation is treated as a conceptual definition | Preserve notation, change teaching expansion |
| Cultural misclassification | A label collapses distinct practices or asserts an outsider's hierarchy | Replace indexing policy through consultation |
| Externally imposed designation | Named people do not recognize the label or reject its use | Record authority and prefer warranted self-designation |
| Translation artifact | A familiar translated word suggests the wrong technical sense | Retain source term with scoped gloss and translator |
| Misleading antonym or false binary | Proposed alternatives overlap or leave unacknowledged possibilities | Expose dimensions; abandon false partition |
| Redundant synonyms without mappings | Search and instruction fragment across unlinked labels | Link records and specify exact versus approximate equivalence |
| Lost-context pointer | The label requires an unavailable document, institution, or oral convention | Preserve context and add recoverable descriptive fields |
| Noncompositional compression | Several independent variables are packed into one token | Make variables explicit in the descriptive layer |
| False transparency | A plausible descriptive label identifies the wrong or broader concept | Reject the replacement; perform neighbor tests |
| Unstated reference frame | Numbers or directions omit root, tonic, bass, observer, or time | Name the reference frame |
| Layout-induced ontology | Types change because a line or page is full | Separate semantic model from rendering |

The last three are essential additions. Descriptive naming can create defects as well as repair them. A wrong explicit name may be more damaging than an opaque one because it confidently teaches a false construction.

## 6. Intervention taxonomy and rules

| Intervention | Use when | Required output |
|---|---|---|
| Retain | The existing name meets the task or carries indispensable identity | Scope and reason for retention |
| Retain with descriptor | Name and explanation convey different valuable information | Conventional name plus scoped descriptor |
| Alias | Two expressions designate the same sense in the declared scope | Bidirectional mapping and evidence of equivalence |
| Rename | A replacement improves the required distinctions without changing the concept | Old/new mapping, rationale, transition policy |
| Structurally rename | A stable construction can generate family names | Grammar, primitives, and neighbor tests |
| Disambiguate | Several meanings can be separated by qualifiers | Explicit domain or sense qualifiers |
| Split overloaded term | Different concepts need different records | Multiple identifiers; no indiscriminate global redirect |
| Preserve as historical label only | Current use is misleading but historical retrieval is necessary | Historical status, dates, and retrieval handling |
| Preserve symbol, change pedagogical expansion | Compact notation is efficient but its spoken expansion hides structure | Unchanged symbol plus descriptive teaching name |

An intervention must not disguise a substantive conceptual revision as a cosmetic rename. If *Cartesian dualism* is narrowed to one aspect of Descartes's position, the mapping must say so. If a genre descriptor covers more than the genre, it is a broader description, not an exact alias.

The default for a culturally meaningful name is retention with an appropriate descriptor. Determine whether provenance is constitutive, whether the label is a self-designation, who can authorize changes, whether communities disagree, and whether a proposed replacement would erase a lineage. Institutional adoption alone is not community consent. Local Contexts provides a concrete model for carrying community-specific authority and protocols in digital records; SDED does not substitute itself for that authority. [Local Contexts TK Labels](https://localcontexts.org/labels/traditional-knowledge-labels/).

### Attribution and participation

The default SDED display is `Descriptive name ("Historical name", est. YYYY)`. The alternative `Descriptive name ("Historical name"™, est. YYYY)` is acceptable, as is the ASCII marker `(TM)` after the historical name. **The ™ marker is optional, never necessary for participation, acceptance, or conformance.** It is not part of the concept identifier, and its inclusion or omission must not create duplicate entries. Plain quotes and punctuation are sufficient. No special symbol input is required from contributors.

This is a protocol convention, not a blanket assertion of trademark ownership or legal protection. The old universal assurances about parody are not carried forward. Nor is ™ a copyright symbol.

Every published vocabulary entry must contain a researched calendar date, approximate period, or documented range. The date must name an event in the record: publication of the concept, attested use of the term, a construction, or another specified event. These dates often differ. For example, 1963 dates Gettier's paper; it does not prove the later label *Gettier problem* was coined that year. When a source establishes existence by a year but not first use, display a bound such as `est. by 1872`. This is a range with a supported upper endpoint; do not invent a lower endpoint. Blank or unknown dates are not acceptable in the published vocabulary. A date-free proposal can enter the review queue, preserving low-friction participation, while editors complete the historical research before publication.

Retain the original low-friction reference idea: a first-use note can say *Following the SDED descriptor-first naming convention*, with a link to the relevant version. An optional *Learn more about SDED* link or a plain-text source note can explain unfamiliar formatting without interrupting each sentence. Refer to the actual version used; do not present the previous version DOI as the identity of this unpublished draft. Attribution requirements for reused licensed text are distinct from requiring a special marker in every name.

## 7. Music: theory and analysis

### 7.1 Seventh chords as a coordinate system

For the major/minor subset, hold the root and perfect fifth fixed. Vary triad quality and seventh quality independently. The seventh is measured **from the root**, not from the fifth or from the current key's tonic.

| Triad quality | Seventh above root | Root-relative formula | Conventional symbol on C | Descriptive expansion |
|---|---|---|---|---|
| Major | Major | 1-3-5-7 | Cmaj7 | Major triad with major seventh |
| Major | Minor | 1-3-5-flat 7 | C7 | Major triad with minor seventh |
| Minor | Minor | 1-flat 3-5-flat 7 | Cm7 | Minor triad with minor seventh |
| Minor | Major | 1-flat 3-5-7 | Cm(maj7) | Minor triad with major seventh |

This is not new chord theory. *Open Music Theory* explicitly teaches major-major, major-minor, and minor-minor names alongside conventional aliases. The proposed contribution is consistent exposure of both coordinates, explicit typing of naming layers, and testing of the resulting interface. [Hamm, Seventh Chords](https://viva.pressbooks.pub/openmusictheory/chapter/seventh-chords/).

There is also a much older descriptive precedent. Henry Wylde’s 1872 harmony treatise lists seventh chords by their seventh, fifth, and third; its table on pages 105–106 includes the eight constructions used here. SDED therefore extends an existing practice of describing chord structure. The current date ledger uses this as a documented upper bound for the constructions, without assigning every modern alias to 1872. [Wylde, Harmony and the Science of Music](https://books.google.com/books?id=TV_v18DaRzkC).

The conventional family is structurally inconsistent as a construction interface. *Major seventh* and *minor seventh* compress matched qualities; *minor-major seventh* exposes two qualities; *dominant seventh* uses a historically functional association for a reusable quality. A learner cannot infer the whole naming grammar from the siblings alone.

The structural sense of *dominant seventh* is nevertheless established. The defect is not that every contemporary utterance is semantically false. The defect is hidden category migration and an extra mapping in a pedagogical task. Saying “it is a conventional quality name” explains its legitimacy; it does not establish that it is the best teaching interface.

Two tests separate the axes. First, hold C-E-G-B-flat fixed while moving from an F-tonal context to a C-blues context. The construction stays fixed while its function can change. Second, hold dominant function fixed across different realizations: a dominant triad, a seventh chord, a suspension, or a leading-tone harmony can participate in dominant-oriented behavior under a particular analytical model. Function cannot be read off a single four-note set alone.

The 2×2 matrix establishes combinatorial symmetry, not equal musical prevalence. Minor-major seventh chords need not be as frequent or as stable in a repertoire as major-minor seventh chords. A pedagogical vocabulary can expose a symmetric possibility space while teaching its unequal distribution separately.

### 7.2 Extending the grammar without exceptions

| Additional type | Root-relative formula | Proposed structural expansion | Existing aliases/symbols |
|---|---|---|---|
| Diminished triad, minor seventh | 1-flat 3-flat 5-flat 7 | Diminished triad with minor seventh | Half-diminished seventh; m7(flat 5); half-diminished symbol |
| Diminished triad, diminished seventh | 1-flat 3-flat 5-double-flat 7 | Diminished triad with diminished seventh | Fully diminished seventh; dim7 |
| Augmented triad, minor seventh | 1-3-sharp 5-flat 7 | Augmented triad with minor seventh | Augmented seventh; 7(sharp 5) in appropriate notation |
| Augmented triad, major seventh | 1-3-sharp 5-7 | Augmented triad with major seventh | Augmented major seventh; maj7(sharp 5) |

*Half-diminished* is a poor literal construction cue unless its convention is known: it does not mean reduce half the notes, halve an interval, or partially perform an operation. The two-coordinate expansion identifies the actual difference. Conversely, not every arbitrary combination of interval labels is a commonly used chord type. A productive grammar must distinguish well-formed descriptions from claims about repertoire frequency.

An extended-chord grammar must go beyond this two-field schema. C9, Cadd9, Cmaj9, and Cm9 differ in the presence and quality of the seventh, not just an added ninth. A symbol can also permit omitted tones in performance. The full record therefore distinguishes **chord type**, **required/optional extensions**, **actual voicing**, and **omissions**. A structurally explicit pedagogical expansion for C9 is *major triad with minor seventh and major ninth*, with a separate voicing policy. For Cadd9 it is *major triad with added major ninth and no specified seventh*. These are teaching expansions, not a demand to speak every field while performing. [Chord-symbol defaults](https://viva.pressbooks.pub/openmusictheory/chapter/chord-symbols/).

### 7.3 Record-level audit of the calibration example

**Concept:** the tertian quality 1-3-5-flat 7. **Current name says:** a seventh associated with the dominant. **Hidden information:** the triad is major, the seventh minor, both relative to the chord root. **Why it arose:** association with the seventh chord built on scale degree 5 in tonal practice; a precise chronology of lexical generalization still requires historical corpus work. **History's value:** high for tonal analysis, lower for construction without context. **Candidate:** *major triad with minor seventh above its root*. **Loss if renamed universally:** fluent conventional speech and access to a large literature. **Alias treatment:** retain the quality sense as a conventional alias, record the functional sense separately, and preserve symbols.

The following family audits use the same eight fields. Where no defensible origin date has been verified, history is described without inventing one. Each intervention is a proposal unless explicitly identified as an existing term.

### 7.4 Scale degrees, intervals, and reference frames

**Scale-degree names.** Concept: ordered positions relative to a tonic, with characteristic relations in a tonal system. Current names: tonic, supertonic, mediant, subdominant, dominant, submediant, and leading tone/subtonic. Hidden: the numerical positions and the distinction between the two seventh-degree situations. Origin: inherited relational vocabulary; subdominant can be understood through a fifth below tonic, not merely as an inferior dominant. History value: useful for understanding tonal relationships. Descriptor: *tonic-relative degree 1/2/3/4/5/6/7*, supplemented by the actual interval or alteration. Loss: functional associations disappear if numbers replace every term. Alias: retain the traditional terms and specify whether naming a degree, a chord root, or a harmonic function. Do not use *leading tone* for every degree 7 regardless of its interval and behavior.

**Leading tone versus subtonic.** Concept: in a standard tonal account, a seventh degree one semitone below tonic versus a seventh a whole tone below tonic. Name says: directed leading versus below-tonic position; neither is a complete pitch formula. Hidden: distance and context. Origin: tonal orientation. History value: valuable because tendency is musical information. Descriptor: *semitone-below-tonic seventh degree* versus *whole-tone-below-tonic seventh degree*, with tendency analyzed separately. Loss: a purely distance-based term omits behavior. Alias: retain; prevent degree number, interval, and tendency from collapsing into one field.

**Interval size and quality.** Concept: a relation between spelled pitches; generic number counts diatonic positions, quality specifies size within that spelling. Name says: major/minor, perfect, augmented/diminished plus ordinal number. Hidden: inclusive counting and a different quality family for unisons, fourths, fifths, and octaves. Origin: inherited diatonic notation and interval classification, not a modern Cartesian design. History value: voice-leading and spelling distinctions remain important. Descriptor: *spelled fourth, augmented; six semitones in twelve-tone equal temperament*, when that extra precision is needed. Loss: replacing everything with semitone counts collapses augmented fourth and diminished fifth. Alias: preserve interval names; teach a two-field grammar and a separate acoustic measure. [Intervals](https://viva.pressbooks.pub/openmusictheory/chapter/intervals/).

**Inversion versus voicing.** Concept: inversion class depends on the chord member in the bass; spacing and octave distribution are separate. Name says: first, second, third inversion, without naming the bass member. Hidden: third/fifth/seventh in bass, respectively. Origin: root-based chord classification. History value: practical analytical shorthand. Descriptor: *third-in-bass voicing*, *fifth-in-bass voicing*, *seventh-in-bass voicing*. Loss: little conceptual loss, but symbol and literature compatibility matter. Alias: retain inversion labels; do not call every rearranged voicing an inversion change.

**Figured bass.** Concept: intervals above a notated bass, with conventions for omissions and alterations. Name says: figures attached to bass; labels such as 6 or 6/4 are compact. Hidden: omitted intervals and the bass-relative frame. Origin: a practical realization notation, not initially a chord-quality taxonomy. History value: essential for historical performance. Descriptor: *bass-relative interval figures*; in elementary triad interpretation expand 6 as 6/3 while stating the context. Loss: translating into root-relative chord names can erase suspensions and realization choices. Alias: retain the notation and teach its reference frame. [OMT glossary](https://viva.pressbooks.pub/openmusictheorycopy/back-matter/glossary/).

### 7.5 Events, functions, and chromatic constructions

**Suspension versus sus chord.** Concept: a prepared tone sustained across a harmonic change and subsequently resolved is a temporal event; sus4 in chord-symbol practice specifies a fourth replacing the third in a sonority. Name says: suspension in both cases. Hidden: preparation and resolution are not required by the static symbol. Origin: an event term extended into a structural usage. History value: important to both traditions. Descriptor: *prepared held-tone dissonance with stepwise resolution* for the specified event; *third-replaced-by-fourth chord* for the basic structural type. Loss: a universal rewrite would sever established notation and understate jazz voicing variety. Alias: split senses and retain both conventional forms; never infer an actual preceding preparation solely from sus4.

**Passing tone, neighbor tone, appoggiatura, escape tone.** Concept: families of embellishing events distinguished by approach, departure, accent, and relation to stable tones. Name says: mixed metaphors and inherited words. Hidden: the event coordinates. Origin: contrapuntal and pedagogical traditions. History value: useful repertoire-specific conventions. Descriptor: describe an event as *stepwise connection*, *stepwise departure and return*, or *accented leap-in, step-out embellishment* within a declared textbook profile. Loss: a single universal expansion could erase disagreements over appoggiatura classification. Alias: retain scoped aliases; show the approach/departure/accent matrix rather than pretend every textbook agrees. [Embellishing tones](https://viva.pressbooks.pub/openmusictheorycopy/chapter/embellishing-tones-old/).

**Secondary dominant / applied dominant.** Concept: a harmony directed toward a locally tonicized target other than the global tonic. Name says: secondary or applied, without identifying the target. Hidden: target and distinction from modulation. Origin: extended tonal analysis. History value: substantial. Descriptor: *dominant of scale-degree-two harmony*, for V/ii in the appropriate key, with quality and voicing separate. Loss: no need to replace the useful applied-dominant family. Alias: retain; require the target field and do not infer sustained key change from one occurrence.

**Borrowed chord / modal mixture.** Concept: use of pitch material associated with a parallel mode in a tonal context. Name says: a borrowing metaphor or mixing operation. Hidden: source mode and which components differ. Origin: explanatory accounts of chromatic harmony. History value: useful when source association is analytically justified. Descriptor: *parallel-minor flat-sixth-degree major triad* for a specified major-key example. Loss: a pitch-only description may omit the expressive or stylistic association; a borrowing account may itself be disputed. Alias: retain with an analysis-confidence field, not an asserted literal borrowing event.

**Neapolitan sixth.** Concept: in the standard tonal case, a major triad on lowered scale degree 2, commonly in first inversion. Name says: place association plus a bass-interval convention. Hidden: root, quality, and third in bass. Origin: historical geographic association; the label is not proof that every use originated in Naples. History value: literature retrieval, not construction. Descriptor: *lowered-second-degree major triad, third in bass*. Loss: established analytical and historical references. Alias: retain *Neapolitan* and N6; distinguish the triad type from its common inversion and predominant use. A root-position form is not logically excluded by the broader chord concept.

**Italian, French, German augmented-sixth chords.** Concept: a tonal chromatic family containing lowered 6 and raised 4, commonly directed outward toward degree 5. Name says: geographic identities and an interval. Hidden: internal members. Origin: inherited national labels, not reliable national origin certificates. History value: high for historical literature, low for reconstructing the chord. Descriptor: *augmented-sixth sonority with tonic*; *with tonic and degree 2*; *with tonic and lowered degree 3*, respectively, under a major-reference scale-degree convention. Loss: compact distinctions and some historical discourse. Alias: preserve national names but attach explicit degree sets. [Augmented-sixth chords](https://viva.pressbooks.pub/openmusictheorycopy/chapter/augmented-sixth-chords/).

In C, the familiar degree sets yield A-flat-C-F-sharp; A-flat-C-D-F-sharp; and A-flat-C-E-flat-F-sharp. The last is enharmonically equivalent to A-flat-C-E-flat-G-flat in twelve-tone equal temperament, but spelling and expected voice-leading differ. Therefore *major triad with minor seventh* is not a lossless replacement for every German augmented-sixth analysis. This is a decisive limit on purely pitch-class renaming. Common-tone uses further show that a structural family need not have one fixed function. [Common-tone chords](https://viva.pressbooks.pub/openmusictheory/chapter/common-tone-chords/).

**Altered chord / altered dominant.** Concept: a context-dependent set of departures from a specified baseline; in jazz the altered-scale association adds another convention. Name says: changed, but not from what or how. Hidden: alteration set and permitted omissions. Origin: practice-relative modification vocabulary. History value: efficient rehearsal shorthand. Descriptor: record exact altered fifths/ninths and seventh quality, plus any declared scale association. Loss: full expansions can overprescribe voicings that the symbol intentionally leaves open. Alias: retain alt as a constrained performance instruction, not a single fully specified pitch set.

**Cadence families.** Concept: contextually articulated phrase arrivals, not simply any occurrence of two adjacent chords. Names say: authentic, plagal, deceptive, half; these mix evaluative metaphors and inherited categories. Hidden: arrival harmony, bass position, melodic endpoint, and phrase role. Origin: historical theories of closure. History value: essential to analytical literature. Descriptor: *dominant-to-tonic phrase close*; *subdominant-to-tonic phrase close*; *dominant-arrival phrase close*; or a specified diverted arrival. Loss: replacing cadence categories with chord arrows alone erases phrase function. Alias: retain and qualify the analytical tradition. “Perfect” and “imperfect” do not have identical scope across all national teaching systems. [Cadence examples](https://musictheory.pugetsound.edu/mt21c/cadences.html).

### 7.6 Modes, collections, and named scales

For the seven modern diatonic modes, a major-reference interval template makes the family constructible:

| Mode alias | Major-reference degrees | Descriptive teaching label |
|---|---|---|
| Ionian | 1 2 3 4 5 6 7 | Major diatonic mode |
| Dorian | 1 2 flat 3 4 5 6 flat 7 | Diatonic mode with lowered third and seventh |
| Phrygian | 1 flat 2 flat 3 4 5 flat 6 flat 7 | Diatonic mode with lowered second, third, sixth, seventh |
| Lydian | 1 2 3 sharp 4 5 6 7 | Diatonic mode with raised fourth |
| Mixolydian | 1 2 3 4 5 6 flat 7 | Diatonic mode with lowered seventh |
| Aeolian | 1 2 flat 3 4 5 flat 6 flat 7 | Diatonic mode with lowered third, sixth, seventh |
| Locrian | 1 flat 2 flat 3 4 flat 5 flat 6 flat 7 | Diatonic mode with lowered second, third, fifth, sixth, seventh |

Concept: tonic/final-oriented organization of a diatonic collection in this modern usage. Current names: inherited mode labels. Hidden: interval pattern and tonal center. Origin: a complicated transmission of Greek and later modal names; modern meanings must not be projected unchanged onto ancient or medieval systems. History value: substantial, but context-sensitive. Candidate: the templates above, or shorter relative descriptors such as *natural-minor pattern with raised sixth* after declaring that baseline. Loss: universal renaming would confuse historical modes and modern pitch collections. Alias: retain, with domain and period qualifiers. A mode is not adequately taught as “the same notes starting somewhere else” without tonal orientation. [Introduction to diatonic modes](https://viva.pressbooks.pub/openmusictheory/chapter/intro-to-diatonic-modes-and-the-chromatic-scale/).

**Harmonic and melodic minor.** Concept: particular minor-scale forms and usage conventions. Name says: a division between harmony and melody. Hidden: exact alterations and differences between classical direction-dependent teaching and jazz use of melodic minor. Origin: pedagogical accounts of minor-key practice. History value: informative if treated as an account rather than a prohibition. Descriptor: *natural-minor pattern with raised seventh*; *natural-minor pattern with raised sixth and seventh*, plus explicit direction/profile. Loss: a formula alone omits melodic behavior. Alias: retain scoped forms. The names do not imply harmonic minor cannot be melodic or melodic minor cannot underlie harmony.

**Whole-tone, octatonic, bebop, and culturally named scales.** Concept: several different kinds of collection or practice. Name says: interval size, cardinality, style, or cultural association, respectively. Hidden: *octatonic* alone says eight notes, not which eight; *bebop scale* does not choose a unique insertion pattern. Origin: mathematical description and practice labels coexist. History value: variable, high for real traditions. Descriptor: *alternating semitone/whole-tone eight-note collection*, with starting interval specified; for a bebop teaching pattern, specify the base and inserted passing tone. Loss: replacing a raga or maqam with a pitch list would erase behavior and cultural identity. Alias: distinguish a pitch collection from a musical tradition. [Collections](https://viva.pressbooks.pub/openmusictheory/chapter/collections/).

### 7.7 Rhythm, counterpoint, form, and tuning

**Simple/compound and duple/triple meter.** Concept: beat grouping and beat subdivision are different dimensions. Name says: simple/compound can sound like easy/complex; duple/triple counts beats. Hidden: two-part versus three-part primary subdivision. Origin: notational classification. History value: useful conventional vocabulary. Descriptor: *two beats per bar, each divided into three* for ordinary compound duple 6/8. Loss: little at the introductory level, but additive and ambiguous cases exceed this grid. Alias: retain conventional labels and show both axes. 6/8 is not automatically six perceived beats; 3/4 can contain the same number of eighth-note units with a different grouping. [Rhythm and meter curriculum](https://viva.pressbooks.pub/openmusictheory/part/rhythm-and-meter/).

**Polyrhythm, polymeter, hemiola, and syncopation.** Concept: concurrent subdivision ratios, differing metric cycles, particular regroupings, and displaced accents are not identical. Name says: multiple rhythms/meters, an inherited ratio term, or a displacement convention. Hidden: common span, pulse, grouping, and alignment. Origin: theoretical descriptions of rhythmic practice; origin dates not assigned here. History value: useful expert distinctions. Descriptor: *three equal attacks against two over one shared span*, or *three-beat cycle against four-beat cycle*, with unit specified. Loss: ratio labels alone can erase metrical interpretation and performance feel. Alias: retain scoped terms; require timeline examples before declaring equivalence.

**Contrapuntal inversion, retrograde, augmentation, diminution.** Concept: pitch-direction reversal, temporal reversal, and proportional duration change under declared operations. Name says: inversion and augmentation are also used for chord position and interval quality. Hidden: axis, sequence order, or time factor. Origin: contrapuntal transformational vocabulary. History value: useful and already partly compositional. Descriptor: *pitch-direction inversion about [axis]*; *time-order reversal*; *duration doubling*, where doubling is the actual operation. Loss: a numerical label that fixes one factor may be narrower than augmentation. Alias: qualify the operation, not rename the whole tradition. *Real* and *tonal* fugue answers should be taught as literal versus tonally adjusted transposition, not true versus false answers.

**Binary, ternary, rondo, sonata, verse, chorus, bridge.** Concept: some terms describe layout, others formal function, genre history, or repeated lyrical/musical behavior. Name says: two/three, return, genre association, or metaphor, inconsistently. Hidden: criteria for section identity and distinctions between schematic return and formal function. Origin: diverse compositional and analytical traditions. History value: often central. Descriptor: supplement a particular analysis with *two-section form with return within section two* or *recurring refrain alternating with episodes*. Loss: reducing sonata form to ABA misidentifies its tonal and thematic organization. Alias: retain scoped formal types; distinguish a section labeled B from a bridge function.

**Voice leading, parallel motion, contrary motion, contrary versus oblique.** Concept: relations between moving parts, with direction and interval preservation as separate properties. Name says: some motion relations are already informative; *voice* need not mean a singer. Hidden: part identity through changes of register or instrument. Origin: part-writing practice. History value: useful. Descriptor: *part-to-part pitch motion* when teaching instrumental textures; retain *parallel*, *similar*, *contrary*, and *oblique* with definitions. Loss: replacing a well-functioning relational vocabulary adds switching cost. Alias: retention is the default; clarify that similar direction need not preserve interval size.

**Equal temperament, just intonation, Pythagorean tuning, well temperament.** Concept: different tuning constructions and families. Name says: equality, an evaluative-sounding adjective, a person, or a broad positive descriptor. Hidden: equal in which measure, selected ratios, fifth-based construction, and the nonidentity of well and equal temperament. Origin: tuning practice and historical classification. History value: essential for historical sound. Descriptor: *twelve equal logarithmic divisions of the octave* for 12-TET; *specified rational-frequency-ratio tuning* for a particular just system; *fifth-generated tuning* with construction and comma handling specified. Loss: generic descriptions can collapse distinct temperaments; Pythagorean labeling can be historically useful. Alias: retain with ratio or cents data. Twelve equal steps do not mean equal frequency differences, and well temperament is not simply another name for equal temperament.

**Pitch-class, set-class, interval-class vector, and Forte number.** Concept: classifications under explicitly chosen equivalences. Name says: class or vector, but not always the quotient relation; a catalogue number points externally. Hidden: octave equivalence, transposition/inversion equivalence, ordering, and indexing convention. Origin: analytical formalization and cataloguing. History value: high for reproducible literature reference. Descriptor: *pitch-class set modulo transposition and inversion*, where that is the chosen equivalence; accompany a catalogue identifier with representative set and interval data. Loss: a vector alone need not uniquely identify a set class; a pitch-class list omits register and voicing. Alias: retain catalogue identifiers as identifiers, not self-documenting names. [Integer interval notation](https://viva.pressbooks.pub/openmusictheory/chapter/intervals-in-integer-notation/); [interval-class vectors](https://viva.pressbooks.pub/openmusictheory/chapter/interval-class-vectors/).

## 8. Music: practice, performance, notation, culture, and instruments

### 8.1 Practice and performance

**Shell voicing.** Concept: a reduced voicing, commonly root, third, and seventh in the present teaching context. Name says: an outer or essential shell, not its contents. Hidden: which notes are omitted and what distinctions disappear. Origin: practical jazz/guitar pedagogy; a first-use date is not established here. History value: efficient shared shorthand. Descriptor: *root-third-seventh voicing*. Loss: narrowing every use of shell to these three tones ignores other practice. Alias: retain with content specified. Omitting the fifth makes minor-seventh and half-diminished realizations identical in this shell; the full chord quality is then contextual or separately specified. The original conversation's “harmonic ID” claim must therefore be qualified.

**Drop-2 voicing.** Concept: lower the second-highest voice of a specified close-position arrangement by an octave. Name says: drop 2, but does not state second from which end or by how far. Hidden: starting arrangement and ordering. Origin: arranging terminology. History value: compact and productive once its operation is taught. Descriptor: *second-from-top voice lowered one octave from close position*. Loss: long speech is inefficient during rehearsal. Alias: retain drop-2, with source voicing in instructional examples. It is not a general command to lower scale degree 2.

**Guitar positions, shapes, and CAGED.** Concept: fretboard location and movable fingering patterns; shape names do not necessarily name the sounding root. Name says: a position number or open-chord template. Hidden: string tuning, fret offset, root location, and actual pitch. Origin: instrument-specific pedagogy. History value: useful motor chunking. Descriptor: *E-form major-triad fingering, root at fret [n] on string [s]*, with actual chord named separately. Loss: replacing familiar shapes with full coordinates can impede fluent practice. Alias: keep shapes and distinguish motor template, sounding harmony, and neck location. A capo makes that distinction especially important.

**Tremolo and vibrato.** Concept: amplitude modulation, pitch modulation, and rapid note repetition are different operations. Current usage: instrument technique and equipment names distribute the words inconsistently. Hidden: the parameter being changed. Origin: separate performing and product-naming histories. History value: necessary for finding equipment and reading scores. Descriptor: *pitch modulation*, *amplitude modulation*, or *rapid repeated-note tremolo*, as applicable. Loss: renaming product controls would break compatibility and still not capture every technique. Alias: retain equipment names, add parameter descriptors. This is a strong test because the defect is operationally demonstrable, not merely etymological.

**Legato, staccato, rubato, and expressive directions.** Concept: articulation, connection, separation, and temporal shaping, not one universal physical action. Name says: inherited performance instructions, often Italian. Hidden: instrument- and style-specific realization. Origin: performance tradition. History value: shared practical vocabulary and interpretive latitude. Descriptor: *connected articulation*, *detached articulation*, or a specified timing instruction when teaching a particular passage. Loss: numerical overdefinition can destroy legitimate expressive freedom. Alias: retain with demonstrations; an explicit name does not substitute for hearing and doing.

**Orchestration: doubling, divisi, and unison.** Concept: allocation of lines among instruments and players. Name says: doubling can mean more performers on a line, not necessarily an octave; divisi splits an ensemble; unison may require clarity about octave equivalence. Hidden: actual assignment and register. Origin: score and rehearsal economy. History value: high. Descriptor: *section split into [n] parts* or *same line at octave displacement*, when intended. Loss: exhaustive allocation language can overwhelm a score. Alias: retain standard score directions and attach explicit assignment in ambiguous situations.

### 8.2 Notation and pedagogy

**Whole/half/quarter/eighth notes and regional names.** Concept: proportional notated durations, not fixed seconds or unconditional beat counts. Name says: fractions of a whole-note unit; semibreve/minim/crotchet use a different historical vocabulary. Hidden: the reference unit and time-signature interpretation. Origin: notational history. History value: literature and regional communication. Descriptor: *one-quarter of a whole-note duration*, then separately state beats in the current meter. Loss: replacing conventional names would hinder regional literacy. Alias: retain both systems with a ratio table. A whole note need not fill a bar.

**Clefs and solfège.** Concept: a clef anchors a staff position to a pitch; fixed-do and movable-do assign syllables differently. Name says: treble/bass/alto suggest register or voice; do does not announce its reference system. Hidden: exact pitch anchor and syllable policy. Origin: notational and pedagogical traditions. History value: substantial. Descriptor: *G clef on line two*, *F clef on line four*, *C clef on line three*; explicitly label *fixed-pitch do* or *tonic-relative do*. Loss: conventional names are efficient and not inherently defective. Alias: keep them; teach anchor and policy first.

**Accidental, natural, sharp, flat.** Concept: alterations relative to notated pitch spelling and its governing context. Name says: accidental can suggest unintentional; natural can suggest privileged acoustic purity. Hidden: scope within measure and key signature, including cancellations. Origin: notation rather than a moral or natural hierarchy. History value: conventional literacy. Descriptor: *pitch-alteration sign* and explicit alteration/cancellation rule. Loss: universal replacement would disrupt notation teaching. Alias: retain with scope rules; do not equate a natural sign with “white key” as a universal definition.

### 8.3 History, genre, and culture

Names of traditions are often historical coordinates, not compressed acoustic recipes. A structural descriptor can help a listener notice features while being a disastrous replacement for the name of a practice.

**Tango.** Concept: connected music, dance, poetry, and social practices with a Río de la Plata history. Name says: an established tradition, not a complete rhythmic formula. Hidden: regional histories, participation, and stylistic variation. Origin: documented Argentinian and Uruguayan communities and their interactions. History value: constitutive. Descriptor: *Río de la Plata music-dance tradition* is a broad orientation, not an exact synonym. Loss: replacing tango with a meter/tempo recipe erases identity and variation. Alias: retain tango as the preferred cultural designation and add attributes. [UNESCO Tango record](https://ich.unesco.org/en/RL/tango-00258).

**Flamenco and its internal terms.** Concept: traditions of cante, baile, and toque with community transmission, not merely a scale. Name says: a cultural practice; internal terms distinguish roles. Hidden: repertoire, compás, lineage, and embodied knowledge. Origin: rooted in Andalusia and other regions, with an essential Gitano/Roma contribution. History value: constitutive. Descriptor: add local descriptions of song, dance, guitar practice, and a particular palo's features. Loss: replacing the name by “Phrygian music” would be a severe false reduction. Alias: retain self-designations and consult practitioners about descriptors. [UNESCO flamenco documentation](https://ich.unesco.org/doc/src/17331-EN.pdf).

**Classical, Romantic, modern, contemporary.** Concept: repertoire umbrellas, historical periods, aesthetics, and temporal relations. Name says: exemplary, emotional, recent, or present, which can mislead outside its register. Hidden: dates, geography, and historiographic convention. Origin: inherited periodization and later classifications; no universal date boundaries are asserted here. History value: essential to historiography. Descriptor: *European art music of [specified period]* where appropriate, not as a replacement for every use of classical. Loss: reducing a period to dates loses debates about style and institutions. Alias: split senses and retain period labels with explicit region and criteria.

**Genres, subgenres, movements, and scenes.** Concept: overlapping clusters of sound, lineage, institutions, markets, and self-identification. Name says: jazz, bebop, indie, ambient, minimalism, a city scene, or a historical school may encode different axes. Hidden: membership criteria and changes over time. Origin: mixed self-designation, criticism, marketing, and later scholarship; each case requires its own evidence. History value: often high. Descriptor: add separate attributes for sound, production, circulation, scene, and period. Loss: *independent distribution* is not coextensive with every stylistic use of *indie*. Alias: do not collapse exact names into generic descriptions; qualify independent production versus indie style.

**World music / ethnic music / primitive music.** Concept: historically used umbrella classifications whose boundaries depend on the classifier. Name says: an apparent global or group category, sometimes an explicit hierarchy. Hidden: whose music forms the unmarked default. Origin: institutional and commercial classification, with different histories for these distinct expressions; this paper does not assign one origin to all three. History value: useful as evidence of classificatory practice, not necessarily as a current descriptive category. Descriptor: name actual traditions, communities, places, and practices when known. Loss: legacy catalogue retrieval must remain possible. Alias: historical indexing with contextual notes; no new universal substitute that merely renames the same residual bucket.

**Production: comping, sampling, sidechain, and live.** Concept: accompaniment versus assembling a performance from takes; reuse of recorded sound; a control-signal route; and several senses of real-time performance. Name says: some terms encode an operation, others require a studio convention. Hidden: source/target, editing history, and whether live means recording conditions or audience presence. Origin: studio and performance practice. History value: useful shorthand. Descriptor: *take-composite editing*, *harmonic accompaniment*, *gain controlled by [source]*, or *performed in real time before an audience*, as applicable. Loss: exhaustive process descriptions can be cumbersome and may reveal facts not known. Alias: split overloaded uses and leave unknown fields unknown. A sidechain is not necessarily compression; its effect depends on the processor.

### 8.4 Instrument terminology

**Woodwind, brass, percussion, strings.** Concept: conventional orchestral families whose classification bases differ. Name says: material, material, excitation action, and vibrating element. Hidden: membership is not consistently determined by literal construction material. Origin: instrument and orchestral history. History value: highly useful for score organization and player communities. Descriptor: maintain independent fields for vibrating element, excitation mechanism, resonator, material, and ensemble family. A saxophone can then be metal-bodied, single-reed, and conventionally woodwind without contradiction. Loss: replacing orchestral families would disrupt practical organization. Alias: retain family names; do not treat them as a single material taxonomy.

**Hornbostel-Sachs classification.** Concept: a classification based substantially on sound production, with detailed subtypes and later extensions. Name says: authors' names; numerical codes require a key. Hidden: classification criteria and revision. Origin: a named scholarly system. History value: identifies a particular classification, not just any sound-production taxonomy. Descriptor: *sound-production instrument classification, [specified edition]* as orientation. Loss: replacing the historical label alone obscures which system is used. Alias: retain the system name and code version; expose criteria alongside codes. An eponym can be the precise name of an intellectual artifact even when its contents are descriptively organized.

These audits support selective intervention. Seventh-chord construction and meter benefit from explicit coordinates. Performance instructions often need examples more than renaming. Genre and scene labels frequently need richer metadata while remaining canonical cultural names. A single global renaming policy cannot serve all five music domains.

## 9. Philosophy: descriptions must not decide the argument

Philosophy presents a harder test than a small chord-construction matrix. A label may identify a particular text, an argument schema, a disputed interpretation, a family of positions, or a recurring problem. Those are different objects. A descriptor that makes one interpretation look inevitable is worse than an opaque but stable reference. The eight-field audits below therefore distinguish an orienting gloss from an exact replacement. They are proposed editorial treatments, not reports of community adoption.

### 9.1 Arguments, problems, and thought experiments

**Gettier problem.** Concept: the challenge to justified true belief as a sufficient analysis of knowledge, illustrated by cases in which justification and truth coincide without knowledge. Name says: a personal association and a problem type. Hidden: the target analysis and the role of epistemic luck. Origin: Gettier's 1963 article. History value: high for the specific intervention and subsequent debate. Descriptor: *justified-true-belief insufficiency problem*, with *Gettier problem* retained. Loss: the descriptor does not distinguish every later version or competing account of what fails. Alias: retain; individual examples require separate records. *Accidentally true belief* alone is an inadequate replacement because it omits justification and does not delimit the problem. [Gettier, “Is Justified True Belief Knowledge?”](https://academic.oup.com/analysis/article-abstract/23/6/121/109949).

**Hume's guillotine / is–ought problem.** Concept: a problem about the relation between descriptive premises and normative conclusions; formulations differ over logical entailment, justification, and interpretation. Name says: an eponym plus a cutting metaphor, or a contrast between two verbs. Hidden: which inferential restriction is asserted and what counts as a normative premise. Origin: a passage in Hume's *Treatise*, with the guillotine metaphor functioning as a later label; no first-use date for that label is asserted here. History value: needed to distinguish Hume's text from later reconstructions. Descriptor: *descriptive-to-normative inference problem*, followed by the exact claim under discussion. Loss: a categorical “facts never matter to values” paraphrase would distort the issue. Alias: retain both conventional labels, scope them, and do not merge this problem with every use of *naturalistic fallacy*. [Scholarly account of Hume's moral philosophy](https://plato.stanford.edu/entries/hume-moral/).

**Occam's razor.** Concept: a family of methodological preferences for economy, with disagreements about what to minimize and when. Name says: personal association and a trimming metaphor. Hidden: whether economy concerns entities, kinds, assumptions, or another measure, and what is held equal. Origin: a historical association with William of Ockham, not a claim that every modern simplicity criterion originated with him. History value: useful historical pointer. Descriptor: *parsimony preference under specified adequacy constraints*. Loss: this is too broad to replace a particular historical formulation; “simplest explanation is true” would introduce a false guarantee. Alias: retain with an explicit simplicity metric and defeasibility clause. [Simplicity](https://plato.stanford.edu/archives/spr2026/entries/simplicity/).

**Ship of Theseus.** Concept: problems of persistence and identity across replacement, sharpened by variants involving reassembly of removed parts. Name says: an artifact and a narrative association. Hidden: the rival continuities and the precise variant. Origin: an inherited philosophical story with subsequent elaborations. History value: high because the narrative supports shared comparison. Descriptor: *artifact identity under gradual replacement and possible reassembly*. Loss: the memorable narrative and variant history; the descriptor still needs a scenario. Alias: retain as the preferred scenario label and add the problem descriptor. This is a case where the historical name can outperform its replacement in discussion. [Identity over time](https://plato.stanford.edu/entries/identity-time/).

**Chinese room.** Concept: Searle's argument using a symbol-manipulation scenario to challenge a claim about computation and understanding. Name says: a language and a room; it does not state the inferential target. Hidden: the program, the operator/system distinction, and the move from the scenario to the conclusion. Origin: Searle's 1980 paper. History value: essential for tracing the argument and replies. Descriptor: *symbol-manipulation and understanding thought experiment*. Loss: neither “syntax cannot produce semantics” nor “computers cannot think” neutrally names the argument; each risks embedding a conclusion or overgeneralization. Alias: retain the conventional title with a neutral descriptor and links to the systems and other replies. The language in the example is not evidence of anything distinctive about Chinese cognition. [Searle, “Minds, Brains, and Programs”](https://zoo.cs.yale.edu/classes/cs458/materials/minds-brains-and-programs.pdf).

These cases expose a type distinction absent from universal replacement rules: a historical name can refer exactly to an intellectual artifact while a descriptive expression refers only to its subject. An argument about understanding is not necessarily Searle's argument; an identity puzzle is not necessarily the Ship of Theseus. A glossary must mark the relation as *orientation*, *broader topic*, or *exact alias*, rather than silently equating them.

### 9.2 Positions, schools, and conceptual coordinates

**Cartesian dualism.** Concept: a historically specific account of mind and body, often discussed through substance dualism. Name says: association with Descartes plus two-ness. Hidden: what the two kinds are, the ontology, and the account of interaction. Origin: Descartes's work and its reception. History value: high. Descriptor: *Descartes's mind–body substance dualism* for the historical position; *mind–body substance dualism* for the wider type. Loss: substituting the wider type for the historical view erases commitments and distinctions. Alias: preserve the eponym for the historical record; distinguish substance, property, and causal claims as separate fields. [Dualism](https://plato.stanford.edu/entries/dualism/).

**Platonic realism / platonism.** Concept: context-dependent views about Forms or abstract objects, with modern usage not identical to Plato's philosophy. Name says: historical association and an overloaded realism label. Hidden: which objects exist, how they exist, and the historical register. Origin: Plato-related philosophical traditions and later extensions. History value: essential in historical scholarship, less construction-bearing in a modern ontology exercise. Descriptor: *realism about abstract objects* for the relevant modern sense; name a specific account of Forms for a specific historical sense. Loss: treating those as interchangeable misrepresents both. Alias: split senses, retain historical naming, and reject *Forms* as a universal replacement for every form of idealism or platonism. [Platonism in metaphysics](https://plato.stanford.edu/entries/platonism/index.html).

**Idealism, realism, materialism, and naturalism.** Concept: families of commitments whose subjects and contrasts vary by debate. Name says: ideas, reality, matter, or nature; the common-language associations are inadequate definitions. Hidden: realism *about what*, dependence *on what*, and the relevant exclusion. Origin: multiple traditions and usages rather than a single symmetric classification. History value: very high for schools and texts. Descriptor: *mind-independence of [specified domain]*, *mental dependence of [specified domain]*, or an explicitly stated naturalist commitment where accurate. Loss: imposing one binary scheme erases positions that cross these dimensions. Alias: retain qualified terms; no bare *realism* concept ID spanning ethics, mathematics, perception, and international relations.

**Stoicism; analytic and continental philosophy.** Concept: a historical school in the first case and broad, contested intellectual classifications in the latter pair. Name says: a school label, or apparent method/geography. Hidden: doctrines, institutions, periods, and internal differences. Origin: historical affiliation and later historiography. History value: constitutive. Descriptor: *the Stoic school, [period/text]*; for the latter pair, state the particular method, author network, or period actually meant. Loss: “emotion suppression” is not a replacement for Stoic ethics, and “logical versus European philosophy” is an indefensible binary. Alias: retain school labels and separate ordinary-language *stoic* from doctrinal uses. A school name should not be judged by whether it generates its entire philosophy from its syllables.

### 9.3 Logic and epistemology: preserve distinctions hidden by familiar words

**Valid / sound.** Concept: in standard deductive usage, validity concerns preservation of truth from premises to conclusion; soundness of an argument adds true premises. Name says: ordinary approval words. Hidden: the technical criteria, including the fact that validity does not assert actual premise truth. Origin: technical logical usage, not dated here. History value: efficient disciplinary convention. Descriptor: *deductively truth-preserving argument* and *valid argument with true premises*. Loss: replacing all occurrences would be cumbersome and would not cover the distinct metatheoretic use of *soundness* without qualification. Alias: retain; type the record as argument validity, argument soundness, or soundness of a proof system. Do not let ordinary approval senses leak into evaluation.

**Necessary / sufficient conditions.** Concept: directional relations; if A is sufficient for B, A implies B; if A is necessary for B, B implies A. Name says: requirement versus enoughness, but language can obscure direction. Hidden: argument order and scope. Origin: logical vocabulary. History value: useful and substantially meaningful. Descriptor: pair the phrase with *A implies B* or *B implies A* and, where appropriate, a counterexample. Loss: renaming adds little if the real failure is reversed arguments. Alias: retain; use directional notation as an additional layer. This is an example of fixing an interface without replacing the term.

**Analytic/synthetic, a priori/a posteriori, necessary/contingent.** Concept: distinctions about meaning or truth conditions, epistemic warrant, and modality, respectively, with disputed analyses. Name says: inherited technical contrasts that do not by themselves expose these axes. Hidden: the criterion for each distinction and whether proposed correlations are theses rather than definitions. Origin: philosophical traditions and subsequent debates. History value: central. Descriptor: annotate *semantic status*, *epistemic basis*, and *modal status*, then state the author's criterion. Loss: replacing these with one “reason versus experience” binary makes claims of equivalence that require argument. Alias: retain; use a matrix that allows contested cells and rejects an automatic diagonal. This is analogous to separating chord quality from harmonic function, but the philosophical axes are more theory-dependent.

**Knowledge by acquaintance / knowledge by description; knowing-how / knowing-that.** Concept: distinctions concerning relations to objects or modes and contents of knowing, under particular accounts. Name says: more than an eponym does, but ordinary-language components do not settle the theory. Hidden: the relevant philosophical definition and contested reductions. Origin: established philosophical debates. History value: needed to locate arguments. Descriptor: provide an account-specific scope note and examples rather than minting a supposedly neutral replacement. Loss: *skill versus facts* can prejudge whether practical knowledge is propositional. Alias: retain, with explicit account and argument links. Transparency does not remove theoretical disagreement.

### 9.4 Ethics, aesthetics, politics, and philosophy of science

**Consequentialism / deontology / virtue ethics.** Concept: broad families of ethical approaches, not a clean partition generated by one agreed criterion. Name says: consequences, duties, or virtues with uneven etymological accessibility. Hidden: criterion of rightness, deliberative procedure, account of value, and agent evaluation. Origin: philosophical traditions and classificatory practices. History value: strong. Descriptor: separate those dimensions and state the specific view, such as *rightness determined by consequences under [specified account]*. Loss: “results/rules/character” is a useful first orientation but not an exhaustive taxonomy, and hybrid views undermine a forced three-way exclusive classification. Alias: retain family labels plus qualified descriptors.

**Intentional fallacy / affective fallacy.** Concept: particular critical arguments about the role of authorial intention or audience response in literary evaluation and interpretation. Name says: an error associated with intention or affect. Hidden: the argument's scope, target, and contested premises. Origin: named twentieth-century critical interventions; the present audit does not establish a first-use date. History value: high. Descriptor: *critique of using authorial intention as [specified interpretive criterion]* or its response-based counterpart. Loss: “authorial intention is irrelevant” turns a critical label into an unqualified rule. Alias: retain as titles of positions or arguments, not automatic diagnoses of another reader's mistake.

**Negative / positive liberty.** Concept: distinctions often organized around absence of interference and forms of self-direction, with substantial disagreement. Name says: a minus/plus pair that can falsely suggest bad/good. Hidden: whose liberty, from what constraints, to do or be what. Origin: a philosophical and political history rather than mathematical sign. History value: substantial. Descriptor: *liberty as absence of [specified interference]* and *liberty as [specified self-direction]* for the relevant account. Loss: these descriptors do not settle whether every use belongs to the same two categories. Alias: retain and expose the account; avoid presenting the pair as a value ranking. [Positive and negative liberty](https://plato.stanford.edu/entries/liberty-positive-negative/).

**Falsifiability, paradigm, and scientific law.** Concept: a proposed criterion concerning possible refutation; a term with multiple uses in Kuhn-related philosophy and everyday speech; and statements whose status differs across sciences and philosophies. Name says: potential falsity, a model/pattern, or apparent legal command. Hidden: criterion, level of analysis, and modality. Origin: distinct histories, which must not be collapsed into one theory of science. History value: high for named authors' accounts. Descriptor: *testable exposure to potential counterevidence under [criterion]*; *disciplinary exemplar/framework in [account]*; or *law statement under [theory]*. Loss: “proved false,” “any worldview,” and “exceptionless command” are misleading expansions. Alias: split registers and retain author-specific labels when they identify a particular proposal.

### 9.5 Translation is not a universal decoding function

Translation can reveal structure, but it can also conceal a choice of interpretation. The appropriate record stores source language, script, transliteration policy, passage or tradition, candidate renderings, and the reason for the chosen gloss. A bilingual reviewer should assess both directions; an English phrase does not become culturally neutral by being longer.

**Greek: logos and eudaimonia.** Concept: terms with philosophical uses that depend on author and passage, rather than one English concept each. Name says: an untranslated token to an English reader. Hidden: the relevant range and theoretical role. Origin: Greek language and philosophical reuse. History value: indispensable for textual comparison. Descriptor: give a passage-specific gloss, such as *account/reason* or *human flourishing* only where appropriate. Loss: declaring these the single translations suppresses semantic range; “happiness” can also import modern assumptions. Alias: preserve the source term and document translation choices. These are illustrative glosses, not new canonical replacements.

**Latin: a priori and a posteriori.** Concept: epistemic distinctions in a specified philosophical account. Name says: little to readers without Latin or technical training. Hidden: that epistemic priority is not simply chronological “before learning.” Origin: inherited Latin philosophical vocabulary. History value: intertextual continuity. Descriptor: *justification independent of experience* and *justification dependent on experience* where that account uses these criteria. Loss: the simple expansion can hide qualifications about concept acquisition and justification. Alias: retain, link to the account, and distinguish the epistemic sense from ordinary *prior*.

**German: Dasein.** Concept: in Heidegger's use, a philosophically developed term whose role cannot be recovered by a literal spatial gloss. Name says: a German expression familiar in ordinary language but specialized in the text. Hidden: the philosophical account and its relation to ordinary usage. Origin: Heidegger's appropriation of an existing word. History value: high. Descriptor: a text-specific explanatory scope note, not “there-being” as a complete definition. Loss: literal translation creates false transparency. Alias: retain the source term and distinguish ordinary German from the technical use. [Heidegger](https://plato.stanford.edu/entries/heidegger/).

**French: différance.** Concept: a term whose written distinction and associated philosophical operations matter to its use. Name says: a deliberate spelling difference that may disappear in speech or normalization. Hidden: the text's distinctions and argument. Origin: Derrida's philosophical writing. History value: constitutive. Descriptor: a scoped explanation of the relevant operation, preserving the written form. Loss: replacing it with ordinary *difference* erases part of the object being discussed. Alias: retain spelling; store searchable variants without declaring them equivalent concepts. [Derrida](https://plato.stanford.edu/entries/derrida/).

**Sanskrit: śūnyatā and svabhāva.** Concept: emptiness and the kind of intrinsic nature or existence under criticism in a specified Buddhist account; traditions and interpretations matter. Name says: source-language terms whose familiar English glosses can mislead. Hidden: the relation between the two and the philosophical scope. Origin: Buddhist philosophical traditions. History value: very high. Descriptor: a qualified explanation such as *emptiness of intrinsic nature in [account]*. Loss: “nothing exists” is not a neutral translation, and one English account cannot replace a family of textual uses. Alias: retain source terms and competing documented renderings. [Nāgārjuna](https://plato.stanford.edu/entries/nagarjuna/).

**Chinese: wuwei.** Concept: an action-related concept interpreted within particular Chinese texts and traditions. Name says: a transliteration; “non-action” can suggest mere inactivity. Hidden: the text's account of agency, effort, and appropriate action. Origin: Chinese philosophical traditions, not assigned a single establishment date here. History value: high. Descriptor: a passage-specific explanation of action and non-forcing where warranted. Loss: treating *effortless action* as an exact universal translation imposes a reading. Alias: retain the source term; this candidate requires a language specialist's review before registry approval. [Laozi](https://plato.stanford.edu/archives/sum2021/entries/laozi/).

**Arabic: wujūd.** Concept: existence-related vocabulary whose philosophical senses depend on account and context. Name says: an untranslated term; “existence” gives an orientation. Hidden: distinctions involving essence, being, and the use in a particular text. Origin: Arabic philosophical language and its development. History value: necessary for comparative work. Descriptor: provide *existence in [author/passage]* plus the operative distinction. Loss: unqualified equivalence can flatten the source's conceptual organization. Alias: retain and version translation notes. [Essence and existence in Arabic and Islamic philosophy](https://plato.stanford.edu/entries/arabic-islamic-essence/).

The test is not whether an English beginner understands everything immediately. It is whether the interface exposes the remaining dependency honestly. In these cases, a visible scope note saying “interpretation depends on this text” is better engineering than a fluent replacement that hides the dependency.

## 10. Arts and humanities: a survey organized by failure mode

The following selection covers the requested fields without claiming a validated cross-disciplinary vocabulary. Each audit is a candidate for specialist review. Historical origin is stated only at the level supported here; no unknown first-use date is filled by inference. The aim is to show how the same diagnostic distinguishes very different interventions.

### 10.1 Literal appearance mistaken for classification

**Visual art — negative space.** Concept: areas around and between depicted forms as organized within a composition. Name says: “negative,” which can suggest absence or inferior value. Hidden: that these areas actively shape perception and composition. Origin: established art and design teaching vocabulary; first use not established here. History value: useful shared practice. Descriptor: *space around and between focal forms* as an instructional gloss. Loss: the gloss does not capture every figure–ground reversal or compositional use. Alias: retain with examples; do not rename merely because the adjective has other senses.

**Architecture and art history — Gothic.** Concept: historical classifications of architecture and art, with regional and period variation. Name says: a geographic/ethnic association that does not describe the construction system. Hidden: chronology, historiography, and formal criteria. Origin: a later historically evaluative label, not a claim of construction by ancient Goths. History value: indispensable to reception history. Descriptor: attach *pointed arches*, *rib vaulting*, or other warranted attributes to a particular building; none is a universal exact substitute. Loss: *pointed-arch architecture* changes the extension and erases historiography. Alias: retain the period/style label with qualified attributes. [Gothic architecture introduction](https://smarthistory.org/gothic-architecture-an-introduction/).

**Literature — free verse.** Concept: verse without a regular metrical pattern in the relevant usage, still capable of organized rhythm and other formal constraints. Name says: freedom, potentially suggesting absence of form. Hidden: which constraints are relaxed and which remain. Origin: poetic practice and critical terminology. History value: substantial. Descriptor: *verse without regular meter*, qualified for the poem and critical account. Loss: replacing every occurrence obscures historical movements and individual formal practices. Alias: retain with a contrast to *formless*. [Poetry Foundation glossary](https://www.poetryfoundation.org/education/glossary/free-verse).

**Design — intuitive interface.** Concept: an evaluation claim that users can act successfully with little instruction, relative to a population and task. Name says: an apparent intrinsic property. Hidden: prior conventions, accessibility requirements, and actual evidence. Origin: common evaluative design language, not a single doctrine. History value: little for a test report, more in historical rhetoric. Descriptor: *[population] completed [task] under [instruction condition]* with observed results. Loss: a longer description is unsuitable as a casual adjective but essential as evidence. Alias: keep the everyday term only as a gloss; no registry rating of “intuitive” without a defined measure.

### 10.2 One label hides multiple independent dimensions

**Linguistics — voiced/unvoiced versus aspirated/unaspirated stops.** Concept: laryngeal and timing distinctions in particular languages and analyses. Name says: separate dimensions, although a classroom binary can hide timing variation. Hidden: language-specific realization and phonological versus phonetic classification. Origin: technical linguistic analysis. History value: established and useful. Descriptor: distinguish phonological category from measured voice-onset timing and other relevant cues. Loss: renaming all categories by a single timing number confuses realization with contrast. Alias: retain linguistic labels with language and analysis scope; require phonetics review for numerical thresholds. The engineering repair is an explicit type distinction.

**Film — documentary / fiction.** Concept: broad production, presentation, and reception categories with hybrid cases. Name says: an apparent fact/invention opposition. Hidden: staging, reconstruction, editing, truth claims, and institutional conventions. Origin: film practice and classification. History value: high. Descriptor: independently state *staged/reconstructed footage*, *documentary truth claim*, and other supported attributes. Loss: a replacement binary such as “real/unreal film” is worse. Alias: retain genre categories with provenance and method fields; do not infer truth from genre alone.

**Archaeology — Bronze Age.** Concept: a periodizing classification used in regionally specific chronologies. Name says: a material plus a temporal category. Hidden: regional dates, criteria, coexistence of materials, and limits of the periodization. Origin: archaeological classification. History value: central. Descriptor: *[regional chronology], [date range], Bronze Age under [scheme]*. Loss: a universal date or “all tools made of bronze” misrepresents the category. Alias: retain with region and chronology; never store an unqualified global date interval as its definition.

**Anthropology — kinship terms such as cousin.** Concept: culturally and linguistically organized relationships and categories, not merely one universal genealogical distance. Name says: an English relational category. Hidden: which distinctions the language marks, social versus genealogical relations, and local usage. Origin: community language and comparative classification. History value: constitutive. Descriptor: add a genealogical path when relevant and known, while retaining the local social category. Loss: treating that path as the whole meaning erases social relations. Alias: cross-language mappings must distinguish approximate correspondence from exact synonymy.

### 10.3 Overloading, notation leakage, and inconsistent families

**Rhetoric — anaphora versus anaphora in linguistics.** Concept: repetition at the beginnings of successive units in one rhetorical usage, versus a relation of linguistic reference in another field. Name says: one inherited technical word. Hidden: the domain and the different criteria. Origin: technical reuse of inherited vocabulary; no single first-use claim is made. History value: strong in both fields. Descriptor: *successive-unit initial repetition* versus *anaphoric reference*, with further scope as needed. Loss: a global replacement or global alias collapses different concepts. Alias: retain in separately identified records; pair rhetorical anaphora with *epistrophe / successive-unit final repetition* to expose the family axis.

**Theatre — monologue / soliloquy.** Concept: extended speech by one speaker and a more specific dramatic convention of voicing thought, with definitions sensitive to dramatic context. Name says: “one speaker” more directly in the first term, while the second requires technical convention. Hidden: address, audience within the fiction, and performance convention. Origin: theatrical and critical vocabulary. History value: valuable. Descriptor: specify *single-speaker speech* and separately *thought voiced under [dramatic convention]*. Loss: “speech delivered alone” is not a safe universal equivalence, and the terms are not exhaustive antonyms. Alias: retain and model speech configuration separately from dramatic function. [Soliloquy glossary](https://www.poetryfoundation.org/education/glossary/soliloquy).

**Media studies — medium / platform / channel.** Concept: different possible units of technical support, distribution, organization, or communication. Name says: spatial/material metaphors that do not define a shared ontology. Hidden: whether a claim concerns infrastructure, interface, company, audience, or format. Origin: heterogeneous technical and theoretical traditions. History value: useful within an identified account. Descriptor: state *distribution service*, *communication path*, *representational format*, or the actual analytical unit. Loss: one universal taxonomy can erase a theorist's deliberate usage. Alias: disambiguate within the work; do not map all three to one database field.

### 10.4 Historical reference and contested interpretation

**Literary criticism — New Criticism.** Concept: a historically situated critical formation rather than every newly published act of criticism. Name says: temporal novelty. Hidden: period, participants, texts, and practices. Origin: a historical critical label. History value: constitutive. Descriptor: *New Criticism, [specified historical context]* plus relevant methodological attributes. Loss: *close reading* alone is broader and not an exact replacement. Alias: retain; treat “new” as part of a historical proper label, not a moving date filter.

**Classics — classical.** Concept: a disciplinary or evaluative designation whose extension depends on context. Name says: exemplary status or a historical register. Hidden: the region, languages, periods, and institutional boundaries assumed. Origin: inherited scholarly and evaluative usage. History value: essential to the history of the discipline. Descriptor: *ancient Greek and Roman [specified subject]* when that is the intended scope, or the actual broader scope where it is not. Loss: globally equating *classical* with that descriptor reproduces one unmarked cultural default. Alias: split disciplinary, period, and evaluative senses.

**Historiography — Dark Ages.** Concept: a historically variable label sometimes referring to limited surviving evidence and sometimes carrying a broad evaluative judgment. Name says: darkness as an apparent property of a period. Hidden: region, dates, evidence base, and whose evaluation. Origin: historical periodization and reception. History value: useful when studying the label's own history. Descriptor: give the actual period and region; if evidence scarcity is intended, identify the specific corpus. Loss: historical quotations must remain retrievable and intelligible. Alias: preserve as a contextualized historical label when inappropriate for the present classification, not as a blanket synonym for a uniformly deficient era.

### 10.5 Community identity cannot be replaced by an analyst's recipe

**Dance — ballet position names and culturally situated dance names.** Concept: codified positions or actions within a practice, versus the identity of a whole tradition. Name says: some French terms encode an action for French speakers, while a tradition name identifies a history. Hidden: embodiment, training system, and stylistic norms. Origin: practice-specific transmission. History value: high. Descriptor: pair a position name with anatomical orientation, demonstration, and school-specific qualification; pair a tradition with community-approved context. Loss: “bent” alone is not an adequate performance instruction for plié, and a movement recipe cannot replace a tradition. Alias: retain; distinguish the technique record from the cultural identity record.

**Religious studies — pagan / indigenous religion / world religion.** Concept: historically and institutionally situated classifications, with differing self-identifications and external uses. Name says: apparent classes whose boundaries can hide a classifier's standpoint. Hidden: who applies the term, whether a community accepts it, and which comparison is intended. Origin: distinct religious, scholarly, and political histories; these terms are not interchangeable. History value: high as historical evidence and sometimes as present self-designation. Descriptor: identify a particular tradition and use, with community terminology where appropriate. Loss: indiscriminate removal can erase a reclaimed self-designation just as indiscriminate use can impose an unwanted label. Alias: record speaker/community, period, and status rather than apply one global ban or preferred name.

**Cultural studies — high / low / popular culture.** Concept: classificatory practices involving prestige, institutions, circulation, and audience, often themselves objects of critique. Name says: vertical value and apparent popularity. Hidden: the authority, metric, and historical setting. Origin: social and critical classifications. History value: necessary for analyzing power and reception. Descriptor: expose *institutional prestige*, *circulation*, or *audience practice* as separate, evidenced claims. Loss: silently replacing terms in a historical argument can remove the hierarchy that the argument examines. Alias: retain as attributed analytical or historical vocabulary; avoid turning it into an unqualified universal ranking.

Across this survey, the same failure mode does not mandate the same intervention. Literal opacity in a construction instruction can justify a structural name. Literal opacity in a community name can justify a descriptor alongside the name. Opacity in a historical title can be the price of exact reference. The registry must record which of these jobs the expression is doing.

## 11. What scholarship supports—and what it does not

This is a targeted interdisciplinary review, not a systematic review or meta-analysis. Sources were selected to challenge the design argument as well as support it. Searches covered terminology and controlled vocabularies, knowledge representation, HCI naming, semantic transparency, memory, expertise, and relevant domain teaching and scholarship. No study retrieved here directly tests the full proposed SDED architecture across arts and humanities disciplines. No participant experiment was conducted for this paper.

**Terminology and knowledge representation.** ISO 704:2022 establishes terminology work as a standards subject; only its publicly accessible description was consulted, so this paper does not claim clause-level compliance. W3C SKOS supplies an established separation of concepts, preferred and alternative labels, notation, and documentation. It supports the feasibility of the architecture, not a finding that descriptive labels teach better. Getty's vocabulary guidance demonstrates the importance of warranted terms, scope, multilingual choices, and editorial governance. SDED should interoperate with such work rather than describe itself as the invention of concept–label separation. [ISO 704:2022](https://www.iso.org/standard/79077.html); [SKOS Primer](https://www.w3.org/TR/skos-primer/); [Getty AAT editorial rules](https://www.getty.edu/publications/vocabularies-editorial-guidelines/aat-guidelines/3_editorial_rules/3.3/).

**Controlled natural languages.** Kuhn's survey treats precision, expressiveness, naturalness, and simplicity as dimensions along which designed languages differ. That is relevant to SDED's refusal to maximize one score. It does not establish that English technical names can be made universally unambiguous or that more words always help. [Kuhn (2014), “A Survey and Classification of Controlled Natural Languages”](https://aclanthology.org/J14-1005/).

**HCI and lexicography.** Furnas and colleagues' vocabulary-problem research is a direct warning against expecting one chosen word to match every user's spontaneous expression. Alternative access terms therefore matter even when a preferred label is well designed. This supports a retrieval strategy with aliases; it does not establish that the preferred label should always be the longest or most compositional option. [Furnas et al. (1987), “The Vocabulary Problem in Human-System Communication”](https://doi.org/10.1145/32206.32212). A lexicographic record also needs sense separation, usage domain, and historical evidence. A dictionary's established usage is evidence about a term, not a proof that its instructional design is optimal.

**Semantic transparency and memory.** Natural-language compound studies do not yield a simple law that transparent expressions are always processed faster. Frisson, Niswander-Klement, and Pollatsek's work on English compounds found task-dependent effects: forcing an assembly route changed the role of transparency. Wong and Rotello found greater false recognition for certain recombinations involving transparent compounds. These findings concern particular word-recognition and memory tasks, not music terminology, but they directly defeat an unqualified transparency-equals-robustness claim. Compositional components can support reconstruction and also support plausible miscombination. [Frisson, Niswander-Klement, and Pollatsek (2008)](https://research.birmingham.ac.uk/en/publications/the-role-of-semantic-transparency-in-the-processing-of-english-co); [Wong and Rotello (2010)](https://doi.org/10.3758/MC.38.1.47).

**Expertise and chunking.** Chase and Simon's chess work links expertise to structured, domain-related perception and memory. It is an analogy for why a familiar short music symbol can be extremely efficient to an expert, not direct evidence about chord names. SDED must compare intermediate learning with expert use rather than assume that decomposing every familiar chunk improves performance. [Chase and Simon (1973), “Perception in Chess”](https://doi.org/10.1016/0010-0285%2873%2990004-2).

**Music pedagogy.** The major/minor decomposition of seventh chords is already taught in Open Music Theory. The new proposal is therefore not discovery of the chord matrix. Its contribution is to place such construction-bearing expansions in a general, versioned naming architecture, alongside conventional symbols and contextual functions, and to propose comparative tests of when each layer helps. The textbooks establish accepted analyses and notation conventions; they do not supply a controlled trial demonstrating SDED's pedagogical superiority. [Open Music Theory: Seventh Chords](https://viva.pressbooks.pub/openmusictheory/chapter/seventh-chords/).

**Classification and community authority.** Local Contexts' Traditional Knowledge Labels demonstrate that provenance and community protocols can require structured representation beyond generic public access. The Library of Congress's 2021 subject-heading change concerning noncitizens also illustrates that revising a label may require separating concepts and preserving catalogue access, rather than performing a text substitution. Neither example supplies a universal rule for all communities or vocabularies. [Local Contexts TK Labels](https://localcontexts.org/labels/traditional-knowledge-labels/); [Library of Congress decision](https://www.loc.gov/aba/pcc/saco/cpsoed/psd-211115.html).

**Eponym replacement debates.** The paired 2007 BMJ arguments by Woywodt and Matteson and by Whitworth explicitly oppose abandonment to historical and practical retention. They are position arguments, not controlled evidence that one naming policy improves recall. SDED takes that disagreement seriously by separating a descriptive access layer from the historical label, then testing whether the combination is worth its maintenance cost. [Woywodt and Matteson, “Should Eponyms Be Abandoned? Yes”](https://pubmed.ncbi.nlm.nih.gov/17762033/); [Whitworth, “Should Eponyms Be Abandoned? No”](https://pubmed.ncbi.nlm.nih.gov/17762034/).

**Philosophy of language and linguistic relativity.** Successful reference and successful description are different achievements: a stable name can pick out a particular argument without stating its content. This paper uses that distinction analytically; it does not claim to resolve a general theory of names. Nor does it claim that vocabulary determines what people can think. The narrower, testable proposal is that labels can alter task-specific inference, retrieval, and error rates under stated conditions. Broader claims about worldview or linguistic relativity require separate evidence.

**Software engineering, API design, and information theory.** Separate fields, explicit types, stable identifiers, deprecated aliases, and versioned migrations are engineering design patterns used here by analogy. They make implementation inspectable. They do not turn conceptual correctness into a compiler guarantee: a parser can accept a perfectly well-formed but philosophically mistaken descriptor. Similarly, redundancy may allow a person to notice a chord/formula mismatch, but no error-correcting code has been demonstrated. Conditional uncertainty and recovery cost are useful modeling targets, not measured quantities in this manuscript.

The evidence status is consequently asymmetric: concept–label separation and vocabulary governance are established practices; seventh-chord construction is established domain knowledge; SDED's audit and layered recommendation are design proposals; improved retention, transfer, and graceful degradation are empirical hypotheses. Cultural acceptability and philosophical adequacy require appropriate judgment as well as experiments.

## 12. Counterarguments and failure cases

1. **A name is not a definition.** Correct. The proposed preferred descriptor carries selected discriminating information, while a definition and examples remain mandatory. Where no concise faithful descriptor exists, retain the stable name with a scope note.
2. **Expert compression is valuable.** Correct. A trained musician can read C7 faster than a full construction phrase. The symbol layer remains. Long names should not be inserted into performance notation merely to satisfy an editorial ideology.
3. **The components are also learned.** Correct. *Major triad* and *minor seventh* require prior knowledge. The claim is reduced additional arbitrary mapping relative to an explicit prerequisite set, not understanding without education.
4. **Long descriptions can be falsely reassuring.** Correct. *Power Series* is more ordinary than *Taylor series* but underdetermines the object. Semantic equivalence and near-neighbor discrimination precede transparency ratings.
5. **A neat grammar can enforce a bad ontology.** Correct. Philosophical positions, genres, and cultural identities need not form exhaustive, disjoint cells. The system must permit overlaps, disputed relations, and multiple accounts.
6. **Aliases add complexity.** Correct. They create maintenance and retrieval costs, especially when a legacy expression has multiple senses. One-to-many mappings require disambiguation; an automatic search-and-replace migration is unsafe.
7. **Long names can worsen speech and memory.** Correct. Similar compositional phrases can be confused by a single omitted word. Test auditory discrimination, interruption, accessibility, and conjunction errors. A well-chosen opaque mnemonic may win.
8. **Translation can be easier for a stable international token.** Correct. Established borrowed vocabulary can outperform a long English-centric paraphrase. Store language-specific preferred labels and mappings rather than translating components mechanically.
9. **Renaming redistributes authority.** Correct. A formally clear outsider's descriptor can erase identity or impose a contested theory. Community self-designations and intellectual-artifact titles often remain preferred names.
10. **Backward compatibility may outweigh local elegance.** Correct. Citation, discovery, teaching materials, and institutional adoption impose real switching costs. A new pedagogical expansion can be useful without universal migration.
11. **Structural symmetry may overstate musical importance.** Correct. A complete seventh-chord matrix says what can be constructed, not what is equally frequent or aesthetically equivalent. Add usage evidence separately.
12. **The framework could become an enormous bureaucracy.** Correct. Use lightweight records for low-risk glosses and fuller review for canonical replacement, disputed meaning, or cultural authority. Do not make the optional trademark marker or ornamental punctuation a participation hurdle.

SDED fails if it replaces a precise opaque label with an imprecise fluent one, hides disagreement in its canonical field, or treats adoption as evidence of learning. A satisfactory intervention must improve a specified use without silently changing the concept or erasing a valued relation.

## 13. Revised naming principles

1. Start with the concept, audience, task, and near neighbors; never start by replacing an unpleasant word.
2. Audit terminology families before isolated labels. Expose independent dimensions where the domain warrants them.
3. Preserve informative components and conceptual type. Change only what the diagnosed problem requires.
4. Prefer a discriminating description to a generic explanation. A broader topic label is not an exact alias.
5. Keep structural classification, contextual function, provenance, and cultural identity distinct.
6. Permit separate preferred names, symbols, shorthands, historical labels, and functional annotations.
7. Make prerequisite knowledge and hidden defaults explicit. Transparency is relative to those prerequisites.
8. Allow controlled verbosity when it carries useful information; measure its costs instead of imposing a word-count ceiling.
9. Keep stable concept identifiers independent of mutable display text, symbols, punctuation, and ™ styling.
10. Preserve history with sourced metadata. Default to `("<name>", est. <date>)`; ™ is acceptable but never required.
11. Do not invent dates, origins, equivalences, or community approval. State the dated event and uncertainty.
12. Retain self-designations and exact historical references when their identity-bearing role matters. Add descriptors without falsely equating them.
13. Separate semantic relations from layout and genealogy. A longer line is not a reason to invent a subdomain.
14. Version changes, preserve retrieval, and publish rationale, dissent, and evidence status.
15. Treat improvements in learning, memory, and transfer as testable claims. Reject a proposed replacement when evidence or semantic review shows harm.

These rules supersede blanket eponym replacement, universal drop-in substitutability, line-length-driven taxonomy, and mandatory symbolic branding. They retain the original project's strongest demand: the replacement must communicate something substantively distinguishing rather than merely look more descriptive.

## 14. Empirical research agenda

### 14.1 Primary study: seventh-chord construction and transfer

Recruit readers with independently assessed prerequisite knowledge of triads and intervals. Stratify by music training; do not infer expertise from self-label alone. Randomly assign instructional conditions: conventional names; structural expansions; dual labels; and a conventional-name condition with equally available definitions. Keep instructional content, examples, practice time, and feedback comparable. Counterbalance order and items. Where length cannot be matched without destroying the intervention, report length as a design property and include a separate matched-length control to distinguish informative content from mere extra exposure.

Pre-register primary outcomes: accurate chord construction on previously untaught roots and discrimination between quality and function in context. Secondary outcomes: delayed recall, time to correct response, confidence calibration, conventional-symbol recognition, and transfer to unfamiliar triad/seventh combinations. Present both written and aural tasks where appropriate, but do not mistake an aural skill difference for a naming effect. Use unfamiliar roots and held-out combinations so that success cannot be explained solely by rehearsing the four training examples.

Test graceful degradation directly: after a delay, provide a partial name or remove access to the glossary and measure which features can be recovered, which are guessed, and which are correctly marked unknown. Include misleading near neighbors such as major triad + major seventh versus minor triad + major seventh. Measure false confident reconstruction as a harm, not just missing recall. In contextual tasks, include major-triad/minor-seventh chords that are not functioning as V7; accept analysis under the stipulated harmonic framework rather than force one interpretation of ambiguous music.

Model participant and item variability. Determine sample size from a pilot and a pre-specified smallest effect of practical interest; no unsupported numerical power claim is made here. Publish materials, exclusions, analysis code, uncertainty intervals, and null or adverse results. A finding restricted to English-speaking intermediate learners must be reported with that scope.

### 14.2 Separate studies for separate claims

| Claim | Comparison and task | Evidence that would count against it |
|---|---|---|
| Construction-bearing names reduce new arbitrary mappings | Novel but rule-governed families; construct unseen members | No transfer advantage after time and prerequisite controls |
| Controlled verbosity improves error detection | Correct and deliberately mismatched names/formulas | More confident acceptance of errors or slower detection without accuracy gain |
| Layering preserves expert efficiency | Conventional symbols versus symbols with optional expansions in realistic reading tasks | Distraction or slower execution from added display content |
| Aliases improve retrieval | Queries elicited independently of the registry; held-out query set | No recall gain, or precision loss from overloaded aliases |
| Descriptors aid interdisciplinary communication | Matched domain pairs explain and reconstruct concepts | Fluent paraphrase with poorer conceptual accuracy |
| Names survive partial forgetting | Delayed and partial-cue reconstruction | Increased plausible recombination errors |
| Multilingual mapping is portable | Independent bilingual interpretation and back-mapping | Systematic loss of distinctions or false equivalence |
| Cultural supplementation is acceptable | Community-led review and documented revision | Rejection, erasure, or inappropriate disclosure despite formal clarity |

### 14.3 Philosophy and cultural-domain validation

For philosophy, compare label-only, gloss-only, and label-plus-gloss conditions on identifying an argument's target, distinguishing a claim from its criticism, and recognizing that a descriptor does not settle a dispute. Use independently reviewed cases with an explicit scoring rubric and allow more than one defensible interpretation. A participant who repeats “syntax cannot produce semantics” without understanding the Chinese room argument has not demonstrated successful learning.

For cultural names, do not reduce legitimacy to an outsider comprehension score. Invite relevant practitioners or communities to define the task, decide what may be described, review wording, and determine whether publication is appropriate. Report the scope of participation; a few respondents cannot certify an entire tradition. Quantitative usability evidence complements rather than replaces this authority.

### 14.4 Registry evaluation and adoption

Before approving a descriptor, ask at least two domain reviewers to independently identify its referent and distinguish close alternatives. Record disagreements and revise the definition or mapping. Pilot integration in a glossary or lesson with aliases intact. Track correction rates, failed searches, ambiguity reports, and maintenance effort. Separate *proposed*, *semantically reviewed*, *pilot-tested*, and *adopted* statuses. An author-generated example in this paper has the first status unless explicitly stated otherwise.

Longitudinal tests should examine whether users still find the historical literature, whether new terms fragment the vocabulary, and whether teachers omit important qualifications because the new name seems self-explanatory. The architecture succeeds only if its benefits survive these realistic costs.

## 15. Publication structure, titles, and figures

The proposed main title is **SDED 2.0: Self-Documenting Terminology for the Arts and Humanities**. The subtitle, **Naming as an Engineered Knowledge Interface**, states the method without implying that artistic practice should be reduced to a formal system. The historical acronym remains a project identifier; it is not retroactively re-expanded.

Alternative titles are **Beyond Eponym Deprecation: Layered Naming in Music and Philosophy**; **Names That Expose Structure: A Framework for Terminology Design**; and **Structure, Function, and Provenance: Revising SDED for the Arts and Humanities**. The first is best for readers of the original paper; the selected title makes the enlarged domain most visible.

For a shorter journal submission, the publishable outline is: (1) problem and prior SDED; (2) related work and evidence limits; (3) concept/label architecture and family audit; (4) seventh-chord calibration and contrasting music cases; (5) philosophy and cultural countercases; (6) intervention rules and governance; (7) empirical protocol and limitations. The full domain sweep can become a supplementary appendix rather than displace the argument. This version retains the detailed audits requested by the author.

The strongest figures and tables are:

- The two-by-two seventh-chord matrix: structural symmetry beside conventional naming asymmetry.
- One chord, six naming layers: C7, a construction name, historical/conventional alias, spoken shorthand, root, and contextual V7 where applicable.
- The same pitch collection in different harmonic contexts: quality does not determine function.
- Shell voicings that omit the fifth: an audible/voiced subset does not uniquely identify every parent quality.
- A replacement that fails: *Power Series* for *Taylor series*, illustrating false transparency and lost scope.
- Gettier versus Chinese room versus tango: preferred descriptor, exact historical pointer, and canonical cultural identity require different treatments.
- A semantic relation diagram distinguishing exact alias, broader topic, historical derivation, and contextual function.
- The study matrix in Section 14: every promised benefit paired with a possible disconfirming result.

## 16. Relationship to the original project

| Original commitment or implementation | 2.0 treatment | Reason |
|---|---|---|
| Descriptive-first naming and epistemic transparency in v1.1 metadata | Retain as a task-relative preference | Names can carry discriminating information, but not every naming job is descriptive |
| Eponym-focused scope | Extend to opacity, category mixing, defaults, drift, and inconsistent families | Seventh-chord naming exposes a failure without an eponym |
| Attribution and community participation | Retain and simplify | Default quoted historical name/date; ™ optional; evidence and correction routes matter more than typography |
| v1.2 Minimal Intervention | Retain | Informative components and conceptual type should survive |
| v1.2 Sufficiently Substantive Descriptor | Strengthen with near-neighbor and equivalence review | Fluent generic replacements can be wrong |
| Universal syntactic substitution | Replace with scoped label roles and mappings | An argument title, a function, and a structural class are not interchangeable |
| Intermediate-level abbreviation exception | Generalize to explicit prerequisite and audience fields | DNA or a music symbol need not be expanded in every context |
| Parent/derivative punctuation | Separate display, genealogy, and semantic relations | Formatting cannot establish conceptual subsumption |
| Length-triggered subdomain splitting | Supersede | Layout constraints must not invent ontology |
| Early exclusion for identity-bearing historical/cultural references | Retain and elaborate with community authority and translation scope | Some names identify the subject itself rather than describe a construction |
| v1.1 ASCII marker and propagation guidance in the drafting record | Retain ASCII compatibility and simple reference notes; make all TM styling optional | Participation should not depend on typography |
| Historical stylization and legal assertions | Make marker optional; remove blanket assurances | Conformance does not determine legal status |
| Approved vocabulary as a universal replacement list | Replace with versioned, scoped, evidence-labeled records | Domain review and counterexamples remain necessary |
| Pedagogical and knowledge-system benefits | Retain as research questions where not demonstrated | Plausibility is not experimental evidence |

The v1.1 comparison in this release uses verified publication metadata and the recovered October 22 drafting transcript; detailed later rule comparisons use v1.2 source and the October 23 transcript and saved excerpt. The deposited v1.0/v1.1 PDF text could not be retrieved during this preparation despite recovering the record and file metadata. No claim of exact textual equivalence between those editions is made. This limitation must remain visible until a later source comparison can resolve it.

SDED 2.0 therefore retains a substantive descriptive ambition while replacing universal deprecation with a decision procedure. Its strongest immediate result is an explicit separation of what a thing is, what it does in context, what its name historically refers to, and which representation serves the present reader. Whether that separation improves learning and recovery is a question the proposed studies can answer.

## Appendix A. Deliverable map

| Requested deliverable | Location |
|---|---|
| 1. Original project reconstruction | Section 2; research/HISTORY.md |
| 2. Evolution in transcripts | Section 2; research/HISTORY.md |
| 3. Revised title and scope | Title; Sections 1 and 15 |
| 4. Formal definition | Sections 3–4 |
| 5. Naming failure taxonomy | Section 5 |
| 6. Intervention taxonomy | Section 6 |
| 7. Deep music case study | Sections 7–8 |
| 8. Deep philosophy case study | Section 9 |
| 9. Broader humanities survey | Section 10 |
| 10. Before/after examples | Sections 7–10; data/examples.json |
| 11. Counterarguments and failure cases | Section 12 |
| 12. Naming principles | Section 13 |
| 13. Empirical research agenda | Section 14 |
| 14. Successor-paper outline | Section 15 |
| 15. Draft abstract | Opening abstract |
| 16. Candidate titles | Section 15 |
| 17. Figure/table candidates | Section 15 |
| 18. Original-to-revision mapping | Section 16 |

## Appendix B. Publication and evidence note

This is an author-directed conceptual revision prepared with AI assistance for historical retrieval, source discovery, drafting, and artifact production. The manuscript's proposed descriptors have not undergone independent specialist or community review unless a specific entry says otherwise. It reports no new human-participant data. Linked sources support local factual or scholarly claims; engineering evaluations and proposed interventions are the present analysis. No external scholar or community is represented as endorsing SDED.

The historical publication is Brian Wijaya, *SDED™ Protocol Specification: Substantive-Description Eponym Deprecation — A Community Standard for Non-Arbitrary Naming in Knowledge Bases*, v1.1 (2025), [doi:10.5281/zenodo.17418489](https://doi.org/10.5281/zenodo.17418489). The version-series DOI is [10.5281/zenodo.17418488](https://doi.org/10.5281/zenodo.17418488). Repository history is available at [SignalAssembly/SDED](https://github.com/SignalAssembly/SDED). The present draft must not be cited as already deposited under a new DOI until publication is verified.
