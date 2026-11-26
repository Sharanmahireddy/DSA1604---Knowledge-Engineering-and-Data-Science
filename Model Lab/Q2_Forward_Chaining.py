facts = {"valid_policy", "reported_within_24h",
         "police_report_filed", "no_fraud_flag"}

if {"valid_policy", "reported_within_24h"}.issubset(facts):
    facts.add("claim_admissible")
if {"claim_admissible", "police_report_filed"}.issubset(facts):
    facts.add("claim_verified")
if {"claim_verified", "no_fraud_flag"}.issubset(facts):
    facts.add("claim_approved")
if "claim_approved" in facts:
    facts.add("release_payment")

print("Inferred facts:")
for fact in sorted(facts):
    print(fact)
print("Final Decision: Claim Approved" if "claim_approved" in facts
      else "Final Decision: Claim Not Approved")
