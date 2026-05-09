# Audit & Hardening Lab
 
Audit de sécurité Linux automatisé et laboratoire de durcissement avec Docker, Ansible, Lynis et GitHub Actions.
 
---
 
## Présentation du projet
 
Ce projet illustre un workflow complet de sécurisation d'infrastructure Linux dans une approche DevSecOps moderne.
 
L'objectif est de simuler un environnement de sécurité système réaliste en automatisant :
 
- l'audit d'un serveur Linux vulnérable,
- l'application de mesures de hardening,
- la validation des contrôles de sécurité,
- la génération de rapports,
- ainsi que l'intégration CI/CD.
Le projet applique les principes d'Infrastructure-as-Code (IaC) et d'automatisation de sécurité.
 
---
 
## Fonctionnalités principales
 
- Déploiement automatisé d'un laboratoire Linux vulnérable
- Audit système Linux automatisé
- Hardening SSH
- Configuration automatique du pare-feu UFW
- Désactivation des services vulnérables
- Mise en place de règles d'audit système
- Intégration Fail2ban
- Audit de sécurité avec Lynis
- Génération de rapports HTML et JSON
- Pipeline GitHub Actions DevSecOps
- Publication automatique du rapport HTML via GitHub Pages
---
 
## Technologies utilisées
 
- Docker
- Docker Compose
- Ansible
- Python
- GitHub Actions
- Lynis
- UFW
- auditd
- Fail2ban
---
 
## Architecture
 
| Composant          | Rôle                                  |
|--------------------|---------------------------------------|
| linux-target       | Serveur Ubuntu vulnérable             |
| ansible-controller | Contrôleur Ansible                    |
| reports/           | Stockage des rapports générés         |
| scripts/           | Scripts Python d'automatisation       |
| GitHub Actions     | Pipeline CI/CD DevSecOps              |
| GitHub Pages       | Publication du rapport HTML           |
 
---
 
## Architecture DevSecOps
 
```text
Docker
  ↓
Ansible
  ↓
Linux Hardening
  ↓
Lynis Audit
  ↓
Validation
  ↓
HTML / JSON Reporting
  ↓
GitHub Actions CI/CD
  ↓
GitHub Pages (Publication du rapport)
```
 
---
 
## Contrôles de sécurité implémentés
 
### Durcissement SSH
- Connexion root SSH désactivée
- Authentification par mot de passe désactivée
- MaxAuthTries réduit
### Sécurité réseau
- Pare-feu UFW activé
- Politique par défaut : refus des connexions entrantes
- SSH en liste blanche
### Durcissement des services
- Suppression des services vulnérables
- Telnet supprimé
- vsftpd désactivé
### Protection contre les intrusions
- Fail2ban installé et configuré
- Bannissement automatique des IP malveillantes
### Audit système
- auditd installé
- Règles de surveillance ajoutées pour :
  - `/etc/passwd`
  - `/etc/shadow`
  - `/etc/ssh/sshd_config`
---
 
## Structure du projet
 
```text
audit-hardening-lab/
├── .github/
│   └── workflows/
│       └── devsecops.yml
├── docker-compose.yml
├── inventory/
├── playbooks/
├── roles/
├── reports/
├── scripts/
└── README.md
```
 
---
 
## Démarrage rapide
 
### Lancer le laboratoire
 
```bash
docker compose up -d --build
```
 
### Exécuter l'audit Linux
 
```bash
ansible-playbook -i inventory/hosts.yml playbooks/audit_linux.yml
```
 
### Appliquer le durcissement
 
```bash
ansible-playbook -i inventory/hosts.yml playbooks/harden_linux.yml
```
 
### Valider les contrôles de sécurité
 
```bash
ansible-playbook -i inventory/hosts.yml playbooks/validate.yml
```
 
### Lancer l'audit Lynis
 
```bash
ansible-playbook -i inventory/hosts.yml playbooks/audit_lynis.yml
```
 
### Générer les rapports
 
```bash
python3 scripts/compare_results.py
python3 scripts/build_report.py
```
 
---
 
## Pipeline CI/CD GitHub Actions
 
Le pipeline DevSecOps s'exécute automatiquement à chaque push sur la branche `main` :
 
1. Démarrage de l'environnement Docker
2. Exécution de l'audit initial
3. Application du hardening
4. Validation des contrôles
5. Génération des rapports HTML et JSON
6. Publication automatique sur GitHub Pages
---
 
## Résultats de sécurité
 
| Contrôle de sécurité     | Avant       | Après      |
|--------------------------|-------------|------------|
| Connexion root SSH       | Vulnérable  | Sécurisé   |
| Authentification par MDP | Activée     | Désactivée |
| Pare-feu                 | Inactif     | Actif      |
| Fail2ban                 | Absent      | Configuré  |
| Règles d'audit           | Absentes    | Configurées|
 
### Score Lynis
 
| État               | Score |
|--------------------|-------|
| Avant durcissement | 0     |
| Après durcissement | 54    |
 
---
 
## Rapports générés
 
Le projet génère automatiquement :
 
- Rapport de comparaison JSON
- Rapport de sécurité HTML
- Rapports de validation
- Rapport d'audit Lynis
Les rapports sont stockés dans :
 
```
reports/final/
```
 
Le rapport HTML est publié automatiquement via **GitHub Pages**.
 
---
 
## Limitations connues
 
- Les conteneurs Docker limitent certaines fonctionnalités de sécurité au niveau du noyau
- auditd est partiellement fonctionnel à l'intérieur des conteneurs
- Ce laboratoire n'est pas une implémentation complète de conformité ANSSI
- Pas de SIEM ni de journalisation centralisée
---
 
## Améliorations futures
 
- Contrôles de conformité OpenSCAP
- Tableau de bord Grafana / Loki
- Inventaire multi-hôtes
- Gestion des secrets avec Ansible Vault
---
 
## Objectif pédagogique
 
Ce projet a été conçu pour renforcer les compétences pratiques en :
 
- Durcissement Linux
- Sécurité d'infrastructure
- DevSecOps
- Automatisation Ansible
- Audit de sécurité
- Infrastructure-as-Code
- Intégration continue (CI/CD)
---
 
## Auteur
 
Kamil Mandi
 
