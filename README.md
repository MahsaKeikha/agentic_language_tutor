# F167 | Agentic Language Tutor | L3 Gold Standard | v1.0

A governed five-agent reference architecture for language learning across level assessment, lesson planning, practice generation, correction, progress review, accessibility, cultural respect, academic integrity, privacy, provenance, and learner-controlled approval.

F167 is a tutoring and learning-support system. It is not an accredited school, examination board, certification authority, therapist, speech-language pathologist, translator of record, immigration adviser, or autonomous academic decision maker. It cannot complete assessed work for the learner, impersonate the learner, publish private learning data, make high-stakes certification decisions, override consent or preferences, or generate deceptive authorship and answer leakage.

## Language-learning lifecycle

```text
Learner Context and Goals
        -> Level and Diagnostic Assessment
        -> Lesson Goals and Sequencing
        -> Guided Practice and Retrieval
        -> Correction and Explanation
        -> Progress and Mastery Review
        -> Learner Approval and Adaptation
```

The workflow fails closed when required reviews are missing or when material level-assessment, lesson-alignment, practice-quality, correction, progress, accessibility, integrity, privacy, or provenance issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Assessment Agent | Structures learner goals, proficiency, prior knowledge, modalities, confidence, diagnostic evidence, and uncertainty | What does the learner currently understand and what remains uncertain? |
| Lesson Agent | Designs objectives, sequencing, examples, explanations, vocabulary, grammar, pronunciation, cultural context, and modality | What should be taught next and why? |
| Practice Agent | Generates retrieval practice, conversation, reading, listening, writing, drills, transfer tasks, and spaced review | What practice best strengthens durable language use? |
| Correction Agent | Reviews grammar, vocabulary, pronunciation, usage, register, fluency, intelligibility, and error patterns | What needs correction, and how can the explanation help future performance? |
| Progress Agent | Synthesizes mastery evidence, retention, fluency, transfer, goals, review intervals, and next steps | What has actually improved and what should be revisited? |

## Repository structure

```text
AGENTS/
├── assessment_agent.py
├── lesson_agent.py
├── practice_agent.py
├── correction_agent.py
└── progress_agent.py

SKILLS/
├── level_assessment.py
├── lesson_design.py
├── conversation_practice.py
├── error_correction.py
└── progress_reasoning.py

TOOLS/
├── vocabulary_bank.py
├── exercise_bank.py
├── error_log.py
├── progress_tracker.py
└── approval_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Learner context

A tutoring plan should begin with the target language, learner goals, proficiency, native or known languages, preferred modalities, available study time, accessibility needs, desired register, relevant dialect or variety, and intended use such as travel, academic study, work, conversation, literature, or heritage-language development.

The system should not infer intelligence, motivation, education, immigration status, ethnicity, or cultural identity from language proficiency.

## Level assessment

The executable policy requires `learner_level_reviewed`. `level_assessment_gap` blocks release when material learner level, prerequisite, placement, confidence, or diagnostic uncertainty remains unresolved.

Assessment can draw from comprehension, production, vocabulary, grammar, pronunciation, listening, reading, writing, conversation, task completion, and learner self-report.

## Placement uncertainty

A short diagnostic cannot establish every dimension of proficiency. Reading may be stronger than speaking, or receptive vocabulary stronger than productive vocabulary. F167 should preserve profile differences rather than collapsing performance into one false-precision score.

## CEFR and proficiency frameworks

Frameworks such as CEFR can provide useful reference points when applied carefully. F167 does not issue official CEFR, ACTFL, IELTS, TOEFL, or other accredited certifications.

## High-stakes assessment boundary

`make_high_stakes_certification_decision` is protected. A tutor may estimate readiness or identify skill gaps but cannot award, revoke, or represent official test or certification status.

## Lesson architecture

The executable policy requires `lesson_goal_reviewed`. `lesson_alignment_gap` blocks release when material lesson objective, sequence, difficulty, modality, cultural context, or learner-goal mismatch remains unresolved.

A lesson should define a realistic objective, prerequisite knowledge, target forms or functions, examples, guided practice, independent practice, retrieval opportunities, and a check for understanding.

## Sequencing

Language learning benefits from cumulative sequencing. New material should connect to prior vocabulary, grammar, sounds, patterns, and communicative functions while allowing spiraled review.

## Comprehensible input

Input should be challenging enough to create learning without overwhelming comprehension. Difficulty should adapt to the learner rather than remaining fixed.

## Vocabulary

Vocabulary teaching can include meaning, pronunciation, spelling, morphology, collocations, register, frequency, example sentences, contrasts, and retrieval practice.

## Grammar

Grammar explanations should connect form, meaning, and use. Rules should not be presented as universal when dialect, register, context, or exception materially changes usage.

## Pronunciation

Pronunciation coaching should prioritize intelligibility and learner goals. It should not treat one prestige accent as inherently superior or require erasure of cultural identity.

## Accent respect

Accent is not a proxy for intelligence, competence, credibility, or fluency. Feedback should focus on communication effectiveness and the learner's chosen objectives.

## Listening

Listening practice can vary speed, accent, register, topic, noise level, turn-taking, and inference demands over time.

## Speaking

Speaking practice can include controlled production, role play, conversation, explanation, storytelling, negotiation, presentation, and spontaneous response.

## Reading

Reading tasks can develop decoding, vocabulary, syntax, gist, detail, inference, argument structure, genre awareness, and critical reading.

## Writing

Writing practice can address sentence formation, cohesion, structure, genre, tone, audience, register, revision, editing, and authorship.

## Practice architecture

The executable policy requires `practice_quality_reviewed`. `practice_quality_gap` blocks release when material exercise validity, answer quality, spacing, transfer, interaction, or difficulty issues remain unresolved.

## Retrieval practice

Learners benefit from recalling language rather than only rereading it. Exercises should create opportunities to retrieve vocabulary, forms, meanings, and communicative patterns.

## Spaced review

Previously learned content should reappear over time. F167 can use spaced review heuristics but should adapt when the learner repeatedly succeeds or struggles.

## Interleaving

Mixing related skills can improve discrimination and transfer when the learner is ready, though early instruction may still require focused practice.

## Conversation practice

Conversation should encourage genuine language production, repair, clarification, turn-taking, and adaptation rather than forcing the learner through a rigid script.

## Role play

Role plays can simulate travel, workplace, school, healthcare, service, social, or other scenarios while respecting privacy and avoiding deceptive real-world impersonation.

## Exercises and answer quality

Generated exercises must have valid prompts and defensible answers. Ambiguous questions, multiple valid answers, dialect variation, or context-dependent usage should be marked appropriately.

## Correction architecture

The executable policy requires `correction_quality_reviewed`. `correction_feedback_gap` blocks release when material grammar, vocabulary, pronunciation, usage, register, explanation, or feedback-quality issues remain unresolved.

## Error correction

Not every deviation should be corrected at once. Correction priority can reflect communicative impact, lesson objective, recurrence, learner readiness, and whether the form is actually nonstandard within the relevant variety.

## Error types

Useful categories can include grammar, vocabulary, word choice, morphology, syntax, pronunciation, spelling, punctuation, register, collocation, pragmatics, discourse, and transfer from another language.

## Explanations

A correction should explain why the revised form works where useful rather than providing only a replacement answer.

## Self-correction

Prompting the learner to notice and repair an error can be more valuable than immediately revealing the answer when the learner has enough knowledge to do so.

## Fluency versus accuracy

During fluency practice, excessive interruption can reduce communication. During focused form practice, more immediate correction may be appropriate.

## Pronunciation feedback

Pronunciation feedback should distinguish intelligibility problems from harmless accent differences.

## Register and pragmatics

A grammatically correct sentence can still be too formal, too casual, too direct, or culturally inappropriate for a context. F167 should explain register without stereotyping cultures.

## Cultural context

Language and culture are connected, but cultural explanations should avoid essentializing entire populations. Regional, generational, professional, and individual variation should remain visible.

## Language varieties

Different dialects and standards can each be legitimate. The tutor should identify the target variety and explain alternatives when relevant rather than treating one variety as universally correct.

## Multilingual learners

Known languages can support transfer, contrastive explanation, cognates, and metalinguistic awareness. The system should not assume interference is always negative.

## Heritage learners

Heritage-language learners can have strong listening or speaking with weaker literacy, formal register, or grammar terminology. Plans should respect that profile rather than treating them as ordinary beginners.

## Literacy differences

Learners may be literate in one script but not another. Script teaching, transliteration, handwriting, typing, and phonological awareness may require separate sequencing.

## Transliteration

Transliteration can support early access but should not silently replace target-script learning when script mastery is part of the learner's goal.

## Translation

Translation can be a useful learning tool when used intentionally. F167 is not a certified translator and should not represent translations as legally or professionally authoritative.

## Progress architecture

The executable policy requires `progress_evidence_reviewed`. `progress_evidence_gap` blocks release when material mastery, retention, fluency, transfer, assessment validity, or progress-claim evidence remains unresolved.

## Mastery evidence

Mastery should rely on demonstrated performance over more than one prompt where practical. One successful answer is weak evidence for durable learning.

## Retention

Delayed retrieval provides stronger evidence than immediate repetition after explanation.

## Transfer

A learner should eventually use language in new contexts, not only reproduce the exact examples used during instruction.

## Fluency

Fluency can include speed, ease, automaticity, repair, comprehensibility, and interaction. It should not be reduced to speaking fast.

## Progress claims

The system should not claim that a learner has become fluent, mastered a level, or is guaranteed to pass an exam without appropriate evidence.

## Error tracking

Recurring errors can be logged by type, context, frequency, severity, and revision status. Error logs should support learning rather than create a permanent negative profile.

## Motivation and confidence

The tutor can encourage practice and acknowledge progress, but it should not manipulate the learner, create dependency, or make psychological diagnoses.

## Accessibility and inclusion

The executable policy requires `accessibility_inclusion_reviewed`. `accessibility_inclusion_gap` blocks release when material disability access, language variety, accent respect, cultural inclusion, age appropriateness, or usability issues remain unresolved.

## Disability access

Learning materials can support captions, transcripts, keyboard access, screen-reader-friendly structure, alternative formats, adjustable pacing, simplified interfaces, and multimodal presentation.

## Neurodiversity

Learners can differ in attention, working memory, sensory needs, processing speed, and preferred structure. F167 should adapt instructional format without diagnosing conditions.

## Age appropriateness

Examples, role plays, topics, media, and feedback should be appropriate to learner age and context. Younger learners require stronger privacy and safeguarding boundaries.

## Cultural inclusion

Examples should avoid discriminatory stereotypes and should represent people and contexts respectfully.

## Bias

Accent, grammar variety, code-switching, and nonstandard forms should not be used as proxies for intelligence or worth.

## Academic integrity

The executable policy requires `privacy_integrity_reviewed`. `privacy_integrity_risk` blocks release when material learner privacy, sensitive data, plagiarism, academic integrity, answer leakage, authorship, or consent concerns remain unresolved.

## Assessed work boundary

`complete_assessed_work_for_learner` is protected. F167 can explain concepts, generate analogous practice, critique drafts, ask guiding questions, and teach revision, but it should not deceptively complete graded work on the learner's behalf.

## Answer leakage

When an exercise is intended to test learning, the system should not reveal the answer prematurely unless the learner requests explanation or the pedagogical design calls for it.

## Deceptive authorship boundary

`generate_deceptive_authorship_or_answer_leakage` is protected. The system should not help a learner misrepresent AI-generated work as independently authored when that violates the relevant academic rules.

## Source checking

Grammar references, dictionaries, corpora, style guides, educational materials, and other sources can disagree. The system should preserve uncertainty where usage is contested.

## Copyright

Practice can use short examples and transformed material, but the tutor should avoid reproducing substantial copyrighted textbooks, tests, answer keys, or proprietary course content without permission.

## Privacy

The tutor may handle names, recordings, writing samples, school information, workplace information, learning disabilities, immigration-related language goals, or other sensitive data. Collection and retention should be minimized.

## Voice and recordings

Audio or video rehearsal data should be used with consent. Recordings should not be published or shared automatically.

## Private learning data boundary

`publish_private_learning_data` is protected. Progress reports, mistakes, recordings, and learner profiles remain private unless the learner or authorized guardian explicitly approves sharing.

## Third-party boundary

`impersonate_learner_or_contact_third_party` is protected. F167 can draft messages or practice conversations but cannot contact teachers, schools, employers, exam bodies, or other parties as the learner.

## Learner autonomy

`override_learner_consent_or_preferences` is protected. The learner controls goals, target variety, correction intensity, topics, pace, and whether to continue a particular exercise.

## Learner approval

The executable policy requires `learner_approval_reviewed`. Lesson and progress packages should remain subject to learner review and adaptation.

## Provenance

`provenance_approval_gap` blocks release when material source, lesson, exercise, correction, assessment, progress, revision, or learner-approval provenance is incomplete.

F167 must never fabricate test scores, certifications, teacher feedback, source citations, learner history, mastery evidence, progress, recordings, approvals, or completed coursework.

## Memory and state

The `memory/` layer can preserve learner goals, confirmed level estimates, vocabulary, recurring errors, completed lessons, practice history, progress evidence, preferred correction style, and review state.

Memory should distinguish current confirmed preferences from stale assumptions and support correction or deletion where appropriate.

## Observability

The `observability/` layer supports traceability across level estimates, lessons, exercises, corrections, progress evidence, privacy status, integrity flags, approvals, and protected-action attempts.

Useful telemetry includes stale placement evidence, repeated error categories, unresolved ambiguities, overly difficult exercises, missing review, answer leakage flags, privacy concerns, and progress claims awaiting evidence.

## Required reviews

The executable policy requires all eight conditions:

```text
learner_level_reviewed
lesson_goal_reviewed
practice_quality_reviewed
correction_quality_reviewed
progress_evidence_reviewed
accessibility_inclusion_reviewed
privacy_integrity_reviewed
learner_approval_reviewed
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- learner level, prerequisites, placement, confidence, or diagnostic uncertainty remains unresolved
- lesson objectives, sequence, difficulty, modality, cultural context, or learner goals are misaligned
- exercise validity, answer quality, spacing, transfer, interaction, or difficulty issues remain unresolved
- grammar, vocabulary, pronunciation, usage, register, explanation, or correction quality remains unresolved
- mastery, retention, fluency, transfer, assessment validity, or progress evidence remains unresolved
- accessibility, language variety, accent respect, cultural inclusion, age appropriateness, or usability remains unresolved
- learner privacy, sensitive data, plagiarism, academic integrity, answer leakage, authorship, or consent concerns remain unresolved
- source, lesson, exercise, correction, assessment, progress, revision, or learner-approval provenance is incomplete
- any required review is missing
- learner approval is missing

## Protected actions

```text
complete_assessed_work_for_learner
impersonate_learner_or_contact_third_party
publish_private_learning_data
make_high_stakes_certification_decision
override_learner_consent_or_preferences
generate_deceptive_authorship_or_answer_leakage
```

These remain outside autonomous authority even after all required reviews pass.

## Explicit failure states

```text
LEARNER LEVEL REVIEW REQUIRED
LESSON GOAL REVIEW REQUIRED
PRACTICE QUALITY REVIEW REQUIRED
CORRECTION QUALITY REVIEW REQUIRED
PROGRESS EVIDENCE REVIEW REQUIRED
ACCESSIBILITY AND INCLUSION REVIEW REQUIRED
PRIVACY AND INTEGRITY REVIEW REQUIRED
LEARNER APPROVAL REVIEW REQUIRED
LEVEL ASSESSMENT GAP
LESSON ALIGNMENT GAP
PRACTICE QUALITY GAP
CORRECTION OR FEEDBACK GAP
PROGRESS EVIDENCE GAP
ACCESSIBILITY OR INCLUSION GAP
PRIVACY OR ACADEMIC INTEGRITY RISK
PROVENANCE OR APPROVAL GAP
ASSESSED-WORK COMPLETION PROHIBITED
LEARNER IMPERSONATION PROHIBITED
PRIVATE LEARNING DATA PUBLICATION PROHIBITED
HIGH-STAKES CERTIFICATION DECISION PROHIBITED
LEARNER CONSENT OVERRIDE PROHIBITED
DECEPTIVE AUTHORSHIP OR ANSWER LEAKAGE PROHIBITED
```

## End-to-end reference workflow

1. Capture target language, learner goals, known languages, modality preferences, desired variety or register, accessibility needs, and study constraints.
2. Run a diagnostic across relevant receptive and productive skills and preserve uncertainty rather than forcing one simplistic level.
3. Define a lesson objective tied to learner goals and prerequisites.
4. Teach target vocabulary, grammar, pronunciation, discourse, or communicative function with accurate examples and cultural context.
5. Generate guided practice, retrieval practice, conversation, reading, listening, writing, and transfer tasks at an appropriate level.
6. Provide proportionate correction with explanations, self-correction opportunities, and respect for legitimate language varieties.
7. Revisit prior material through spaced review and interleaving where appropriate.
8. Evaluate progress using retention, transfer, fluency, comprehension, and repeated performance evidence.
9. Review accessibility, cultural inclusion, age appropriateness, privacy, academic integrity, answer leakage, authorship, and consent.
10. Preserve provenance for lessons, sources, exercises, corrections, progress evidence, revisions, and approvals.
11. Apply fail-closed governance and require learner approval.
12. Keep assessed-work completion, impersonation, private-data publication, certification, consent override, and deceptive authorship outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test placement reasoning, lesson sequencing, exercise validity, answer quality, correction accuracy, pronunciation sensitivity, progress evidence, cultural respect, accessibility, academic integrity, privacy, provenance, and protected-action behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved tutoring release, level-assessment gaps, lesson misalignment, practice-quality problems, correction gaps, progress-evidence gaps, accessibility or inclusion issues, privacy or integrity risks, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance, held-out scenarios, and execution of the governed five-agent tutoring workflow.

## Reproducibility

A reproducible tutoring state should preserve target language, learner goals, level evidence, lesson objectives, source references, exercises, answers, corrections, recurring errors, progress evidence, review dates, preferences, and approval state.

## Extension points

Organization-specific implementations can add governed integrations for dictionaries, corpora, speech recognition, text-to-speech, spaced-repetition systems, learning management systems, language labs, classroom tools, and assessment platforms.

Any integration capable of submitting coursework, changing grades, communicating with schools or employers, publishing recordings, issuing credentials, or exposing private learner data should remain behind explicit authorization, least privilege, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include beginner language learning, conversation practice, pronunciation coaching, grammar review, vocabulary acquisition, heritage-language learning, professional language, academic language, travel preparation, reading support, writing feedback, exam preparation without answer leakage, and multilingual skill maintenance.

F167 is not an autonomous teacher of record, examination board, accredited language assessor, certified translator, speech-language clinician, or substitute for the learner's judgment and institutional requirements.

## Design principles

1. Adapt to the learner's goals, evidence, level profile, language variety, accessibility needs, and preferred pace.
2. Teach for durable retrieval, transfer, comprehension, and communication rather than answer imitation alone.
3. Preserve legitimate dialects and accents and never equate one language variety with intelligence or worth.
4. Distinguish correction from rewriting and learning support from deceptive authorship.
5. Never fabricate sources, scores, certifications, mastery, teacher feedback, progress, or learner approval.
6. Treat privacy, academic integrity, consent, accessibility, cultural respect, and age appropriateness as first-class governance concerns.
7. Preserve uncertainty when usage, placement, proficiency, or progress evidence is incomplete.
8. Fail closed when level, lesson design, practice, correction, progress, accessibility, integrity, provenance, or approval is incomplete.
9. Keep assessed-work completion, third-party impersonation, certification, private-data publication, and consent override under accountable human control.

## Scope statement

F167 demonstrates a governed multi-agent architecture for language tutoring. It combines specialized assessment, lesson, practice, correction, and progress agents with deterministic vocabulary, exercise, error, progress, and approval tools, observability, held-out evaluation, and fail-closed governance while preserving learner autonomy, academic integrity, privacy, accessibility, and strict human authority over consequential educational actions.

Author: Mahsa Keikha
