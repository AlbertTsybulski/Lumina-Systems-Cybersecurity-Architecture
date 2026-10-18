**UNIT 2 CAPSTONE — STUDENT REPORT TEMPLATE**

*Build & Defend a Company in Python • Cybersecurity Architecture & Risk Report*

Student(s): [REDACTED]

 Company: **Lumina** **Systems**		  Class/Period: [REDACTED]

**This template is a roadmap, not a worksheet to answer with one-line responses. Replace bracketed prompts with complete analysis, tables, diagrams, and evidence from YOUR fictional company and Python program.**

Required reasoning: Asset → Vulnerability → Threat → Likelihood → Impact → Controls → Justification

Detection reasoning: Event → Detection → Alert → Investigation → Decision

# **How to Use This Template**

* Write approximately 8–12 substantive pages, plus diagrams and appendices.  
* Delete instructional prompts before final submission.  
* Do not paste your entire Python source code into the report. Refer to important data structures/functions and explain what they implement.  
* Every major security decision should answer: What did we decide? Why? Where does our Python program implement it?  
* Evidence does not automatically equal conclusion. Explain what an event supports and what cannot yet be concluded.

# **1\. Executive Summary**

\[In 1–3 paragraphs: What does your company do? What are its three crown jewels? What are its highest-priority risks? What major security strategy did your team choose? What important residual risk remains?\]

Lumina Systems is a company with 10,000 employees that focuses on artificial intelligence (AI) and cybersecurity. Its goal is to develop advanced AI and create systems that can complete tasks independently. The company’s security program focuses on protecting its customer data, important computer systems, and intellectual property. Its three most valuable assets are its AI threat detection models, its core source code, and its patents and encryption technology. 

The biggest risks to Lumina Systems include hackers stealing its technology, employees leaking sensitive information, and security problems caused by third-party software. These threats could damage the company’s operations and reputation.

To protect itself, Lumina uses a Zero-Trust security system. This means every user, device, and service must prove its identity before accessing important systems. The company also uses security keys, network protections, and automated threat detection. However, some risks remain, such as new software vulnerabilities, attacks targeting its AI models, and employees misusing their access without being detected.

 

Do not turn this section into a list of every feature. Write for an executive audience.

# **2\. Company & Security Architecture**

| Role | Primary business/security need |
| :---- | :---- |
| Receptionist | Handle incoming employees and the lobby. They have no server access. |
| Frontier Research | Responsible for inventing new model architectures and theoretical frameworks that push beyond narrow AI. |
| AI Governance | Ensures AI remains controllable and aligned with human intent. Makes sure the AI does not break out of its environment and accesses sensitive company data |
| Core Algorithm Coding | Writes the main source code for the AGI and defines the main neural network. Translates theory in practicality. |
| Executive | Business systems and offices where they do not need server access. They sell their AGI to clients so they can chat with the AI. |
| Human Evaluator | Ensure that the AI is learning properly in the way that we intended it. Ensuring the AI is not learning the wrong information and is being correctly rewarded. |

![][image1]

The facility contains a lobby, an office, server room, SOC room, records room, and utility/power room. The lobby is meant for the general public to enter and where employees can enter and scan their employee id cards in order to enter the main building. The other rooms are restricted to employees only because they contain crown-jewel assets which would cause critical damage if compromised.

Our model includes a source code repository for the main AI engineers, a visitor system to manage visitors, business system, admin console, a production build server for compiling code into executable computer binaries, and a main messaging hub for everyone in the company with sub channels for more specific conversations. Roles are given out based on the person’s qualifications and if they can serve the business the best.![][image2]

# **3\. Asset Inventory & CIA Analysis**

\[Identify at least 8 assets and clearly mark 3 crown jewels. For major assets, identify the most important CIA concern and justify it.\]

| Asset | Value | Primary CIA Concern | Reason |
| :---- | :---- | :---- | :---- |
| Security Logs/Videos | Moderate | Integrity  | It ensures that data remains accurate and trustworthy. |
| AI Power Infrastructure  | High  | Availability  | Critical systems and AI algorithms need continuous power supply. |
| Customer Data | High  | Confidentiality  | Customer dialogues and chats with AI need to be protected to ensure safety because the chats could contain sensitive information. |
| Core Source Code and Detection Engines | High / Crown Jewel | Integrity  | Unauthorized access to the source code could alter software and product behaviors. Detection engines are needed to check possible technical or human errors. |
| Proprietary Threat Intelligence & Behavior Models | High / Crown Jewel | Confidentiality | Proprietary threat intelligence and behavior models represent a company's special intellectual property (IP) and competitive advantage. These assets need to be protected from unauthorized parties. |
| Patent Portfolios & Cryptographic IP  | High / Crown Jewel | Confidentiality | Patent portfolios need to be confidential before publication because they contain trade secrets and strategies. Cryptographic IP requires enduring protection to prevent security failures. |
| Production Servers | High  | Availability | Software services and large amounts of data storage need servers to run. |
| Employee Access Endpoints | Moderate | Confidentiality | Employees could leak company information if improperly accessed. Different layers of access need to be established for security. |

# **4\. Risk Assessment/5. Physical Security Analysis**

\[Explain your risk-rating method. If using numbers, state that your thresholds are your classroom/company model, not a universal industry standard.\]

\[Complete the risk register below. Include at least 8 risks and both physical and digital risk.\]

**Risk-rating method:** Lumina Systems uses a classroom risk model that rates likelihood and impact as Low, Moderate, or High. Overall risk is determined by considering both factors, with High likelihood and High impact producing a High or Critical priority. These ratings are estimates for our fictional company, not a universal industry standard. Residual risk represents the risk remaining after controls are implemented.

## **Risk Register**

We have IDs starting from 11 and up to label the risks

| ID | Asset | Vulnerability | Threat | Likelihood | Controls |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 11 | Security Logs/Videos | Attackers can insert malicious code or fake entries into logs; Many IP cameras use weak passwords and outdated firmware. | Fake security entries and useless security videos increase the chance of compromises and information leak. This would be **physical device access**. | High | Use MFA \+ mandated strong passwords for IP cameras; Manage logs in a secured and centralized system. Residual: moderate |
| 12 | Office Desktops | An employee leaves their computer open while going on a bathroom break | An attacker could go to the open computer and quickly steal any data which can be vital source code. This would be **piggybacking** | Moderate | Raise awareness for this risk and tell employees to lock their computer to protect company and personal data. Residual risk: moderate |
| 13 | Power Infrastructure | Stress from extreme weather and increasing electricity demand. | Severe storms, heat waves, and flooding can damage above ground transmission lines, blow transformers, and trigger blackouts. This would be an **environmental disruption**. | Moderate | Upgrade stronger materials, bury selected critical lines in high-risk areas, and use drones and AI analysis to spot any weaknesses. Residual: low |
| 14 | Garbage and Dumpsters | Throwing out packages can show what the company has inside. | An attacker can see what the company is buying and potentially see serial codes and manufacturing information about the product. They could use this to possibly hack that device, this is **dumpster diving**. | Moderate | Ensure anything thrown out has been broken down or any labels have been properly ripped off. The residual risk would be low |
| 15 | Entrance Door | Suspicious people can slip in through usually locked doors when an employee goes through them. | Unauthorized access can allow an adversary to steal any tangible assets or possibly software. This would be an example of **tailgating** | High | Replace locked doors with key scanners where a person can only access an area with an employee card. The door would close immediately after the person passes and security by the lobby can watch over the doors. Residual risk would be low |
| 16 | Corporate Facilities Checkpoints | An employee's access badge could be cloned by attackers using skimming devices to read the radio frequency signal of the badge. | The cloned card allows attackers to have the exact digital twin of the access badges, enabling attackers to bypass physical security checkpoints. This would be an example of **card cloning**. | Moderate | Use multi-factor authentication with biometrics scanners and a unique personal identification number alongside badge scan. Moreover, the company should segment the facilities into sections with different levels of accessibility. Residual: moderate |
| 17 | Open Laptops/Desktops | An employee may have a large monitor and a person who may have sneaked in can record or watch their screen. | The attacker can watch the employee input confidential information or watch the employee pull up blueprints. This would be an example of **shoulder surfing**. | Low | This could be fixed with the same method used for tailgating where they stop before they enter. If they still enter the building, there can be more employee access doors to heavily restricted spaces. |
| 18 | Core Source Code | Dev endpoints using static API keys | An attacker can compromise developer credentials to inject malicious backdoors into the AGI build line. This would be **code tampering**. | Moderate | Require YubiKeys for all code commits and repository keys with hardware security module for cryptographic signing of build releases. Residual risk: Low |

# **6\. Access Control Design**

Authentication verifies the person trying to access the system while authorization allows the person to access a certain aspect of the system. Examples of authentication would be touch pads and employee cards which are scanned. Examples include checking a login attempt to make sure the user is allowed.

Our company uses role based access control. Authentication authorizes the user based on their role and whether or not the role fits the area they are trying to access. The \[input function here\] checks the user’s role and sees if they are allowed to access that specific system.

| User | Resource | Physical/Digital | Decision | Justification |
| :---- | :---- | :---- | :---- | :---- |
| Alex/Core Algorithm coding | Source Code  | Digital | Allow | The core software engineers are allowed to access the source code repo and change it. |
| Riley/Receptionist | Server Room | Physical | Deny | The receptionist is not allowed to access the server room.  |
| Mark/Frontier Research | Admin Console | Digital | Deny | Training AI models does not need administrative access. |
| Sam/AI governance | Audit Logs | Digital | Allow | Compliance officers require visibility into security logs to audit AI safety. |
| Jordan/Executive | Utility room | Physical | Deny | Corporate leadership does not perform maintenance  |

\[Code connection: identify the structures/functions that enforce permissions.\]

# **7\. Corporate Security Policies**

\[Explain policies for physical access, visitors/vendors, workstations, authentication/authorization, removable media, document disposal, power/continuity/recovery, and monitoring/reporting.\]

Physical security: All restricted rooms such as the server room, SOC, records room, power/utility room require employee badges or biometrics such as hand prints to be accessed. Lobby doors use scanners to close automatically after each entry. Security guards monitor entrances and verify visitor badges. High value areas such as the AI mode lab require two-person rule entry. This is a physical type with preventative functions.

Visitor and Vendor Policy: Visitors must be pre-registered in the visitor management system. Reception issues temporary badges with limited access. Visitor logs are retained for one year and monitored by the SOC team.

Workstation: All employee endpoints auto-lock after 3 minutes of inactivity. Screen privacy filters are mandatory in open areas. USB ports are restricted except for approved devices. 

Authentication And authorization: MFA is required for all internal systems. RBAC determines access to source code, AI models, and production servers. Privilege escalation requires manager approval and SOC logging. This is a technical type with preventative functions.

Removable Device Policy: Sensitive data cannot be copied to removable storage devices under any circumstances unless given explicit permission. Exceptions require SOC approval and automatic malware scanning.

# **8\. \$250,000 Security Budget & Risk Management**

\[Explain how your team allocated the fictional \$250,000. What did you buy? What did you defer/reject? Why?\]

\[Connect each major purchase to one or more risks. Explain residual risk after the purchase.\]

\[Discuss Avoid, Transfer, Mitigate, and Accept where appropriate. Do not claim that buying a control eliminates all risk.\]

| Item | Cost | Status | Risk Response | Primary Function | Residual Risk |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Smart Gate mantraps and biometric scanners | 85,000 | Bought | Mitigate | Replaces standard doors with dual doors to ensure only authorized personnel can enter. Prevents physical card cloning and tailgating | Low risk because it reduces tailgating greatly but forced entry or social engineering is still possible. |
| Hardware Keys and Hardware Security Module | 62,000 | Bought | Mitigate | YubiKeys are given to all 10000 employees plus a network Hardware Security Module for signing production build releases and securing GPG commit keys. | Low risk because hardware keys eliminate credential phishing but insider misuse by an authenticated developer remains as a risk. |
| Centralized SIEM Engine and WORM storage | 48,000 | Bought | Mitigate | Deploys centralized log aggregation with WORM storage which replaces security logs and automatically pulls all event records into one unified platform into a storage that cannot be changed by anyone. | Moderate risk because it ensures tamper-proof logging though log latency presents minor operational window risks. |
| Polarized Privacy Filters and CCTV upgrade | 30,000 | Bought | Mitigate | Gives high risk workstations with privacy screens and upgrade perimeter waste storage areas with locked enclosures and high definition cameras. | Low risk because shoulder surfing is restricted to direct viewing angles to be more suspicious. Physical document theft is restricted but visual leaks via cameras from exterior locations remain. |
| Cyber Liability and IP theft insurance policy | 25,000 | Bought | Transfer | Transfers non mitigatable financial exposure(potential loss that cannot be reduced) to a third party underwriter | Provides financial recovery but cannot restore stolen algorithms one leaked. |
| Third-Party Automated Red-Teaming Suite  | 0 | Reject | Avoid | Automated red teaming software was rejected due to high costs and capabilities were built in-house to save money. | Moderate risk because In-house scripts cover known internal attacks but lack niche scenarios provided by commercial suites.  |
| Underground Utility Line Re-Wiring  | 0 | Defer | Accept | Burying power utility lines to prevent weather blackouts exceeded the budget. The risk was accepted while leveraging existing generators and UPS backups.  | Moderate risk because extended utility blackouts exceeding generator fuel reserves will force non-essential secondary compute nodes offline.  |
| Dual Flywheel UPS for Secondary Racks  | 0 | Reject | Accept | Installing battery units to bridge the brief generator cutover gap for secondary test racks was rejected. Capital was prioritized for primary AGI crown jewels instead.  | Low risk because secondary test servers experience a brief  reboot during power grid cutovers, requiring researchers to restart non-critical test scripts.   |
| Complete Physical Security Perimeter Guard Detachment | 0 | Defer | Mitigate | Hiring 24/7 guards was deferred because reliance was placed on automated optical speed gates, biometric man-traps, and lobby staff instead. | Low risk: Automated doors prevent unauthorized physical entry, but physical response time during an active intrusion relies on local law enforcement dispatch.  |
| Full Air-Gapping of all Research Workstations | 0 | Reject | Accept | Completely isolating research workstations from the internet was rejected since researchers need external resources in order to conduct research. | Moderate risk: Internet access allows research productivity but introduces dangerous paths where hackers can steal sensitive company data |

# **9\. Detection & Monitoring**

\[Describe at least 12 fictional events and at least 3 detection rules.\]

Lumina Systems maintains a central Security Operations Center (SOC) running automated SIEM (Security Information and Event Management) and physical access control systems to monitor digital endpoints and physical facilities.

| Rule | Description |
| :---- | :---- |
| Rule 1: Repeated Authentication Failure | Triggers when a user or service account experiences 5 or more authentication attempts within 3 minutes. |
| Rule 2: Identity Mismatch | Triggers when a badge scan and biometric scan do not match or if the privileges are insufficient. |
| Rule 3: Core Source Code Theft | Triggers when an unauthorized account attempts to download or transfer 100 MB or more of source code repositories outside standard business hours. |

| Event | Timestamp | Category | Source | Action / Event Description | Expected System Response |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 08:15:22 | Physical | Receptionist (Riley) | Swiped employee badge at Lobby entrance  | Access allowed because it was during normal business hours. |
| 2 | 08:32:04 | Digital  | Senior Engineer (Alex) | Logged into source code repository using a secured and authorized USB stick. | Access allowed because it was accessed by an authorized user within business hours. |
| 3 | 09:12:45 | Physical | Receptionist  (Riley) | Swiped badge at server room reader. | Access denied because a receptionist doesn’t have access to the server room.  |
| 4 | 09:12:51 | Physical  | Receptionist (Riley) | Attempted second badge swipe at Server Room door reader immediately after event 3\. | Access denied and logged into the system. |
| 5 | 09:13:02 | Physical  | Receptionist (Riley) | Attempted third badge swipe at Server Room reader. | Access denied and triggered rule 1 because of consecutive failed attempts.  |
| 6 | 11:45:10 | Digital | Reseacher (Mark) | Attempted login to admin console from office desktop. | Access denied because of insufficient privileges (rule 2).  |
| 7 | 13:20:00 | Physical | Unknown Individual | Entered smart gate mantrap behind an authorized employee without completing secondary biometric scan. | Mantrap doors locked and triggered rule 2\. |
| 8 | 14:05:30 | Physical | AI Governance Staff | Inserted unapproved USB flash drive into workstation USB port. | Endpoint security blocks port and quarantines device interface. |
| 9 | 22:30:15 | Physical | Third-Party Janitorial Staff | Routine after-hours cleaning sweep in the open office area, walking past work stations. | Normal Activity because the action is whitelisted, and an authorized badge is used under security cameras. Therefore, it does not trigger an alert. |
| 10 | 01:14:40 | Digital | Insider | Initiated transfer of 450MB of core source code archives to an unidentified external cloud storage bucket. | Triggered rule 3 and data loss prevention staff intervened immediately to prevent data leak.  |
| 11 | 02:00:00 | Physical  | Automated Power Infrastructure Monitor | Periodic health check for the power infrastructure and cooling grid. | The result was normal and thus no alert. |
| 12 | 04:30:12 | Digital | Automated Security system check | Automatic backup of daily Security Operations Center video logs to immutable storage which prevents files from being modified. | No alert and logged the status of success confirmation. |

\[Include repeated denied access, a physical-security detection scenario, and normal activity that should NOT alert.\]

\[For each important alert: what evidence triggered it? What does it suggest? What does it NOT prove? What should the analyst investigate next?\]

Repeated Authentication Failures (Events 3 to 5):  Three consecutive failed physical badge scans within a 45-second window. It suggests either an honest mistake or a lost badge being tested by an unauthorized individual. It does not prove a malicious cyberattack or card cloning. The analyst should review lobby security camera footage corresponding to the timestamps of 3 to 5 visually.

Physical Security Breach (Event 7): Smart Gate mantrap sensors detected two thermal signatures inside the safety airlock chamber while only one valid biometric and badge credential was authenticated. It suggests an unauthorized individual attempted to slip through right behind an authorized employee (tailgating or piggybacking) to bypass the main security checkpoint. It does not prove malicious intent, nor does it prove that the intruder successfully penetrated the inner facility, as the mantrap doors were held and locked. The analyst should immediately dispatch on-duty security guards to the specific mantrap location, review security cameras feeds for that gate, and question the authorized employee who scanned in.

Core Source Code Theft (Event 10): An unusual data transfer of 450 MB originating from a non-engineering workstation/account accessing core source code repositories during off-peak hours (1:14 AM). It suggests potential insider threat and  data exfiltration, compromised credentials of a privileged account, or an unauthorized automated script attempting to steal Lumina's crown jewel source code. It does not prove that the data successfully left the corporate perimeter (since it was intercepted and got blocked), nor does it prove whether it was an intentional malicious act or an authorized emergency backup by a legitimate admin working staff. The analyst should immediately isolate the source endpoint from the network, check recent authentication logs for session anomalies and contact the employee assigned to the account to verify their activity.

\[Code connection: identify the functions/rules that create alerts.\]

# **10\. Incident Response**

\[Explain how your company uses Preparation → Detection → Analysis → Containment → Eradication → Recovery → Lessons Learned.\]

\[Walk through at least one alert. Show how analysis occurs before a confirmed-incident decision.\]

Lumina Systems follows a simple, 7-step process to handle security issues. Our main goal is to protect our crown jewels (our AI source code, threat intelligence, and patents) while making sure we don't jump to conclusions without checking the facts first.

7 Steps:

1. Preparation   
* **What we do:** We set up automated monitoring and tamper-proof logging *before* anything goes wrong  
* **Why:** So we have accurate records whenever suspicious activity happens  
2. Detection  
* **What we do:** Automated security rules constantly watch for strange activity.  
* **Why:** Humans can't watch 10,000 employees manually; software flags potential problems instantly  
3. Analysis   
* **What we do:** Security analysts investigate alerts to see if a real attack is happening or if it's just a mistake.  
* **Why:** An alert doesn't automatically mean an attack is occurring—it could be an employee making an error or working late  
4. Containment  
* **What we do:** Once a breach is confirmed, we instantly block the attacker from spreading further.  
* **Why:** Stopping lateral movement protects our core AI source code from being stolen  
5. Eradication  
* **What we do:** We remove all malware, unauthorized access keys, and backdoors left by the attacker.  
* **Why:** To make sure the attacker cannot simply log back in later  
6. Recovery  
* **What we do:** We safely restore systems using clean, verified backups and bring services back online carefully.  
* **Why:** Restoring too fast could reintroduce corrupted files or hidden backdoors  
7. Lessons Learned  
* **What we do:** After every major incident, the team holds a review meeting to discuss what happened and how to improve.  
* **Why:** This helps us update our defenses so the exact same attack can't happen twice

# **11\. Security Audit & Remediation**

\[List meaningful audit findings. For each, choose and justify: Accept finding / Dispute with evidence / Modify architecture / Accept residual risk.\]

\[Explain at least one design decision you changed after testing or auditing.\]

| Finding ID | Audit Finding and Observation | Asset Impacted | Risk | Selected | Justification and Remediation Action |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AUD-01 | Unencrypted telemetry stream | Security Logs | High | Modify Architecture | We update edge firmware to enforce encryption on all video telemetry |
| AUD-02 | Simultaneous Dual-Enclave Login Flaw where the person already left but it shows they’re still digitally active meaning another person can manipulate the session without the dev monitoring. | Core Source Code | Critical | Modify Architecture | Updated out code to ingest real-time badge event streams, reducing session evaluation latency to milliseconds and terminating digital activity upon physical exit |
| AUD-03 | Alleged Yubikey session hijacking where the yubikey could be bypassed if a dev’s workstation was physically stolen while a session remained active. | Employee Access Endpoints | Moderate | Dispute with Evidence | Now it requires physical touch on the yubi key for every individual cryptographic operation |
| AUD-04 | Single Grid Power Dependency for Secondary Server Enclaves: non essential servers will temporarily lose power when backup turns on because of a delay | Production Servers | Low | Accept Residual Risk | The cost to install additional industrial grade flywheel would exceed our budgets so we decided to accept the minor delay  |

# **12\. Final Security Assessment**

\[What is best protected in your design? What remains most exposed? What important residual risks remain?\]

\[If you received additional budget/time, what would you improve next and WHY? Base the recommendation on your company’s evidence and risk, not on a generic “best” control.\]

Lumina Systems protects its three most important assets: its source code, AI threat intelligence, and patents. We use hardware security keys, access controls, security cameras, and monitoring systems to reduce the risk of cyberattacks and physical break-ins. However, no security system can prevent every attack.

Our biggest remaining risks are employees misusing their access, stolen computers, third-party software vulnerabilities, and power outages. Our security systems may reduce these risks, but they cannot eliminate them completely.

If we had more money and time, we would improve session security, monitor suspicious employee activity, and conduct more security testing. We would also improve backup power for our servers. These changes would help protect our most valuable assets and reduce the risks identified in our security audit. 

# **Required Working Tables**

# **Appendix A — Required Testing Evidence**

Document at least 15 meaningful tests. Your final table may be longer.

| Test ID | Input / Action | Expected | Actual | Pass/Fail | Fix made |
| :---- | :---- | :---- | :---- | :---- | :---- |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

# **Appendix B — Program Evidence**

* Attach or reproduce a representative security event log.  
* Attach your program-generated executive security report.  
* Include any additional output needed to prove required features work.

# **Final Pre-Submission Check**

| Check | Requirement |
| :---- | :---- |
| ☐ | Python source file(s) run without known classroom-blocking errors |
| ☐ | README explains how to run the program |
| ☐ | 8–12 substantive-page written report completed |
| ☐ | Facility/floor-plan diagram included |
| ☐ | Digital infrastructure diagram included |
| ☐ | 3 crown jewels and CIA analysis included |
| ☐ | 8+ risks with residual risk included |
| ☐ | All required physical-security categories addressed |
| ☐ | \$250,000 budget and tradeoffs justified |
| ☐ | 12+ events and 3+ detection rules documented |
| ☐ | Incident response and audit/remediation documented |
| ☐ | 15+ tests with expected vs. actual results included |
| ☐ | Sample event log and executive output included |
| ☐ | Every team member is ready for the live defense |