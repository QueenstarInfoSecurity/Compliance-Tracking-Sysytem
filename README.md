# Compliance-Tracking. GDPR & ISO 27001
A lightweight Python tool to log, monitor, and report on data security compliance standards.

# Overview
This project helps organizations and IT teams maintain visibility into their compliance posture by logging and tracking adherence to key requirements of GDPR and ISO 27001. It stores entries in a local SQLite database and generates JSON reports for audit and review purposes.
Designed to be simple, extendable, and usable as a CLI or intergrated into a web interface.

# Features
 - Log compliance items with timestamped status
 - Store data in a local SQLite database
 - Automatically generate structred compliance reports in JSON
 - Directory structure designed for CLI and web expansion
 - Easy to customize and deploy

# Prerequisities
 - Python 3.13.0 or higher
 - No external dependencies required

# Setup

```bash
git clone 
cd compliance-tracker
python tracker.py.
```

# Output
 -  Logs entries in db/compliance.db
 -  Generates a report at reports/compliance_report.json

# Sample Report Output

```json
[
    [1, "GDPR - Data Encryption", "Compliant", "2025-04-22 14:35:12"],
    [2, "ISO 27001 - Access Control", "Non-Compliant", "2025-04-22 14:36:01"]
]
```

# Roadmap
 - Add CLI interface for manual logging and querying
 - Build interactive web dashboard
 - Add logging to logs/ for audit trails
 - Support importing/ exporting compliance checklists
 - Email alerts for non-compliance
   
# Contributing
Welcome contributions! If you would like to help with development, suggest features, or report issues:
1. Fork the repo
2. Create a new branch
3. Submit a pull request with a clear description
   
## License
 This project is licensed under the MIT License.
 
## ** Disclaimer:**
This project is provided **as is**, without any warranties or guarantees. The author assumes **no responsibility** for any issues, damages,or legal consequences arising from the use of this content. Users should consult legal professionals before implementing any contractual or security related clauses.

# Feedback
Found a bug or want a feature? Open an issue - I love to hear from you.

Let me know if you want a Markdown file version of this, or help setting up the web interface or CLI next.   
  
   
