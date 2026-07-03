# Software Safety Classification (IEC 62304)

> SIMULATION / TRAINING EXERCISE. DermaScan is a personal portfolio project, NOT a certified
> medical device. No real clinical use. Content is written in submission style for learning.

| Field | Value |
|---|---|
| Document ID | SSC-001 |
| Version | 0.1 |
| Status | Draft |
| Author | Akhila N Pillai |
| Date | 2026-06-27 |
| Reviewed by | - |
| Approved by | - |

**Standard:** IEC 62304:2006+A1:2015 (clause 4.3 and 5.1.1). **Related:** RMF-RA-001 (risk
analysis), RMF-RPT-001, CLS-001 (§7), SDP-001. **Study reference:** `steps/step-04-iec62304-software.html`.

---

## 1. Purpose

This document determines and justifies the IEC 62304 software safety class for DermaScan. The MDR
device class (Class IIa, CLS-001) and the IEC 62304 software safety class are **distinct**: the MDR
class drives the conformity route, while the software safety class drives the rigour of the software
lifecycle. The class is derived from the risk analysis (RMF-RA-001); it is **not** assumed.

## 2. The classification rule (IEC 62304 4.3)

The software safety class is assigned according to the **severity of the harm** that could result
from a hazardous situation to which the software system can contribute, **after taking into account
risk control measures external to the software system**:

| Class | Criterion |
|---|---|
| A | No injury or damage to health is possible, or the software cannot contribute to a hazardous situation. |
| B | Non-serious injury is possible. |
| C | Death or serious injury is possible. |

Two points of method:
1. Classification is driven by **severity** (the worst credible harm), not by probability.
2. External risk control measures may reduce the class **only if** they can be relied upon to
   prevent the hazardous situation from leading to that harm.

## 3. Can the software contribute to a hazardous situation?

Yes. Per RMF-RA-001, an erroneous DermaScan output (notably a false negative, RISK-001, or an
out-of-distribution input scored as valid, RISK-003) can contribute to a clinician under-triaging a
malignant lesion.

## 4. Worst credible harm (severity)

The worst credible harm is a **delayed diagnosis and treatment of melanoma**, which can lead to
disease progression and is potentially fatal. On the RMF-PLAN-001 severity scale this is **S4
(Critical, irreversible serious deterioration)**, bordering S5. This is a **serious injury / death**
outcome.

On severity alone, the baseline software safety class is therefore **Class C**.

## 5. Effect of external risk control measures

The principal external risk control is **mandatory independent review of every output by a qualified
clinician** (IU-001, and the dominant control in RMF-RA-001 / RMF-RPT-001). The question for
declassification is whether this control can be **relied upon to prevent** the serious harm.

It cannot be fully relied upon, for the following documented reasons:
- **Automation bias (RISK-005):** clinicians can over-trust a confident-looking output and reduce
  independent scrutiny, so the review is not a guaranteed barrier.
- The review is a **procedural** measure outside the manufacturer's full control; its effectiveness
  cannot be verified by the manufacturer in the way a technical interlock could.
- It reduces the **probability** of harm but does not change the **severity** of the worst case,
  and IEC 62304 classifies on severity.

Therefore the external clinician-review control is treated as a **risk-reducing measure** (reflected
in the probability reduction in RMF-RA-001), **not** as a declassifying measure.

## 6. Classification decision

**DermaScan software is classified as IEC 62304 Software Safety Class C.**

Rationale summary: the software can contribute to a hazardous situation whose worst credible harm is
death or serious injury (delayed melanoma treatment), and the available external control (clinician
review) cannot be relied upon to prevent that harm because of automation bias and its procedural,
unverifiable nature. The conservative and defensible classification is therefore Class C.

This decision is deliberately **not** reduced to Class B to lessen the documentation burden;
choosing the lower class would require a verifiable, non-bypassable external control that does not
currently exist in the design.

## 7. Condition under which Class B could be justified (documented alternative)

A Class B classification could become defensible **only if** a robust, verifiable independent
confirmation mechanism were designed and validated such that a single erroneous software output
could not, in normal use, lead to serious harm (for example a mandatory, logged, independent
two-step confirmation with effectiveness demonstrated against automation bias). Until such a control
exists and is verified, Class C stands. Any future change toward Class B must be recorded here and
must update SDP-001, CLS-001 §7, and RMF-RPT-001.

## 8. Consequences of Class C

- Detailed design (5.4) is required in addition to architectural design.
- Unit-level verification with documented acceptance criteria is required.
- Full integration and system testing with traceability to requirements is required.
- Anomaly evaluation at release (5.8) is required.
These are reflected in the deliverable set in SDP-001.

## 9. Segregation note

If, in architecture (architecture.md), software items that cannot contribute to serious harm are
demonstrably segregated from those that can, those items may be documented at a lower class with a
justified rationale. No such segregation is claimed at this stage; the system is treated as Class C
as a whole.

## 10. Change history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-27 | Akhila N Pillai | Initial draft (simulation): Class C decision with documented Class B condition |
