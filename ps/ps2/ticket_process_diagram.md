# Chicago Parking Ticket Process Diagrams

## Diagram 1: notice_level Process Flow

```mermaid
graph TD
    A[Ticket Issued] -->|Initial Notice| B[notice_level = 1<br/>First Notice Sent]
    B -->|Payment Deadline Passes| C[notice_level = 2<br/>Second Notice Sent]
    C -->|Still Unpaid| D[notice_level = 3<br/>Third Notice Sent]
    D -->|Still Unpaid| E[notice_level = 4<br/>Final Notice / Collection Notice]
    E -->|Escalation| F[notice_level = 5<br/>Delinquency Notice]
    
    B -->|Payment Received| G[Ticket Paid<br/>notice_level remains at highest reached]
    C -->|Payment Received| G
    D -->|Payment Received| G
    E -->|Payment Received| G
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#ffe1e1
    style D fill:#ffe1e1
    style E fill:#ffcccc
    style F fill:#ff9999
    style G fill:#ccffcc
```

**How I arrived at this conclusion:**
- By examining the data, `notice_level` typically shows values 1, 2, 3, 4, 5 (or higher)
- The sequence is progressive: tickets generally move from lower to higher notice levels
- This represents the escalation process: if a ticket remains unpaid, the city sends increasingly urgent notices
- Notice level 1 = initial notice after ticket issuance
- Each subsequent level represents additional notices/warnings sent as the ticket remains unpaid

## Diagram 2: ticket_queue Process Flow (Combined with Contest Outcome)

```mermaid
graph TD
    A[Ticket Issued] --> B[ticket_queue = Payment<br/>Waiting for Payment]
    
    B -->|Payment Made| C[ticket_queue = Payment<br/>Ticket Paid - Case Closed]
    B -->|No Payment| D[ticket_queue = Collection<br/>Sent to Collections Agency]
    B -->|Contest Request| E[ticket_queue = Adjudication<br/>Under Review / Hearing]
    
    D -->|Payment Made| C
    D -->|Still Unpaid| F[ticket_queue = Boot<br/>Vehicle Eligible for Boot]
    D -->|Still Unpaid| G[ticket_queue = Tow<br/>Vehicle Eligible for Tow]
    
    E -->|Found Liable| H[ticket_queue = Payment<br/>Must Pay Original Fine + Fees]
    E -->|Found NOT Liable| I[ticket_queue = Payment<br/>notice_level reset / case dismissed]
    
    H --> C
    I --> J[Case Dismissed<br/>No payment required]
    
    F -->|Payment Made| C
    G -->|Payment Made| C
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#ccffcc
    style D fill:#ffe1e1
    style E fill:#e1e1ff
    style F fill:#ffcccc
    style G fill:#ff9999
    style H fill:#ffe1e1
    style I fill:#ccffcc
    style J fill:#ccffcc
```

**Key Observations:**
- `ticket_queue` indicates the current status/queue of the ticket in the system
- When someone **contests their ticket and is found NOT liable**:
  - **notice_level**: May be reset to a lower value (or marked as dismissed) since the ticket is voided
  - **ticket_queue**: Changes to indicate the case was dismissed (may remain as "Payment" but with a flag, or move to a "Dismissed" state)
- If found liable after contesting: ticket returns to payment queue, potentially with higher fees

## Combined Process: Interaction between notice_level and ticket_queue

The two variables interact:
- **notice_level** tracks the escalation of notices sent (administrative process)
- **ticket_queue** tracks the ticket's position in different processing queues (operational status)

A ticket can be at a high `notice_level` (e.g., level 4) but still in `ticket_queue = "Payment"` if it hasn't been sent to collections yet. Once it moves to `ticket_queue = "Collection"`, the `notice_level` may continue to increase.
