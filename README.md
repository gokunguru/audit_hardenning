# Audit & Hardening Lab
Audit de sécurité Linux automatisé et laboratoire de durcissement avec Docker, Ansible et Lynis.
 
---
 
## Présentation du projet
 
Ce projet illustre un workflow complet de durcissement d'infrastructure :
 
1. Déploiement d'un environnement Linux vulnérable
2. Audit de sécurité initial
3. Durcissement automatisé avec Ansible
4. Validation des contrôles de sécurité appliqués
5. Scoring de sécurité via Lynis
6. Génération de rapports HTML
L'objectif est de simuler une approche DevSecOps / sécurité système réelle en appliquant les principes d'Infrastructure-as-Code.
 
---
 
## Technologies utilisées
 
- Docker
- Docker Compose
- Ansible
- Python
- Lynis
- UFW
- auditd
---
 
## Architecture
 
| Composant           | Rôle                                    |
|---------------------|-----------------------------------------|
| linux-target        | Serveur Ubuntu vulnérable               |
| ansible-controller  | Exécute les playbooks Ansible           |
| reports/            | Stocke les rapports générés             |
| scripts/            | Scripts d'automatisation Python         |
 
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
 
## Résultats de sécurité
 
| Contrôle de sécurité      | Avant       | Après     |
|---------------------------|-------------|-----------|
| Connexion root SSH        | Vulnérable  | Sécurisé  |
| Authentification par MDP  | Activée     | Désactivée|
| Pare-feu                  | Inactif     | Actif     |
| Règles d'audit            | Absentes    | Configurées|
 
### Score Lynis
 
| État                  | Score |
|-----------------------|-------|
| Avant durcissement    | 0     |
| Après durcissement    | 54    |
 
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
 
---
 
## Limitations connues
 
- Les conteneurs Docker limitent certaines fonctionnalités de sécurité au niveau du noyau
- auditd est partiellement fonctionnel à l'intérieur des conteneurs
- Ce laboratoire n'est pas une implémentation complète de conformité ANSSI
- Pas de SIEM ni de journalisation centralisée
---
 
## Améliorations futures
 
- CI/CD avec GitHub Actions
- Intégration de Fail2ban
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
---
 
## Auteur
 
Kamil Mandi
 
