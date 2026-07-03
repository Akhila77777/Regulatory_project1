# MDR Classification Rationale

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | CLS-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Regulations:** EU MDR 2017/745 (Art. 2, Art. 51, Annex VIII); guidance MDCG 2019-11; EU AI Act
2024/1689 (Art. 6). **Related:** intended_use.md (IU-001), risk_management_file/ (RMF-*),
eu_ai_act/ (AIA-*), iec62304/. **Study reference:** `steps/step-02-mdr-classification-gspr.html`.

---

## 1. Purpose

This document records the reasoning for the regulatory qualification and classification of
DermaScan. It is derived from the intended purpose (IU-001) and is a prerequisite for selecting the
conformity assessment route. Any change to IU-001 requires this document to be re-evaluated.

## 2. Step 1 - Qualification as a medical device

Per **MDR Article 2(1)**, a device includes software intended by the manufacturer to be used for a
medical purpose such as diagnosis, prevention, monitoring, prediction, prognosis, or treatment of
disease.

Applying the **MDCG 2019-11** qualification logic:
- DermaScan performs an action on data **beyond** storage, archival, communication, or simple
  search: it analyses an image to compute a malignancy-risk estimate.
- It does so for a **medical purpose** (supporting diagnosis of a possible malignancy) for the
  benefit of an **individual patient**.

**Conclusion:** DermaScan qualifies as a medical device and, being standalone software, is
**Software as a Medical Device (SaMD)**.

## 3. Step 2 - Is it active software?

DermaScan is active software (it depends on a source of energy and processes data). This makes the
software-specific classification rule, Rule 11, applicable.

## 4. Step 3 - Application of Rule 11 (Annex VIII)

**Rule 11 text (paraphrased):** Software intended to provide information used to take decisions for
diagnostic or therapeutic purposes is **Class IIa**, unless such decisions have an impact that may
cause:
- death or an irreversible deterioration of health -> **Class III**; or
- a serious deterioration of health or a surgical intervention -> **Class IIb**.
Software intended to monitor physiological processes is Class IIa (IIb if vital parameters where
variation could result in immediate danger). All other software is Class I.

### 4.1 Does DermaScan provide information used for diagnostic decisions?
Yes. Per IU-001, the output (a malignancy-risk estimate) is explicitly intended to inform the
clinician's diagnostic triage decision. Therefore Rule 11 applies and the **baseline class is IIa**.

### 4.2 Could the decision lead to death or irreversible deterioration (-> III) or serious
deterioration / surgery (-> IIb)?

This is the crux. An erroneous output (notably a false negative, RISK-001) could in principle
contribute to a delayed melanoma diagnosis, which is a serious and potentially irreversible harm.
Read in isolation, that consequence could argue for IIb or even III.

However, classification under Rule 11 is assessed in light of the device's **intended purpose and
its role in the decision**:
- DermaScan is positioned strictly as **decision-support**, an adjunct that provides information
  to a **qualified clinician who independently confirms every output** (IU-001 Sections 3, 6, 11).
- The software does **not** itself diagnose, triage autonomously, or direct treatment; the
  responsible clinician makes and owns the decision.
- The intended use is **triage support**, not a definitive or sole basis for a treatment decision
  that could directly cause death or irreversible harm.

On this basis, the information DermaScan provides is one input among several to a clinician-led
decision, and the device is **not** intended to drive decisions that, by themselves, cause death,
irreversible deterioration, serious deterioration, or surgical intervention.

### 4.3 Classification decision
**DermaScan is classified as Class IIa under Rule 11.**

### 4.4 Sensitivity of the decision and conditions
This classification is **conditional on the decision-support, mandatory-clinician-review framing**
being preserved. If the intended purpose were changed so that the output could be used
autonomously, for definitive diagnosis, or to direct treatment without independent confirmation,
re-classification to IIb (or higher) would be required. This dependency is recorded as a constraint
on IU-001 and is consistent with the residual-risk reasoning in RMF-RPT-001.

> Note: Rule 11 is widely regarded as over-classifying clinical decision software and is a target of
> the MDR/IVDR revision and the EU Digital Omnibus simplification debate (see
> step-02 and step-13). This does not change the present classification but is noted for currency.

## 5. Conformity assessment route (consequence of IIa)

As a Class IIa device, DermaScan requires the involvement of a **Notified Body**. The intended
route is **MDR Annex IX** (QMS assessment plus assessment of the technical documentation on a
representative basis), with Annex XI as an alternative. Details are developed in
technical_documentation/ (build phase 12).

## 6. Interaction with the EU AI Act

DermaScan uses machine learning and is a **safety component of / is itself** a product (the medical
device) covered by Annex I EU harmonisation law (the MDR) that requires **third-party conformity
assessment** (because it is Class IIa). Under **AI Act Article 6(1)**, both conditions are met, so
DermaScan is a **high-risk AI system**. The MDR conformity assessment and the AI Act high-risk
requirements are intended to be satisfied through a single integrated technical file and assessment
(see eu_ai_act/, build phase 6, and AI Act Art. 8(2)).

## 7. Note on IEC 62304 software safety class

The MDR class (IIa) is distinct from the IEC 62304 software safety class (A/B/C), which is derived
separately from the risk analysis (RMF-RA-001). The pivotal question (whether mandatory clinician
review credibly prevents the software alone from causing serious harm) is the same dependency
identified in Section 4.2 and RMF-RPT-001. That decision has now been made and documented in
SSC-001: because clinician review reduces probability but cannot be relied upon to prevent serious
harm (automation bias; procedural, unverifiable control), the software is classified **IEC 62304
Software Safety Class C**. Note the two arguments point in different directions and both are
defensible: for the MDR class, the decision-support framing supports the lower class (IIa); for the
IEC 62304 class, that same framing is conservatively **not** relied upon to lower the class, so
Class C is assigned.

## 8. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): qualification, Rule 11 IIa rationale, AI Act Art. 6(1) |
