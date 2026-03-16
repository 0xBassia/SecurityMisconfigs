# Contributing to SecurityMisconfigs

Thanks for helping grow the database! Here's how to contribute.

## Adding New Entries

### Format

Each entry in `SecurityMisconfigs.csv` has 7 fields:

```
product,category,misconfiguration,check,severity,impact,reference
```

| Field | Rules |
|-------|-------|
| `product` | Official product name. Use consistent naming (check existing entries first). |
| `category` | One of: `web-server`, `database`, `ci-cd`, `container`, `cloud`, `monitoring`, `network`, `cms`, `web-framework`, `iot`, `mail`, `vpn-remote` |
| `misconfiguration` | Short, clear description. Start with what's wrong, not the product name. |
| `check` | URL path, port + command, or detection method. Be specific. |
| `severity` | `CRITICAL` / `HIGH` / `MEDIUM` / `LOW` based on direct exploitability. |
| `impact` | What an attacker gains. Be concrete (not "security issue" but "Remote Code Execution"). |
| `reference` | Official documentation or security advisory URL. |

### Severity Guidelines

| Severity | Criteria |
|----------|----------|
| **CRITICAL** | Direct RCE, full admin access without auth, data breach of entire database |
| **HIGH** | Credential disclosure, significant data access, auth bypass |
| **MEDIUM** | Information disclosure, user enumeration, configuration details |
| **LOW** | Version disclosure, technology fingerprinting, minor info leak |

### Rules

1. **Only default misconfigurations** — things that ship misconfigured out of the box, not user error
2. **Must include a check** — every entry needs a way to verify it
3. **Must include a reference** — official docs, advisory, or reliable writeup
4. **No duplicates** — search the CSV before adding
5. **Sort alphabetically** by product name: `tail -n +2 SecurityMisconfigs.csv | sort -t',' -k1 -u`
6. **Rate severity honestly** — don't inflate. A version disclosure is LOW, not HIGH.

### Process

1. Fork this repository
2. Add your entries to `SecurityMisconfigs.csv`
3. Sort the file (keep the header row first)
4. Submit a pull request with a description of what you added

### What We're Looking For

- Products not yet covered (check the CSV first)
- Cloud-specific misconfigurations (AWS, GCP, Azure services)
- IoT and embedded device misconfigurations
- New software versions with changed defaults
- Enterprise software (SAP, Oracle, ServiceNow, etc.)
