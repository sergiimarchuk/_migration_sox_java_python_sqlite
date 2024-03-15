# Migration Toolkit: Python, Java, Ansible, SQLite

## Overview

This repository serves as a comprehensive toolkit designed to streamline the migration process from legacy servers to new environments. It includes a collection of scripts and tools written in Python and Java, integrated with Ansible for deployment automation, and utilizes SQLite for efficient data storage and management.

## Key Components

1. **Python Data Collection (Decommissioning Process):**
   - Scripts for gathering data from remote servers undergoing decommissioning.
   - Collects system configurations, user details, and other relevant data from decommissioning servers.

2. **Java GUI Tool for Data Filtering:**
   - A Java-based graphical user interface (GUI) tool for filtering and processing collected data.
   - Allows users to interactively filter and organize data for further analysis and usage.

3. **Jump Server File Processing:**
   - Files collected from decommissioning servers are transferred to a designated jump server.
   - Scripts on the jump server filter out unnecessary information and format the data into YAML files compatible with Ansible.

4. **Ansible Deployment:**
   - Utilizes Ansible playbooks to deploy configurations and provision new servers.
   - YAML files generated from the processed data specify user attributes, ACLs, permissions, and other configurations required on the new servers.
