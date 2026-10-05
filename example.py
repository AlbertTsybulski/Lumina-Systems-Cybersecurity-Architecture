"""
TitanTech Advanced Systems
Unit 2 Python Cybersecurity Company Capstone
Complete Teacher Demonstration

DEFENSIVE EDUCATIONAL SIMULATION ONLY.
All employees, resources, events, costs, and incidents are fictional.

Demonstrates:
- Company / asset modeling
- CIA reasoning
- RBAC and least privilege
- Physical + digital access control
- Corporate security policies
- Risk assessment and residual risk
- Security budget management
- Event logging
- Attack detection
- Incident-response reasoning
- Security auditing
- Executive reporting
- Automated testing

Cybersecurity reasoning:
Asset -> Vulnerability -> Threat -> Likelihood -> Impact -> Controls -> Justification
Event -> Detection -> Alert -> Investigation -> Decision
"""

from datetime import datetime
from pathlib import Path

# ============================================================
# 1. COMPANY PROFILE
# ============================================================

COMPANY = {
    "name": "TitanTech Advanced Systems",
    "industry": "Robotics and Cybersecurity Technology",
    "mission": "Design secure industrial robotics and control software.",
    "size": 220,
}

EMPLOYEES = {
    "alex": {"name": "Alex Morgan", "role": "Software Engineer"},
    "riley": {"name": "Riley Chen", "role": "Robotics Engineer"},
    "sam": {"name": "Sam Rivera", "role": "IT/Security Administrator"},
    "jordan": {"name": "Jordan Patel", "role": "Receptionist"},
    "taylor": {"name": "Taylor Brooks", "role": "Facilities Technician"},
    "casey": {"name": "Casey Williams", "role": "Executive"},
}

ASSETS = {
    "robot_control_source": {
        "display": "Robot Control Source Code",
        "crown_jewel": True,
        "cia": "Integrity",
        "value": "High",
    },
    "prototype_designs": {
        "display": "Prototype Designs",
        "crown_jewel": True,
        "cia": "Confidentiality",
        "value": "High",
    },
    "customer_data": {
        "display": "Customer Contracts and Data",
        "crown_jewel": True,
        "cia": "Confidentiality",
        "value": "High",
    },
    "identity_access_system": {
        "display": "Identity and Access System",
        "crown_jewel": False,
        "cia": "Integrity",
        "value": "High",
    },
    "production_build_server": {
        "display": "Production Build Server",
        "crown_jewel": False,
        "cia": "Availability",
        "value": "High",
    },
    "network_infrastructure": {
        "display": "Network Infrastructure",
        "crown_jewel": False,
        "cia": "Availability",
        "value": "High",
    },
    "employee_endpoints": {
        "display": "Employee Endpoints",
        "crown_jewel": False,
        "cia": "Confidentiality",
        "value": "Moderate",
    },
    "prototype_robots": {
        "display": "Prototype Robots",
        "crown_jewel": False,
        "cia": "Integrity",
        "value": "High",
    },
    "power_infrastructure": {
        "display": "Power Infrastructure",
        "crown_jewel": False,
        "cia": "Availability",
        "value": "High",
    },
    "security_evidence": {
        "display": "Security Logs and Video",
        "crown_jewel": False,
        "cia": "Integrity",
        "value": "Moderate",
    },
}

# ============================================================
# 2. PHYSICAL + DIGITAL INFRASTRUCTURE
# ============================================================

PHYSICAL_SPACES = {
    "lobby",
    "engineering_office",
    "prototype_lab",
    "server_room",
    "loading_dock",
    "utility_room",
    "records_room",
}

DIGITAL_RESOURCES = {
    "visitor_system",
    "source_repo",
    "design_files",
    "admin_console",
    "business_system",
    "build_server",
}

ALL_RESOURCES = PHYSICAL_SPACES | DIGITAL_RESOURCES

# ============================================================
# 3. ROLE-BASED ACCESS CONTROL
# ============================================================

PERMISSIONS = {
    "Receptionist": {
        "lobby",
        "visitor_system",
    },
    "Software Engineer": {
        "lobby",
        "engineering_office",
        "source_repo",
        "build_server",
    },
    "Robotics Engineer": {
        "lobby",
        "engineering_office",
        "prototype_lab",
        "design_files",
    },
    "IT/Security Administrator": {
        "lobby",
        "engineering_office",
        "server_room",
        "admin_console",
        "build_server",
    },
    "Facilities Technician": {
        "lobby",
        "loading_dock",
        "utility_room",
    },
    "Executive": {
        "lobby",
        "business_system",
    },
}

# ============================================================
# 4. CORPORATE SECURITY POLICIES
# ============================================================

POLICIES = {
    "Physical Access": {
        "policy": (
            "Employees must badge individually into restricted areas "
            "and may not admit another person using their credential."
        ),
        "risk": "Piggybacking, tailgating, unauthorized physical access",
        "controls": "Badge readers, vestibules, awareness, monitoring",
    },
    "Visitors and Vendors": {
        "policy": (
            "Visitors must verify identity, receive temporary identification, "
            "remain in approved areas, and be escorted in restricted zones."
        ),
        "risk": "Unauthorized physical access",
        "controls": "Reception procedures, visitor badges, escorts",
    },
    "Workstation Security": {
        "policy": (
            "Unattended devices must be locked and sensitive information "
            "must not remain unnecessarily exposed."
        ),
        "risk": "Shoulder surfing and physical information exposure",
        "controls": "Screen locks, privacy filters, workstation positioning",
    },
    "Authentication and Authorization": {
        "policy": (
            "TitanTech uses unique credentials, MFA where appropriate, "
            "RBAC, least privilege, and need-to-know."
        ),
        "risk": "Unauthorized digital access",
        "controls": "MFA, RBAC, least privilege",
    },
    "Removable Media": {
        "policy": (
            "Unapproved removable media is prohibited on restricted systems. "
            "Ports may be disabled where business need does not require them."
        ),
        "risk": "Unauthorized physical device or port access",
        "controls": "Endpoint policy, port restrictions, endpoint controls",
    },
    "Document Disposal": {
        "policy": (
            "Sensitive paper must be placed in approved locked destruction "
            "containers and may not be placed in ordinary trash."
        ),
        "risk": "Dumpster diving and information exposure",
        "controls": "Locked destruction bins, shredding, clean-desk policy",
    },
    "Power and Continuity": {
        "policy": (
            "Critical systems use UPS and surge protection. Selected services "
            "receive generator support, backups, and tested recovery procedures."
        ),
        "risk": "Power and environmental disruption",
        "controls": "UPS, surge protection, generator, backups, recovery",
    },
    "Monitoring and Reporting": {
        "policy": (
            "Employees must report suspicious activity. Alerts trigger "
            "investigation and do not automatically prove compromise or intent."
        ),
        "risk": "Delayed or inaccurate attack detection",
        "controls": "Logging, cameras, access records, employee reporting",
    },
}

# ============================================================
# 5. RISK REGISTER
# ============================================================

RISKS = [
    {
        "id": "R1",
        "asset": "prototype_designs",
        "vulnerability": "Employees may hold a restricted door for another person.",
        "threat": "Piggybacking",
        "likelihood": 3,
        "impact": 5,
        "controls": "Badge vestibule + awareness + camera",
        "residual": "Moderate",
        "response": "Mitigate",
    },
    {
        "id": "R2",
        "asset": "production_build_server",
        "vulnerability": "A person may follow an employee through a restricted door unnoticed.",
        "threat": "Tailgating",
        "likelihood": 3,
        "impact": 5,
        "controls": "Badge reader + vestibule + door-open monitoring + camera",
        "residual": "Moderate",
        "response": "Mitigate",
    },
    {
        "id": "R3",
        "asset": "customer_data",
        "vulnerability": "Sensitive information may be visible on screens.",
        "threat": "Shoulder surfing",
        "likelihood": 3,
        "impact": 3,
        "controls": "Screen locks + privacy filters + workstation positioning",
        "residual": "Low",
        "response": "Mitigate",
    },
    {
        "id": "R4",
        "asset": "prototype_designs",
        "vulnerability": "Sensitive paper may enter ordinary trash.",
        "threat": "Dumpster diving",
        "likelihood": 3,
        "impact": 5,
        "controls": "Locked destruction bins + shredding + clean-desk policy",
        "residual": "Low",
        "response": "Mitigate",
    },
    {
        "id": "R5",
        "asset": "identity_access_system",
        "vulnerability": "A copied access badge could be presented.",
        "threat": "Card cloning",
        "likelihood": 2,
        "impact": 5,
        "controls": "Secondary verification + revocation + access-log monitoring",
        "residual": "Moderate",
        "response": "Mitigate",
    },
    {
        "id": "R6",
        "asset": "employee_endpoints",
        "vulnerability": "USB or device ports may be physically reachable.",
        "threat": "Unauthorized physical device or port access",
        "likelihood": 3,
        "impact": 4,
        "controls": "Restrict removable media + endpoint controls",
        "residual": "Moderate",
        "response": "Mitigate",
    },
    {
        "id": "R7",
        "asset": "power_infrastructure",
        "vulnerability": "Critical services depend on continuous power.",
        "threat": "Power or environmental disruption",
        "likelihood": 3,
        "impact": 5,
        "controls": "UPS + surge protection + selected generator support",
        "residual": "Moderate",
        "response": "Mitigate",
    },
    {
        "id": "R8",
        "asset": "robot_control_source",
        "vulnerability": "Credentials may be weak, reused, or compromised.",
        "threat": "Unauthorized digital access",
        "likelihood": 3,
        "impact": 5,
        "controls": "MFA + unique credentials + RBAC + least privilege",
        "residual": "Moderate",
        "response": "Mitigate",
    },
    {
        "id": "R9",
        "asset": "customer_data",
        "vulnerability": "Employees may be manipulated by deceptive messages.",
        "threat": "Social engineering",
        "likelihood": 4,
        "impact": 5,
        "controls": "Awareness + verification procedures + MFA + reporting",
        "residual": "Moderate",
        "response": "Mitigate",
    },
    {
        "id": "R10",
        "asset": "production_build_server",
        "vulnerability": "A critical service could be disrupted.",
        "threat": "Ransomware or service disruption",
        "likelihood": 3,
        "impact": 5,
        "controls": "Least privilege + protected backups + endpoint controls + recovery",
        "residual": "Moderate",
        "response": "Mitigate",
    },
]

# ============================================================
# 6. SECURITY CONTROL CATALOG + BUDGET
# ============================================================

INITIAL_BUDGET = 250_000

CONTROL_CATALOG = {
    "badge_vestibule": {
        "name": "Restricted-Area Badge/Vestibule Upgrades",
        "cost": 70_000,
        "type": "Physical",
        "function": "Preventative",
        "risks": ["R1", "R2", "R5"],
    },
    "camera_monitoring": {
        "name": "Camera + Door-Open Monitoring",
        "cost": 35_000,
        "type": "Physical",
        "function": "Detective",
        "risks": ["R1", "R2", "R5"],
    },
    "ups": {
        "name": "UPS + Surge Protection",
        "cost": 30_000,
        "type": "Technical",
        "function": "Preventative",
        "risks": ["R7"],
    },
    "generator": {
        "name": "Selected Generator Support",
        "cost": 45_000,
        "type": "Physical",
        "function": "Corrective",
        "risks": ["R7"],
    },
    "document_destruction": {
        "name": "Secure Document Destruction",
        "cost": 12_000,
        "type": "Managerial",
        "function": "Preventative",
        "risks": ["R4"],
    },
    "awareness": {
        "name": "Security Awareness + Visitor Procedures",
        "cost": 18_000,
        "type": "Managerial",
        "function": "Preventative",
        "risks": ["R1", "R9"],
    },
    "mfa": {
        "name": "MFA + Access-Control Improvements",
        "cost": 25_000,
        "type": "Technical",
        "function": "Preventative",
        "risks": ["R5", "R8", "R9"],
    },
    "endpoint": {
        "name": "Endpoint + Removable-Media Controls",
        "cost": 15_000,
        "type": "Technical",
        "function": "Preventative",
        "risks": ["R6", "R10"],
    },

    # These two alternatives intentionally cannot both fit into the
    # TitanTech model allocation. They create budget tradeoffs.
    "privacy": {
        "name": "Expanded Privacy-Filter Program",
        "cost": 10_000,
        "type": "Physical",
        "function": "Preventative",
        "risks": ["R3"],
    },
    "backup_upgrade": {
        "name": "Additional Backup/Recovery Upgrade",
        "cost": 28_000,
        "type": "Technical",
        "function": "Corrective",
        "risks": ["R10"],
    },
}

MODEL_PURCHASES = [
    "badge_vestibule",
    "camera_monitoring",
    "ups",
    "generator",
    "document_destruction",
    "awareness",
    "mfa",
    "endpoint",
]

budget_remaining = INITIAL_BUDGET
purchased_controls = []

# ============================================================
# 7. RUNTIME EVIDENCE
# ============================================================

EVENTS = []
ALERTS = []
INVESTIGATIONS = []
CONFIRMED_INCIDENTS = []

BASE_FOLDER = Path.cwd()
LOG_FILE = BASE_FOLDER / "titantech_security_log.txt"
REPORT_FILE = BASE_FOLDER / "titantech_executive_security_report.txt"

# ============================================================
# 8. UTILITY FUNCTIONS
# ============================================================

def line():
    print("-" * 72)


def pause():
    input("\nPress Enter to continue...")


def safe_int(prompt, minimum=None, maximum=None):
    """Safely request an integer from the user."""
    while True:
        raw = input(prompt).strip()

        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Value must be no greater than {maximum}.")
            continue

        return value


# ============================================================
# 9. COMPANY + INFRASTRUCTURE DISPLAY
# ============================================================

def display_company_profile():
    print("\nTITANTECH COMPANY PROFILE")
    line()

    print(f"Company:  {COMPANY['name']}")
    print(f"Industry: {COMPANY['industry']}")
    print(f"Mission:  {COMPANY['mission']}")
    print(f"Size:     {COMPANY['size']} employees")

    print("\nCRITICAL ASSETS")
    line()

    for key, asset in ASSETS.items():
        crown = "  [CROWN JEWEL]" if asset["crown_jewel"] else ""

        print(
            f"{asset['display']:<32} "
            f"CIA={asset['cia']:<16} "
            f"Value={asset['value']}{crown}"
        )


def display_infrastructure():
    print("\nTITANTECH INFRASTRUCTURE")
    line()

    print("\nPhysical Spaces:")
    for item in sorted(PHYSICAL_SPACES):
        print(f"  - {item}")

    print("\nDigital Resources:")
    for item in sorted(DIGITAL_RESOURCES):
        print(f"  - {item}")

    print("\nRole-Based Permissions:")
    line()

    for role, resources in PERMISSIONS.items():
        print(f"\n{role}")
        for resource in sorted(resources):
            print(f"  - {resource}")


# ============================================================
# 10. SECURITY EVENT LOGGING
# ============================================================

def log_security_event(
    user,
    resource,
    result,
    reason,
    category="Access"
):
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
                f"{event['category']} | "
                f"{event['user']} | "
                f"{event['resource']} | "
                f"{event['result']} | "
                f"{event['reason']}\n"
            )

    except OSError:
        # The simulation continues even if disk output is unavailable.
        pass

    return event


# ============================================================
# 11. ACCESS CONTROL
# ============================================================

def check_access(username, resource):
    username = username.lower().strip()
    resource = resource.lower().strip()

    if username not in EMPLOYEES:
        log_security_event(
            username,
            resource,
            "DENY",
            "Unknown user"
        )
        return False, "Unknown user"

    if resource not in ALL_RESOURCES:
        log_security_event(
            username,
            resource,
            "DENY",
            "Unknown resource"
        )
        return False, "Unknown resource"

    role = EMPLOYEES[username]["role"]
    allowed_resources = PERMISSIONS.get(role, set())

    if resource in allowed_resources:
        reason = f"Authorized for role: {role}"

        log_security_event(
            username,
            resource,
            "ALLOW",
            reason
        )

        return True, reason

    reason = f"Role not authorized: {role}"

    log_security_event(
        username,
        resource,
        "DENY",
        reason
    )

    return False, reason


def access_control_console():
    print("\nEMPLOYEE ACCESS CONTROL")
    line()

    print("\nEmployees:")
    for username, data in EMPLOYEES.items():
        print(
            f"  {username:<10} "
            f"{data['name']:<20} "
            f"{data['role']}"
        )

    print("\nResources:")
    for resource in sorted(ALL_RESOURCES):
        print(f"  - {resource}")

    username = input("\nUsername: ").strip()
    resource = input("Requested resource: ").strip()

    allowed, reason = check_access(
        username,
        resource
    )

    print("\nACCESS DECISION")
    line()

    print(
        "ACCESS GRANTED"
        if allowed
        else "ACCESS DENIED"
    )

    print(f"Reason: {reason}")

    if not allowed and username.lower() in EMPLOYEES:
        alert, message = detect_repeated_denials(
            username.lower()
        )

        if alert:
            print("\nDETECTION ALERT")
            print(message)


# ============================================================
# 12. RISK ASSESSMENT
# ============================================================

def assess_risk(likelihood, impact):
    """
    Classroom risk model.

    1-6   Low
    7-14  Moderate
    15-25 High

    This is a classroom model, not a universal industry standard.
    """

    if not isinstance(likelihood, int):
        return None, "Invalid likelihood"

    if not isinstance(impact, int):
        return None, "Invalid impact"

    if likelihood not in range(1, 6):
        return None, "Likelihood must be 1-5"

    if impact not in range(1, 6):
        return None, "Impact must be 1-5"

    score = likelihood * impact

    if score >= 15:
        level = "High"

    elif score >= 7:
        level = "Moderate"

    else:
        level = "Low"

    return score, level


def display_risk_register():
    print("\nTITANTECH RISK REGISTER")
    line()

    for risk in RISKS:
        score, level = assess_risk(
            risk["likelihood"],
            risk["impact"]
        )

        asset = ASSETS[risk["asset"]]["display"]

        print(f"\n{risk['id']} - {risk['threat']}")
        print(f"Asset:          {asset}")
        print(f"Vulnerability:  {risk['vulnerability']}")
        print(f"Likelihood:     {risk['likelihood']}")
        print(f"Impact:         {risk['impact']}")
        print(f"Risk Score:     {score}")
        print(f"Risk Level:     {level}")
        print(f"Response:       {risk['response']}")
        print(f"Controls:       {risk['controls']}")
        print(f"Residual Risk:  {risk['residual']}")


def interactive_risk_assessment():
    print("\nINTERACTIVE RISK ASSESSMENT")
    line()

    print(
        "Classroom model: likelihood and impact are each rated 1-5."
    )

    likelihood = safe_int(
        "Likelihood (1-5): ",
        1,
        5
    )

    impact = safe_int(
        "Impact (1-5): ",
        1,
        5
    )

    score, level = assess_risk(
        likelihood,
        impact
    )

    print("\nRESULT")
    line()

    print(f"Likelihood: {likelihood}")
    print(f"Impact:     {impact}")
    print(f"Score:      {score}")
    print(f"Risk Level: {level}")

    print(
        "\nThe number helps organize the assessment. "
        "The analyst must still justify the likelihood and impact."
    )


# ============================================================
# 13. POLICY ENGINE
# ============================================================

def display_policies():
    print("\nTITANTECH CORPORATE SECURITY POLICIES")
    line()

    for name, data in POLICIES.items():
        print(f"\n{name.upper()}")
        print(f"Policy:   {data['policy']}")
        print(f"Risk:     {data['risk']}")
        print(f"Controls: {data['controls']}")


# ============================================================
# 14. SECURITY BUDGET
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
            f"Purchase blocked. "
            f"Cost=${cost:,}; remaining=${budget_remaining:,}"
        )

    purchased_controls.append(control_key)
    budget_remaining -= cost

    return (
        True,
        f"Purchased {control['name']} for ${cost:,}. "
        f"Remaining=${budget_remaining:,}"
    )


def display_budget():
    print("\nTITANTECH SECURITY BUDGET")
    line()

    print(f"Initial Budget:   ${INITIAL_BUDGET:,}")
    print(f"Remaining Budget: ${budget_remaining:,}")

    print("\nCONTROL CATALOG")
    line()

    for key, control in CONTROL_CATALOG.items():
        status = (
            "PURCHASED"
            if key in purchased_controls
            else "AVAILABLE"
        )

        print(
            f"{key:<22} "
            f"${control['cost']:>7,}  "
            f"{control['type']:<10} "
            f"{control['function']:<11} "
            f"{status}"
        )


def security_budget_console():
    while True:
        display_budget()

        print(
            "\nEnter a control key to purchase, "
            "'model' for TitanTech's model allocation, "
            "'reset' to reset the budget, "
            "or press Enter to return."
        )

        choice = input("\nSelection: ").strip().lower()

        if choice == "":
            return

        if choice == "reset":
            reset_budget()
            print("Budget reset.")
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
# 15. DETECTION RULES
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
    username = username.lower().strip()

    count = sum(
        1
        for event in EVENTS
        if event["user"] == username
        and event["result"] == "DENY"
    )

    if count >= threshold:
        message = (
            f"{count} denied access attempts were recorded for "
            f"{username}. Investigate the activity and correlate "
            f"it with other evidence. This does NOT prove "
            f"malicious intent."
        )

        create_alert(
            "Repeated Denied Access",
            username,
            message
        )

        return True, message

    return (
        False,
        f"No alert. Denied attempts for {username}: {count}"
    )


def detect_possible_following(
    badge_entries,
    people_observed
):
    if people_observed > badge_entries:
        message = (
            "Observed entrants exceed recorded badge entries. "
            "Possible piggybacking or tailgating. Review access "
            "records and camera evidence. Current evidence does "
            "not establish whether the authorized person knowingly "
            "assisted the second person."
        )

        create_alert(
            "Restricted Door Entry Mismatch",
            "Restricted Door",
            message
        )

        return True, message

    return (
        False,
        "No entry-mismatch alert."
    )


def detect_document_exposure(
    sensitive_document_outside_secure_bin
):
    if sensitive_document_outside_secure_bin:
        message = (
            "Sensitive document observed outside the approved "
            "destruction process. Investigate document handling "
            "and possible exposure. This observation does not "
            "prove dumpster diving occurred."
        )

        create_alert(
            "Sensitive Document Exposure",
            "Records / Disposal",
            message
        )

        return True, message

    return (
        False,
        "No document-exposure alert."
    )


# ============================================================
# 16. SECURITY EVENT SIMULATOR
# ============================================================

def reset_evidence():
    EVENTS.clear()
    ALERTS.clear()
    INVESTIGATIONS.clear()
    CONFIRMED_INCIDENTS.clear()


def run_model_event_simulation():
    """
    Runs 12 fictional events.

    Some are normal.
    Some are suspicious.
    Detection does not automatically equal compromise.
    """

    reset_evidence()

    print("\nRUNNING TITANTECH MODEL EVENT SET")
    line()

    # Event 1: normal authorized digital access
    check_access("alex", "source_repo")

    # Events 2-4: repeated denied physical access
    check_access("alex", "server_room")
    check_access("alex", "server_room")
    check_access("alex", "server_room")

    # Detection rule 1
    detect_repeated_denials("alex")

    # Event 5: authorized physical access
    check_access("riley", "prototype_lab")

    # Event 6: denied digital access
    check_access("riley", "admin_console")

    # Event 7: unknown user
    check_access("unknown", "source_repo")

    # Event 8: normal facilities access
    check_access("taylor", "utility_room")

    # Event 9: receptionist denied sensitive digital access
    check_access("jordan", "design_files")

    # Event 10: physical entry mismatch
    log_security_event(
        "door_sensor",
        "prototype_lab",
        "OBSERVATION",
        "1 badge entry; 2 people observed",
        "Physical Detection"
    )

    detect_possible_following(
        badge_entries=1,
        people_observed=2
    )

    # Event 11: document exposure
    log_security_event(
        "employee_report",
        "records_room",
        "OBSERVATION",
        "Sensitive engineering paper found outside secure bin",
        "Physical Detection"
    )

    detect_document_exposure(True)

    # Event 12: normal physical entry relationship
    log_security_event(
        "door_sensor",
        "engineering_office",
        "NORMAL",
        "2 badge entries; 2 people observed",
        "Physical Detection"
    )

    detect_possible_following(
        badge_entries=2,
        people_observed=2
    )

    print(
        f"Simulation complete: "
        f"{len(EVENTS)} events, "
        f"{len(ALERTS)} alerts."
    )

    print(
        "\nRemember: alerts identify evidence that deserves "
        "analysis. They do not automatically prove an incident."
    )


def display_events():
    print("\nSECURITY EVENT LOG")
    line()

    if not EVENTS:
        print("No in-memory events recorded.")
        return

    for number, event in enumerate(EVENTS, start=1):
        print(
            f"{number:>2}. "
            f"{event['category']:<18} "
            f"{event['user']:<14} "
            f"{event['resource']:<20} "
            f"{event['result']:<11} "
            f"{event['reason']}"
        )


def display_alerts():
    print("\nDETECTION ALERTS")
    line()

    if not ALERTS:
        print("No alerts recorded.")
        return

    for number, alert in enumerate(ALERTS, start=1):
        print(f"\nAlert {number}")
        print(f"Rule:    {alert['rule']}")
        print(f"Subject: {alert['subject']}")
        print(f"Message: {alert['message']}")


# ============================================================
# 17. INCIDENT RESPONSE
# ============================================================

INCIDENT_RESPONSE_STAGES = [
    (
        "Preparation",
        "Maintain policies, controls, backups, contacts, and logging."
    ),
    (
        "Detection",
        "Identify an alert or employee report."
    ),
    (
        "Analysis",
        "Correlate logs, access records, camera evidence, user context, and affected assets."
    ),
    (
        "Containment",
        "Use safe defensive controls to limit supported exposure."
    ),
    (
        "Eradication",
        "Remove the confirmed cause where applicable."
    ),
    (
        "Recovery",
        "Restore normal operations and validate security."
    ),
    (
        "Lessons Learned",
        "Document evidence, decisions, gaps, and improvements."
    ),
]


def display_incident_response():
    print("\nTITANTECH INCIDENT RESPONSE")
    line()

    for stage, explanation in INCIDENT_RESPONSE_STAGES:
        print(f"\n{stage}")
        print(f"  {explanation}")

    print(
        "\nANALYST STANDARD:\n"
        "An alert is not automatically a confirmed incident."
    )


def investigate_alert():
    if not ALERTS:
        print(
            "\nNo alerts exist. Run the model event simulation first."
        )
        return

    display_alerts()

    alert_number = safe_int(
        "\nAlert number to investigate: ",
        1,
        len(ALERTS)
    )

    alert = ALERTS[alert_number - 1]

    print("\nINVESTIGATION")
    line()

    print(f"Rule:    {alert['rule']}")
    print(f"Subject: {alert['subject']}")
    print(f"Evidence: {alert['message']}")

    print(
        "\nPossible analyst decision:"
        "\n1. Continue investigation"
        "\n2. Treat as confirmed incident (teacher demo)"
        "\n3. Close as explained/benign"
    )

    decision = input("Decision: ").strip()

    if decision == "1":
        result = "Continue investigation"

    elif decision == "2":
        result = "Confirmed incident"
        CONFIRMED_INCIDENTS.append(alert.copy())

    elif decision == "3":
        result = "Closed as explained/benign"

    else:
        print("Invalid selection. No decision recorded.")
        return

    INVESTIGATIONS.append({
        "alert": alert.copy(),
        "decision": result,
    })

    print(f"Recorded decision: {result}")


# ============================================================
# 18. SECURITY AUDIT
# ============================================================

def audit_security():
    findings = []

    # Least privilege audit
    if "server_room" in PERMISSIONS.get(
        "Executive",
        set()
    ):
        findings.append({
            "severity": "High",
            "finding": (
                "Executive role has server-room access "
                "without demonstrated job need."
            ),
            "response": (
                "Modify architecture: remove access "
                "under least privilege."
            ),
        })

    # Policy completeness audit
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

    missing = required_policies - set(POLICIES)

    if missing:
        findings.append({
            "severity": "High",
            "finding": (
                "Missing required policies: "
                + ", ".join(sorted(missing))
            ),
            "response": (
                "Modify architecture: add missing "
                "policies and connect them to risks."
            ),
        })

    # Budget/control audit
    if purchased_controls:
        purchased = set(purchased_controls)

        if not (
            {"badge_vestibule", "mfa"}
            & purchased
        ):
            findings.append({
                "severity": "Moderate",
                "finding": (
                    "No purchased layered access-control "
                    "improvement protects high-value access paths."
                ),
                "response": (
                    "Modify or explicitly accept residual risk."
                ),
            })

        if not (
            {"ups", "generator", "backup_upgrade"}
            & purchased
        ):
            findings.append({
                "severity": "Moderate",
                "finding": (
                    "No purchased continuity/recovery "
                    "improvement is present."
                ),
                "response": (
                    "Modify or explicitly accept "
                    "availability risk."
                ),
            })

    else:
        findings.append({
            "severity": "Moderate",
            "finding": (
                "No security-budget controls have "
                "been purchased in this runtime."
            ),
            "response": (
                "Use the budget to prioritize controls "
                "or explicitly justify accepted risk."
            ),
        })

    if not findings:
        findings.append({
            "severity": "Informational",
            "finding": (
                "No programmed audit rule currently fails."
            ),
            "response": (
                "Do not claim zero risk. "
                "Document and monitor residual risk."
            ),
        })

    return findings


def display_audit():
    print("\nTITANTECH SECURITY AUDIT")
    line()

    findings = audit_security()

    for number, finding in enumerate(
        findings,
        start=1
    ):
        print(f"\nFinding {number}")
        print(f"Severity: {finding['severity']}")
        print(f"Issue:    {finding['finding']}")
        print(f"Response: {finding['response']}")


# ============================================================
# 19. EXECUTIVE SECURITY REPORT
# ============================================================

def risk_summary():
    summary = {
        "High": 0,
        "Moderate": 0,
        "Low": 0,
    }

    for risk in RISKS:
        _, level = assess_risk(
            risk["likelihood"],
            risk["impact"]
        )

        summary[level] += 1

    return summary


def control_summary():
    type_counts = {
        "Physical": 0,
        "Technical": 0,
        "Managerial": 0,
    }

    function_counts = {
        "Preventative": 0,
        "Detective": 0,
        "Corrective": 0,
    }

    for key in purchased_controls:
        control = CONTROL_CATALOG[key]

        type_counts[control["type"]] += 1
        function_counts[control["function"]] += 1

    return type_counts, function_counts


def generate_executive_report():
    risks = risk_summary()
    type_counts, function_counts = control_summary()
    findings = audit_security()

    crown_jewels = [
        asset["display"]
        for asset in ASSETS.values()
        if asset["crown_jewel"]
    ]

    lines = [
        "TITANTECH ADVANCED SYSTEMS",
        "EXECUTIVE SECURITY REPORT",
        "=" * 72,
        "",
        "CROWN-JEWEL ASSETS",
    ]

    for asset in crown_jewels:
        lines.append(f"- {asset}")

    lines += [
        "",
        "RISK SUMMARY",
        f"High:     {risks['High']}",
        f"Moderate: {risks['Moderate']}",
        f"Low:      {risks['Low']}",
        "",
        "SECURITY BUDGET",
        f"Initial:   ${INITIAL_BUDGET:,}",
        f"Remaining: ${budget_remaining:,}",
        f"Spent:     ${INITIAL_BUDGET - budget_remaining:,}",
        "",
        "PURCHASED CONTROLS",
    ]

    if purchased_controls:
        for key in purchased_controls:
            control = CONTROL_CATALOG[key]

            lines.append(
                f"- {control['name']} "
                f"({control['type']} / "
                f"{control['function']})"
            )
    else:
        lines.append("- None in current runtime")

    lines += [
        "",
        "CONTROL COVERAGE",
        f"Physical:   {type_counts['Physical']}",
        f"Technical:  {type_counts['Technical']}",
        f"Managerial: {type_counts['Managerial']}",
        f"Preventative: {function_counts['Preventative']}",
        f"Detective:    {function_counts['Detective']}",
        f"Corrective:   {function_counts['Corrective']}",
        "",
        "SECURITY EVIDENCE",
        f"Events:              {len(EVENTS)}",
        f"Alerts:              {len(ALERTS)}",
        f"Investigations:      {len(INVESTIGATIONS)}",
        f"Confirmed Incidents: {len(CONFIRMED_INCIDENTS)}",
        "",
        "AUDIT FINDINGS",
    ]

    for finding in findings:
        lines.append(
            f"- [{finding['severity']}] "
            f"{finding['finding']}"
        )

    lines += [
        "",
        "RESIDUAL RISK",
        (
            "Controls reduce risk but do not eliminate "
            "credential compromise, human error, control failure, "
            "environmental disruption, or sophisticated adversary activity."
        ),
        "",
        "ANALYST STANDARD",
        (
            "Evidence supports investigation. "
            "An alert does not automatically prove "
            "compromise or malicious intent."
        ),
    ]

    report = "\n".join(lines)

    try:
        REPORT_FILE.write_text(
            report,
            encoding="utf-8"
        )

    except OSError:
        pass

    return report


# ============================================================
# 20. AUTOMATED TEACHER TEST SUITE
# ============================================================

def run_teacher_test_suite():
    """
    Tests important student-facing behavior.

    This is not a proof that every possible path is perfect,
    but it verifies the core requirements demonstrated here.
    """

    print("\nTITANTECH AUTOMATED TEST SUITE")
    line()

    reset_evidence()
    reset_budget()

    results = []

    def record(
        test_id,
        description,
        actual,
        expected
    ):
        passed = actual == expected
        results.append(passed)

        print(
            f"{'PASS' if passed else 'FAIL'} | "
            f"{test_id:<4} | "
            f"{description}"
        )

        if not passed:
            print(
                f"       Expected: {expected!r}"
                f"\n       Actual:   {actual!r}"
            )

    # T01 Authorized physical access
    record(
        "T01",
        "Authorized physical access",
        check_access(
            "riley",
            "prototype_lab"
        )[0],
        True
    )

    # T02 Denied physical access
    record(
        "T02",
        "Denied physical access",
        check_access(
            "alex",
            "server_room"
        )[0],
        False
    )

    # T03 Authorized digital access
    record(
        "T03",
        "Authorized digital access",
        check_access(
            "alex",
            "source_repo"
        )[0],
        True
    )

    # T04 Denied digital access
    record(
        "T04",
        "Denied digital access",
        check_access(
            "riley",
            "admin_console"
        )[0],
        False
    )

    # T05 Unknown user
    record(
        "T05",
        "Unknown user fails closed",
        check_access(
            "nobody",
            "source_repo"
        )[0],
        False
    )

    # T06 Unknown resource
    record(
        "T06",
        "Unknown resource fails closed",
        check_access(
            "alex",
            "moon_base"
        )[0],
        False
    )

    # T07 Invalid risk input
    record(
        "T07",
        "Invalid risk input rejected",
        assess_risk(9, 2)[0],
        None
    )

    # T08 Low risk
    record(
        "T08",
        "Low risk classification",
        assess_risk(2, 2)[1],
        "Low"
    )

    # T09 Moderate risk
    record(
        "T09",
        "Moderate risk classification",
        assess_risk(3, 3)[1],
        "Moderate"
    )

    # T10 High risk
    record(
        "T10",
        "High risk classification",
        assess_risk(4, 5)[1],
        "High"
    )

    # T11 Repeated denied access alert
    check_access("jordan", "server_room")
    check_access("jordan", "server_room")
    check_access("jordan", "server_room")

    record(
        "T11",
        "Repeated denials generate alert",
        detect_repeated_denials(
            "jordan"
        )[0],
        True
    )

    # T12 Normal physical activity does not alert
    record(
        "T12",
        "Normal entry count does not alert",
        detect_possible_following(
            2,
            2
        )[0],
        False
    )

    # T13 Physical mismatch alerts
    record(
        "T13",
        "Entry mismatch generates alert",
        detect_possible_following(
            1,
            2
        )[0],
        True
    )

    # T14 Document exposure alerts
    record(
        "T14",
        "Sensitive document exposure alerts",
        detect_document_exposure(
            True
        )[0],
        True
    )

    # T15 Valid budget purchase
    record(
        "T15",
        "Valid purchase succeeds",
        purchase_control(
            "badge_vestibule"
        )[0],
        True
    )

    # T16 Duplicate purchase blocked
    record(
        "T16",
        "Duplicate purchase blocked",
        purchase_control(
            "badge_vestibule"
        )[0],
        False
    )

    # Fill budget with model controls after reset.
    reset_budget()

    for control in MODEL_PURCHASES:
        purchase_control(control)

    record(
        "T17",
        "Model allocation spends full budget",
        budget_remaining,
        0
    )

    # T18 Overspend blocked
    record(
        "T18",
        "Overspend blocked",
        purchase_control(
            "backup_upgrade"
        )[0],
        False
    )

    # T19 Audit returns findings/list
    record(
        "T19",
        "Audit produces output",
        isinstance(
            audit_security(),
            list
        ),
        True
    )

    # T20 Executive report
    report = generate_executive_report()

    record(
        "T20",
        "Executive report generated",
        (
            "EXECUTIVE SECURITY REPORT"
            in report
        ),
        True
    )

    print()
    line()

    passed = sum(results)
    total = len(results)

    print(
        f"RESULT: {passed}/{total} tests passed."
    )

    if passed == total:
        print(
            "Core TitanTech reference behaviors passed."
        )

    else:
        print(
            "One or more core behaviors require review."
        )

    return passed == total


# ============================================================
# 21. DEMO MODE
# ============================================================

def run_full_teacher_demo():
    """
    Gives the teacher a predictable classroom demonstration.
    """

    print("\nTITANTECH FULL TEACHER DEMO")
    line()

    reset_budget()

    print(
        "\n1. Loading TitanTech's model "
        "$250,000 security allocation..."
    )

    for control in MODEL_PURCHASES:
        success, message = purchase_control(
            control
        )

        print(message)

    print(
        "\n2. Running TitanTech's fictional "
        "security event set..."
    )

    run_model_event_simulation()

    print(
        "\n3. Running security audit..."
    )

    display_audit()

    print(
        "\n4. Generating executive report..."
    )

    report = generate_executive_report()

    print()
    print(report)

    print(
        f"\nReport file: {REPORT_FILE}"
    )

    print(
        f"Event log file: {LOG_FILE}"
    )


# ============================================================
# 22. MAIN MENU
# ============================================================

def main():
    while True:
        print(
            """
========================================================================
 TITANTECH ADVANCED SYSTEMS
 CYBERSECURITY MANAGEMENT SYSTEM
========================================================================

 1. Company Profile & Critical Assets
 2. Facility / Digital Infrastructure
 3. Employee Access Control
 4. Corporate Security Policies
 5. Risk Register
 6. Interactive Risk Assessment
 7. Security Budget
 8. Run Model Security Event Simulation
 9. View Security Event Log
10. View Detection Alerts
11. Incident Response
12. Investigate an Alert
13. Security Audit
14. Executive Security Report
15. Run Automated Teacher Test Suite
16. Run Full Teacher Demo
 0. Exit

Cybersecurity reasoning:
Asset -> Vulnerability -> Threat -> Likelihood -> Impact -> Controls -> Justification
Event -> Detection -> Alert -> Investigation -> Decision
"""
        )

        choice = input(
            "Select an option: "
        ).strip()

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

            print("\n")
            print(report)

            print(
                f"\nSaved to: {REPORT_FILE}"
            )

            pause()

        elif choice == "15":
            run_teacher_test_suite()
            pause()

        elif choice == "16":
            run_full_teacher_demo()
            pause()

        elif choice == "0":
            print(
                "\nTitanTech Cybersecurity "
                "Management System closed."
            )
            break

        else:
            print(
                "\nInvalid selection. "
                "Choose a menu option."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
