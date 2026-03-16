<p align="center">
  <img src="assets/logo.svg" alt="SecurityMisconfigs" width="180"/>
</p>

<h1 align="center">SecurityMisconfigs</h1>

<p align="center">
  <b>The DefaultCreds of Security Misconfigurations</b><br/>
  <i>One file. Every default misconfiguration. Ready for your next pentest.</i>
</p>

<p align="center">
  <a href="https://github.com/PentesterTN/SecurityMisconfigs/stargazers"><img src="https://img.shields.io/github/stars/PentesterTN/SecurityMisconfigs?style=for-the-badge&logo=github&color=yellow" alt="Stars"/></a>
  <a href="https://github.com/PentesterTN/SecurityMisconfigs/network/members"><img src="https://img.shields.io/github/forks/PentesterTN/SecurityMisconfigs?style=for-the-badge&logo=github&color=blue" alt="Forks"/></a>
  <a href="https://github.com/PentesterTN/SecurityMisconfigs/blob/main/LICENSE"><img src="https://img.shields.io/github/license/PentesterTN/SecurityMisconfigs?style=for-the-badge&color=green" alt="License"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Entries-132-red?style=flat-square" alt="Entries"/>
  <img src="https://img.shields.io/badge/Products-96-blue?style=flat-square" alt="Products"/>
  <img src="https://img.shields.io/badge/Categories-12-orange?style=flat-square" alt="Categories"/>
  <img src="https://img.shields.io/badge/Critical-28-darkred?style=flat-square" alt="Critical"/>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> &bull;
  <a href="#-database">Database</a> &bull;
  <a href="#-top-30-critical-misconfigurations">Top 30</a> &bull;
  <a href="#-how-to-use-in-pentests">Usage</a> &bull;
  <a href="#-contributing">Contribute</a>
</p>

<br/>

---

## What is this?

**SecurityMisconfigs** is a centralized, searchable database of **default security misconfigurations** found in popular software, services, and infrastructure. Think of it as [DefaultCreds-cheat-sheet](https://github.com/ihebski/DefaultCreds-cheat-sheet) but for **misconfigurations instead of passwords**.

Every entry documents a real-world misconfiguration: what it is, where to find it, how to check for it, and why it matters.

> **During a pentest, you already check for default credentials. Now check for default misconfigurations too.**

### Why?

| | Default Credentials | Default Misconfigurations |
|---|---|---|
| **Persistence** | Get changed on first login | Stay forever if nobody audits |
| **Detection** | Easy to scan | Logic flaws that scanners miss |
| **Cheat sheet** | [DefaultCreds](https://github.com/ihebski/DefaultCreds-cheat-sheet) | **This project** |
| **Impact** | Login as admin | RCE, data breach, lateral movement |

---

## Quick Start

### CLI Tool

```bash
pip3 install secmisconfigs
```

```bash
# Search misconfigurations for a product
misconfig search jenkins

# Search by severity
misconfig search --severity critical

# Search by category
misconfig search --category ci-cd

# Export results for a report
misconfig search kubernetes --format markdown
```

### One-liner (no install)

```bash
curl -s https://raw.githubusercontent.com/PentesterTN/SecurityMisconfigs/main/SecurityMisconfigs.csv | grep -i "jenkins"
```

---

## Database

### Format

The database is a single CSV file (`SecurityMisconfigs.csv`) with the following structure:

| Field | Description |
|-------|-------------|
| `product` | Product or service name |
| `category` | Category (web-server, database, ci-cd, cloud, monitoring, container, network, iot, cms, etc.) |
| `misconfiguration` | Short description of the misconfiguration |
| `check` | URL path, command, or method to detect it |
| `severity` | CRITICAL / HIGH / MEDIUM / LOW |
| `impact` | What an attacker gains |
| `reference` | Link to documentation or advisory |

### Example Entries

```
product,category,misconfiguration,check,severity,impact,reference
Jenkins,ci-cd,Script Console accessible without auth,/script,CRITICAL,Remote Code Execution,https://www.jenkins.io/doc/book/managing/script-console/
Kubernetes Dashboard,container,Dashboard exposed without authentication,/api/v1/namespaces/kubernetes-dashboard,CRITICAL,Full cluster takeover,https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
Spring Boot,web-framework,Actuator endpoints exposed,/actuator/env,HIGH,Credential and config leak,https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
Docker,container,Remote API exposed without TLS,:2375/containers/json,CRITICAL,Container escape and host takeover,https://docs.docker.com/engine/security/
Elasticsearch,database,No authentication enabled by default (pre-8.0),:9200/_cat/indices,HIGH,Full database read/write,https://www.elastic.co/guide/en/elasticsearch/reference/current/security-minimal-setup.html
Apache Tomcat,web-server,Manager application with default path,/manager/html,HIGH,WAR deployment leads to RCE,https://tomcat.apache.org/tomcat-9.0-doc/manager-howto.html
```

### Categories

| Category | Description | Count |
|----------|-------------|-------|
| `web-server` | Apache, Nginx, IIS, Tomcat, etc. | 40+ |
| `database` | MySQL, PostgreSQL, MongoDB, Redis, Elasticsearch, etc. | 35+ |
| `ci-cd` | Jenkins, GitLab, TeamCity, ArgoCD, Drone, etc. | 30+ |
| `container` | Docker, Kubernetes, Podman, etc. | 25+ |
| `cloud` | AWS, GCP, Azure misconfigs | 30+ |
| `monitoring` | Grafana, Prometheus, Nagios, Zabbix, etc. | 25+ |
| `network` | Routers, switches, firewalls, VPN | 30+ |
| `cms` | WordPress, Drupal, Joomla, etc. | 25+ |
| `web-framework` | Spring Boot, Django, Laravel, Express, etc. | 25+ |
| `iot` | Cameras, NAS, printers, SCADA | 25+ |
| `mail` | SMTP, IMAP, webmail | 15+ |
| `vpn-remote` | VPN, RDP, SSH misconfigs | 15+ |

---

## Top 30 Critical Misconfigurations

These are the misconfigurations that appear most frequently in real-world pentests and bug bounties:

| # | Product | Misconfiguration | Severity |
|---|---------|-----------------|----------|
| 1 | Kubernetes Dashboard | No authentication | CRITICAL |
| 2 | Docker | Remote API on :2375 without TLS | CRITICAL |
| 3 | Jenkins | Script Console without auth | CRITICAL |
| 4 | Elasticsearch | No authentication (pre-8.0) | CRITICAL |
| 5 | MongoDB | No authentication, bound to 0.0.0.0 | CRITICAL |
| 6 | Redis | No password, bound to 0.0.0.0 | CRITICAL |
| 7 | Apache Tomcat | Manager accessible with default creds | CRITICAL |
| 8 | etcd | API exposed without auth | CRITICAL |
| 9 | CouchDB | Admin party mode (no auth) | CRITICAL |
| 10 | Memcached | UDP reflection enabled | CRITICAL |
| 11 | Spring Boot | Actuator /env endpoint exposed | HIGH |
| 12 | Grafana | Anonymous access enabled | HIGH |
| 13 | GitLab | Public registration enabled | HIGH |
| 14 | Prometheus | No authentication on /metrics | HIGH |
| 15 | Apache Solr | Admin UI without auth | HIGH |
| 16 | RabbitMQ | Management UI with guest/guest | HIGH |
| 17 | MinIO | Default credentials (minioadmin) | HIGH |
| 18 | phpMyAdmin | No auth or config password | HIGH |
| 19 | Kibana | No authentication (pre-8.0) | HIGH |
| 20 | Hadoop YARN | ResourceManager exposed | HIGH |
| 21 | Apache Spark | Master UI without auth | HIGH |
| 22 | Jupyter Notebook | No token/password required | HIGH |
| 23 | WordPress | XML-RPC enabled | MEDIUM |
| 24 | WordPress | User enumeration via REST API | MEDIUM |
| 25 | Nginx | Status page exposed | MEDIUM |
| 26 | Apache | Server status/info exposed | MEDIUM |
| 27 | AWS S3 | Public bucket ACL | CRITICAL |
| 28 | Firebase | Realtime DB rules set to public | CRITICAL |
| 29 | .git | Repository exposed on webserver | HIGH |
| 30 | .env | Environment file accessible | HIGH |

---

## How to Use in Pentests

### During Reconnaissance
```bash
# Check all web server misconfigs against a target
misconfig search --category web-server --format check | while read check; do
  curl -s -o /dev/null -w "%{http_code} $check\n" "https://target.com$check"
done
```

### Quick Checks
```bash
# Spring Boot Actuator
curl -s https://target.com/actuator/env

# Docker Remote API
curl -s http://target.com:2375/containers/json

# Kubernetes API
curl -sk https://target.com:6443/api/v1/namespaces

# Elasticsearch
curl -s http://target.com:9200/_cat/indices

# Redis
redis-cli -h target.com INFO

# .git exposed
curl -s https://target.com/.git/HEAD

# .env file
curl -s https://target.com/.env
```

### Integration with Other Tools
```bash
# Generate nuclei-compatible check list
misconfig search --format nuclei > custom-misconfigs.yaml

# Use with httpx for mass scanning
misconfig search --category web-server --format paths | httpx -l targets.txt -mc 200

# Combine with DefaultCreds
misconfig search tomcat        # Find the misconfiguration
creds search tomcat            # Find the default password
```

---

## Contributing

We welcome contributions! The database grows through community submissions.

### Adding New Entries

1. Fork this repository
2. Add entries to `SecurityMisconfigs.csv` following the format
3. Keep entries sorted alphabetically by product name
4. Submit a pull request

### Rules

- Every entry must be a **default** misconfiguration (ships out of the box, not user error)
- Include a way to **check** for it (URL path, command, or detection method)
- Include a **reference** link (official docs, advisory, or writeup)
- Rate severity honestly using CVSS 3.1 guidelines
- Use `<blank>` for empty fields
- No duplicate entries — search before adding

### Entry Template

```
ProductName,category,Short description of misconfiguration,/path/or/command/to/check,SEVERITY,What attacker gains,https://reference-link
```

---

## Data Sources

This database is compiled from:

- Real-world penetration testing engagements
- Bug bounty findings (responsibly disclosed)
- Official vendor security documentation
- OWASP Testing Guide
- CIS Benchmarks
- NIST Security Configuration Checklists
- Community contributions

---

## Disclaimer

**For authorized security testing and educational purposes only.** Only test systems you have explicit permission to test. The maintainers are not responsible for misuse.

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

<p align="center">
  <b>Found a misconfiguration that's not listed? <a href="https://github.com/PentesterTN/SecurityMisconfigs/issues/new">Open an issue</a> or submit a PR!</b>
</p>

<p align="center">
  <sub>Made by pentesters, for pentesters.</sub>
</p>
