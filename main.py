"""
Lumina Systems
Unit 2 Python Cybersecurity Company Capstone
Cybersecurity Management System

DEFENSIVE EDUCATIONAL SIMULATION ONLY.
All employees, resources, events, costs, and incidents are fictional.

Demonstrates:
- Company and crown-jewel asset modeling loaded from JSON files
- CIA triad reasoning
- Role-Based Access Control (RBAC) and least privilege
- Physical and digital access control enforcement
- Corporate security policies
- Risk assessment engine and residual risk calculation
- $250,000 security budget management and trade-offs
- Security event logging and tamper-proof storage model
- Attack detection rules (repeated denials, tailgating, data exfiltration)
- Incident-response workflow (Preparation -> Lessons Learned)
- Security auditing and architecture remediation
- Program-generated executive security report
- Automated testing suite
"""

import json
from datetime import datetime
from pathlib import Path

# ============================================================
# 1. DATA INITIALIZATION & JSON LOADERS
# ============================================================

BASE_FOLDER = Path(__file__).resolve().parent
JSON_DIR = BASE_FOLDER / "json"

LOG_FILE = BASE_FOLDER / "lumina_security_log.txt"
REPORT_FILE = BASE_FOLDER / "lumina_executive_security_report.txt"

INITIAL_BUDGET = 250_000
budget_remaining = INITIAL_BUDGET
purchased_controls = []

EVENTS = []
ALERTS = []
INVESTIGATIONS = []
CONFIRMED_INCIDENTS = []


def load_json(filename):
    """Safely loads a JSON configuration file from the json/ directory."""
    filepath = JSON_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"Required JSON file not found: {filepath}")
    with filepath.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_all_data():
    """Loads all company, asset, policy, risk, and control data from JSON files."""
    global COMPANY, EMPLOYEES, ASSETS, PHYSICAL_SPACES, DIGITAL_RESOURCES
    global ALL_RESOURCES, PERMISSIONS, POLICIES, RISKS, CONTROL_CATALOG, MODEL_PURCHASES

    COMPANY = load_json("company_profile.json")
    EMPLOYEES = load_json("employees.json")
    ASSETS = load_json("assets.json")
    PHYSICAL_SPACES = set(load_json("physical_spaces.json"))
    DIGITAL_RESOURCES = set(load_json("digital_resources.json"))
    ALL_RESOURCES = PHYSICAL_SPACES | DIGITAL_RESOURCES

    raw_permissions = load_json("permissions.json")
    PERMISSIONS = {
        role: set(resources) for role, resources in raw_permissions.items()
    }

    POLICIES = load_json("policies.json")
    RISKS = load_json("risks.json")
    CONTROL_CATALOG = load_json("control_catalog.json")
    MODEL_PURCHASES = load_json("model_purchases.json")


# Initial load of JSON data
load_all_data()

# ============================================================
# 2. UTILITY FUNCTIONS
# ============================================================


def line():
    print("-" * 72)


def pause():
    input("\nPress Enter to continue...")


def safe_int(prompt, minimum=None, maximum=None):
    """Safely request an integer from the user within an optional range."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Value must be no greater than {maximum}.")
            continue

        return value


# ============================================================
# 3. COMPANY & INFRASTRUCTURE DISPLAY
# ============================================================


def display_company_profile():
    print(f"\n{COMPANY['name'].upper()} COMPANY PROFILE")
    line()

    print(f"Company:  {COMPANY['name']}")
    print(f"Industry: {COMPANY['industry']}")
    print(f"Mission:  {COMPANY['mission']}")
    print(f"Size:     {COMPANY['size']:,} employees")

    print("\nCRITICAL ASSETS & CIA CLASSIFICATION")
    line()

    for key, asset in ASSETS.items():
        crown = "  [CROWN JEWEL]" if asset["crown_jewel"] else ""
        print(
            f"{asset['display']:<48} "
            f"CIA={asset['cia']:<16} "
            f"Value={asset['value']}{crown}"
        )


def display_infrastructure():
    print(f"\n{COMPANY['name'].upper()} INFRASTRUCTURE")
    line()

    print("\nPhysical Spaces:")
    for item in sorted(PHYSICAL_SPACES):
        print(f"  - {item}")

    print("\nDigital Resources:")
    for item in sorted(DIGITAL_RESOURCES):
        print(f"  - {item}")

    print("\nRole-Based Access Control (RBAC) Permissions:")
    line()

    for role, resources in sorted(PERMISSIONS.items()):
        print(f"\n{role}:")
        for resource in sorted(resources):
            print(f"  - {resource}")


# ============================================================
# 4. SECURITY EVENT LOGGING
# ============================================================


def log_security_event(user, resource, result, reason, category="Access"):
    """Records an event in memory and appends to the persistent security log."""
    event = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": category,
        "user": user,
        "resource": resource,
        "result": result,
        "reason": reason,
    }

    EVENTS.append(event)

    try:
        with LOG_FILE.open("a", encoding="utf-8") as file:
            file.write(
                f"{event['time']} | "
                f"{event['category']:<18} | "
                f"{event['user']:<14} | "
                f"{event['resource']:<24} | "
                f"{event['result']:<8} | "
                f"{event['reason']}\n"
            )
    except OSError:
        pass

    return event


# ============================================================
# 5. ACCESS CONTROL ENGINE (RBAC & LEAST PRIVILEGE)
# ============================================================


def check_access(username, resource):
    """
    Evaluates whether a user is authorized to access a given resource.
    Enforces fail-safe defaults for unknown users or resources.
    """
    username = username.lower().strip()
    resource = resource.lower().strip()

    if username not in EMPLOYEES:
        log_security_event(
            username, resource, "DENY", "Unknown user - fail closed"
        )
        return False, "Unknown user"

    if resource not in ALL_RESOURCES:
        log_security_event(
            username, resource, "DENY", "Unknown resource - fail closed"
        )
        return False, "Unknown resource"

    role = EMPLOYEES[username]["role"]
    allowed_resources = PERMISSIONS.get(role, set())

    if resource in allowed_resources:
        reason = f"Authorized for role: {role}"
        log_security_event(username, resource, "ALLOW", reason)
        return True, reason

    reason = f"Role '{role}' not authorized (Least Privilege)"
    log_security_event(username, resource, "DENY", reason)
    return False, reason


def access_control_console():
    print("\nEMPLOYEE ACCESS CONTROL CONSOLE")
    line()

    print("\nRegistered Employees:")
    for username, data in EMPLOYEES.items():
        print(f"  {username:<12} {data['name']:<22} {data['role']}")

    print("\nProtected Resources:")
    for resource in sorted(ALL_RESOURCES):
        print(f"  - {resource}")

    username = input("\nUsername: ").strip()
    resource = input("Requested resource: ").strip()

    allowed, reason = check_access(username, resource)

    print("\nACCESS DECISION")
    line()
    print("ACCESS GRANTED" if allowed else "ACCESS DENIED")
    print(f"Reason: {reason}")

    if not allowed and username.lower() in EMPLOYEES:
        alert, message = detect_repeated_denials(username.lower())
        if alert:
            print("\nDETECTION ALERT")
            print(message)


# ============================================================
# 6. RISK ASSESSMENT ENGINE
# ============================================================


def assess_risk(likelihood, impact):
    """
    Classroom risk model:
    Likelihood (1-5) * Impact (1-5) = Risk Score (1-25)

    1-6   Low
    7-14  Moderate
    15-25 High
    """
    if not isinstance(likelihood, int):
        return None, "Invalid likelihood"

    if not isinstance(impact, int):
        return None, "Invalid impact"

    if likelihood not in range(1, 6):
        return None, "Likelihood must be between 1 and 5"

    if impact not in range(1, 6):
        return None, "Impact must be between 1 and 5"

    score = likelihood * impact

    if score >= 15:
        level = "High"
    elif score >= 7:
        level = "Moderate"
    else:
        level = "Low"

    return score, level


def display_risk_register():
    print(f"\n{COMPANY['name'].upper()} RISK REGISTER")
    line()

    for risk in RISKS:
        score, level = assess_risk(risk["likelihood"], risk["impact"])
        asset_info = ASSETS.get(risk["asset"])
        asset_display = asset_info["display"] if asset_info else risk["asset"]

        print(f"\nRisk ID:        {risk['id']} - {risk['threat']}")
        print(f"Asset:          {asset_display}")
        print(f"Vulnerability:  {risk['vulnerability']}")
        print(f"Likelihood:     {risk['likelihood']} / 5")
        print(f"Impact:         {risk['impact']} / 5")
        print(f"Risk Score:     {score} ({level})")
        print(f"Response:       {risk['response']}")
        print(f"Controls:       {risk['controls']}")
        print(f"Residual Risk:  {risk['residual']}")


def interactive_risk_assessment():
    print("\nINTERACTIVE RISK ASSESSMENT")
    line()
    print("Rate Likelihood and Impact on a scale of 1 to 5.")

    likelihood = safe_int("Likelihood (1-5): ", 1, 5)
    impact = safe_int("Impact (1-5): ", 1, 5)

    score, level = assess_risk(likelihood, impact)

    print("\nRESULT")
    line()
    print(f"Likelihood:  {likelihood}")
    print(f"Impact:      {impact}")
    print(f"Risk Score:  {score}")
    print(f"Risk Level:  {level}")
    print(
        "\nNote: Numerical scoring structures analysis; "
        "defensive justification remains mandatory."
    )


# ============================================================
# 7. POLICY ENGINE
# ============================================================


def display_policies():
    print(f"\n{COMPANY['name'].upper()} CORPORATE SECURITY POLICIES")
    line()

    for name, data in POLICIES.items():
        print(f"\n{name.upper()}")
        policy_val = data.get("policy", "")
        if isinstance(policy_val, list):
            policy_text = "\n          ".join(policy_val)
        else:
            policy_text = str(policy_val)
        print(f"Policy:   {policy_text}")
        print(f"Risk:     {data.get('risk', '')}")
        print(f"Controls: {data.get('controls', '')}")


# ============================================================
# 8. SECURITY BUDGET & CONTROL CATALOG
# ============================================================


def reset_budget():
    global budget_remaining
    budget_remaining = INITIAL_BUDGET
    purchased_controls.clear()


def purchase_control(control_key):
    global budget_remaining

    if control_key not in CONTROL_CATALOG:
        return False, "Unknown security control."

    if control_key in purchased_controls:
        return False, "That control has already been purchased."

    control = CONTROL_CATALOG[control_key]
    cost = control["cost"]

    if cost > budget_remaining:
        return (
            False,
            f"Purchase blocked: Cost=${cost:,} exceeds remaining budget of ${budget_remaining:,}.",
        )

    purchased_controls.append(control_key)
    budget_remaining -= cost

    return (
        True,
        f"Purchased '{control['name']}' for ${cost:,}. Remaining: ${budget_remaining:,}",
    )


def display_budget():
    print(f"\n{COMPANY['name'].upper()} SECURITY BUDGET")
    line()

    print(f"Initial Budget:   ${INITIAL_BUDGET:,}")
    print(f"Remaining Budget: ${budget_remaining:,}")
    print(f"Total Spent:      ${INITIAL_BUDGET - budget_remaining:,}")

    print("\nCONTROL CATALOG")
    line()

    for key, control in CONTROL_CATALOG.items():
        status = "PURCHASED" if key in purchased_controls else "AVAILABLE"
        print(
            f"{key:<24} "
            f"${control['cost']:>7,}  "
            f"{control['type']:<10} "
            f"{control['function']:<12} "
            f"{status}"
        )


def security_budget_console():
    while True:
        display_budget()
        print(
            "\nEnter a control key to purchase, "
            "'model' for Lumina's $250k allocation, "
            "'reset' to reset budget, or press Enter to return."
        )

        choice = input("\nSelection: ").strip().lower()

        if choice == "":
            return

        if choice == "reset":
            reset_budget()
            print("Budget reset to initial $250,000.")
            continue

        if choice == "model":
            reset_budget()
            for control in MODEL_PURCHASES:
                success, message = purchase_control(control)
                print(message)
            continue

        success, message = purchase_control(choice)
        print(message)


# ============================================================
# 9. ATTACK DETECTION RULES
# ============================================================


def create_alert(rule, subject, message):
    alert = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rule": rule,
        "subject": subject,
        "message": message,
    }
    ALERTS.append(alert)
    return alert


def detect_repeated_denials(username, threshold=3):
    """Detection Rule 1: Flags repeated failed access attempts."""
    username = username.lower().strip()
    count = sum(
        1
        for event in EVENTS
        if event["user"] == username and event["result"] == "DENY"
    )

    if count >= threshold:
        message = (
            f"{count} denied access attempts recorded for '{username}'. "
            f"Suggests badge misuse, lost card, or testing access boundaries. "
            f"Review CCTV footage and badge reader logs. "
            f"Does NOT prove malicious intent."
        )
        create_alert("Repeated Authentication Failure", username, message)
        return True, message

    return False, f"No alert. Denied attempts for {username}: {count}"


def detect_possible_following(badge_entries, people_observed):
    """Detection Rule 2: Identifies discrepancy between badge scans and optical count."""
    if people_observed > badge_entries:
        message = (
            f"Discrepancy detected at entry portal: {people_observed} persons observed "
            f"for {badge_entries} badge authorization(s). Possible tailgating or piggybacking. "
            f"Review portal camera footage. Does NOT prove whether the employee assisted."
        )
        create_alert("Physical Access Discrepancy", "Restricted Door", message)
        return True, message

    return False, "No entry discrepancy alert."


def detect_document_exposure(sensitive_document_outside_secure_bin):
    """Detection Rule: Identifies improper physical handling of sensitive IP."""
    if sensitive_document_outside_secure_bin:
        message = (
            "Proprietary technical paper or packaging observed outside secure destruction bin. "
            "Potential dumpster diving or improper disposal vulnerability. "
            "Does NOT prove intentional data exfiltration."
        )
        create_alert("Sensitive Document Exposure", "Records / Disposal", message)
        return True, message

    return False, "No document exposure alert."


def detect_source_code_theft(transfer_mb, outside_hours=True, threshold_mb=100):
    """Detection Rule 3: Flags abnormal large source code transfers outside business hours."""
    if transfer_mb >= threshold_mb and outside_hours:
        message = (
            f"Abnormal source repository transfer of {transfer_mb} MB recorded outside standard hours "
            f"(threshold={threshold_mb} MB). Cross-reference with authorized developer commit keys "
            f"and SIEM activity. Does NOT prove external exfiltration or compromise."
        )
        create_alert("Core Source Code Exfiltration Alert", "source_repo", message)
        return True, message

    return False, "No exfiltration alert."


# ============================================================
# 10. SECURITY EVENT SIMULATOR
# ============================================================


def reset_evidence():
    EVENTS.clear()
    ALERTS.clear()
    INVESTIGATIONS.clear()
    CONFIRMED_INCIDENTS.clear()


def run_model_event_simulation():
    """
    Simulates 12 security events representing both normal activity
    and realistic physical/digital attack scenarios.
    """
    reset_evidence()

    print(f"\nRUNNING {COMPANY['name'].upper()} MODEL EVENT SET")
    line()

    # Event 1: Normal authorized physical access
    check_access("riley", "lobby")

    # Event 2: Normal authorized digital access
    check_access("alex", "source_repo")

    # Events 3-5: Repeated denied physical access attempts
    check_access("riley", "server_room")
    check_access("riley", "server_room")
    check_access("riley", "server_room")
    detect_repeated_denials("riley")

    # Event 6: Unauthorized digital access attempt
    check_access("mark", "admin_console")

    # Event 7: Physical tailgating scenario (1 badge scan, 2 observed entrants)
    log_security_event(
        "smart_gate_sensor",
        "ai_model_lab",
        "OBSERVATION",
        "1 badge entry; 2 people observed entering smart gate",
        "Physical Detection",
    )
    detect_possible_following(badge_entries=1, people_observed=2)

    # Event 8: Normal physical entry
    log_security_event(
        "smart_gate_sensor",
        "office",
        "NORMAL",
        "2 badge entries; 2 people observed",
        "Physical Detection",
    )
    detect_possible_following(badge_entries=2, people_observed=2)

    # Event 9: Document disposal vulnerability observation
    log_security_event(
        "custodial_report",
        "records_room",
        "OBSERVATION",
        "Proprietary AI model architecture printout found in standard waste receptacle",
        "Physical Detection",
    )
    detect_document_exposure(True)

    # Event 10: Digital abnormal repository transfer outside business hours
    log_security_event(
        "siem_monitor",
        "source_repo",
        "OBSERVATION",
        "185 MB source code repository download recorded at 02:14 AM",
        "Digital Detection",
    )
    detect_source_code_theft(transfer_mb=185, outside_hours=True)

    # Event 11: Normal authorized administrative/governance access
    check_access("ethan", "soc_room")

    # Event 12: Unknown external entity fails closed
    check_access("external_guest", "source_repo")

    print(
        f"Simulation complete: {len(EVENTS)} events recorded, {len(ALERTS)} alerts triggered."
    )
    print("\nRemember: Alerts warrant investigation; they do not automatically prove an incident.")


def display_events():
    print(f"\n{COMPANY['name'].upper()} SECURITY EVENT LOG")
    line()

    if not EVENTS:
        print("No security events recorded in current runtime.")
        return

    for idx, event in enumerate(EVENTS, start=1):
        print(
            f"{idx:>2}. "
            f"{event['category']:<18} "
            f"{event['user']:<16} "
            f"{event['resource']:<22} "
            f"{event['result']:<10} "
            f"{event['reason']}"
        )


def display_alerts():
    print(f"\n{COMPANY['name'].upper()} DETECTION ALERTS")
    line()

    if not ALERTS:
        print("No active detection alerts recorded.")
        return

    for idx, alert in enumerate(ALERTS, start=1):
        print(f"\nAlert {idx}:")
        print(f"Rule:     {alert['rule']}")
        print(f"Subject:  {alert['subject']}")
        print(f"Time:     {alert['time']}")
        print(f"Evidence: {alert['message']}")


# ============================================================
# 11. INCIDENT RESPONSE WORKFLOW
# ============================================================

INCIDENT_RESPONSE_STAGES = [
    (
        "1. Preparation",
        "Maintain zero-trust policies, SIEM logging with WORM storage, and hardware-backed MFA.",
    ),
    (
        "2. Detection",
        "Automated rules trigger alerts on repeated failures, tailgating, or large off-hours transfers.",
    ),
    (
        "3. Analysis",
        "Correlate event logs, CCTV camera timestamps, badge history, and employee job roles.",
    ),
    (
        "4. Containment",
        "Isolate affected endpoint, suspend compromised access tokens, or lock smart gate portal.",
    ),
    (
        "5. Eradication",
        "Revoke compromised commit keys, invalidate skimming-cloned badges, and purge unauthorized scripts.",
    ),
    (
        "6. Recovery",
        "Reissue hardware keys, restore build server from verified WORM backups, validate services.",
    ),
    (
        "7. Lessons Learned",
        "Document evidence, identify detection gaps, update RBAC boundaries, and report to executive team.",
    ),
]


def display_incident_response():
    print(f"\n{COMPANY['name'].upper()} INCIDENT RESPONSE FRAMEWORK")
    line()

    for stage, details in INCIDENT_RESPONSE_STAGES:
        print(f"\n{stage}")
        print(f"  {details}")

    print("\nANALYST STANDARD:")
    print("An alert is an invitation to investigate; it is not a proven breach.")


def investigate_alert():
    if not ALERTS:
        print("\nNo alerts available to investigate. Run the event simulation first.")
        return

    display_alerts()
    choice = safe_int("\nSelect alert number to investigate: ", 1, len(ALERTS))
    alert = ALERTS[choice - 1]

    print("\nINVESTIGATION IN PROGRESS")
    line()
    print(f"Rule:     {alert['rule']}")
    print(f"Subject:  {alert['subject']}")
    print(f"Evidence: {alert['message']}")

    print("\nSelect Analyst Decision:")
    print("1. Continue investigation (Gather additional camera/SIEM evidence)")
    print("2. Confirm security incident (Escalate to containment)")
    print("3. Close as benign/explained (Authorized anomaly or mistake)")

    decision_choice = input("Decision (1-3): ").strip()
    if decision_choice == "1":
        decision = "Continue investigation"
    elif decision_choice == "2":
        decision = "Confirmed incident"
        CONFIRMED_INCIDENTS.append(alert.copy())
    elif decision_choice == "3":
        decision = "Closed as explained/benign"
    else:
        print("Invalid selection. No decision recorded.")
        return

    INVESTIGATIONS.append({"alert": alert.copy(), "decision": decision})
    print(f"\nDecision recorded: {decision}")


# ============================================================
# 12. SECURITY AUDIT & REMEDIATION
# ============================================================


def audit_security():
    """
    Audits the current cybersecurity architecture against least privilege,
    policy completeness, and budget allocations.
    """
    findings = []

    # Least privilege check
    if "server_room" in PERMISSIONS.get("Executive", set()):
        findings.append({
            "severity": "High",
            "finding": "Executive role has server room access without demonstrated business need.",
            "response": "Modify architecture: Remove server room access under least privilege.",
        })

    # Policy completeness check
    required_policies = {
        "Physical Access",
        "Visitors and Vendors",
        "Workstation Security",
        "Authentication and Authorization",
        "Removable Media",
        "Document Disposal",
        "Power and Continuity",
        "Monitoring and Reporting",
    }
    missing_policies = required_policies - set(POLICIES)
    if missing_policies:
        findings.append({
            "severity": "High",
            "finding": f"Missing required policies: {', '.join(sorted(missing_policies))}",
            "response": "Modify architecture: Author missing policies and connect to risks.",
        })

    # Budget control check
    if purchased_controls:
        purchased = set(purchased_controls)
        if not ({"smart_gate_mantraps", "hardware_keys_hsm"} & purchased):
            findings.append({
                "severity": "Moderate",
                "finding": "No purchased layered access control (smart gates/hardware keys) protects crown jewels.",
                "response": "Modify architecture: Prioritize core access controls.",
            })

        if not ({"ups_generator_upgrade"} & purchased):
            findings.append({
                "severity": "Moderate",
                "finding": "Power continuity and generator support deferred under $250k budget constraint.",
                "response": "Accept residual availability risk: Document outage tolerance and seek next-cycle funding.",
            })
    else:
        findings.append({
            "severity": "Moderate",
            "finding": "No security budget controls have been purchased in current runtime.",
            "response": "Allocate the $250,000 budget to address prioritized risks.",
        })

    if not findings:
        findings.append({
            "severity": "Informational",
            "finding": "All automated audit rules passed.",
            "response": "Maintain ongoing monitoring; do not claim zero residual risk.",
        })

    return findings


def display_audit():
    print(f"\n{COMPANY['name'].upper()} SECURITY AUDIT")
    line()

    findings = audit_security()
    for idx, item in enumerate(findings, start=1):
        print(f"\nFinding {idx} [{item['severity']} Severity]:")
        print(f"Issue:    {item['finding']}")
        print(f"Response: {item['response']}")


# ============================================================
# 13. EXECUTIVE SECURITY REPORT
# ============================================================


def risk_summary():
    summary = {"High": 0, "Moderate": 0, "Low": 0}
    for risk in RISKS:
        _, level = assess_risk(risk["likelihood"], risk["impact"])
        if level in summary:
            summary[level] += 1
    return summary


def control_summary():
    type_counts = {"Physical": 0, "Technical": 0, "Managerial": 0}
    func_counts = {"Preventative": 0, "Detective": 0, "Corrective": 0}

    for key in purchased_controls:
        control = CONTROL_CATALOG[key]
        type_counts[control["type"]] += 1
        func_counts[control["function"]] += 1

    return type_counts, func_counts


def generate_executive_report():
    risks = risk_summary()
    type_counts, func_counts = control_summary()
    findings = audit_security()

    crown_jewels = [
        asset["display"] for asset in ASSETS.values() if asset["crown_jewel"]
    ]

    report_lines = [
        "=" * 72,
        f"{COMPANY['name'].upper()} CYBERSECURITY ARCHITECTURE",
        "EXECUTIVE SECURITY & RISK REPORT",
        "=" * 72,
        "",
        "1. CROWN-JEWEL ASSETS",
    ]
    for cj in crown_jewels:
        report_lines.append(f"  * {cj}")

    report_lines += [
        "",
        "2. RISK REGISTER SUMMARY",
        f"  High Priority Risks:     {risks['High']}",
        f"  Moderate Priority Risks: {risks['Moderate']}",
        f"  Low Priority Risks:      {risks['Low']}",
        "",
        "3. SECURITY BUDGET ALLOCATION ($250,000 TOTAL)",
        f"  Initial Budget:          ${INITIAL_BUDGET:,}",
        f"  Spent:                   ${INITIAL_BUDGET - budget_remaining:,}",
        f"  Remaining:               ${budget_remaining:,}",
        "",
        "4. PURCHASED SECURITY CONTROLS",
    ]

    if purchased_controls:
        for key in purchased_controls:
            c = CONTROL_CATALOG[key]
            report_lines.append(
                f"  * {c['name']} (${c['cost']:,}) - {c['type']} / {c['function']}"
            )
    else:
        report_lines.append("  * None in current runtime")

    report_lines += [
        "",
        "5. CONTROL PORTFOLIO BALANCE",
        f"  Physical Controls:       {type_counts['Physical']}",
        f"  Technical Controls:      {type_counts['Technical']}",
        f"  Managerial Controls:     {type_counts['Managerial']}",
        f"  Preventative Functions:  {func_counts['Preventative']}",
        f"  Detective Functions:     {func_counts['Detective']}",
        f"  Corrective Functions:    {func_counts['Corrective']}",
        "",
        "6. SECURITY MONITORING & INCIDENT EVIDENCE",
        f"  Events Logged:           {len(EVENTS)}",
        f"  Alerts Generated:        {len(ALERTS)}",
        f"  Analyst Investigations:  {len(INVESTIGATIONS)}",
        f"  Confirmed Incidents:     {len(CONFIRMED_INCIDENTS)}",
        "",
        "7. SECURITY AUDIT FINDINGS",
    ]

    for item in findings:
        report_lines.append(f"  * [{item['severity']}] {item['finding']}")

    report_lines += [
        "",
        "8. RESIDUAL RISK & DEFENSIVE STATEMENT",
        "  Controls substantially mitigate physical and digital vectors, but",
        "  residual risk remains regarding side-channel AI attacks, third-party",
        "  dependencies, and insider misuse. No security design eliminates all risk.",
        "",
        "9. ANALYST EVIDENCE STANDARD",
        "  Evidence -> Investigation -> Decision.",
        "  Alerts highlight anomalous evidence and require human correlation",
        "  before declaring a malicious incident.",
        "=" * 72,
    ]

    report_text = "\n".join(report_lines)

    try:
        REPORT_FILE.write_text(report_text, encoding="utf-8")
    except OSError:
        pass

    return report_text


# ============================================================
# 14. AUTOMATED TEST SUITE
# ============================================================


def run_automated_test_suite():
    """
    Executes automated tests validating access control, risk logic,
    attack detection, budget enforcement, and reporting.
    """
    print(f"\n{COMPANY['name'].upper()} AUTOMATED TEST SUITE")
    line()

    reset_evidence()
    reset_budget()
    results = []

    def record(test_id, description, actual, expected):
        passed = actual == expected
        results.append(passed)
        status = "PASS" if passed else "FAIL"
        print(f"{status} | {test_id:<4} | {description}")
        if not passed:
            print(f"       Expected: {expected!r}\n       Actual:   {actual!r}")

    # T01: Authorized physical access
    record("T01", "Authorized physical access (Riley -> lobby)", check_access("riley", "lobby")[0], True)

    # T02: Denied physical access (least privilege)
    record("T02", "Denied physical access (Riley -> server_room)", check_access("riley", "server_room")[0], False)

    # T03: Authorized digital access
    record("T03", "Authorized digital access (Alex -> source_repo)", check_access("alex", "source_repo")[0], True)

    # T04: Denied digital access (least privilege)
    record("T04", "Denied digital access (Mark -> admin_console)", check_access("mark", "admin_console")[0], False)

    # T05: Unknown user fails closed
    record("T05", "Unknown user fails closed", check_access("unknown_attacker", "source_repo")[0], False)

    # T06: Unknown resource fails closed
    record("T06", "Unknown resource fails closed", check_access("alex", "moon_lab")[0], False)

    # T07: Invalid risk input rejected
    record("T07", "Invalid risk likelihood rejected", assess_risk(10, 2)[0], None)

    # T08: Low risk classification
    record("T08", "Low risk rating (2 * 2 = 4)", assess_risk(2, 2)[1], "Low")

    # T09: Moderate risk classification
    record("T09", "Moderate risk rating (3 * 3 = 9)", assess_risk(3, 3)[1], "Moderate")

    # T10: High risk classification
    record("T10", "High risk rating (4 * 5 = 20)", assess_risk(4, 5)[1], "High")

    # T11: Repeated denied access alerts
    check_access("riley", "server_room")
    check_access("riley", "server_room")
    check_access("riley", "server_room")
    record("T11", "Repeated denials trigger alert", detect_repeated_denials("riley")[0], True)

    # T12: Normal physical entry count does not alert
    record("T12", "Normal entry count does not alert", detect_possible_following(2, 2)[0], False)

    # T13: Physical entry mismatch alerts (possible tailgating)
    record("T13", "Entry mismatch triggers alert", detect_possible_following(1, 2)[0], True)

    # T14: Document disposal exposure alerts
    record("T14", "Improper document disposal alerts", detect_document_exposure(True)[0], True)

    # T15: Large code transfer off-hours alerts
    record("T15", "Off-hours data exfiltration alerts", detect_source_code_theft(150, True)[0], True)

    # T16: Valid budget purchase succeeds
    record("T16", "Valid budget purchase succeeds", purchase_control("smart_gate_mantraps")[0], True)

    # T17: Duplicate budget purchase blocked
    record("T17", "Duplicate budget purchase blocked", purchase_control("smart_gate_mantraps")[0], False)

    # Reset and execute model $250,000 purchases
    reset_budget()
    for ctrl in MODEL_PURCHASES:
        purchase_control(ctrl)

    # T18: Model allocation spends full $250,000 budget
    record("T18", "Model allocation spends exact $250,000", budget_remaining, 0)

    # T19: Overspend blocked
    record("T19", "Overspend blocked when budget exhausted", purchase_control("ups_generator_upgrade")[0], False)

    # T20: Security audit generates findings
    record("T20", "Security audit produces findings list", isinstance(audit_security(), list), True)

    # T21: Executive report generation
    report = generate_executive_report()
    record("T21", "Executive report generated successfully", "EXECUTIVE SECURITY & RISK REPORT" in report, True)

    line()
    passed = sum(results)
    total = len(results)
    print(f"TEST RESULTS: {passed}/{total} passed.")

    if passed == total:
        print("All core cybersecurity behaviors passed successfully.")
    else:
        print("One or more tests failed review.")

    return passed == total


# ============================================================
# 15. FULL SYSTEM DEMONSTRATION
# ============================================================


def run_full_system_demo():
    print(f"\n{COMPANY['name'].upper()} FULL SYSTEM DEMONSTRATION")
    line()

    reset_budget()
    print("\n1. Applying model $250,000 security budget allocation...")
    for control in MODEL_PURCHASES:
        success, msg = purchase_control(control)
        print(f"  {msg}")

    print("\n2. Simulating representative security events (physical and digital)...")
    run_model_event_simulation()

    print("\n3. Executing architectural security audit...")
    display_audit()

    print("\n4. Generating program executive security report...")
    report = generate_executive_report()
    print("\n" + report)

    print(f"\nLog file written to:    {LOG_FILE}")
    print(f"Report file written to: {REPORT_FILE}")


# ============================================================
# 16. MAIN INTERACTIVE MENU
# ============================================================


def main():
    while True:
        print(
            f"""
========================================================================
 {COMPANY['name'].upper()}
 CYBERSECURITY MANAGEMENT SYSTEM
========================================================================

 1. Company Profile & Critical Assets
 2. Facility / Digital Infrastructure
 3. Employee Access Control
 4. Corporate Security Policies
 5. Risk Register
 6. Interactive Risk Assessment
 7. Security Budget ($250,000)
 8. Run Model Security Event Simulation
 9. View Security Event Log
10. View Detection Alerts
11. Incident Response Framework
12. Investigate an Alert
13. Security Audit & Remediation
14. Executive Security Report
15. Run Automated Test Suite
16. Run Full System Demonstration
 0. Exit

Reasoning:
Asset -> Vulnerability -> Threat -> Likelihood -> Impact -> Controls -> Justification
Event -> Detection -> Alert -> Investigation -> Decision
"""
        )

        choice = input("Select an option (0-16): ").strip()

        if choice == "1":
            display_company_profile()
            pause()
        elif choice == "2":
            display_infrastructure()
            pause()
        elif choice == "3":
            access_control_console()
            pause()
        elif choice == "4":
            display_policies()
            pause()
        elif choice == "5":
            display_risk_register()
            pause()
        elif choice == "6":
            interactive_risk_assessment()
            pause()
        elif choice == "7":
            security_budget_console()
        elif choice == "8":
            run_model_event_simulation()
            pause()
        elif choice == "9":
            display_events()
            pause()
        elif choice == "10":
            display_alerts()
            pause()
        elif choice == "11":
            display_incident_response()
            pause()
        elif choice == "12":
            investigate_alert()
            pause()
        elif choice == "13":
            display_audit()
            pause()
        elif choice == "14":
            report = generate_executive_report()
            print("\n" + report)
            print(f"\nReport saved to: {REPORT_FILE}")
            pause()
        elif choice == "15":
            run_automated_test_suite()
            pause()
        elif choice == "16":
            run_full_system_demo()
            pause()
        elif choice == "0":
            print(f"\n{COMPANY['name']} Cybersecurity Management System closed.")
            break
        else:
            print("\nInvalid selection. Please choose an option between 0 and 16.")


if __name__ == "__main__":
    main()